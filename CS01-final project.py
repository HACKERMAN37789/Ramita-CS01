from tkinter import * 
root = Tk()
root.title("เครื่องคิดเลข_Calculator")

content = ""
txt_input = StringVar(value="0")

def btn(number):
    global content
    content = content+str(number)
    txt_input.set(content)

def equal():
    global content
    calculate=float(eval(content))
    txt_input.set(calculate)
    content = ""

def clear():
    global content
    calculate=""
    txt_input.set("")
    display.insert(0,"0")

display = Entry(font=('arial',30,'bold'),fg="black",bg="gray",textvariable=txt_input,justify="right")
display.grid(columnspan=4)

#row1
num7=Button(fg="white",bg="blue",font=('arial',30,'bold'),text="7",command=lambda:btn(7),padx=30,pady=15).grid(row=1,column=0)
num8=Button(fg="white",bg="blue",font=('arial',30,'bold'),text="8",command=lambda:btn(8),padx=30,pady=15).grid(row=1,column=1)
num9=Button(fg="white",bg="blue",font=('arial',30,'bold'),text="9",command=lambda:btn(9),padx=30,pady=15).grid(row=1,column=2)
Cbtn=Button(fg="white",bg="red",font=('arial',30,'bold'),text="C",command=clear,padx=30,pady=15).grid(row=1,column=3)

#row2
num4=Button(fg="white",bg="blue",font=('arial',30,'bold'),text="4",command=lambda:btn(4),padx=30,pady=15).grid(row=2,column=0)
num5=Button(fg="white",bg="blue",font=('arial',30,'bold'),text="5",command=lambda:btn(5),padx=30,pady=15).grid(row=2,column=1)
num6=Button(fg="white",bg="blue",font=('arial',30,'bold'),text="6",command=lambda:btn(6),padx=30,pady=15).grid(row=2,column=2)
PlusBtn=Button(fg="black",bg="white",font=('arial',30,'bold'),text="+",command=lambda:btn("+"),padx=32,pady=15).grid(row=2,column=3)

#row3
num3=Button(fg="white",bg="blue",font=('arial',30,'bold'),text="3",command=lambda:btn(3),padx=30,pady=15).grid(row=3,column=0)
num2=Button(fg="white",bg="blue",font=('arial',30,'bold'),text="2",command=lambda:btn(2),padx=30,pady=15).grid(row=3,column=1)
num1=Button(fg="white",bg="blue",font=('arial',30,'bold'),text="1",command=lambda:btn(1),padx=30,pady=15).grid(row=3,column=2)
MinusBtn=Button(fg="black",bg="white",font=('arial',30,'bold'),text="-",command=lambda:btn("-"),padx=37,pady=15).grid(row=3,column=3)

#row4
dot=Button(fg="white",bg="blue",font=('arial',30,'bold'),text=".",command=lambda:btn("."),padx=30,pady=15).grid(row=4,column=0)
num0=Button(fg="white",bg="blue",font=('arial',30,'bold'),text="0",command=lambda:btn(0),padx=30,pady=15).grid(row=4,column=1)
DivideBtn=Button(fg="black",bg="white",font=('arial',30,'bold'),text="/",command=lambda:btn("/"),padx=36,pady=15).grid(row=4,column=2)
TimeBtn=Button(fg="black",bg="white",font=('arial',30,'bold'),text="X",command=lambda:btn("*"),padx=33,pady=15).grid(row=4,column=3)

#row5
Equal=Button(fg="black",bg="white",font=('arial',30,'bold'),text="=",command=lambda:equal,padx=93,pady=15).grid(row=5,column=0,columnspan=2)
OpenBtn=Button(fg="black",bg="white",font=('arial',30,'bold'),text="(",command=lambda:btn("("),padx=36,pady=15).grid(row=5,column=2)
CloseBtn=Button(fg="black",bg="white",font=('arial',30,'bold'),text=")",command=lambda:btn(")"),padx=36,pady=15).grid(row=5,column=3)

root.mainloop()