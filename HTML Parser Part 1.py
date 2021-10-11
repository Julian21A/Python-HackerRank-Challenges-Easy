from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, atributos):
        print ('Start :', tag)
        for i in atributos:
            print ('->', i[0], '>', i[1])

    def handle_endtag(self, tag):
        print ('End   :', tag)

    def handle_startendtag(self, tag, atributos):
        print ('Empty :', tag)
        for i in atributos:
            print ('->', i[0], '>', i[1])


parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())