from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement

movies = collection.getElementsByTagName("movie")

for movie in movies:
    print("Movie : ")

    if movie.hasAttribute("title"):
        print("\tTitle :", movie.getAttribute("title"))

    type = movie.getElementsByTagName('type')[0]
    print("\tType :", type.childNodes[0].data)

    format = movie.getElementsByTagName('format')[0]
    print("\tFormat :", format.childNodes[0].data)

    description = movie.getElementsByTagName('description')[0]
    print("\tDescription :", description.childNodes[0].data)
