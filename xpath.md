# overview
XPath is really very simple: you just string together conditions. Evaluation begins with a set of nodes so far. Then a new set of nodes is selected based on the given ones, and the condition is checked on this new set.


# absolute vs relative
absolute: /html/body/div[x]/div[y]/
relative: //tagname[@attribute='value']

//: match any descendant node
/: match only child nodes

@: select an attribute, like //div[@class='thumbnail'] or //a[@href='https://example.com']

..: get parent of currently active node, //span[@class='u-textScreenReader']/.. 

elements are 1-indexed, not 0-indexed

contains: search for string A in string B, where contains(B, A), //div/a/span[contains(text(), 'Homepage')]


# resources
http://plasmasturm.org/log/xpath101/ (linked from scrapy docs)
http://zvon.org/comp/r/tut-XPath_1.html (linked from scrapy docs)