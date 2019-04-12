from spenx.parser import Parser, MAKO_STATEMENT

# instantiate once
mako_parser = Parser(MAKO_STATEMENT)

def preprocessor(source):
  return mako_parser.parse(source)