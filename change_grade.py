#!/usr/bin/env python

from sys import stdin,stdout,stderr, argv, exit
import re
import os.path

scriptName=argv[0]
name=argv[1]
grade=argv[2]

#Check if received atleast one argument.
if len(argv) > 3:
      fileName=argv[3]
      #if exists.      
      if os.path.exists(fileName):
            #Print reading lines from file.  Switch file to over to stdin
            stdin=file(fileName)
      else:
            #Print error and exit.
            stderr.write(scriptName + ": " + fileName + ": no such file or directory \n")
            exit(1)      

linecount=0;
#print line by line.
for availLine in stdin:
      if re.search(name, availLine):
            stdout.write(re.sub("[0-9].", grade, availLine))
      else:
            stdout.write(availLine)
exit(0)
