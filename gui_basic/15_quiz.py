from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("제목 없음 - windows 메모장")
root.geometry("640x480")


def load_file():
    filename = filedialog.askopenfilename(
        initialdir="./",
        title="Select file",
        filetypes=(("text file", "*.txt"), ("all files", "*.*")),
    )

    with open(filename, "r", encoding="utf8") as file:
        txt.delete("1.0", END)
        txt.insert(END, file.read())


def save_file():
    filename = filedialog.asksaveasfilename(
        initialdir="./",
        title="Select file",
        filetypes=(("text file", "*.txt"), ("all files", "*.*")),
    )

    with open(filename + ".txt", "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))


# 메뉴
menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=load_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

menu_edit = Menu(menu, tearoff=0)
menu.add_cascade(label="편집", menu=menu_edit)

menu_format = Menu(menu, tearoff=0)
menu.add_cascade(label="서식", menu=menu_format)

menu_view = Menu(menu, tearoff=0)
menu.add_cascade(label="보기", menu=menu_view)

menu_help = Menu(menu, tearoff=0)
menu.add_cascade(label="도움말", menu=menu_help)


# 스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 텍스트 입력
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt.yview)

root.config(menu=menu)
root.mainloop()

