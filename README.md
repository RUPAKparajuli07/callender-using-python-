## Code Documentation

This code is a simple GUI application that displays a calendar for a given year using the Tkinter library in Python. It also shows the current time in a label and allows the user to enter a year to display the corresponding calendar.

### Importing Required Modules

The code starts by importing the necessary modules:
```python
from tkinter import *
import calendar
import time
```
- `tkinter`: It is a standard Python interface to the Tk GUI toolkit and is used for creating the GUI elements.
- `calendar`: It provides useful functions to generate and manipulate calendars.
- `time`: It provides functions to work with time-related operations.

### Function: `show_calendar(year)`

This function creates a new window to display the calendar for the given year:
```python
def show_calendar(year):
    # create new window for calendar
    calendar_window = Toplevel(root)
    calendar_window.config(background='grey')
    calendar_window.title(f"Calendar for {year}")
```
- `Toplevel(root)`: It creates a new top-level window (child window) associated with the root window.
- `background`: Sets the background color of the calendar window to grey.
- `title`: Sets the title of the window to "Calendar for {year}".

Next, the function makes the window fullscreen:
```python
    # make the window fullscreen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    calendar_window.geometry(f"{screen_width}x{screen_height}")
```
- `winfo_screenwidth()`: Returns the width of the screen in pixels.
- `winfo_screenheight()`: Returns the height of the screen in pixels.
- `geometry()`: Sets the dimensions of the window to match the screen width and height.

Then, the calendar for the specified year is generated using the `calendar` module and displayed in a label within the calendar window:
```python
    # create calendar label
    gui_content = calendar.calendar(year)
    cal_year = Label(calendar_window, text=gui_content, font="Consolas 10 bold", justify=LEFT)
    cal_year.pack(padx=20, pady=20)
```
- `calendar(year)`: Generates the calendar for the specified year as a multi-line string.
- `Label(calendar_window, text=gui_content, font="Consolas 10 bold", justify=LEFT)`: Creates a label widget to display the calendar content.
- `pack(padx=20, pady=20)`: Packs the label widget into the calendar window with a padding of 20 pixels on each side.

### Function: `get_year()`

This function is called when the "Show Calendar" button is clicked. It retrieves the year entered by the user, converts it to an integer, and calls the `show_calendar(year)` function to display the calendar:
```python
def get_year():
    year = int(year_field.get())
    show_calendar(year)
```
- `year_field.get()`: Retrieves the text entered in the year entry field.
- `int(year_field.get())`: Converts the entered text to an integer.

### Creating the Root Window

The root window is the main window of the application. It is created using `Tk()` and configured with a grey background and a title:
```python
root = Tk()
root.config(background='grey')
root.title("Calendar")
```

The root window is then set to fullscreen:
```python
# make the root window fullscreen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
```

### Creating GUI Elements

The code creates various GUI elements and places them in the root window using pack geometry manager

- Creating the time label:
```python
time_label = Label(root, font=("Arial", 12), bg="grey", fg="white")
time_label.pack(side=TOP, fill=X)
```
- Creating the year label:
```python
year_label = Label(root, text="Enter year:", font=("Arial", 12), bg="grey", fg="white")
year_label.pack(pady=(50,0))
```
- Creating the year entry field:
```python
year_field = Entry(root, font=("Arial", 12), justify="center")
year_field.pack(ipady=5, padx=10)
```
- Creating the "Show Calendar" button:
```python
show_button = Button(root, text="Show Calendar", font=("Arial", 12), bg="blue", fg="white", command=get_year)
show_button.pack(pady=20)
```

### Making the Root Window Responsive

To make the GUI elements resize and adapt to window resizing, the pack_configure method is called on each element:
```python
time_label.pack_configure(expand=True, anchor=NW)
year_label.pack_configure(expand=True)
year_field.pack_configure(expand=True)
show_button.pack_configure(expand=True)
root.pack_propagate(0)
```
- `pack_configure(expand=True, anchor=NW)`: Allows the time label to expand horizontally and anchor to the northwest corner of the window.
- `pack_configure(expand=True)`: Allows the year label, year entry field, and show button to expand horizontally.
- `pack_propagate(0)`: Prevents the root window from resizing based on the size of its packed elements.

### Function: `update_time()`

This function is used to update the time label with the current time every second:
```python
def update_time():
    current_time = time.strftime("%H:%M:%S %p")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)
```
- `time.strftime("%H:%M:%S %p")`: Formats the current time as "HH:MM:SS AM/PM".
- `time_label.config(text=current_time)`: Updates the text of the time label with the current time.
- `time_label.after(1000, update_time)`: Schedules the update_time function to be called after 1000 milliseconds (1 second).

### Updating the Time Label

The update_time() function is called once to start updating the time label:
```python
update_time()
```

### Running the Application

Finally, the main event loop is started to run the application:
```python
root.mainloop()
```
The program remains in the event loop until the window is closed or the program is terminated.
