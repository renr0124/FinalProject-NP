from tkinter import *

buttonList = []

myMark = 'X'

for i in range(9):
    buttonList.append('')

mySize = 1

def ttt(buttons,idx):
    buttons.config(text = myMark,state = DISABLED)
    buttonList[idx] = myMark
    print(buttonList)


button1Str = ''

tk = Tk()
tk.resizable(False,False)

button1 = Button(tk,text="",width = mySize*3,height = mySize, font=('Times 50 bold'),bg='gray',fg='white',command=lambda:ttt(button1,0))
button1.grid(row=1,column=0)


button2 = Button(tk,text=' ', width = mySize*3,height = mySize,font=('Times 50 bold'),bg='gray',fg='white',command=lambda:ttt(button2,1))
button2.grid(row=1,column=1)

button3 = Button(tk,text=' ', width = mySize*3,height = mySize,font=('Times 50 bold'),bg='gray',fg='white',command=lambda:ttt(button3,2))
button3.grid(row=1,column=2)

button4 = Button(tk,text=' ',width = mySize*3,height = mySize, font=('Times 50 bold'),bg='gray',fg='white',command=lambda:ttt(button4,3))
button4.grid(row=2,column=0)

button5 = Button(tk,text=' ', width = mySize*3,height = mySize,font=('Times 50 bold'),bg='gray',fg='white',command=lambda:ttt(button5,4))
button5.grid(row=2,column=1)

button6 = Button(tk,text=' ',width = mySize*3,height = mySize, font=('Times 50 bold'),bg='gray',fg='white',command=lambda:ttt(button6,5))
button6.grid(row=2,column=2)

button7 = Button(tk,text=' ', width = mySize*3,height = mySize,font=('Times 50 bold'),bg='gray',fg='white',command=lambda:ttt(button7,6))
button7.grid(row=3,column=0)

button8 = Button(tk,text=' ',width = mySize*3,height = mySize,font=('Times 50 bold'),bg='gray',fg='white',command=lambda:ttt(button8,7))
button8.grid(row=3,column=1)

button9 = Button(tk,text=' ',width = mySize*3,height = mySize, font=('Times 50 bold'),bg='gray',fg='white',command=lambda:ttt(button9,8))
button9.grid(row=3,column=2)


tk.mainloop()

#def initialize_board():
 #   top = Tk()
  # top.title("Tic-Tac-Toe")
  #  top.resizable(False, False)
  #  w = Frame(top, bg="grey", height=500, width=500)
  #  w.pack()


   # top.mainloop()

#initialize_board()






