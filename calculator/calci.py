from tkinter import *
import tkinter as tk

def button_click(sym):
    current = input_txt.get()
    input_txt.set(current + str(sym))

def clear():
    input_txt.set("")

def backspace():
    current = input_txt.get()
    input_txt.set(current[:-1])
def calculate():
    try:
        result = str(eval(input_txt.get()))
        input_txt.set(result)
    except:
        input_txt.set("Error")

root = tk.Tk()
root.title("Simple Calculator by THARANI L")
root.state('zoomed')

input_txt = tk.StringVar()

frame1 = Frame(root, height=500, width=500, bd=3, bg='grey', relief='groove')
frame1.pack(side=TOP, pady=(30, 20))

field = tk.Entry(frame1, textvariable=input_txt, bd=8, width=30, font=('arial', 18, 'bold'), bg='green', justify='right')
field.pack(ipady=10, pady=(40, 40), padx=(20, 20))

btns_frame = Frame(frame1, bg='grey')
btns_frame.pack(pady=(20, 20))

button_padx = 15
button_pady = 7


tk.Button(btns_frame, text='(', command=lambda: button_click("("), height=4, width=9, bg='lightblue').grid(row=0, column=0, padx=button_padx, pady=button_pady)
tk.Button(btns_frame, text=')', command=lambda: button_click(")"), height=4, width=9, bg='lightblue').grid(row=0, column=1, padx=button_padx, pady=button_pady)
tk.Button(btns_frame, text='⌫', command=backspace, height=4, width=9, bg='lightblue').grid(row=0, column=2, padx=button_padx, pady=button_pady)
tk.Button(btns_frame, text='/', command=lambda: button_click("/"), height=4, width=9, bg='lightblue').grid(row=0, column=3, padx=button_padx, pady=button_pady)


tk.Button(btns_frame, text='7', command=lambda: button_click("7"), height=4, width=9, bg='lightblue').grid(row=1, column=0, padx=button_padx, pady=button_pady)
tk.Button(btns_frame, text='8', command=lambda: button_click("8"), height=4, width=9, bg='lightblue').grid(row=1, column=1, padx=button_padx, pady=button_pady)
tk.Button(btns_frame, text='9', command=lambda: button_click("9"), height=4, width=9, bg='lightblue').grid(row=1, column=2, padx=button_padx, pady=button_pady)
tk.Button(btns_frame, text='x', command=lambda: button_click("*"), height=4, width=9, bg='lightblue').grid(row=1, column=3, padx=button_padx, pady=button_pady)


tk.Button(btns_frame, text='4', command=lambda: button_click("4"), height=4, width=9, bg='lightblue').grid(row=2, column=0, padx=button_padx, pady=button_pady)
tk.Button(btns_frame, text='5', command=lambda: button_click("5"), height=4, width=9, bg='lightblue').grid(row=2, column=1, padx=button_padx, pady=button_pady)
tk.Button(btns_frame, text='6', command=lambda: button_click("6"), height=4, width=9, bg='lightblue').grid(row=2, column=2, padx=button_padx, pady=button_pady)
tk.Button(btns_frame, text='-', command=lambda: button_click("-"), height=4, width=9, bg='lightblue').grid(row=2, column=3, padx=button_padx, pady=button_pady)


tk.Button(btns_frame, text='1', command=lambda: button_click("1"), height=4, width=9, bg='lightblue').grid(row=3, column=0, padx=button_padx, pady=button_pady)
tk.Button(btns_frame, text='2', command=lambda: button_click("2"), height=4, width=9, bg='lightblue').grid(row=3, column=1, padx=button_padx, pady=button_pady)
tk.Button(btns_frame, text='3', command=lambda: button_click("3"), height=4, width=9, bg='lightblue').grid(row=3, column=2, padx=button_padx, pady=button_pady)
tk.Button(btns_frame, text='+', command=lambda: button_click("+"), height=4, width=9, bg='lightblue').grid(row=3, column=3, padx=button_padx, pady=button_pady)


tk.Button(btns_frame, text='0', command=lambda: button_click("0"), height=4, width=9, bg='lightblue').grid(row=4, column=0, padx=button_padx, pady=button_pady)
tk.Button(btns_frame, text='00', command=lambda: button_click("00"), height=4, width=9, bg='lightblue').grid(row=4, column=1, padx=button_padx, pady=button_pady)
tk.Button(btns_frame, text='.', command=lambda: button_click("."), height=4, width=9, bg='lightblue').grid(row=4, column=2, padx=button_padx, pady=button_pady)
tk.Button(btns_frame, text='%', command=lambda: button_click("%"), height=4, width=9, bg='lightblue').grid(row=4, column=3, padx=button_padx, pady=button_pady)


tk.Button(btns_frame, text='C', command=clear, height=4, width=24, bg='lightblue').grid(row=5, column=0,columnspan=2, padx=button_padx, pady=button_pady)
tk.Button(btns_frame, text='=', command=calculate, height=4, width=24, bg='lightblue').grid(row=5, column=2,columnspan=2, padx=button_padx, pady=button_pady)
root.mainloop()
