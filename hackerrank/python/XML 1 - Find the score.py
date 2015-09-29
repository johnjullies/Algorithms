# https://www.hackerrank.com/challenges/xml-1-find-the-score

import xml.etree.ElementTree as etree

xml = ""
for _ in range(int(input())): xml += input()
    
tree = etree.ElementTree(etree.fromstring(xml))
root = tree.getroot()

score = len(root.attrib)
for child in root.findall(".//"):
    score += len(child.attrib)
    
print(score)