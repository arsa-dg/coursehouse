def toGraph(filename):
  theString = []
  with open(filename,'r') as file:
    for line in file:
      theString.append(line.replace(', ', ' ')
      .replace('.', '').replace('\n', ''));

  return theString

def nodeList(theList):
  theString = ''
  for i in theList:
    theString += i + ' '
  
  toSet = theString.split()
  return list(set(toSet))

def graphInList(theList, listOfNode):
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
def nextisVisitedList(index, graphRepre):
  result = []
  for x in graphRepre:
    if ((index == x[0]) and (len(x) == 2)):
      result.append(x)

  return result

def DFSAlgorithm(i, isVisitedList, visitedNodes, graphRepre):
  isVisitedList[i] = True

  nextList = nextisVisitedList(i, graphRepre)
  
  for j in range(len(nextList)):
    if isVisitedList[nextList[j][1]] == False:
      DFSAlgorithm(nextList[j][1], isVisitedList, visitedNodes, graphRepre)

  visitedNodes.append(i) 

def topSort(isVisitedList, graphRepre):
  theOrder = []
  
  for i in range(len(isVisitedList)):
    if (isVisitedList[i] == False):
      visitedNodes = []
      DFSAlgorithm(i, isVisitedList, visitedNodes, graphRepre)
      
      for nodeId in visitedNodes:
        theOrder.append(nodeId)
  
  theOrder.reverse()
  return theOrder

def printResult(resultList, listOfNode):
  for i in range(len(resultList)):
    print('Semester {}: {}'.format(i+1, listOfNode[result[i]]))


#main program
txtfile = input('Masukkan nama file yang terletak di folder /test/ (contoh: 1.txt) : ')
source = 'test/'+txtfile

try:
  open(source)
except:
  source = '../test/'+txtfile
try:
  open(source)
except:
  source = 'Tucil2_13519037/test/'+txtfile

listFromFile = toGraph(source)
listOfNode = nodeList(listFromFile)
isVisitedList = [False for x in range(len(listOfNode))]
graphRepre = graphInList(listFromFile, listOfNode)
result = topSort(isVisitedList, graphRepre)

# print(listFromFile)

# print('listofnode')

# print(listOfNode)

# print('isVisitedList')

# print(isVisitedList)

# print('directed graph representation in list')

# print(graphRepre)


# print('hasil')

print(result)
printResult(result, listOfNode)