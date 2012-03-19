#!/usr/bin/env python
import re
def change_grade(stdin, nameToFind, gradeChange):
      for availLine in stdin:
            if re.search(name, availLine):
                  stdout.write(re.sub("[0-9].", grade, availLine))
            else:
                  stdout.write(availLine)

if __name__ == '__main__':
      from sys import stdin,stdout,stderr, argv, exit
      import os.path
      if len(argv) > 3:    
            scriptName=argv[0]
            name=argv[1]
            grade=argv[2]
            fileName=argv[3]
            #if exists.      
            if os.path.exists(fileName):
                  #Print reading lines from file.  Switch file to over to stdin
                  stdin=file(fileName)
            else:
                  #Print error and exit.
                  stderr.write(scriptName + ": " + fileName + ": no such file or directory \n")
                  exit(1)
      else: 
            stderr.write("Change arguments to <name of kid> <grade %> <file report card>")
      change_grade(stdin, name, grade)
      exit(0)    



