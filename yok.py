import re

#mencari list matkul yang ada
def courseList(filename):
  theString = ''
  with open(filename,'r') as file:
    for line in file:
      theString += line

  theList = re.split(', |\n', theString)
  return theList


print(courseList("tes.txt"))