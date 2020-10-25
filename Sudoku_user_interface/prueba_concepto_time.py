# def time_format(seconds):
#     form_sec= seconds%60
#     Min= seconds//60
#     form_min= Min%60
#     form_hour= Min//60
    
#     if form_sec<10:
#         str_sec='0'+str(form_sec)
#     else:
#         str_sec= str(form_sec)

#     if form_min<10:
#         str_min='0'+str(form_min)
#     else:
#         str_min= str(form_min)
    
#     if form_hour<10:
#         str_hour='0'+ str(form_hour)
#     else:
#         str_hour=str(form_hour)

#     return(str_hour+':'+str_min+':'+str_sec)

# print(time_format(564))

import tkinter as tk
import time


class App():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)

app=App()

