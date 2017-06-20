<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    
    <title>Welcome to dnutils’s documentation! &#8212; dnutils 0.1.0 documentation</title>
    
    <link rel="stylesheet" href="_static/bootstrap-sphinx.css" type="text/css" />
    <link rel="stylesheet" href="_static/pygments.css" type="text/css" />
    
    <script type="text/javascript">
      var DOCUMENTATION_OPTIONS = {
        URL_ROOT:    './',
        VERSION:     '0.1.0',
        COLLAPSE_INDEX: false,
        FILE_SUFFIX: '.html',
        HAS_SOURCE:  true,
        SOURCELINK_SUFFIX: '.txt'
      };
    </script>
    <script type="text/javascript" src="_static/jquery.js"></script>
    <script type="text/javascript" src="_static/underscore.js"></script>
    <script type="text/javascript" src="_static/doctools.js"></script>
    <script type="text/javascript" src="_static/js/jquery-1.11.0.min.js"></script>
    <script type="text/javascript" src="_static/js/jquery-fix.js"></script>
    <script type="text/javascript" src="_static/bootstrap-3.3.6/js/bootstrap.min.js"></script>
    <script type="text/javascript" src="_static/bootstrap-sphinx.js"></script>
    <link rel="index" title="Index" href="genindex.html" />
    <link rel="search" title="Search" href="search.html" />
<meta charset='utf-8'>
<meta http-equiv='X-UA-Compatible' content='IE=edge,chrome=1'>
<meta name='viewport' content='width=device-width, initial-scale=1.0, maximum-scale=1'>
<meta name="apple-mobile-web-app-capable" content="yes">

  </head>
  <body>

  <div id="navbar" class="navbar navbar-default navbar-fixed-top">
    <div class="container">
      <div class="navbar-header">
        <!-- .btn-navbar is used as the toggle for collapsed navbar content -->
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".nav-collapse">
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="#">
          dnutils</a>
        <span class="navbar-text navbar-version pull-left"><b>0.1</b></span>
      </div>

        <div class="collapse navbar-collapse nav-collapse">
          <ul class="nav navbar-nav">
            
            
              <li class="dropdown globaltoc-container">
  <a role="button"
     id="dLabelGlobalToc"
     data-toggle="dropdown"
     data-target="#"
     href="#">Site <b class="caret"></b></a>
  <ul class="dropdown-menu globaltoc"
      role="menu"
      aria-labelledby="dLabelGlobalToc"></ul>
</li>
              
                <li class="dropdown">
  <a role="button"
     id="dLabelLocalToc"
     data-toggle="dropdown"
     data-target="#"
     href="#">Page <b class="caret"></b></a>
  <ul class="dropdown-menu localtoc"
      role="menu"
      aria-labelledby="dLabelLocalToc"><ul>
<li><a class="reference internal" href="#">Welcome to dnutils’s documentation!</a><ul>
<li><a class="reference internal" href="#debugging">Debugging</a><ul>
<li><a class="reference internal" href="#printing">Printing</a></li>
<li><a class="reference internal" href="#stack-traces">Stack Traces</a></li>
</ul>
</li>
<li><a class="reference internal" href="#tools">Tools</a></li>
<li><a class="reference internal" href="#console">Console</a><ul>
<li><a class="reference internal" href="#progress-bars">Progress Bars</a></li>
<li><a class="reference internal" href="#status-messages">Status Messages</a></li>
</ul>
</li>
</ul>
</li>
<li><a class="reference internal" href="#indices-and-tables">Indices and tables</a></li>
</ul>
</ul>
</li>
              
            
            
              
                
              
            
            
            
            
              <li class="hidden-sm">
<div id="sourcelink">
  <a href="_sources/index.rst.txt"
     rel="nofollow">Source</a>
</div></li>
            
          </ul>

          
            
<form class="navbar-form navbar-right" action="search.html" method="get">
 <div class="form-group">
  <input type="text" name="q" class="form-control" placeholder="Search" />
 </div>
  <input type="hidden" name="check_keywords" value="yes" />
  <input type="hidden" name="area" value="default" />
</form>
          
        </div>
    </div>
  </div>

<div class="container">
  <div class="row">
    <div class="col-md-12 content">
      
  <div class="section" id="welcome-to-dnutils-s-documentation">
<h1>Welcome to dnutils’s documentation!<a class="headerlink" href="#welcome-to-dnutils-s-documentation" title="Permalink to this headline">¶</a></h1>
<p><cite>dnutils</cite> is a collection of convenience functions, tools and classes
for situations I find myself very frequently. I have developed this
toolbox with the goal to provide a practical, easy-to-use and
well-documented collection of utilities for debugging, console output
and data structures.</p>
<div class="section" id="debugging">
<h2>Debugging<a class="headerlink" href="#debugging" title="Permalink to this headline">¶</a></h2>
<p>The <code class="xref py py-mod docutils literal"><span class="pre">dnutils.debug</span></code> module provides a couple of useful tools
for convenient and lightweight debugging.</p>
<div class="section" id="printing">
<h3>Printing<a class="headerlink" href="#printing" title="Permalink to this headline">¶</a></h3>
<p>The first and simplest function is the <code class="xref py py-func docutils literal"><span class="pre">out()</span></code> function:</p>
<dl class="function">
<dt id="dnutils.debug.out">
<code class="descclassname">dnutils.debug.</code><code class="descname">out</code><span class="sig-paren">(</span><em>*args</em>, <em>file=&lt;_io.TextIOWrapper name=’&lt;stdout&gt;’ mode=’w’ encoding=’UTF-8’&gt;</em>, <em>sep=’ ‘</em>, <em>end=’\n’</em>, <em>flush=False</em>, <em>tb=1</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/dnutils/debug.html#out"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#dnutils.debug.out" title="Permalink to this definition">¶</a></dt>
<dd><p>Basic output function that prints a str-converted list of its arguments.</p>
<p><cite>out</cite> forwards all arguments to the ordinary <cite>print</cite> function, but appends 
the file and line of its call, so it can be found easier from the console output.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>file</strong> – a file-like object (stream); defaults to the current sys.stdout.</li>
<li><strong>sep</strong> – string inserted between values, default a space.</li>
<li><strong>end</strong> – string appended after the last value, default a newline.</li>
<li><strong>flush</strong> – whether to forcibly flush the stream.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>The keyword arguments are inherited from Python’s <code class="xref py py-func docutils literal"><span class="pre">print()</span></code> function. 
There is an additional keyword argument, <code class="docutils literal"><span class="pre">tb</span></code>, which determines the depth of the
calling frame. It is not passed to <code class="xref py py-func docutils literal"><span class="pre">print()</span></code>.</p>
</dd></dl>

<p>The <code class="xref py py-func docutils literal"><span class="pre">out()</span></code> function is a simple wrapper around Python’s ordinary
<code class="xref py py-func docutils literal"><span class="pre">print()</span></code> function, but it prepends to any output the module’s file
name and line number of the calling frame. Let us consider an exemplay
python module <code class="docutils literal"><span class="pre">test.py</span></code>:</p>
<div class="highlight-python"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">dnutils</span> <span class="kn">import</span> <span class="n">out</span>

<span class="k">if</span> <span class="vm">__name__</span> <span class="o">==</span> <span class="s1">&#39;__main__&#39;</span><span class="p">:</span>
    <span class="n">out</span><span class="p">(</span><span class="s1">&#39;hello, world!&#39;</span><span class="p">)</span>
</pre></div>
</td></tr></table></div>
<p>Running the module prints</p>
<div class="highlight-default"><div class="highlight"><pre><span></span>$ python test.py
test.py: l.4: hello, world!
</pre></div>
</div>
<p>So, <a class="reference internal" href="#dnutils.debug.out" title="dnutils.debug.out"><code class="xref py py-func docutils literal"><span class="pre">dnutils.debug.out()</span></code></a> is basically a print function that allows
to trace back where the call to it was actually issued.</p>
<p>Ideally, one should set up a real logging infrastructure
properly instead of using <code class="docutils literal"><span class="pre">print</span></code>. However, the <code class="xref py py-func docutils literal"><span class="pre">out()</span></code>
function provides a convenient way of doing it the “quick-and-dirty”
way, which lets one locate the print statements that one has introduced
in the code, which can be really cumbersome to detect.</p>
<p>The <code class="xref py py-func docutils literal"><span class="pre">out()</span></code> function has a parameter <code class="docutils literal"><span class="pre">tb</span></code> that extends the
parameter list inherited from <code class="xref py py-func docutils literal"><span class="pre">print()</span></code>. Normally, when just
printing single statements to the console, one can just disregard it.
However, it might happen that one wants to outsource a more complex
debug output into a separate function. For example, consider the
following function that prints all global variables in the current
frame:</p>
<div class="highlight-python"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">print_globals</span><span class="p">():</span>
    <span class="n">out</span><span class="p">(</span><span class="s1">&#39;global variables&#39;</span><span class="p">):</span>
    <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="nb">globals</span><span class="p">()</span><span class="o">.</span><span class="n">iter</span><span class="p">():</span>
        <span class="k">print</span><span class="p">(</span><span class="n">k</span><span class="p">,</span> <span class="s1">&#39;: &#39;</span><span class="p">,</span> <span class="n">v</span><span class="p">)</span>
</pre></div>
</td></tr></table></div>
<p>If the <code class="xref py py-func docutils literal"><span class="pre">print_globals()</span></code> function is now used somewhere in the
code, the location printed would always be the <code class="xref py py-func docutils literal"><span class="pre">out()</span></code> call (in
this example, line 2). The desirable output, however, would be the
location of the <code class="xref py py-func docutils literal"><span class="pre">print_globals()</span></code> function. The <code class="xref py py-func docutils literal"><span class="pre">out()</span></code>
function provides an additional parameter <code class="docutils literal"><span class="pre">tb</span></code>, which lets us control
the number of indirections that it traces back to find the actual
caller frame. As <code class="xref py py-func docutils literal"><span class="pre">out()</span></code> is used in one additional level of
indirections,</p>
<div class="highlight-python"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">print_globals</span><span class="p">():</span>
    <span class="n">out</span><span class="p">(</span><span class="s1">&#39;global variables&#39;</span><span class="p">,</span> <span class="n">tb</span><span class="o">=</span><span class="mi">2</span><span class="p">):</span>
    <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="nb">globals</span><span class="p">()</span><span class="o">.</span><span class="n">iter</span><span class="p">():</span>
        <span class="k">print</span><span class="p">(</span><span class="n">k</span><span class="p">,</span> <span class="s1">&#39;: &#39;</span><span class="p">,</span> <span class="n">v</span><span class="p">)</span>
</pre></div>
</td></tr></table></div>
<p>Always prints the desired location in the code, where
<code class="xref py py-func docutils literal"><span class="pre">print_globals()</span></code> is called.</p>
<p>The <a class="reference internal" href="#dnutils.debug.stop" title="dnutils.debug.stop"><code class="xref py py-func docutils literal"><span class="pre">dnutils.debug.stop()</span></code></a> function is a modification of
<a class="reference internal" href="#dnutils.debug.out" title="dnutils.debug.out"><code class="xref py py-func docutils literal"><span class="pre">dnutils.debug.out()</span></code></a>, which stops after having printed the
desired output and waits until the user presses the return key:</p>
<dl class="function">
<dt id="dnutils.debug.stop">
<code class="descclassname">dnutils.debug.</code><code class="descname">stop</code><span class="sig-paren">(</span><em>*args</em>, <em>file=&lt;_io.TextIOWrapper name=’&lt;stdout&gt;’ mode=’w’ encoding=’UTF-8’&gt;</em>, <em>sep=’ ‘</em>, <em>end=’\n’</em>, <em>flush=False</em>, <em>tb=1</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/dnutils/debug.html#stop"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#dnutils.debug.stop" title="Permalink to this definition">¶</a></dt>
<dd><p>Same as <a class="reference internal" href="#dnutils.debug.out" title="dnutils.debug.out"><code class="xref py py-func docutils literal"><span class="pre">dnutils.debug.out()</span></code></a>, but stops with a promt after having printed 
the respective arguments until <cite>&lt;enter&gt;</cite> is pressed.</p>
</dd></dl>

<div class="highlight-python"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="kn">from</span> <span class="nn">dnutils</span> <span class="kn">import</span> <span class="n">stop</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">stop</span><span class="p">(</span><span class="s1">&#39;waiting...&#39;</span><span class="p">)</span>
<span class="go">&lt;stdin&gt;: l.1: waiting...</span>
<span class="go">&lt;press enter to continue&gt; # hit enter here</span>
<span class="go">&gt;&gt;&gt;</span>
</pre></div>
</div>
</div>
<div class="section" id="stack-traces">
<h3>Stack Traces<a class="headerlink" href="#stack-traces" title="Permalink to this headline">¶</a></h3>
<dl class="function">
<dt id="dnutils.debug.trace">
<code class="descclassname">dnutils.debug.</code><code class="descname">trace</code><span class="sig-paren">(</span><em>*args</em>, <em>**kwargs</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/dnutils/debug.html#trace"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#dnutils.debug.trace" title="Permalink to this definition">¶</a></dt>
<dd><p>Prints a stack trace of the current frame and terminates with
a call of <a class="reference internal" href="#dnutils.debug.out" title="dnutils.debug.out"><code class="xref py py-func docutils literal"><span class="pre">dnutils.debug.out()</span></code></a> of the given arguments.</p>
</dd></dl>

<div class="toctree-wrapper compound">
</div>
</div>
</div>
<div class="section" id="tools">
<h2>Tools<a class="headerlink" href="#tools" title="Permalink to this headline">¶</a></h2>
<p>The <a class="reference internal" href="#dnutils.tools.ifnone" title="dnutils.tools.ifnone"><code class="xref py py-func docutils literal"><span class="pre">dnutils.tools.ifnone()</span></code></a> function is supposed to make the
ternary Python <code class="docutils literal"><span class="pre">if-then-else</span></code> idiom less verbose. The basic idea
of this function is that in many cases one is supposed to do only
little operations on a variable <code class="docutils literal"><span class="pre">x</span></code>, but only if <code class="docutils literal"><span class="pre">x</span></code> is not <code class="docutils literal"><span class="pre">None</span></code>.
A popular case is, for example, to obtain a string representation of <code class="docutils literal"><span class="pre">x</span></code>,
but some special treatment of the <code class="docutils literal"><span class="pre">None</span></code> case:</p>
<div class="highlight-default"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="nb">str</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="k">if</span> <span class="n">x</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="s1">&#39;N/A&#39;</span>
</pre></div>
</div>
<p>So far, so good. As long as <code class="docutils literal"><span class="pre">x</span></code> is a pretty short expression, there is
nothing to argue against the above construct. But what if <code class="docutils literal"><span class="pre">x</span></code> is, for
instance, a concatenation of functions or dictionary queries, like</p>
<div class="highlight-default"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="nb">str</span><span class="p">(</span><span class="n">myobj</span><span class="o">.</span><span class="n">textfield</span><span class="o">.</span><span class="n">gettext</span><span class="p">()</span><span class="o">.</span><span class="n">getdata</span><span class="p">())</span> <span class="k">if</span> <span class="n">myobj</span><span class="o">.</span><span class="n">textfield</span><span class="o">.</span><span class="n">gettext</span><span class="p">()</span><span class="o">.</span><span class="n">getdata</span><span class="p">()</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="s1">&#39;&#39;</span>
</pre></div>
</div>
<p>There are at least three shortcomings with such a construct:</p>
<blockquote>
<div><ul class="simple">
<li>Verbosity: myobj.textfield.gettext().getdata() needs to be written twice</li>
<li>Speed: myobj.textfield.gettext().getdata() needs to be evaluated twice</li>
<li>Readability: the expression is hard to read</li>
</ul>
</div></blockquote>
<p>To make such constructs more convenient, <cite>dnutils</cite> provide the
<a class="reference internal" href="#dnutils.tools.ifnone" title="dnutils.tools.ifnone"><code class="xref py py-func docutils literal"><span class="pre">dnutils.tools.ifnone()</span></code></a> function:</p>
<dl class="function">
<dt id="dnutils.tools.ifnone">
<code class="descclassname">dnutils.tools.</code><code class="descname">ifnone</code><span class="sig-paren">(</span><em>if_</em>, <em>else_</em>, <em>transform=None</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/dnutils/tools.html#ifnone"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#dnutils.tools.ifnone" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns the condition <code class="docutils literal"><span class="pre">if_</span></code> iff it is not <code class="docutils literal"><span class="pre">None</span></code>, or if a transformation is
specified, <code class="docutils literal"><span class="pre">transform(if_)</span></code>. Returns <code class="docutils literal"><span class="pre">else_</span></code> if the condition is <code class="docutils literal"><span class="pre">None</span></code>.
<code class="docutils literal"><span class="pre">transform</span></code> can be any callable, which will be passed <code class="docutils literal"><span class="pre">if_</span></code> in case <code class="docutils literal"><span class="pre">if_</span></code> is not <code class="docutils literal"><span class="pre">None</span></code>.</p>
</dd></dl>

<p>Using <a class="reference internal" href="#dnutils.tools.ifnone" title="dnutils.tools.ifnone"><code class="xref py py-func docutils literal"><span class="pre">dnutils.tools.ifnone()</span></code></a>, the above expression can be written
more concisely as</p>
<div class="highlight-default"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">ifnone</span><span class="p">(</span><span class="n">myobj</span><span class="o">.</span><span class="n">textfield</span><span class="o">.</span><span class="n">gettext</span><span class="p">()</span><span class="o">.</span><span class="n">getdata</span><span class="p">(),</span> <span class="s1">&#39;&#39;</span><span class="p">,</span> <span class="nb">str</span><span class="p">)</span>
</pre></div>
</div>
<p>Another frequent example is parsing a number with a default value in
case of <code class="docutils literal"><span class="pre">None</span></code>:</p>
<div class="highlight-default"><div class="highlight"><pre><span></span><span class="n">ifnone</span><span class="p">(</span><span class="n">str_to_parse</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="nb">int</span><span class="p">)</span>
</pre></div>
</div>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">Note that, in contrast to the ternary <code class="docutils literal"><span class="pre">if-then-else</span></code> construct,
<a class="reference internal" href="#dnutils.tools.ifnone" title="dnutils.tools.ifnone"><code class="xref py py-func docutils literal"><span class="pre">dnutils.tools.ifnone()</span></code></a> always evaluates the <code class="docutils literal"><span class="pre">else</span></code> part, i.e.
it does not support lazy evaluation.</p>
</div>
<p><a class="reference internal" href="#dnutils.tools.ifnot" title="dnutils.tools.ifnot"><code class="xref py py-func docutils literal"><span class="pre">dnutils.tools.ifnot()</span></code></a> is equivalent to <code class="xref py py-func docutils literal"><span class="pre">ifnone()</span></code> except
for it checks for Boolean truth instead of <code class="docutils literal"><span class="pre">None</span></code>:</p>
<dl class="function">
<dt id="dnutils.tools.ifnot">
<code class="descclassname">dnutils.tools.</code><code class="descname">ifnot</code><span class="sig-paren">(</span><em>if_</em>, <em>else_</em>, <em>transform=None</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/dnutils/tools.html#ifnot"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#dnutils.tools.ifnot" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns the condition <code class="docutils literal"><span class="pre">if_</span></code> iff it evaluates to <code class="docutils literal"><span class="pre">True</span></code>, or if a transformation is
specified, <code class="docutils literal"><span class="pre">transform(if_)</span></code>. Returns <code class="docutils literal"><span class="pre">else_</span></code> if the condition is <code class="docutils literal"><span class="pre">False</span></code>.
<code class="docutils literal"><span class="pre">transform</span></code> can be any callable, which will be passed <code class="docutils literal"><span class="pre">if_</span></code> in case <code class="docutils literal"><span class="pre">if_</span></code> is not <code class="docutils literal"><span class="pre">False</span></code>.</p>
</dd></dl>

<dl class="function">
<dt id="dnutils.tools.allnone">
<code class="descclassname">dnutils.tools.</code><code class="descname">allnone</code><span class="sig-paren">(</span><em>it</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/dnutils/tools.html#allnone"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#dnutils.tools.allnone" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns True iff all elements in the iterable <code class="docutils literal"><span class="pre">it</span></code> are <code class="docutils literal"><span class="pre">None</span></code>, and <code class="docutils literal"><span class="pre">False</span></code> otherwise.</p>
</dd></dl>

<dl class="function">
<dt id="dnutils.tools.allnot">
<code class="descclassname">dnutils.tools.</code><code class="descname">allnot</code><span class="sig-paren">(</span><em>it</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/dnutils/tools.html#allnot"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#dnutils.tools.allnot" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns True iff all elements in the iterable <code class="docutils literal"><span class="pre">it</span></code> evaluate to <code class="docutils literal"><span class="pre">False</span></code>, and <code class="docutils literal"><span class="pre">False</span></code> otherwise.</p>
</dd></dl>

</div>
<div class="section" id="console">
<h2>Console<a class="headerlink" href="#console" title="Permalink to this headline">¶</a></h2>
<div class="section" id="progress-bars">
<h3>Progress Bars<a class="headerlink" href="#progress-bars" title="Permalink to this headline">¶</a></h3>
<dl class="class">
<dt id="dnutils.console.ProgressBar">
<em class="property">class </em><code class="descclassname">dnutils.console.</code><code class="descname">ProgressBar</code><span class="sig-paren">(</span><em>layout=‘100%:0%’</em>, <em>value=0</em>, <em>steps=None</em>, <em>label=”</em>, <em>color=None</em>, <em>stream=&lt;_io.TextIOWrapper name=’&lt;stdout&gt;’ mode=’w’ encoding=’UTF-8’&gt;</em>, <em>inf=False</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/dnutils/console.html#ProgressBar"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#dnutils.console.ProgressBar" title="Permalink to this definition">¶</a></dt>
<dd><p>An ASCII progress bar to show progress in the console.</p>
<dl class="method">
<dt id="dnutils.console.ProgressBar.finish">
<code class="descname">finish</code><span class="sig-paren">(</span><em>erase=True</em>, <em>msg=”</em>, <em>end=’\n’</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/dnutils/console.html#ProgressBar.finish"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#dnutils.console.ProgressBar.finish" title="Permalink to this definition">¶</a></dt>
<dd><p>Terminates the progress bar.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>erase</strong> – If <code class="docutils literal"><span class="pre">True</span></code>, the progress bar will be removed (overwritten) from the console.</li>
<li><strong>msg</strong> – Optional “goodbye”-message to be printed.</li>
<li><strong>end</strong> – Final character to be printed (default is ‘n’ to move to a new line)</li>
</ul>
</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="dnutils.console.ProgressBar.inc">
<code class="descname">inc</code><span class="sig-paren">(</span><em>steps=1</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/dnutils/console.html#ProgressBar.inc"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#dnutils.console.ProgressBar.inc" title="Permalink to this definition">¶</a></dt>
<dd><p>Increment the current value of the progress bar by <code class="docutils literal"><span class="pre">steps</span></code> steps.</p>
</dd></dl>

<dl class="method">
<dt id="dnutils.console.ProgressBar.setlayout">
<code class="descname">setlayout</code><span class="sig-paren">(</span><em>layout</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/dnutils/console.html#ProgressBar.setlayout"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#dnutils.console.ProgressBar.setlayout" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the layout of the progress bar.</p>
<p><code class="docutils literal"><span class="pre">layout</span></code> must be a string of the form “X:Y” or “X”, where
<cite>X</cite> determines the width of the bar part of the progress bar and
<cite>Y</cite> determines the width of the label part of the progress bar.
Values can be absolute (in console characters) or relative (in percentage values)
to the console width.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Example:</th><td class="field-body"><div class="first last highlight-default"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">bar</span> <span class="o">=</span> <span class="n">ProgressBar</span><span class="p">(</span><span class="n">value</span><span class="o">=.</span><span class="mi">2</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;green&#39;</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s1">&#39;in progress...please wait...&#39;</span><span class="p">)</span>
<span class="go">[■■■■■■■■■■■■■■■■■■■                                                                           ]  20.000 %</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">bar</span><span class="o">.</span><span class="n">setlayout</span><span class="p">(</span><span class="s1">&#39;70%:30%&#39;</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">print</span><span class="p">(</span><span class="n">bar</span><span class="p">)</span>
<span class="go">[■■■■■■■■■■■■                                                  ]  20.000 % in progress...please wait...</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">bar</span><span class="o">.</span><span class="n">setlayout</span><span class="p">(</span><span class="s1">&#39;100%:0%&#39;</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">print</span><span class="p">(</span><span class="n">bar</span><span class="p">)</span>
<span class="go">[■■■■■■■■■■■■■■■■■■■                                                                           ]  20.000 %</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">bar</span><span class="o">.</span><span class="n">setlayout</span><span class="p">(</span><span class="s1">&#39;60:40&#39;</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">print</span><span class="p">(</span><span class="n">bar</span><span class="p">)</span>
<span class="go">[■■■■■■■■■                                      ]  20.000 % in progress...please wait...</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="dnutils.console.ProgressBar.update">
<code class="descname">update</code><span class="sig-paren">(</span><em>value</em>, <em>label=None</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/dnutils/console.html#ProgressBar.update"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#dnutils.console.ProgressBar.update" title="Permalink to this definition">¶</a></dt>
<dd><p>Set the current value of the bar to <code class="docutils literal"><span class="pre">value</span></code> and update the label by <code class="docutils literal"><span class="pre">label</span></code>.</p>
</dd></dl>

</dd></dl>

</div>
<div class="section" id="status-messages">
<h3>Status Messages<a class="headerlink" href="#status-messages" title="Permalink to this headline">¶</a></h3>
<p><cite>dnutils</cite> contains a class that mimics the behavior of
status messages of a typical Linux boot screen:</p>
<img alt="_images/status-msg.png" src="_images/status-msg.png" />
<dl class="class">
<dt id="dnutils.console.StatusMsg">
<em class="property">class </em><code class="descclassname">dnutils.console.</code><code class="descname">StatusMsg</code><span class="sig-paren">(</span><em>message=”</em>, <em>status=None</em>, <em>width=‘100%’</em>, <em>stati=None</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/dnutils/console.html#StatusMsg"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#dnutils.console.StatusMsg" title="Permalink to this definition">¶</a></dt>
<dd><p>Print a Linux-style status message to the console.</p>
<dl class="method">
<dt id="dnutils.console.StatusMsg.setwidth">
<code class="descname">setwidth</code><span class="sig-paren">(</span><em>width</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/dnutils/console.html#StatusMsg.setwidth"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#dnutils.console.StatusMsg.setwidth" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets the with in relative or absolute numbers of console characters.
:param width:
:return:</p>
</dd></dl>

</dd></dl>

<p>A <a class="reference internal" href="#dnutils.console.StatusMsg" title="dnutils.console.StatusMsg"><code class="xref py py-class docutils literal"><span class="pre">dnutils.console.StatusMsg</span></code></a> object can be instantiated
with an optional width, a message and a status. The width is a
string or a number determining the width (in absolute characters)
or the percentage of console that the status message will consume.
A behavior as shown in the above screenshot, for instance, can be
achieved by somehting like:</p>
<div class="highlight-default"><div class="highlight"><pre><span></span><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">100</span><span class="p">):</span>
    <span class="n">status</span> <span class="o">=</span> <span class="n">StatusMsg</span><span class="p">(</span><span class="n">message</span><span class="o">=</span><span class="s1">&#39;  * Operation #</span><span class="si">%d</span><span class="s1">:&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
    <span class="n">status</span><span class="o">.</span><span class="n">status</span> <span class="o">=</span> <span class="n">StatusMsg</span><span class="o">.</span><span class="n">OK</span> <span class="k">if</span> <span class="n">random</span><span class="o">.</span><span class="n">random</span><span class="p">()</span> <span class="o">&gt;</span> <span class="o">.</span><span class="mi">3</span> <span class="k">else</span> <span class="n">StatusMsg</span><span class="o">.</span><span class="n">ERROR</span>
    <span class="n">status</span><span class="o">.</span><span class="n">finish</span><span class="p">()</span>
</pre></div>
</div>
<p>which will print 100 status bars and assign each the status <code class="docutils literal"><span class="pre">OK</span></code>
with 70% probability and an <code class="docutils literal"><span class="pre">ERROR</span></code> state with 30%. The
following predefined stati are available:</p>
<ul class="simple">
<li><code class="xref py py-attr docutils literal"><span class="pre">dnutils.console.StatusMsg.OK</span></code> - a green “OK” label</li>
<li><code class="xref py py-attr docutils literal"><span class="pre">dnutils.console.StatusMsg.ERROR</span></code> - a red “ERROR” label</li>
<li><code class="xref py py-attr docutils literal"><span class="pre">dnutils.console.StatusMsg.PASSED</span></code> - a green “PASSED” label</li>
<li><code class="xref py py-attr docutils literal"><span class="pre">dnutils.console.StatusMsg.FAILED</span></code> - a red “FAILED” label</li>
<li><code class="xref py py-attr docutils literal"><span class="pre">dnutils.console.StatusMsg.WARNING</span></code> - a yellow “WARNING” label</li>
</ul>
<p>For a particular <code class="docutils literal"><span class="pre">StatusMsg</span></code> instance, the set of available
stati can be customized by handing them over in the <code class="docutils literal"><span class="pre">stati</span></code>
parameter of the constructor. A status is just a (possibly ASCII
escaped color) string. So customized status labels can be
easily created.</p>
</div>
</div>
</div>
<div class="section" id="indices-and-tables">
<h1>Indices and tables<a class="headerlink" href="#indices-and-tables" title="Permalink to this headline">¶</a></h1>
<ul class="simple">
<li><a class="reference internal" href="genindex.html"><span class="std std-ref">Index</span></a></li>
<li><a class="reference internal" href="py-modindex.html"><span class="std std-ref">Module Index</span></a></li>
<li><a class="reference internal" href="search.html"><span class="std std-ref">Search Page</span></a></li>
</ul>
</div>


    </div>
      
  </div>
</div>
<footer class="footer">
  <div class="container">
    <p class="pull-right">
      <a href="#">Back to top</a>
      
    </p>
    <p>
        &copy; Copyright 2017, Daniel Nyga.<br/>
      Created using <a href="http://sphinx-doc.org/">Sphinx</a> 1.6.2.<br/>
    </p>
  </div>
</footer>
  </body>
</html>