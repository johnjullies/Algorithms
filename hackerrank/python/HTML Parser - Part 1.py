# https://www.hackerrank.com/challenges/html-parser-part-1/

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start :', tag)
        for attr in attrs:
                print ('->',' > '.join(map(str, attr)))
    def handle_endtag(self, tag):
        print('End   :', tag)
    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        for attr in attrs:
                print('->',' > '.join(map(str,attr)))

html = ""
for i in range(int(input())):
    html += input()


parser = MyHTMLParser()
parser.feed(html)
parser.close()