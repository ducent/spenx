from pypag.parser import PagParser
from jinja2.ext import Extension

class PagExtension(Extension):
  def __init__(self, environment):
    super().__init__(environment)

    self._parser = PagParser()

  def preprocess(self, source, name, filename=None):
    return self._parser.parse(source)