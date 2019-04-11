from arpeggio.cleanpeg import ParserPEG, visit_parse_tree
from pypag.visitor import PagVisitor

class PagParser(ParserPEG):
  """Inherits from ParserPEG to define the rules made to support a PUG like
  syntax for writing templates easily.

  Instead of managing statements (conditions, loops and so on) itself, we left
  them untouched so the template backend will find and pick them at compile time.

  It helps to make this parser relatively small and easy to understand and you can still
  use your favorite backend capabilities.
  """

  def __init__(self, statement_expression='indent? "{" r\'[^}]+\' "}" EOL?'):
    """Initialize a new parser where statements will be kept intact.

    Args:
      statement_expression (string): Statement expression to capture them
    """

    super().__init__("""
root = (empty_line / multiline_string / expression / definition)+ EOF

EOL = r'\\n|\\r\\n'
indent = r'[ ]+'
spaces = r'[ ]*'
empty_line = spaces EOL

text = r'[^\\n\\r]*'
id = r'#[^. \\n\\r(]+'
class = r'\.[^#. \\n\\r(]+'
tag = r'[^ \\n\\r.#(]+'

attribute_name = r'[^=)]+'
bool = r'true|false|True|False'
string = r"'[^']+'|`[^`]+`"
number = r'[0-9.]+'
attribute_value = (bool / string / number)
attribute = spaces EOL? spaces attribute_name r'=?' attribute_value? spaces r',?' spaces EOL?
attributes = "(" attribute+ ")"

definition = indent? tag? (id / class)* attributes? r'[ ]?' text? EOL?
expression = %s
multiline_string = indent? "| " text EOL
""" % (statement_expression), 'root', skipws=False)

  def parse(self, source):
    """Parse the given input and returns the generated HTML.

    Args:
      source (str): Source to be parsed
    """
    return visit_parse_tree(super().parse(source), PagVisitor())