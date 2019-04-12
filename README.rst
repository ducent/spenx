spenx
=====

Tiny template parser which will convert a `pugjs <https://github.com/kakulukia/pypugjs>`_ like syntax to HTML with the help of popular template engine (Jinja2 only at the time being).

In spenx, statements, like conditions and loops, are not processed and outputted "as it" to be processed by the template engine you wish to use.

At the time being, only Jinja2 has been tested but adding support for anything else should be easy.

Why another parser?
-------------------

I know there's a lot of port of jade, pugjs and so on for python. But everyone seems to be unmaintained. I really like the syntax use by pug and want something simplier and easier to maintain in the future with a strict set of features.

This is why the parser is defined using `Arpeggio <https://github.com/textX/Arpeggio>`_ and the cleanpeg syntax. It's easier to read, understand and maintain.

The spenx code is really tiny, check it yourself!

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