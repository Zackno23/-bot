import tkinter
import sys
import button_result
def btn_clicked(y_no):
    print('hello')
    # exit_request.exit()






class MessageClass:
    def __init__(self, message, year, month, date, hour, minuits):
        self.message = message
        self.year = year
        self.month = month
        self.date = date
        self.hour = hour
        self.minuits = minuits
    # def yes_clicked(self):
    #     print('yes_pressed')
    #     # exit_request.exit()
    # def no_clicked(self):
    #     print('no_pressed')
    #     # sys.exit()


    def display(self):

        display_text = \
            f"{self.year}年{self.month}月{self.date}日{self.hour}時{self.minuits}分\n" \
            f"{self.message}"
        root = tkinter.Tk()
        root.title('入退室BOTメッセージ')
        root.resizable(False, False)
        root.geometry('300x300')
        canvas = tkinter.Canvas(root, width=300, height=300)
        label = tkinter.Label(root, text=display_text, font=("Times New Roman", 20), bg="white")
        label.place(x=0, y=0)
        if self.message == '退出しますか？':
            print('hey!')
            btn1 = tkinter.Button(root, text="はい", width=10, command=btn_clicked)
            print('aaaaaa')
            btn1.pack(fill='x', padx=20, side='left')
            btn2 = tkinter.Button(root, text="いいえ", width=10, command=btn_clicked)
            btn2.pack(fill='x', padx=20, side='left')
        root.mainloop()
