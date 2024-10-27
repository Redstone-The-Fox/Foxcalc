from tkinter import *
from tkinter import font as tkfont
from math import *
from sys import set_int_max_str_digits

#####
### Starting
#####

set_int_max_str_digits(500000)

root = Tk()
root.geometry("600x600")
root.resizable(False, False)
root.title("FoxcalcGUI Release1.0")
root.config(bg="gray")

####
## Fonts
####

csolas28 = tkfont.Font(family='Consolas', size=28, weight='bold')
csolas18 = tkfont.Font(family='Consolas', size=18, weight='bold')
csolas15 = tkfont.Font(family='Consolas', size=15, weight='bold')

####
## Functions and Variables
####

clct = ""
answ = 0
MEMFILE = 'memory'

def append_clct(w=""):
	global clct
	clct += w
	print(f"set calculation to: {clct}")
	clcd.config(text=f"{clct}")

def save_to_mem():
	global clct
	f = open(MEMFILE, 'wt')
	f.write(clct)
	f.close()
	

def load_from_mem():
	global clct
	f = open(MEMFILE, 'rt')
	append_clct(f.read())
	f.close()

def clear_mem():
	f = open(MEMFILE, 'wt')
	f.write("")
	f.close()

def go():
	global clct
	global answ
	if clct == "6.5*2.1+(65+sqrt(144))":
		root.destroy()
		import dm
	try:
		answ = f'{eval(f"{clct}")}'
	except SyntaxError as e:
		print(f"invalid math syntax ({e})")
		return
	except IOError as e:
		print(f"calculation failed ({e})")
		return
	except Exception as e:
		print(f"unknown error ({e})")
		return
	ans.config(text=f"Answer: {answ}")
	c()
	return answ

def c():
	global clct
	global answ
	clct = ""
	clcd.config(text=f"0")
	print("cleared calculation")

def dl():
	global clct
	clct = clct[:-1]
	append_clct()

def key_press(event):
	global clct
	if event.char.isdigit() or event.char in "+-*/().":
		append_clct(event.char)
	elif event.keysym == "Return" or event.char == "=":
		go()
	elif event.char == "^":
		append_clct("**")
	elif event.keysym == "BackSpace":
		dl()
	elif event.char == "c" or event.char == "C":
		c()
####
### Other
####

root.bind("<Key>", key_press)

#####
### Messageboxes
#####

clcd = Label(root, text="0", bg="gray", fg="white", font=("Consolas", 24))
clcd.place(x=0)

ans = Label(root, text="Answer: -", bg="gray", fg="white", font=("Consolas", 24))
ans.place(x=0, y=475)

#####
### Buttons
#####

# Button: +
bpl = Button(root, text="+", command=lambda:append_clct("+"))
bpl['font'] = csolas28
bpl.place(x=0, y=525, height=75, width=75)

# Button: -
bm = Button(root, text="-", command=lambda:append_clct("-"))
bm['font'] = csolas28
bm.place(x=75, y=525, height=75, width=75)

# Button: *
bmu = Button(root, text="*", command=lambda:append_clct("*"))
bmu['font'] = csolas28
bmu.place(x=150, y=525, height=75, width=75)

# Button: /
bdv = Button(root, text="/", command=lambda:append_clct("/"))
bdv['font'] = csolas28
bdv.place(x=225, y=525, height=75, width=75)

# Button: (
blp = Button(root, text="(", command=lambda:append_clct("("))
blp['font'] = csolas28
blp.place(x=300, y=525, height=75, width=75)

# Button: )
brp = Button(root, text=")", command=lambda:append_clct(")"))
brp['font'] = csolas28
brp.place(x=375, y=525, height=75, width=75)

# Button: ^ | **
brp = Button(root, text="^", command=lambda:append_clct("**"))
brp['font'] = csolas28
brp.place(x=450, y=525, height=75, width=75)

# Button: =
beq = Button(root, text="=", command=lambda:print(f"answer: {go()}"))
beq['font'] = csolas28
beq.place(x=525, y=525, height=75, width=75)

# Button: .
bdec = Button(root, text=".", command=lambda:append_clct("."))
bdec['font'] = csolas28
bdec.place(x=0, y=400, height=75, width=75)

# Button: SQRT
bsrt = Button(root, text="√", command=lambda:append_clct("sqrt("))
bsrt['font'] = csolas28
bsrt.place(x=75, y=400, height=75, width=75)

# Button: SIN
bsin = Button(root, text="sin()", command=lambda:append_clct("sin("))
bsin['font'] = csolas18
bsin.place(x=150, y=400, height=75, width=75)

# Button: COS
bcos = Button(root, text="cos()", command=lambda:append_clct("cos("))
bcos['font'] = csolas18
bcos.place(x=225, y=400, height=75, width=75)

# Button: TAN
bcos = Button(root, text="tan()", command=lambda:append_clct("tan("))
bcos['font'] = csolas18
bcos.place(x=300, y=400, height=75, width=75)

# Button: SINH
bsinh = Button(root, text="sinh()", command=lambda:append_clct("sinh("))
bsinh['font'] = csolas15
bsinh.place(x=150, y=350, height=50, width=75)

# Button: COSH
bcosh = Button(root, text="cosh()", command=lambda:append_clct("cosh("))
bcosh['font'] = csolas15
bcosh.place(x=225, y=350, height=50, width=75)

# Button: TANH
btanh = Button(root, text="tanh()", command=lambda:append_clct("tanh("))
btanh['font'] = csolas15
btanh.place(x=300, y=350, height=50, width=75)

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

# Button: 4
b4 = Button(root, text="4", command=lambda:append_clct("4"))
b4['font'] = csolas28
b4.place(x=225, y=50, height=75, width=75)

# Button: 5
b5 = Button(root, text="5", command=lambda:append_clct("5"))
b5['font'] = csolas28
b5.place(x=0, y=125, height=75, width=75)

# Button: 6
b6 = Button(root, text="6", command=lambda:append_clct("6"))
b6['font'] = csolas28
b6.place(x=75, y=125, height=75, width=75)

# Button: 7
b7 = Button(root, text="7", command=lambda:append_clct("7"))
b7['font'] = csolas28
b7.place(x=150, y=125, height=75, width=75)

# Button: 8
b8 = Button(root, text="8", command=lambda:append_clct("8"))
b8['font'] = csolas28
b8.place(x=225, y=125, height=75, width=75)

# Button: 9
b9 = Button(root, text="9", command=lambda:append_clct("9"))
b9['font'] = csolas28
b9.place(x=75, y=200, height=75, width=75)

# Button: 0
b0 = Button(root, text="0", command=lambda:append_clct("0"))
b0['font'] = csolas28
b0.place(x=150, y=200, height=75, width=75)

# Button: C
bC = Button(root, text="C", command=lambda:c())
bC['font'] = csolas28
bC.place(x=525, y=50, height=75, width=75)

# Button: ←
bbs = Button(root, text="←", command=lambda:dl())
bbs['font'] = csolas28
bbs.place(x=525, y=125, height=75, width=75)

# Button: Ans
bans = Button(root, text="Ans", command=lambda:append_clct(answ))
bans['font'] = csolas28
bans.place(x=525, y=200, height=75, width=75)

# Button: MemoryStore
bMS = Button(root, text="MS", command=lambda:save_to_mem())
bMS['font'] = csolas28
bMS.place(x=525, y=275, height=75, width=75)

# Button: MemoryRecall
bMR = Button(root, text="MR", command=lambda:load_from_mem())
bMR['font'] = csolas28
bMR.place(x=525, y=350, height=75, width=75)

# Button: MemoryClear
bMC = Button(root, text="MC", command=lambda:clear_mem())
bMC['font'] = csolas28
bMC.place(x=525, y=425, height=75, width=75)

# Button: EXIT
bC = Button(root, text="Exit", command=lambda:exit(0))
bC['font'] = csolas18
bC.place(x=525, y=0, height=50, width=75)

if __name__ == "__main__":
	root.mainloop()
