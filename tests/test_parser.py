from sure import expect
from spenx.parser import Parser

parser = Parser()

class TestParser:

  def test_it_should_handle_basic_tags_nesting(self):
    html = parser.parse("""
body
  p
    a
      small With some text
      img
  footer
    p The footer
""")

    expect(html).to.equal('<body><p><a><small>With some text</small><img /></a></p><footer><p>The footer</p></footer></body>')

  def test_it_should_handle_comments(self):
    html = parser.parse("""
body
  // A comment
  div
    p Hello, world!
  // A comment on
  // multiple lines
  p Hello again
""")

    expect(html).to.equal('<body><!-- A comment--><div><p>Hello, world!</p></div><!-- A comment on multiple lines--><p>Hello again</p></body>')

  def test_it_should_handle_silent_comments(self):
    html = parser.parse("""
body
  //- A silent comment
  p Hello, world!
  //- This comment should not be outputted either
  p Hello again
""")
    expect(html).to.equal('<body><p>Hello, world!</p><p>Hello again</p></body>')

  def test_it_should_handle_id_and_classes_with_shortcuts(self):
    html = parser.parse("""
div#content.wrapper.container
  p.excerpt This is some excerpt
  p And nothing special here
""")

    expect(html).to.equal('<div id="content" class="wrapper container"><p class="excerpt">This is some excerpt</p><p>And nothing special here</p></div>')

  def test_it_should_use_div_tag_when_no_one_is_specified(self):
    html = parser.parse("""
.container
  .row
    .col First column
    .col Second column
""")

    expect(html).to.equal('<div class="container"><div class="row"><div class="col">First column</div><div class="col">Second column</div></div></div>')
  
  def test_it_should_handle_multiline_string_and_preserve_whitespaces(self):
    html = parser.parse("""
p
  | Use the pipe to keep whitespaces 
  | so the trailing space in the above line 
  | is preserved.
""")

    expect(html).to.equal('<p>Use the pipe to keep whitespaces so the trailing space in the above line is preserved.</p>')

  def test_it_should_handle_string_attributes(self):
    html = parser.parse("""
head
  script(src='/somewhere/else.js', type=`text/javascript`)
""")

    expect(html).to.equal('<head><script src="/somewhere/else.js" type="text/javascript" /></head>')
  
  def test_it_should_handle_number_attributes(self):
    html = parser.parse("""
input(type='number', value=6)
""")

    expect(html).to.equal('<input type="number" value="6" />')
  
  def test_it_should_handle_bool_attributes(self):
    html = parser.parse("""
form
  input.control(required=True, disabled=false, shortcut, id='someid')
""")

    expect(html).to.equal('<form><input required shortcut id="someid" class="control" /></form>')

  def test_it_should_leave_expressions_intact(self):
    html = parser.parse("""
ul.sidebar(class='{{ sidebar_classname | upper }}')
  {% for link in links %}
  li
    a(href='/{{link}}') {{link}}
  {% endfor %}
""")

    expect(html).to.equal('<ul class="sidebar {{ sidebar_classname | upper }}">\n{% for link in links %}\n<li><a href="/{{link}}">{{link}}</a></li>\n{% endfor %}\n</ul>')

  def test_it_should_handle_empty_attributes(self):
    html = parser.parse("""
form(action='', method='post')
""")

    expect(html).to.equal('<form action="" method="post" />')