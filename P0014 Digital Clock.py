#import Tkinter library and Time in Python
from tkinter import Label, Tk
import time

#define title and size, resizable window True(1,1), fixed window False(0,0)
app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("500x150")
app_window.resizable(1,1)

#define time font & color, border width & background color of clock)
text_font= ("Boulder", 68, 'bold')
background = "#f2e750"
foreground= "#363529"
border_width = 25

#combine all elements to define the label of the clock application
label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

#define the main function of the clock, set text of label as the realtime
def digital_clock():
        time_live = time.strftime("%H:%M:%S")
        label.config(text=time_live)
        label.after(200, digital_clock)

#run and see the output
digital_clock()
app_window.mainloop()
