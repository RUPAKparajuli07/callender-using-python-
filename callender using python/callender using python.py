from tkinter import *
import calendar
import time

def show_calendar(year):
    # create new window for calendar
    calendar_window = Toplevel(root)
    calendar_window.config(background='grey')
    calendar_window.title(f"Calendar for {year}")
    
    # make the window fullscreen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    calendar_window.geometry(f"{screen_width}x{screen_height}")
    
    # create calendar label
    gui_content = calendar.calendar(year)
    cal_year = Label(calendar_window, text=gui_content, font="Consolas 10 bold", justify=LEFT)
    cal_year.pack(padx=20, pady=20)

def get_year():
    year = int(year_field.get())
    show_calendar(year)

root = Tk()
root.config(background='grey')
root.title("Calendar")

# make the root window fullscreen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# create label for time
time_label = Label(root, font=("Arial", 12), bg="grey", fg="white")
time_label.pack(side=TOP, fill=X)

# create label and entry for year
year_label = Label(root, text="Enter year:", font=("Arial", 12), bg="grey", fg="white")
year_label.pack(pady=(50,0))

year_field = Entry(root, font=("Arial", 12), justify="center")
year_field.pack(ipady=5, padx=10)

# create button to show calendar
show_button = Button(root, text="Show Calendar", font=("Arial", 12), bg="blue", fg="white", command=get_year)
show_button.pack(pady=20)

# make root window responsive
time_label.pack_configure(expand=True, anchor=NW)
year_label.pack_configure(expand=True)
year_field.pack_configure(expand=True)
show_button.pack_configure(expand=True)
root.pack_propagate(0)

# update the time label every second
def update_time():
    current_time = time.strftime("%H:%M:%S %p")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

update_time()

root.mainloop()
