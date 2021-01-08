import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10)  # 10ms 마다 움직임
# progressbar.pack()

p_var2 = DoubleVar()
progresbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progresbar2.pack()


def btncmd():
    for i in range(1, 100 + 1):
        time.sleep(0.01)  # 0.01초 대기

        p_var2.set(i)  # progress bar 의 값 설정
        progresbar2.update()  # UI 업데이트
        print(p_var2.get())


btn = Button(root, text="중지", command=btncmd)
btn.pack()

root.mainloop()

