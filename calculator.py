from tkinter import *
root=Tk()
root.geometry('600x700')
root.title('calculator')
def click(event):
    global scvalue
    text=event.widget.cget('text')
   # print(text)
    if text=='=':
        value=eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text=='c':
        scvalue.set('')
        screen.update()
    elif text=='<x>':
        value=screen.get()
        scvalue.set(value[:-1])
        scvalue.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

scvalue=StringVar()
scvalue.set('')
screen=Entry(root,bg='skyblue',fg='black',textvar=scvalue,font='lucida 40 bold')
screen.pack(padx=20,pady=20)
f=Frame(root,bg='grey')
b=Button(f,text='c',padx=30,pady=10,font='lucida 30 bold')
b.pack(side=LEFT,)
b.bind('<Button-1>',click)
b=Button(f,text='<x>',padx=30,pady=10,font='lucida 30 bold')
b.pack(side=LEFT)
b.bind('<Button-1>',click)
b=Button(f,text='%',padx=30,pady=10,font='lucida 30 bold')
b.pack(side=LEFT)
b.bind('<Button-1>',click)
b=Button(f,text='/',padx=30,pady=10,font='lucida 30 bold')
b.pack(side=LEFT)
b.bind('<Button-1>',click)
f.pack()
f=Frame(root,bg='grey')
b=Button(f,text='7',padx=37,pady=10,font='lucida 30 bold')
b.pack(side=LEFT)
b.bind('<Button-1>',click)
b=Button(f,text='8',padx=37,pady=10,font='lucida 30 bold')
b.pack(side=LEFT)
b.bind('<Button-1>',click)
b=Button(f,text='9',padx=37,pady=10,font='lucida 30 bold')
b.pack(side=LEFT)
b.bind('<Button-1>',click)
b=Button(f,text='*',padx=37,pady=10,font='lucida 30 bold')
b.pack(side=LEFT)
b.bind('<Button-1>',click)
f.pack()
f=Frame(root,bg='grey')
b=Button(f,text='4',padx=36,pady=10,font='lucida 30 bold')
b.pack(side=LEFT)
b.bind('<Button-1>',click)
b=Button(f,text='5',padx=36,pady=10,font='lucida 30 bold')
b.pack(side=LEFT)
b.bind('<Button-1>',click)
b=Button(f,text='6',padx=36,pady=10,font='lucida 30 bold')
b.pack(side=LEFT)
b.bind('<Button-1>',click)
b=Button(f,text='-',padx=36,pady=10,font='lucida 30 bold')
b.pack(side=LEFT)
b.bind('<Button-1>',click)
f.pack()
f=Frame(root,bg='grey')
b=Button(f,text='1',padx=36,pady=10,font='lucida 30 bold')
b.pack(side=LEFT)
b.bind('<Button-1>',click)
b=Button(f,text='2',padx=36,pady=10,font='lucida 30 bold')
b.pack(side=LEFT)
b.bind('<Button-1>',click)
b=Button(f,text='3',padx=36,pady=10,font='lucida 30 bold')
b.pack(side=LEFT)
b.bind('<Button-1>',click)
b=Button(f,text='+',padx=36,pady=10,font='lucida 30 bold')
b.pack(side=LEFT)
b.bind('<Button-1>',click)
f.pack()
f=Frame(root,bg='grey')
b=Button(f,text='0',padx=36,pady=10,font='lucida 30 bold')
b.pack(side=LEFT)
b.bind('<Button-1>',click)
b=Button(f,text='.',padx=36,pady=10,font='lucida 30 bold')
b.pack(side=LEFT)
b.bind('<Button-1>',click)
b=Button(f,text='=',padx=36,pady=10,font='lucida 30 bold')
b.pack(side=LEFT)
b.bind('<Button-1>',click)
f.pack()
root.mainloop()

