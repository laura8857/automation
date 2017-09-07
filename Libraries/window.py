# @window


import tkinter


wnd = tkinter.Tk()#產生主視窗物件
wnd.title('API TEST')
wnd.geometry('600x600+5+40')
# little = tk.Label(wnd, text='Label: First', bg='skyblue').pack()
bigger = tkinter.Label(wnd, text='Result', bg='pink').pack()
wnd.maxsize(width=700, height=700)
T = tkinter.Text(wnd, height=2, width=30)
T.pack()
T.insert(tkinter.END, "Just a text Widget\nin two lines\n")
wnd.mainloop()#訊息呼叫
