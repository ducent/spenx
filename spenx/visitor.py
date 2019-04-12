from arpeggio.peg import PTNodeVisitor

class HtmlVisitor(PTNodeVisitor):
  """Tree visitor used to constructs the HTML output based on the DSL.

  The syntax is pretty easy and the parser is tight but it should cover the vast
  majority of use cases.
  """
  
  def __init__(self):
    super().__init__()

    # This stack is here to keep track of which tag has been opened
    # and not yet closed.
    self._tag_stack = []

  def _open_tag(self, tag, children):
    """This is where the opening tag is created by appending all attributes.

    Args:
      tag (string): Tag to open
      children (SemanticActionResults): Collected children
    """
    yield '<%s' % tag # Write opening tag

    # Process any attributes
    if children.attributes:
      for name, value in children.attributes[0]:
        # Specific case when attributes contains shortcut names
        if name in ['id', 'class']:
          if name not in children.results:
            children.results[name] = []
          
          children.results[name].append(value)
        elif value == True: # Specific case for boolean values such as disabled
          yield ' {name}'.format(name=name)
        elif value != False:
          yield ' {name}="{value}"'.format(name=name, value=value)

    # Process shortcuts (id and classes)
    if children.id:
      yield ' id="%s"' % children.id[0] # only the first id is taken

    klass = children.results.get('class')

    if klass:
      yield ' class="%s"' % ' '.join(klass)

    # And yield any inner text
    if children.text:
      yield '>%s' % ''.join(children.text)

  def _close_parent_tags(self, indent):
    """Close any tags that are higher in the tree that the current indent level.

    Args:
      indent (int): Current number of indentation
    """
    # Retrieve the last known indent level
    last_indent, _, has_child = self._tag_stack[-1] if self._tag_stack else (0, None, False)

    # We have a superior nesting so the last opened tag now has children.
    # If it doesn't have text, it means we should close the opening tag now.
    if indent > last_indent and not has_child:
      yield '>'

    while(self._tag_stack):
      if self._tag_stack[-1][0] >= indent:
        tag_indent, tag, has_child = self._tag_stack.pop()

        if last_indent == tag_indent and not has_child: # Handle self closing tags!
          yield ' />'
        else:
          yield '</%s>' % tag

        last_indent = tag_indent
      else:
        break

  def visit_attributes(self, node, children):
    return children.attribute

  def visit_attribute(self, node, children):
    # Make a tuple of name, value and accept a shortcut for booleans
    return (children.attribute_name[0], children.attribute_value[0] if children.attribute_value else True)

  def visit_EOF(self, node, children):
    yield from self._close_parent_tags(0)

  def visit_tag(self, node, children):
    return node.value

  def visit_string(self, node, children):
    return node.value[1:-1] # Remove enclosing quotes

  def visit_bool(self, node, chidren):
    return node.value.lower() == 'true' # Convert to a true bool

  def visit_id(self, node, children):
    return node.value[1:]

  def visit_class(self, node, children):
    return node.value[1:]

  def visit_indent(self, node, children):
    return len(node.value) # Count current indentation level

  def visit_empty_line(self, node, children):
    return None

  def visit_multiline_string(self, node, children):
    yield from self._close_parent_tags(children.indent[0] if children.indent else 0)
    # This one is a bit tricky! We have match a multiline string so we want to
    # make sure the last remining tag (the parent one) will let know others it has at least one child
    # now so the closing tag will match correctly.
    if self._tag_stack:
      self._tag_stack[-1] = self._tag_stack[-1][:-1] + (True, )
    yield children.text[0]

  def visit_expression(self, node, children):
    yield from self._close_parent_tags(children.indent[0] if children.indent else 0)
    # Same as multiline string, especially when an expression is the last member
    if self._tag_stack:
      self._tag_stack[-1] = self._tag_stack[-1][:-1] + (True, )
    # Expression are left untouched, just dismiss indents and EOL
    yield '\n%s\n' % ''.join([n.value for n in node if n.rule_name not in ['indent', 'EOL']])

  def visit_definition(self, node, children):
    indent = children.indent[0] if children.indent else 0
    tag = children.tag[0] if children.tag else 'div'

    yield from self._close_parent_tags(indent)

    # Append the current tag to the stack to keep track of what should be closed
    self._tag_stack.append((indent, tag, len(children.text) > 0))

    yield from self._open_tag(tag, children)
  
  def visit_root(self, node, children):
    return ''.join([''.join(c) for c in children]).strip()