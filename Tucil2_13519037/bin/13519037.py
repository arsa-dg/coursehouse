# load text dalam file
def toGraph(filename):
  theString = []
  with open(filename,'r') as file:
    for line in file:
      theString.append(line.replace(',',' ').replace(', ', ' ')
      .replace('.', '').replace('\n', ''));

  return theString

# membuat list daftar mata kuliah yang ada (unik) menggunakan set 
def nodeList(theList):
  theString = ''
  for i in theList:
    theString += i + ' '
  
  toSet = theString.split()
  result = list(set(toSet))

  result.sort()

  return result

# merepresentasikan graph berarah dalam bentuk list 2 dimensi. Dalam setiap list 
# Index pertama sebagai Matakuliah, indeks berikutnya sebagai prerequisite dari mata kuliah tersebut
def graphInList(theList, listOfNode):
  result = []
  for every in theList:
    tmpEvery = every.split()
    tmp = []
    for inside in tmpEvery:
      for i in range(len(listOfNode)):
        if inside == listOfNode[i]:
          tmp.append(i)

    result.append(tmp)

  return result

# pendekatan topological sort
def topSort(graphRepre):
  theOrder = []
  deg0 = []

  # mencari mata kuliah yang memiliki derajat masuk 0 atau tidak memiliki prerequisite
  # termasuk jika prerequisite sudah terpenuhi
  for i in range(len(graphRepre)):
    if len(graphRepre[i]) == 1:
      deg0 += graphRepre[i]
  
  # menghapus mata kuliah yang berderajat masuk 0 dalam graf
  if len(deg0) > 0:
    for j in range(len(deg0)):
      graphRepre.remove([deg0[j]])

      for every in graphRepre:
        if (len(every) > 1 and deg0[j] in every):
          every.remove(deg0[j])

    theOrder.append(deg0)

  # jika dalam 1 semester memiliki lebih dari satu mata kuliah yang tidak memiliki prerequisite
  if (len(graphRepre) > 0):
    nextOrder = topSort(graphRepre)
    theOrder += nextOrder
  
  return theOrder

# mencetak hasil sort
def printResult(resultList, listOfNode):
  print("   ,-,--.   .=-.-.         ,-.--, ")
  print(" ,-.'-  _\ /==/_ /.--.-.  /=/, .' ")
  print("/==/_ ,_.'|==|, | \==\ -\/=/- /   ")
  print("\==\  \   |==|  |  \==\ `-' ,/    ")
  print(" \==\ -\  |==|- |   |==|,  - |    ")
  print(" _\==\ ,\ |==| ,|  /==/   ,   \   ")
  print("/==/\/ _ ||==|- | /==/, .--, - \  ")
  print("\==\ - , //==/. / \==\- \/=/ , /  ")
  print(" `--`---' `--`-`   `--`-'  `--`   ")

  print()

  for i in range(len(resultList)):
    print('Semester {}: '.format(i+1), end='')
    for j in range(len(resultList[i])):
      print('{}'.format(listOfNode[resultList[i][j]]), end='')
      if (j != len(resultList[i])-1):
        print(', ', end='')
    print()


#main program
if __name__ == "__main__":
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

  graphRepre = graphInList(listFromFile, listOfNode)
  result = topSort(graphRepre)

  printResult(result, listOfNode)