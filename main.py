import json, os, random

playerOne = False
def reWriteTrue():
  with open("loggedIN.txt","w") as file:
    file.write("true")
    file.close
def reWriteFalse():
  with open("loggedIN.txt","w") as file:
    file.write("false")
    file.close
def clear():
  os.system('clear')

def diceGame():
  clear()
  reWriteTrue()
  count = 5
  gameOn = 1
  gameEnd = False
  p1Score = 0
  p2Score = 0
  while gameOn == 1 and count >0 and gameEnd == False:
    p1Random3 = 0
    p2Random3 = 0
    p1Random1 = random.randint(1,6)
    p1Random2 = random.randint(1,6)
    p2Random1 = random.randint(1,6)
    p2Random2 = random.randint(1,6)
    if p1Random1 == p1Random2:
      p1Random3 += random.randint(1,6)
    if p2Random1 == p2Random2:
      p2Random3 += random.randint(1,6)
    print(f"player1 -> {p1Random1} and -> {p1Random2} extra if double -> {p1Random3}\nplayer2 -> {p2Random1} and -> {p2Random2} extra if double -> {p2Random3}")
    p1Score += (p1Random1+p1Random2+p1Random3)
    p2Score += (p2Random1+p2Random2+p1Random3)
    if (p1Random1+p1Random2+p1Random3) % 2 == 0:
      p1Score += 10
    else:
      p1Score -= 5
    if (p2Random1+p2Random2+p1Random3) % 2 == 0:
      p2Score += 10
    else:
      p2Score -= 5
    if p1Score <0 or p2Score <0:
      gameEnd = True
    print(f"player1 score -> {p1Score}\nplayer2 score -> {p2Score}")
    gameOn = 3 
    while gameOn == 3:
      playAgain = input("click enter to roll again\n")
      if playAgain == "":
        gameOn = 1
    count -= 1
  print (f"------------------------------------------------------------\n\nfinal scores are:\nplayer1 -> {p1Score}\nplayer2 -> {p2Score}\n\n------------------------------------------------------------")
  playAgain = input("\ndo you want to:\n1)  play again\n2)  menu\n")
  if playAgain == "1":
    clear()
    diceGame()
  elif playAgain == "2":
    clear()
    menu()
def collectUsername():
  with open('usernames.json') as f:
    dump = json.loads(f.read())
    return dump


def authenticate(u,p):
  data = collectUsername()
  for n in data:
    if(n['username']== u):
      if(n['password']== p):
        global playerOne 
        playerOne = True

def checkLogin():
  global playerOne
  if(playerOne)==True:
    return True  
def login():
  print("Please log in")
  u = input("Enter username: ")
  p = input("Enter password: ")
  authenticate(u,p)  
  if playerOne == True:
    print('\nyou are now logged in\n')
    diceGame()
  else:
    print("\nsorry that didn't work\n")
  menu()  

def logOut():
  global playerOne
  playerOne = False 
  print('you have been logged out')
  reWriteFalse()
  menu() 

def menu():
  items = [
    "Login",
    "Log out"
  ]
  try:
    for n in range(len(items)):
      print("{} {}".format(n+1, items[n]))
  
    choice = int(input())
  
    if choice ==1:
      login()
    elif choice ==2:
      logOut()
    else:
      menu()
  except:
    menu()
def checkLogged():
  with open("loggedIN.txt") as file:
    fromFile = [line.strip() for line in file]
    if fromFile[0] == "false":
      menu()
    else:
      diceGame()
checkLogged()