#!/usr/bin/env python
import socket

with file("/usr/share/dict/words") as wordlist:
  words = [ w.strip() for w in wordlist.readlines() ]

def find_domains(extension):
  matches = [ word for word in words if word.endswith(extension) ]
  for match in matches:
    domain = match[0:len(match)-len(extension)] + "." + extension
    fail = "67.215.65.132"
    try:
      if(fail == socket.gethostbyname(domain)):
        yield domain
    except:
      yield domain


if __name__ == '__main__':
  import sys
  for arg in sys.argv[1:]:
    print "%s\n----------\n" % arg
    for domain in sorted(find_domains(arg), key=len):
      print "\t%s" % domain
