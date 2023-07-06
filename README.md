<!DOCTYPE html>
<html>
<head>
    <title>Code Documentation</title>
</head>
<body>
    <h1>Code Documentation</h1>
    <h2>Importing Required Modules</h2>
    <pre><code>from tkinter import *<br>
import calendar<br>
import time</code></pre>
    
    <h2>Function: <code>show_calendar(year)</code></h2>
    <pre><code>def show_calendar(year):<br>
    # create new window for calendar<br>
    calendar_window = Toplevel(root)<br>
    calendar_window.config(background='grey')<br>
    calendar_window.title(f"Calendar for {year}")<br><br>
    
    # make the window fullscreen<br>
    screen_width = root.winfo_screenwidth()<br>
    screen_height = root.winfo_screenheight()<br>
    calendar_window.geometry(f"{screen_width}x{screen_height}")<br><br>
    
    # create calendar label<br>
    gui_content = calendar.calendar(year)<br>
    cal_year = Label(calendar_window, text=gui_content, font="Consolas 10 bold", justify=LEFT)<br>
    cal_year.pack(padx=20, pady=20)</code></pre>
    
    <h2>Function: <code>get_year()</code></h2>
    <pre><code>def get_year():<br>
    year = int(year_field.get())<br>
    show_calendar(year)</code></pre>
    
    <h2>Creating the Root Window</h2>
    <pre><code>root = Tk()<br>
root.config(background='grey')<br>
root.title("Calendar")</code></pre>
    
    <h2>Creating GUI Elements</h2>
    <pre><code>time_label = Label(root, font=("Arial", 12), bg="grey", fg="white")<br>
time_label.pack(side=TOP, fill=X)<br><br>
year_label = Label(root, text="Enter year:", font=("Arial", 12), bg="grey", fg="white")<br>
year_label.pack(pady=(50,0))<br><br>
year_field = Entry(root, font=("Arial", 12), justify="center")<br>
year_field.pack(ipady=5, padx=10)<br><br>
show_button = Button(root, text="Show Calendar", font=("Arial", 12), bg="blue", fg="white", command=get_year)<br>
show_button.pack(pady=20)</code></pre>
    
    <h2>Making the Root Window Responsive</h2>
    <pre><code>time_label.pack_configure(expand=True, anchor=NW)<br>
year_label.pack_configure(expand=True)<br>
year_field.pack_configure(expand=True)<br>
show_button.pack_configure(expand=True)<br>
root.pack_propagate(0)</code></pre>
    
    <h2>Function: <code>update_time()</code></h2>
    <pre><code>def update_time():<br>
    current_time = time.strftime("%H:%M:%S %p")<br>
    time_label.config(text=current_time)<br>
    time_label.after(1000, update_time)</code></pre>
    
    <h2>Updating the Time Label</h2>
    <pre><code>update_time()</code></pre>
    
    <h2>Running the Application</h2>
    <pre><code>root.mainloop()</code></pre>
</body>
</html>
