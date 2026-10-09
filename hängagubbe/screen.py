import WordChoice
import os

def InGame(SemiCorectWord,tryes,tryed):
    os.system("clear")
    print(f"[{tryed}]\ntyres left: {tryes}\n{SemiCorectWord}")

def Lose():
    os.system("clear")
    os.system("cat Napoleon.txt")
    print("Just like Napoleon thers nothing you can do:(")

def Win():
    os.system("clear")
    os.system("cat Terminator.txt")
    print("winning is not for everyone but it is for you!!")
