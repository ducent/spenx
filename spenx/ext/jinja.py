from spenx.parser import Parser, JINJA_STATEMENT
from jinja2.ext import Extension

class Spenx(Extension):
  def __init__(self, environment):
    super().__init__(environment)

    self._parser = Parser(statement_expression=JINJA_STATEMENT)

  def preprocess(self, source, name, filename=None):
    return self._parser.parse(source)