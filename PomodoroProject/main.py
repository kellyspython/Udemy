from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
VINKJE = "\u2713"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text= "Timer")
    vinkjes.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2) # math.floor rond het getal af.
        for _ in range(work_sessions):
            marks += "✓"
        vinkjes.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
label = Label(text="Timer", foreground=GREEN,bg= YELLOW, font=(FONT_NAME, 40, "bold"))
label.grid(column=1, row=0)

button_start = Button(text="Start", command=start_timer, highlightthickness=0)
button_start.grid(column=0, row=3)

button_reset = Button(text="Reset",command=reset, highlightthickness=0)
button_reset.grid(column=2, row=3)

vinkjes = Label(foreground=GREEN, bg=YELLOW, font=(FONT_NAME, 30))
vinkjes.grid(column=1, row=4)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image_tomaat = PhotoImage(file="tomato.png")
canvas.create_image(100, 111,image= image_tomaat )
timer_text = canvas.create_text(100, 135, fill="white", text="00:00", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=2)






window.mainloop()
