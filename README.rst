spenx |travis| |cover| |pypi| |license|
===========================================

.. |travis| image:: https://travis-ci.org/ducent/spenx.svg?branch=master
    :target: https://travis-ci.org/ducent/spenx

.. |cover| image:: https://codecov.io/gh/ducent/spenx/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/ducent/spenx

.. |pypi| image:: https://badge.fury.io/py/spenx.svg
    :target: https://badge.fury.io/py/spenx

.. |license| image:: https://img.shields.io/badge/License-GPL%20v3-blue.svg
    :target: https://www.gnu.org/licenses/gpl-3.0

Tiny template parser which will convert a `pugjs <https://github.com/kakulukia/pypugjs>`_ like syntax to HTML with the help of popular template engines.

In spenx, statements, like conditions and loops, are not processed and outputted "as it" to be processed by the template engine you wish to use.

At the time being, only **Jinja2** and **Mako** has been tested but adding support for anything else should be easy.

Why another parser?
-------------------

I know there's a lot of port of jade, pugjs and so on for python. But everyone seems to be unmaintained. I really like the syntax use by pug and want something simplier and easier to maintain in the future with a strict set of features.

This is why the parser is defined using `Arpeggio <https://github.com/textX/Arpeggio>`_ and the cleanpeg syntax. It's easier to read, understand and maintain.

The spenx code is really tiny, check it yourself!

Installation
------------

.. code-block:: console

  $ pip install spenx

Usage
-----

Using spenx is fairly easy:

.. code-block:: python

  from spenx import Parser

  # Without backend
  parser = Parser()

  parser.parse("""
  p Hello world
  """)

  # => <p>Hello world</p>

  # Using jinja2
  from spenx.ext.jinja import Spenx
  from jinja import Environment

  env = Environment(
    # Common jinja parameters
    extensions=[Spenx], # And the spenx extension
  )

  # Only preprocess files with given extensions
  env.spenx_process_extensions = ['.pug', '.spenx'] # Those are the default

  # And use env.get_template and render as usual

  # Using mako
  from spenx.ext.mako import preprocessor
  from mako.template import Template

  tpl = Template("p Hello world", preprocessor=preprocessor)

  # And use render as usual

Syntax
------

If you're already using pugjs, you should feel familiar with the syntax (see the `tests/` folder for more insights).

*For the moment, you should use the multiline string to handle the doctype but that may change in the future.*

.. code-block:: text

  | <!DOCTYPE html>
  html(lang='en')
    head
      meta(charset='utf-8')
      title My first spenx webpage!
    body
      h1 spenx
      p.welcome
        | Did I said you'll feel right at home if you're using pugjs? 
        | Because I guess that's right!
      .container
        p Without a tag defined, div will be assumed 
          strong pretty cool huh?

And this is what's rendered by spenx:

.. code-block:: text

  <!DOCTYPE html><html lang="en"><head><meta charset="utf-8" /><title>My first spenx webpage!</title></head><body><h1>spenx</h1><p class="welcome">Did I said you'll feel right at home if you're using pugjs? Because I guess that's right!</p><div class="container"><p>Without a tag defined, div will be assumed <strong>pretty cool huh?</strong></p></div></body></html>

And after using BeautifulSoup:

.. code-block:: text

  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="utf-8"/>
    <title>
    My first spenx webpage!
    </title>
  </head>
  <body>
    <h1>
    spenx
    </h1>
    <p class="welcome">
    Did I said you'll feel right at home if you're using pugjs? Because I guess that's right!
    </p>
    <div class="container">
    <p>
      Without a tag defined, div will be assumed
      <strong>
      pretty cool huh?
      </strong>
    </p>
    </div>
  </body>
  </html>

Testing
-------

.. code-block:: bash

  $ pip install -e .[test]
  $ python -m nose --with-doctest -v --with-coverage --cover-package=spenx