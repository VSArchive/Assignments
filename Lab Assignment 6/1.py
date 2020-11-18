import xml.sax


class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            print("Movie : ")
            title = attributes["title"]
            print("\tTitle :", title)

    def endElement(self, tag):
        if self.CurrentData == "type":
            print("\tType :", self.type)
        elif self.CurrentData == "format":
            print("\tFormat :", self.format)
        elif self.CurrentData == "year":
            print("\tYear :", self.year)
        elif self.CurrentData == "rating":
            print("\tRating :", self.rating)
        elif self.CurrentData == "stars":
            print("\tStars :", self.stars)
        elif self.CurrentData == "description":
            print("\tDescription :", self.description)
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content


parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
Handler = MovieHandler()
parser.setContentHandler(Handler)
parser.parse("movies.xml")
