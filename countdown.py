# 生成可执行文件
# pyinstaller countdown.py --onefile --noconsole --noupx
import time
import datetime
import winsound
import tkinter as tk

time_end = datetime.datetime.now() + datetime.timedelta(minutes=40)
time_zero = datetime.timedelta(seconds=0)


def beep():
    global time_end
    for i in range(2):
        winsound.Beep(440, 250)  # frequency, duration
        time.sleep(0.25)         # in seconds (0.25 is 250ms)
        winsound.Beep(600, 250)
        time.sleep(0.25)
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    clock.config(text=u"开始休息")
    time_end = datetime.datetime.now() + datetime.timedelta(minutes=10)
    clock.after(1000, tick)


def restart():
    global time_end
    time_end = datetime.datetime.now() + datetime.timedelta(minutes=40)
    clock.config(command=lambda: root.destroy())
    tick()


def pause():
    time.sleep(2)
    clock.config(text=u"再战一回", bg='#dfd')


flag = 1
def tick():
    global time_end, flag
    deltatime = time_end - datetime.datetime.now()
    if deltatime < time_zero:
        if flag == 1:
            flag = 0
            clock.config(text=u"成功番茄", bg='red')
            clock.config(command=restart)
            clock.after(500, beep)
        else:
            flag = 1
            clock.config(text=u"休息完毕")
            clock.after(500, pause)
    else:
        deltatime = str(deltatime).split('.')[0]

        clock.config(text=deltatime)
        # calls itself every 1s
        # to update the time display as needed
        # after为利用tk自身的事件循环机制进行延时调用
        clock.after(1000, tick)

root = tk.Tk() # create a Tk root window
# root.overrideredirect(True)
# -----------------隐藏标题边框 始-------------------- #
root.attributes('-alpha', 0.0) #For icon
#root.lower()
root.iconify()
window = tk.Toplevel(root)
# -----------------设定窗口位置 始-------------------- #
w = 140 # width for the Tk root
h = 50 # height for the Tk root
# get screen width and height
ws = root.winfo_screenwidth() # 屏幕尺寸 宽 x
hs = root.winfo_screenheight() # height of the screen 高 y
# calculate x and y coordinates for the Tk root window
x = ws - w - 100
y = hs - h - 60
# set the dimensions of the screen and where it is placed
# root.geometry('%dx%d+%d+%d' % (w, h, x, y))
window.geometry('%dx%d+%d+%d' % (w, h, x, y))
# -----------------设定窗口位置 终-------------------- #
window.overrideredirect(1) #Remove border
window.attributes('-topmost', 1)
window.attributes('-alpha', 0.5)
#Whatever buttons, etc 
# close = tk.Button(window, text = "Close Window", command = lambda: root.destroy())
# -----------------隐藏标题边框 终-------------------- #

# root.wm_attributes("-topmost", 1) # 窗口置顶
# clock = tk.Label(window, font=('times', 20, 'bold'), bg='green')
clock = tk.Button(window,
                  font=('times', 20, 'bold'),
                  bg='#dfd',
                  command=lambda: root.destroy(),
                  # command = lambda: root.destroy()
)
clock.pack(fill='both', expand=True)
tick()
window.mainloop()

# another:
# https://stackoverflow.com/questions/10596988/making-a-countdown-timer-with-python-and-tkinter
# tkinter Window Always on Top :
# https://www.daniweb.com/programming/software-development/threads/42766/keeping-python-window-on-top-of-others
# set window postion
# https://stackoverflow.com/questions/14910858/how-to-specify-where-a-tkinter-window-opens
# remove window title bar, border
# https://stackoverflow.com/questions/31085533/how-to-remove-just-the-window-border
# Play simple beep with python without external library
# https://stackoverflow.com/questions/4467240/play-simple-beep-with-python-without-external-library
