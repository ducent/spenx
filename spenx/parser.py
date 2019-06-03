from arpeggio.cleanpeg import ParserPEG, visit_parse_tree
from spenx.visitor import HtmlVisitor

JINJA_STATEMENT = 'indent? r"{.+}" EOL?'
MAKO_STATEMENT = 'indent? (r"<%[\w\W]*%>" / r"</?%.*>" / r"%.*") EOL?'

class Parser(ParserPEG):
  """Inherits from ParserPEG to define the rules made to support a PUG like
  syntax for writing templates easily.

  Instead of managing statements (conditions, loops and so on) itself, we left
  them untouched so the template backend will find and pick them at compile time.

  It helps to make this parser relatively small and easy to understand and you can still
  use your favorite backend capabilities.
  """

  def __init__(self, statement_expression=JINJA_STATEMENT):
    """Initialize a new parser where statements will be kept intact.

    Args:
      statement_expression (string): Statement expression to capture them
    """

    super().__init__("""
root = (empty_line / multiline_string / expression / silent_comment / comment / html / definition)+ EOF

EOL = r'\\n|\\r\\n'
indent = r'\s+'
spaces = r'[ \t]*'
empty_line = spaces EOL

text = r'[^\\n\\r]*'
id = r'#[^. \\n\\r(]+'
class = r'\.[^#. \\n\\r(]+'
tag = r'[^ \\n\\r.#(]+'

attribute_name = r'[^=), ]+'
bool = r'true|false|True|False'
string = r"'.*?'|`.*?`"
number = r'[\d.]+'
attribute_value = (bool / string / number)
attribute = spaces EOL? spaces attribute_name r'=?' attribute_value? spaces r',?' spaces EOL?
attributes = "(" attribute+ ")"

comment_line = "//" text EOL?
comment = (indent? comment_line)+

silent_comment_line = "//-" text EOL?
silent_comment = (indent? silent_comment_line)+

html_tag = r'[^>]*'
html = indent? "<" html_tag ">" EOL?

definition = indent? tag? (id / class)* attributes? r'[ ]?' text? EOL?
expression = %s
multiline_string = indent? "| " text EOL
""" % (statement_expression), 'root', skipws=False)

  def parse(self, source, file_name=None):
    """Parse the given input and returns the generated HTML.

    Args:
      source (str): Source to be parsed
    """
    return visit_parse_tree(super().parse(source), HtmlVisitor())