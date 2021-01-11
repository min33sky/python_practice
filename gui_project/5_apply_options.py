import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *  # __all__에 정의하지 않은 모듈은 임포트를 따로 해야한다.
from tkinter import filedialog
from PIL import Image  # pip install Pillow

root = Tk()
root.title("Nado GUI")

# 파일 추가


def add_file():
    files = filedialog.askopenfilenames(
        title="이미지 파일을 선택하세요",
        filetypes=(("Png File", "*.png"), ("All Files", ".*")),
        initialdir="/",
    )

    for file in files:
        list_file.insert(END, file)


# 파일 삭제
def del_file():
    # 인덱스가 변경으로 인한 비정상적인 삭제를 막기 위해 뒤에서부터 삭제
    for item in reversed(list_file.curselection()):
        list_file.delete(item)


# 저장 경로 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == "":
        print("폴더를 선택하세요")
        return

    txt_dest_path.delete(0, END)  # 이전에 선택한 폴더 경로 삭제
    txt_dest_path.insert(
        0, folder_selected
    )  # Entry는 (0, END), TextWidget은 ('1.0', END)


# 이미지 통합
def merge_image():
    try:
        # 가로 높이
        img_width = cmb_width.get()
        if img_width == '원본유지':
            img_width = -1  # -1 일때는 원본 기준으로
        else:
            img_width = int(img_width)

        # 간격
        img_space = cmb_space.get()
        if img_space == '좁게':
            img_space = 30
        elif img_space == '보통':
            img_space = 60
        elif img_space == '넓게':
            img_space = 90
        else:  # 없음
            img_space = 0

        # 포멧
        img_format = cmb_format.get().lower()  # PNG, JPG, BMP 값을 받아와서 소문자로 변경

        # print(list_file.get(0, END))  # 모든 파일 목록을 가져오기
        images = [Image.open(x) for x in list_file.get(0, END)]
        # size -> size[0] : width, size[1] : height
        # width = [x.size[0] for x in images]
        # height = [x.size[1] for x in images]

        # 이미지 사이즈 리스트에 넣어서 하나씩 처리
        image_sizes = []  # [(width1, height1), (width2, height2), ...]
        if img_width > -1:
            image_sizes = [(int(img_width), int(
                img_width * x.size[1] / x.size[0])) for x in images]
        else:
            # 원본 사이즈
            image_sizes = [(x.size[0], x.size[1]) for x in images]

        # 계산식
        # 100 * 60 이미지가 있음. -> width를 80으로 줄이면 height 는?
        # (원본 width) : (원본 height) = (변경 width) : (변경 height)
        #      100     :       60      =       80    :      ?
        #       x      :       y       =       x'    :      y'
        #    xy` = x`y
        #    y` = x`y / x
        #   100:60=80:48

        # 우리 코드에 대입하려면?
        # x = width = size[0]
        # y = height = size[1]
        # x` = img_width # 이 값으로 변경 해야 함
        # y` = x`y / x = img_width * size[1] / size[0]

        width, height = zip(*(image_sizes))

        # 최대 넓이, 전체 높이 구하기
        max_width, total_height = max(width), sum(height)

        # 스케치북 준비
        if img_space > 0:  # 이미지 간격 옵션 적용
            total_height += (img_space * (len(images) - 1))

        result_img = Image.new(
            'RGB', (max_width, total_height), (255, 255, 255))
        y_offset = 0

        # for img in images:
        #     result_img.paste(img, (0, y_offset))
        #     y_offset += img.size[1]

        for idx, img in enumerate(images):
            # width가 원본유지가 아닐 때는 이미지 크기 조정
            if img_width > -1:
                img = img.resize(image_sizes[idx])

            result_img.paste(img, (0, y_offset))
            y_offset += (img.size[1] + img_space)  # height 값 + 사용자가 지정한 간격

            progress = ((idx + 1) / len(images)) * 100
            p_var.set(progress)
            progress_bar.update()

        # 포맷 옵션 처리
        file_name = "nado_photo." + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path)
        msgbox.showinfo("알림", "작업이 완료되었습니다.")
    except Exception as error:
        msgbox.showerror("에러", error)


# 프로그램 시작

def start():
    # 파일 유무 체크
    if list_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요.")
        return

    # 저장 경로 유무 체크
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요.")
        return

    print(cmb_format.get(), cmb_space.get(), cmb_width.get())

    # 이미지 통합
    merge_image()


# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(
    file_frame, padx=5, pady=5, width=12, text="파일추가", command=add_file
)
btn_add_file.pack(side="left", padx=5, pady=5)

btn_del_file = Button(
    file_frame, padx=5, pady=5, width=12, text="선택삭제", command=del_file
)
btn_del_file.pack(side="right", padx=5, pady=5)


# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5, ipady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(
    list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set
)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True,
                   ipady=4, padx=5, pady=5)  # 높이 변경

btn_dest_path = Button(path_frame, text="찾아보기",
                       width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1. 가로 넓이 옵션
# 가로 넓이 레이블
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

# 가로 넓이 콤보
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly",
                         values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2. 간격 옵션
# 간격 옵션 레이블
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

# 간격 옵션 콤보
opt_width = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly",
                         values=opt_width, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# 3. 파일 포멧 옵션
# 파일 포맷 옵션 레이블
lbl_space = Label(frame_option, text="포맷", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

# 파일 포맷 옵션 콤보
opt_width = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(
    frame_option, state="readonly", values=opt_width, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)


# 진생 상황 Progress Bar
frame_progress = ttk.Labelframe(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5, ipady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기",
                   width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5,
                   text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)


root.resizable(False, False)
root.mainloop()
