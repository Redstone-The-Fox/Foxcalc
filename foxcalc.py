from tkinter import *
from tkinter import font as tkfont
from math import *

#####
### Starting
#####

root = Tk()
root.geometry("600x600")
root.resizable(False, False)
root.title("Fox-calc 1.0")
root.config(bg="gray")

####
## Fonts
####

csolas28 = tkfont.Font(family='Consolas', size=28, weight='bold')

clct: str = ""

def append_clct(w):
	global clct
	clct += w
	print(f"appended calculation to: {clct}")
	clcd.config(text=f"{clct}")

def go():
	global clct
	answ = eval(f"{clct}")
	clct = ""
	append_clct("")
	return answ

# Messageboxes
clcd = Label(root, text="0", bg="gray", fg="white", font=("Consolas", 24))
clcd.place(x=0)

#####
### Buttons
#####

# Button: +
bpl = Button(root, text="+", command=lambda:append_clct("+"))
bpl['font'] = csolas28
bpl.place(x=0, y=525, height=75, width=75)

# Button: =
beq = Button(root, text="=", command=lambda:print(f"answer: {go()}"))
beq['font'] = csolas28
beq.place(x=75, y=525, height=75, width=75)

# Button: 1
b1 = Button(root, text="1", command=lambda:append_clct("1"))
b1['font'] = csolas28
b1.place(x=0, y=50, height=75, width=75)

# Button: 2
b2 = Button(root, text="2", command=lambda:append_clct("2"))
b2['font'] = csolas28
b2.place(x=75, y=50, height=75, width=75)

# Button: 3
b3 = Button(root, text="3", command=lambda:append_clct("3"))
b3['font'] = csolas28
b3.place(x=150, y=50, height=75, width=75)

root.mainloop()