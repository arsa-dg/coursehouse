def toGraph(filename):
  theString = []
  with open(filename,'r') as file:
    for line in file:
      theString.append(line.replace(", ", " ")
      .replace(".", "").replace("\n", ""));

  return theString

def nodeList(theList):
  theString = ""
  for i in theList:
    theString += i + " "
  
  toSet = theString.split()
  return list(set(toSet))

def graphAlaAla(theList, listOfNode):
  result = []
  for every in theList:
    tmpEvery = every.split()
    if (len(tmpEvery) > 2):
      for i in range(1,len(tmpEvery)):
        for j in range(len(listOfNode)):
          if tmpEvery[i] == listOfNode[j]:
            node = j
          if tmpEvery[0] == listOfNode[j]:
            busur = j
        result.append([node, busur])

    else:
      if (len(tmpEvery) == 2):
        for k in range(len(listOfNode)):
          if tmpEvery[1] == listOfNode[k]:
            node = k
          if tmpEvery[0] == listOfNode[k]:
            busur = k
      
        result.append([node, busur])

      else:
        for l in range(len(listOfNode)):
          if tmpEvery[0] == listOfNode[l]:
            result.append([l])

  result.sort()
  return result

# bener
def nextisVisitedList(index, graf):
  result = []
  for x in graf:
    if ((index == x[0]) and (len(x) == 2)):
      result.append(x)

  return result

def topSort(isVisitedList, graf):
  ordering = [0 for x in isVisitedList]
  z = len(isVisitedList)-1
  
  for i in range(len(isVisitedList)):
    if (isVisitedList[i] == False):
      visitedNodes = []
      dfs(i, isVisitedList, visitedNodes, graf)
      for nodeId in visitedNodes:
        ordering[z] = nodeId
        z = z-1
  
  return ordering

def dfs(i, isVisitedList, visitedNodes, graf):
  isVisitedList[i] = True

  nextList = nextisVisitedList(i, graf)
  
  for j in range(len(nextList)):
    if isVisitedList[nextList[j][1]] == False:
      dfs(nextList[j][1], isVisitedList, visitedNodes, graf)

  visitedNodes.append(i) 

listFromFile = toGraph("tes.txt")
print(listFromFile)

print("listofnode")
listOfNode = nodeList(listFromFile)
print(listOfNode)

print("isVisitedList")
isVisitedList = [False for x in range(len(listOfNode))]
print(isVisitedList)

print("directed graf representation in list")
graf = graphAlaAla(listFromFile, listOfNode)
print(graf)


print("hasil")

hasil = topSort(isVisitedList, graf)
print(hasil)