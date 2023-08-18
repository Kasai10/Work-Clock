import customtkinter as ctk
import os

#put in your time to work in hours (2.5 = two and a half hours)
work_time = 2.5

work_time = work_time * 3600 + 1

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, 'time.txt')


window = ctk.CTk()
window.title('Remaining Time')

my_label = ctk.CTkLabel(window, text='', font=('Helvetica', 48), fg_color='black', bg_color='black', text_color='white')
my_label.pack(fill='both', expand=True)

paused = False 

def toggle_pause():
    global paused
    paused = not paused

global remaining_time
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        remaining_time = int(file.readline())
else:
    remaining_time = work_time

global time_0
time_0 = False
def show_time():
    global remaining_time
    remaining_time = int(remaining_time)

    if paused:
        pause_button.configure(fg_color = 'orchid')
        window.after(1000, show_time)
        return
    
    pause_button.configure(fg_color = '#33A1C9')
    remaining_time = remaining_time - 1

    if remaining_time <= 0:
        my_label.configure(text="TIME'S UP!")
        global time_0
        time_0 = True
        return
    
    seconds = remaining_time % 60
    minutes = int(remaining_time / 60) % 60
    hours = int(remaining_time / 3600)

    time_string = f'{hours:02}:{minutes:02}:{seconds:02}'
    my_label.configure(text=time_string)
    
    window.after(1000, show_time)

def reset_time():
    global remaining_time
    remaining_time = int(work_time - 1)
    seconds = remaining_time % 60
    minutes = int(remaining_time / 60) % 60
    hours = int(remaining_time / 3600)

    time_string = f'{hours:02}:{minutes:02}:{seconds:02}'
    my_label.configure(text=time_string)

def save_time():
    with open(file_path, 'w') as file:
        file.write(str(remaining_time))
    
    if time_0:
        with open(file_path, 'w') as file:
            file.write(str(int(work_time)))
    window.destroy()

frame = ctk.CTkFrame(window, bg_color='black', fg_color='black')
pause_button = ctk.CTkButton(frame, text="Pause/Resume", command=toggle_pause, corner_radius = 8)
pause_button.grid(row=0, column=0, padx=2)

reset_button = ctk.CTkButton(frame, text="Reset", command=reset_time, corner_radius = 8, fg_color='#33A1C9')
reset_button.grid(row=0, column=1, padx=2)

frame.pack(fill='both', expand=True)

window.protocol('WM_DELETE_WINDOW', save_time)

window.after(0, show_time)
window.mainloop()


