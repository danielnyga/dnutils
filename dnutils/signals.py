import signal as signal_
import threading
from collections import defaultdict

handlers = defaultdict(list)

SIGINT = signal_.SIGINT
SIGTERM = signal_.SIGTERM
SIGKILL = signal_.SIGKILL
SIGABRT = signal_.SIGABRT
SIGALRM = signal_.SIGALRM
SIGBUS = signal_.SIGBUS
SIGCHLD = signal_.SIGCHLD
SIGCLD = signal_.SIGCLD
SIGCONT = signal_.SIGCONT
SIGFPE = signal_.SIGFPE
SIGHUP = signal_.SIGHUP
SIGILL = signal_.SIGILL
SIGINT = signal_.SIGINT
SIGIO = signal_.SIGIO
SIGIOT = signal_.SIGIO
SIGKILL = signal_.SIGKILL
SIGPIPE = signal_.SIGPIPE
SIGPOLL = signal_.SIGPOLL
SIGPROF = signal_.SIGPROF
SIGPWR = signal_.SIGPWR
SIGQUIT = signal_.SIGQUIT
SIGRTMAX = signal_.SIGRTMAX
SIGRTMIN = signal_.SIGRTMIN
SIGSEGV = signal_.SIGSEGV
SIGSTOP = signal_.SIGSTOP
SIGSYS = signal_.SIGSYS
SIGTERM = signal_.SIGTERM
SIGTRAP = signal_.SIGTRAP
SIGTSTP = signal_.SIGTSTP
SIGTTIN = signal_.SIGTTIN
SIGTTOU = signal_.SIGTTOU
SIGURG = signal_.SIGURG
SIGUSR1 = signal_.SIGUSR1
SIGUSR2 = signal_.SIGUSR2
SIGVTALRM = signal_.SIGVTALRM
SIGWINCH = signal_.SIGWINCH
SIGXCPU = signal_.SIGXCPU
SIGXFSZ = signal_.SIGXFSZ

_lock = threading.Lock()


def _run_handlers(signal, args):
    '''Executes all handlers that are registered for the given
    siganl in the order of registration.'''
    for h in handlers[signal]:
        h(*args)


def add_handler(signal, handler):
    '''
    Add a handler to be executed on the signal ``signal``

    :param signal:  the signal to react to.
    :param handler: a callable that will be called on the signal.
    :return:
    '''
    with _lock:
        handlers_ = handlers[signal]
        if not handlers_:
            signal_.signal(signal, lambda *args: _run_handlers(signal, args))
        if handler not in handlers_:
            handlers_.append(handler)


def rm_handler(signal, handler):
    '''
    Remove a handler if it is registered to the given signal.
    :param signal:
    :param handler:
    :return:
    '''
    with _lock:
        try:
            handlers[signal].remove(handler)
        except ValueError: pass