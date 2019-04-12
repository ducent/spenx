from sure import expect
from spenx.ext.mako import preprocessor
from mako.lookup import TemplateLookup
from mako.template import Template
import os

lookup = TemplateLookup(
  directories=[(os.path.join(os.path.dirname(__file__), 'mako'))], 
  preprocessor=preprocessor
)

class TestMako:

  def test_it_should_render_template_correctly(self):
    tpl = lookup.get_template('page.html')
    html = tpl.render(title='Spenx!', links=['home', 'about', 'contact'])

    expect(html).to.equal('<!DOCTYPE html><html><head>\n\n<title>Spenx! from Mako template!</title></head><body><ul class="sidebar">\n<li><a href="/home" class="sidebar__nav-item">home</a></li>\n<li><a href="/about" class="sidebar__nav-item">about</a></li>\n<li><a href="/contact" class="sidebar__nav-item">contact</a></li>\n</ul><div id="content">\n\n<form action="/signup"><input type="text" required class="control" /><input type="password" class="control" /><button type="submit">Sign up!</button></form>\n\n</div><footer>\n\n<p><small>This is the footer</small></p>\n\n</footer></body></html>')