from sure import expect
from jinja2 import Environment, FileSystemLoader
from spenx.ext.jinja import Spenx
import os

env = Environment(
  loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'jinja')),
  extensions=[Spenx],
)

class TestJinja:

  def test_it_should_render_template_correctly(self):
    tpl = env.get_template('page.html')
    html = tpl.render(title='Spenx!', links=['home', 'about', 'contact'])

    expect(html).to.equal('<html><head><title>Spenx!</title><style href="style.css" rel="stylesheet" /></head><body><ul class="sidebar">\n\n<li><a href="/home" class="sidebar__nav-item">home</a></li>\n\n<li><a href="/about" class="sidebar__nav-item">about</a></li>\n\n<li><a href="/contact" class="sidebar__nav-item">contact</a></li>\n\n</ul><div id="content">\n\n<form action="/signup"><input type="text" required class="control" /><input type="password" class="control" /><button type="submit">Sign up!</button></form>\n\n</div><footer>\n\n<p><small>This is the footer</small></p>\n\n</footer></body></html>')