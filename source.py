#!/usr/bin/env python
import webbrowser
import re
import time

inputHtml = open("input.html", "r")
link = []
for line in inputHtml:
    if re.match("(.*)mp4(.*)", line):
        r = re.compile('href="(.*?)"')
        m = r.search(line)
        if m:
            link.append(m.group(1))

for items in link: 
    webbrowser.open(items)
    time.sleep(5)
