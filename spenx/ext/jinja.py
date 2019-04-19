from spenx.parser import Parser, JINJA_STATEMENT
from jinja2.ext import Extension
from os.path import splitext

class Spenx(Extension):
  def __init__(self, environment):
    super().__init__(environment)

    # Extend the environment
    environment.extend(spenx_process_extensions=['.pug', '.spenx'])

    self._parser = Parser(statement_expression=JINJA_STATEMENT)

  def preprocess(self, source, name, filename=None):
    _, ext = splitext(name)

    # Only preprocess files with allowed extensions
    if ext in self.environment.spenx_process_extensions:
      return self._parser.parse(source)
    
    return source