__author__ = 'Zdeněk'
file.parse(s, XMLContextHandler())

class XMLContextHandler(new.xml.ContentHandler):
    def __init__(self):
        new.xml.ContentHandler.__init__(self)
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

print(pole_book, end="")
s.close()
