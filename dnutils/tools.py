'''
Created on May 22, 2017

@author: nyga
'''


def ifnone(if_, else_, transform=None):
    '''Returns the condition ``if_`` iff it is not ``None``, or if a transformation is
    specified, ``transform(if_)``. Returns ``else_`` if the condition is ``None``.
    ``transform`` can be any callable, which will be passed ``if_`` in case ``if_`` is not ``None``.'''
    if if_ is None:
        return else_
    else:
        if transform is not None: return transform(if_)
        else: return if_


def ifnot(if_, else_, transform=None):
    '''Returns the condition ``if_`` iff it evaluates to ``True``, or if a transformation is
    specified, ``transform(if_)``. Returns ``else_`` if the condition is ``False``.
    ``transform`` can be any callable, which will be passed ``if_`` in case ``if_`` is not ``False``.'''
    if not bool(if_):
        return else_
    else:
        if transform is not None: return transform(if_)
        else: return if_


def allnone(it):
    '''Returns True iff all elements in the iterable ``it`` are ``None``, and ``False`` otherwise.'''
    return not ([1 for e in it if e is not None])


def allnot(it):
    '''Returns True iff all elements in the iterable ``it`` evaluate to ``False``, and ``False`` otherwise.'''
    return not ([1 for e in it if bool(e) is True])


class edict(dict):
    '''
    Enhanced dict with some convenience methods such as dict addition and
    subtraction.
    
    :Example:
    
    >>> s = edict({'a':{'b': 1}, 'c': [1,2,3]})
    >>> r = edict({'x': 'z', 'c': 5})
    >>> print s
    {'a': {'b': 1}, 'c': [1, 2, 3]}
    >>> print r
    {'x': 'z', 'c': 5}
    >>> print s + r
    {'a': {'b': 1}, 'x': 'z', 'c': 5}
    >>> print s - r
    {'a': {'b': 1}}
    >>> print r
    {'x': 'z', 'c': 5}
    '''
    
    def __iadd__(self, d):
        self.update(d)
        return self
    
    def __isub__(self, d):
        for k in d: 
            if k in self: del self[k]
        return self
    
    def __add__(self, d):
        return type(self)({k: v for items in (self.items(), d.items())for k, v in items})
    
    def __sub__(self, d):
        return type(self)({k: v for k, v in self.items() if k not in d})

    def xpath(self, selector):
        '''
        Allows a 'pseudo-xpath' query to a nested set of dictionaries.

        At the moment, only nested dict-selections separated by slashes (``/``) are supported.
        Allows to conveniently access hierarchical dictionart structures without the need
        of checking every key for existence.

        :param selector:    a slash-separated list of dict keys
        :return:
        '''
        keys = map(str.strip, selector.split('/'))
        d = self
        for key in keys:
            d = d.get(key)
            if d is None:
                return None
        return d


class eset(set):
    
    def __add__(self, s):
        return set(self).union(s)



class RStorage(edict, object):
    '''
    Recursive extension of web.util.Storage that applies the Storage constructor
    recursively to all value elements that are dicts.
    '''
    __slots__ = ['_utf8']
    
    def __init__(self, d=None, utf8=False):
        self._utf8 = utf8
        if d is not None:
            for k, v in d.iteritems(): self[k] = v
    
    def __setattr__(self, key, value):
        if key in self.__slots__:
            self.__dict__[key] = value
        else: 
            self[key] = value
            
    def __setitem__(self, key, value):
        if self._utf8 and isinstance(key, str): key = key.encode('utf8')
        dict.__setitem__(self, key, rstorify(value, utf8=self._utf8))
            
    def __getattr__(self, key):
        if key in type(self).__slots__: 
            return self.__dict__[key]
        else:
            try:
                return self[key]
            except KeyError as k:
                raise (AttributeError, k)
             
    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError as k:
            raise (AttributeError, k)
            
    def __repr__(self):     
        return ('<%s ' % type(self).__name__) + dict.__repr__(self) + '>'
        
        
def rstorify(e):
    if type(e) is dict:
        return RStorage(d=e)
    elif type(e) in (list, tuple):
        return [rstorify(i) for i in e]
    else: return e
        
def jsonify(o):
    if hasattr(o, 'json'): 
        return o.json
    elif isinstance(o, dict):
        return {str(k): jsonify(v) for k, v in o.iteritems()}
    elif type(o) in (list, tuple):
        return [jsonify(e) for e in o]
    elif isinstance(o, (int, float, bool, str, type(None))):
        return o
    else:
        raise TypeError('object of type "%s" is not jsonifiable: %s' % (type(o), repr(o)))
    

if __name__ == '__main__':
    d = edict({'a': {'b': {'c': 'hello'}}})
    print(d.xpath('a/d/c'))