__author__ = 'Zdenďż˝k'
s = open("new.xml",'r')
for line in s:
     nacteno = 'NaÄŤteno: %s' % line
     print(nacteno, end="")
