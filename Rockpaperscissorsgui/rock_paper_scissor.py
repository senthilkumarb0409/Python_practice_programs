from tkinter import *
from PIL import Image,ImageTk
import random 

root = Tk()
root.title("Rock Paper Scissors")
root.configure(background="blue")

rock_img =  ImageTk.PhotoImage(Image.open("rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
Scissor_img = ImageTk.PhotoImage(Image.open("scissors.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

user_label = Label(root,image=Scissor_img, bg="blue")
comp_label = Label(root, image = scissor_img_comp, bg="blue")
comp_label.grid(row=1,column=0)
user_label.grid(row=1, column=4)

playerscore = Label(root, text=0,font=100,bg="blue",fg="white")
computerscore = Label(root, text=0,font=100,bg="blue",fg="white")
computerscore.grid(row=1,column=1)
playerscore.grid(row =1,column=3)

user_indicator = Label(root, font=50, text="USER",bg="blue",fg="white")
comp_indicator = Label( root, font=50, text="COMPUTER",bg="blue",fg="white")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

msg = Label(root, font=50, bg="blue",fg="white")
msg.grid(row = 3, column =2)

def updateMessage(x):
    msg['text'] = x
    
def updateUserScore():
    score = int(playerscore["text"])
    score += 1
    playerscore["text"] = str(score)
    
def updateCompScore():
    score = int(computerscore["text"])
    score += 1
    computerscore["text"] = str(score)
    
def CheckWin(player, computer):
    if player == computer:
        updateMessage("It's a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("Computer Wins!!! and you lose")
            updateCompScore()
        else:
            updateMessage("You win!!!")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("Computer Wins!!! and you lose")
            updateCompScore()
        else:
            updateMessage("You win!!!")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("Computer Wins!!! and you lose")
            updateCompScore()
        else:
            updateMessage("You win!!!")
            updateUserScore()
    else:
        pass
            
def updateChoice(x):
    
    compChoice = random.choice(['rock','paper','scissor'])
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice ==  "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)
    
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=Scissor_img)
    
    CheckWin(x, compChoice)

rock = Button(root, height=2,width=20, text="ROCK",bg="black", fg="white", command = lambda:updateChoice("rock")).grid(row=2,column=1)
paper = Button(root, height=2,width=20, text="PAPER",bg="black", fg="white", command = lambda:updateChoice("paper")).grid(row=2,column=2)
scissor = Button(root, height=2,width=20, text="SCISSOR",bg="black", fg="white", command = lambda:updateChoice("scissor")).grid(row=2,column=3)

root.mainloop()
