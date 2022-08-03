def containsOneCapital(password):
   for char in password:
    if char.isupper() :
      return True
   return False

def containsOneSmall(password):
   for char in password:
    if char.islower() :
      return True
   return False

def containsOneNumber(password):
  nums="0123456789"
  for char in password:
    if char in nums:
      return True
  return False

def containsOneSpecialChar(password):
  specials="!@#$%^&*-_"
  for char in password:
    if char in specials:
      return True
  return False

def noSpaces(password):
  res  = password.split()
  return len(res) == 1 

def validLength(password:string):
    return (len(password) > 8 and len(password) < 40)

def isValidPassword(password:string):
  valid = True
  if( not validLength(password)): 
    print("Please enter password from 8 to 40 charachters")
    valid= False
  if( not containsOneCapital(password)): 
    print("It must contains one Capital letter at least")
    valid= False
  if(not containsOneSmall(password)):
    print("It must contains one small letter at least")
    valid= False
  if(not containsOneNumber(password)):
    print("It must contains one number at least")
    valid= False
  if(not containsOneSpecialChar(password)):
    print("It must contains one special charachter from [!@#$%^&*-_] at least")
    valid= False
  if(not containsOneSpecialChar(password)):
    print("Oops..No Spaces are allowed")
    valid= False
  if(valid):
    print("يا عمي انت سكيووور")

  return valid
#--------------main
while True:
   password = input("Please enter a secure password ")
   if(isValidPassword(password)): 
     break
