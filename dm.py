from tkinter import *

dmw = Tk()
dmw.geometry("600x600")
dmw.resizable(False, False)
dmw.title("FC-Devmode")
dmw.focus_force()

import foxcalc
print("Developer Mode")

def getMem():
	f = open(f'{foxcalc.MEMFILE}', 'rt')
	fcontent = f.read()
	f.close()
	return f"memfile: {fcontent}" 

def setMem(to:str|int=""):
	f = open(f'{foxcalc.MEMFILE}', 'wt')
	f.write(to)
	f.close()
	return f"Set memory to {to}"

def clearMem():
	f = open(f'{foxcalc.MEMFILE}')
	f.write('')
	f.close()
	return f"Cleared memory"

def setClcTo(to):
	foxcalc.clct = to
	foxcalc.append_clct()

SetClcToLbl = Label(dmw, text="Set Calculation To")
SetClcToLbl.pack()

SetClcTo = Entry(dmw)
SetClcTo.pack()

SetClcToGo = Button(dmw, text="Set", command=lambda:setClcTo(SetClcTo.get()))
SetClcToGo.pack()

QuickGo = Button(dmw, text="=", command=lambda:foxcalc.go())
QuickGo.place(x=0, y=0)

GetMemB = Button(dmw, text="Send `memory` to <stdout>", command=lambda:print(getMem()))
GetMemB.place(x=0, y=30)

setMemToLbl = Label(dmw, text="\nSet Memory To")
setMemToLbl.pack()

setMemTo = Entry(dmw)
setMemTo.pack()

setMemToGo = Button(dmw, text="Set", command=lambda:setMem(setMemTo.get()))
setMemToGo.pack()

mClear = Button(dmw, text="MC", command=lambda:clearMem())

dmw.mainloop()