from sure import expect
from pypag.parser import PagParser

parser = PagParser()

class TestPagParser:

  def test_it_should_handle_basic_tags_nesting(self):
    html = parser.parse("""
body
  p
    a
      small With some text
  footer
    p The footer
""")

    expect(html).to.equal('<body><p><a><small>With some text</small></a></p><footer><p>The footer</p></footer></body>')

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

    expect(html).to.equal('<head><script src="/somewhere/else.js" type="text/javascript"></script></head>')
  
  def test_it_should_handle_number_attributes(self):
    html = parser.parse("""
input(type='number', value=6)
""")

    expect(html).to.equal('<input type="number" value="6"></input>')
  
  def test_it_should_handle_bool_attributes(self):
    html = parser.parse("""
form
  input.control(required=True, disabled=false, shortcut)
""")

    expect(html).to.equal('<form><input required shortcut class="control"></input></form>')

  def test_it_should_leave_expressions_intact(self):
    html = parser.parse("""
ul.sidebar(class='{{sidebar_classname}}')
  {% for link in links %}
  li
    a(href='/{{link}}') {{link}}
  {% endfor %}
""")

    expect(html).to.equal('<ul class="sidebar {{sidebar_classname}}">{% for link in links %}<li><a href="/{{link}}">{{link}}</a></li>{% endfor %}</ul>')