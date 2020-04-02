import tkinter

class MessageClass:
    def __init__(self,message, year, month, date, hour, minuits):
        self.message = message
        self.year = year
        self.month = month
        self.date = date
        self.hour = hour
        self.minuits = minuits

    def display(self):
        display_text =\
            f"{self.year}年{self.month}月{self.date}日{self.hour}時{self.minuits}分\n" \
            f"{self.message}"
        root = tkinter.Tk()
        root.title('入退室BOTメッセージ')
        root.resizable(False, False)
        canvas = tkinter.Canvas(root, width=600, height=600)
        canvas.pack()
        label = tkinter.Label(root, text=display_text, font=("Times New Roman", 35), bg="white")
        label.place(x=30, y=150)
        root.mainloop()


