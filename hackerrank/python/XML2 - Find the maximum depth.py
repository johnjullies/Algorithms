# https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/

from xml.etree.ElementTree import XMLParser

class MaxDepth:
    maxDepth = 0
    depth = 0
    def start(self, tag, attrib):   # Called for each opening tag.
        self.depth += 1
        if self.depth > self.maxDepth:
            self.maxDepth = self.depth
    def end(self, tag):             # Called for each closing tag.
        self.depth -= 1
    def data(self, data):
        pass            # We do not need to do anything with data.
    def close(self):    # Called when all data has been parsed.
        return self.maxDepth

target = MaxDepth()
parser = XMLParser(target=target)
xml = ""
for _ in range(int(input())): xml += input()

parser.feed(xml)
print(parser.close() - 1)