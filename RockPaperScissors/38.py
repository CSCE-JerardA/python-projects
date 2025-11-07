import tkinter as tk

import random

def determine_winner(comp:str, user:str) -> int or str:
    winner = 0
    if user == "P" and comp == "R":
        winner = 1
    elif user == "R" and comp == "S":
        winner = 1
    elif user == "S" and comp == "P":
        winner = 1
    elif user == "P" and comp == "S":
        winner = -1
    elif user == "R" and comp == "P":
        winner = -1
    elif user == "S" and comp == "R":
        winner = -1
    elif user == "P" and comp == "P":
        winner = 0
    elif user == "S" and comp == "S":
        winner = 0
    elif user == "R" and comp == "R":
        winner = 0
    return winner


def handle_click(choice:str):
        computer_choice = random.choice(["P", "R", "S"])
        winner = determine_winner(computer_choice, "P" or "S" or "R")
        if winner == 0:
                result["text"]="Tie!"
                print(winner)
        else:
                result["text"]=(str(winner) + " " + computer_choice)
                print(winner)



window = tk.Tk()
window.minsize(width=400, height=100)
window.maxsize(width=400,height=100)


paper = tk.Button(text="Paper",command=lambda: handle_click("P"),height=2,width=15)
rock = tk.Button(text="Rock", command= lambda:handle_click("R"),height=2,width=15)
scissors = tk.Button(text="Scissors", command=lambda:handle_click("S"),height=2,width=15)
result = tk.Label(text= "Let's play a game!", height=2,width=15)
#paper.bind("<Button-1>", handle_Pclick)
#rock.bind("<Button-1>", handle_Rclick)
#scissors.bind("<Button-1>", handle_Sclick)
paper.grid(row=0,column=0, sticky="news")
rock.grid(row=0, column=1,sticky="news")
scissors.grid(row=0,column=2,sticky="news")
result.grid(row=1,column=1)

window.mainloop()