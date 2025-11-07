import tkinter as tk

y = 2
x = ""
player1 = []
player2 = []


def click(event:int):
    global player1, player2
    global x,y

    if event == 0:
       if y%2 == 0:
           x = 'X'
           player1.append(event)
           print(player1)

       elif y%2 != 0:
           x = 'O'
           player2.append(event)
           print(player2)

       b1.config(text=x)
       y = y + 1

    if event == 1:
       if y%2 == 0:
           x = 'X'
           player1.append(event)
           print(player1)

       elif y%2 != 0:
           x = 'O'
           player2.append(event)
           print(player2)

       b2.config(text=x)
       y = y + 1

    if event == 2:
       if y%2 == 0:
           x = 'X'
           player1.append(event)
           print(player1)

       elif y%2 != 0:
           x = 'O'
           player2.append(event)
           print(player2)

       b3.config(text=x)
       y = y + 1

    if event == 3:
       if y%2 == 0:
           x = 'X'
           player1.append(event)
           print(player1)

       elif y%2 != 0:
           x = 'O'
           player2.append(event)
           print(player2)

       b4.config(text=x)
       y = y + 1


    if event == 4:
       if y%2 == 0:
           x = 'X'
           player1.append(event)
           print(player1)

       elif y%2 != 0:
           x = 'O'
           player2.append(event)
           print(player2)

       b5.config(text=x)
       y = y + 1


    if event == 5:
       if y%2 == 0:
           x = 'X'
           player1.append(event)
           print(player1)

       elif y%2 != 0:
           x = 'O'
           player2.append(event)
           print(player2)

       b6.config(text=x)
       y = y + 1


    if event == 6:
       if y%2 == 0:
           x = 'X'
           player1.append(event)
           print(player1)

       elif y%2 != 0:
           x = 'O'
           player2.append(event)
           print(player2)

       b7.config(text=x)
       y = y + 1

    if event == 7:
       if y%2 == 0:
           x = 'X'
           player1.append(event)
           print(player1)

       elif y%2 != 0:
           x = 'O'
           player2.append(event)
           print(player2)

       b8.config(text=x)
       y = y + 1

    if event == 8:
       if y%2 == 0:
           x = 'X'
           player1.append(event)
           print(player1)

       elif y%2 != 0:
           x = 'O'
           player2.append(event)
           print(player2)

       b9.config(text=x)
       y = y + 1


def determine_winner(player1,player2):
    winner = ""

    if player1 == player1[0,1,2] or player1[0,3,6] or player1[0,4,8] or player1[2,4,6] or player1[1,4,7] or player1[2,5,8] or player1[3,4,5] or player1[6,7,8]:
        winner = player1
        print("Player 1 Wins!")
    elif player2 == player1[0,1,2] or player1[0,3,6] or player1[0,4,8] or player1[2,4,6] or player1[1,4,7] or player1[2,5,8] or player1[3,4,5] or player1[6,7,8]:
        winner = player2
        print("Player 2 Wins!")
    else:
        winner == "Nobody Wins"

    return winner



window = tk.Tk()
window.minsize(width=200,height=200)
window.maxsize(width=200, height=200)

p1 = tk.Label(window, text="Player 1: X",height=2,width=15)
p2 = tk.Label(window,text="Player 2: O",height=2,width=15)

b1 = tk.Button(width=5, height=2,command=lambda: click(0))
b1.grid(row=0,column=0)
b2 = tk.Button(width=5, height=2, command=lambda: click(1))
b2.grid(row=0,column=1)
b3 = tk.Button(width=5, height=2,command=lambda :click(2))
b3.grid(row=0,column=2)
b4 = tk.Button(width=5, height=2, command=lambda :click(3))
b4.grid(row=1,column=0)
b5 = tk.Button(width=5, height=2,command=lambda :click(4))
b5.grid(row=1,column=1)
b6 = tk.Button(width=5, height=2, command=lambda :click(5))
b6.grid(row=1,column=2)
b7 = tk.Button(width=5, height=2,command=lambda :click(6))
b7.grid(row=2,column=0)
b8 = tk.Button(width=5, height=2,command=lambda :click(7))
b8.grid(row=2,column=1)
b9 = tk.Button(width=5, height=2,command=lambda :click(8))
b9.grid(row=2,column=2)


window.mainloop()