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
    tpl = env.get_template('page.pug')
    html = tpl.render(title='Spenx!', links=['home', 'about', 'contact'])

    expect(html).to.equal('<!DOCTYPE html><html><head><title>Spenx!</title><style href="style.css" rel="stylesheet" /></head><body><ul class="sidebar">\n\n<li><a href="/home" class="sidebar__nav-item">home</a></li>\n\n<li><a href="/about" class="sidebar__nav-item">about</a></li>\n\n<li><a href="/contact" class="sidebar__nav-item">contact</a></li>\n\n</ul><div id="content">\n\n<form action="/signup"><input type="text" required class="control" /><input type="password" class="control" /><button type="submit">Sign up!</button></form>\n\n</div><footer>\n\n<p><small>This is the footer</small></p>\n\n</footer></body></html>')

  def test_it_should_not_process_file_with_an_unknown_extension(self):
    tpl = env.get_template('raw.html')
    html = tpl.render()

    expect(html).to.equal('<p>This file should not be processed by the spenx jinja2 extension since it uses a <code>.html</code> extension</p>')