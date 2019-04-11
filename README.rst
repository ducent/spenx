pypag
=====

Tiny template parser which will convert a pugjs like syntax to HTML with the help of popular template engine (Jinja2 only at the time being).

In pypag, statements, like conditions and loops, are the one defined by the engine you wish to use so you can use its full power, they will not be processed by the parser.

At the time being, only Jinja2 has been tested but adding support for anything else should be easy.

The parser is defined using `Arpeggio <https://github.com/textX/Arpeggio>`_ and the cleanpeg syntax so it's easier to read, understand and maintain.

Syntax
------

If you're already using pugjs, you should feel familiar with the syntax (see the `tests/` folder for more insights).

*For the moment, you should use the multiline string to handle the doctype but that may change in the future. Self-closing tags are in my todo list too BTW.*

.. code-block:: text

  | <!DOCTYPE html>
  html(lang='en')
    head
      meta(charset='utf-8')
      title My first pypag webpage!
    body
      h1 pypag
      p.welcome
        | Did I said you'll feel right at home if you're using pugjs? 
        | Because I guess that's right!
      .container
        p Without a tag defined, div will be assumed 
          strong pretty cool huh?

And this is what's rendered (after a prettify with BeautifulSoup since pypag will output everything in one line):

.. code-block:: text

  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="utf-8"/>
    <title>
    My first pypag webpage!
    </title>
  </head>
  <body>
    <h1>
    pypag
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