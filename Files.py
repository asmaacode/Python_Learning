def createTheFile(text):
    with open("testFile.txt","w") as file:
      file.write(text) 

def readFileLines():
    with open("testFile.txt","r") as file:
      return file.readlines()

def findAllWordsFrequency (wordsList):
  notYet=""
  for word in wordsList:
    if word not in notYet:
      print(word,wordsList.count(word))
    notYet += " " + word

def findWordWithFrequency (wordsList,targetWord):
  for word in wordsList:
    if targetWord == word:
      return True,wordsList.count(word)
  return False,-1

def findUserWord(wordsList,targetWord):
  found,freq = findWordWithFrequency(wordsList,targetWord)
  if found:
    print("The word found with ",freq ," time(s)")
  else:
    print("The word not found :(")

#-------------------main
def main():
  createTheFile("Java Java Python java java JAVa JaVa C# C++ Python C C C ShellScript HTML PHP HTML PHP")
  Lines = readFileLines()
  line = Lines[0]
  line = line.upper()
  wordsList = line.split()
  findAllWordsFrequency(wordsList)
  user_word = input("Please the word you want to find it : ")
  findUserWord(wordsList,user_word.upper())

main()
