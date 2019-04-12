from spenx.parser import Parser
from bs4 import BeautifulSoup

parser = Parser(statement_expression='indent? "%" r"[^\\n\\r]+" EOL')
html = parser.parse("""
| <!DOCTYPE html>
  html(lang='en')
    head
      meta(charset='utf-8')
      title My first spenx webpage!
    body
      h1 spenx
      p.welcome
        | Did I said you'll feel right at home if you're using pugjs? 
        | Because I guess that's right!
      .container
        p Without a tag defined, div will be assumed 
          strong pretty cool huh?
""")

soup = BeautifulSoup(html, 'html.parser')

print (html)
print (soup.prettify())