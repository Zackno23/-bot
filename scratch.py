import tkinter
import scratch_2


def btn_click():
    scratch_2.test()


root = tkinter.Tk()
root.geometry('300x300')
btn = tkinter.Button(root, text='yes', width=14, command=btn_click)
btn.pack()
root.mainloop()
