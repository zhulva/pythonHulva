__author__ = 'student'
#from __future__ import unicode_literals
import xml.sax
s = open("new.xml",'r')
pole_book=[]
file = "new.xml"
for line in s:
     nacteno = ' %s' % line
     print(nacteno, end="")

class XMLContextHandler(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.element = None
        self.user_name = None
        self.user_title = None
        self.genre = None
        self.prize = None
        self.publish_date = None

    def startElement(self, name, attrs):
        self.element = name

    def endElement(self, name):
        self.element = None
        if name =='book':
            self.pole_array=[self.user_name,self.user_title,self.genre,self.prize,self.publish_date]
            pole_book.append(self.pole_array)

    def characters(self, content):
        if self.element == 'author':
            self.user_name = content
            #self.veta_array[self.user_name,]
        if self.element == 'title':
            self.user_title = content
        if self.element == 'genre':
            self.genre = content
        if self.element == 'prize':
            self.prize = content
        if self.element == 'publish_date':
            self.publish_date = content

f = open("new.xml", "r")
xml.sax.parse(f, XMLContextHandler())
print(pole_book, end="")
f.close()

file = open("new1.xml", "w")
file.write("<category>\n")
file.write("<book>\n")
file.write("<author>Mr_Noboby</author>\n")
file.write("<title>XML Developer's Guide</title>\n")
file.write("<genre>Computer</genre>\n")
file.write("<price>44.95</price>\n")
file.write("<publish_date>2015-09-19</publish_date>\n")
file.write("</book>\n")
file.write("</category>\n")
file.close()

nfile = open("new1.xml", "r")
xml.sax.parse(nfile, XMLContextHandler())
print(pole_book, end="")
nfile.close()
