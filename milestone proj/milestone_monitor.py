import tkinter as tk
import datetime

# path to icon image
"""
icon_path = "images/cgev.ico"
"""

# Initialize the root window
root = tk.Tk()
root.title("Junior's Signature's Milestone Monitor")
root.configure(bg="#d8f3dc")
"""
root.icon(icon_path)
"""
root.geometry("1900x300")

# Get today's date and day of the year
today = datetime.date.today()

# Get original day of the year
day_of_year = today.timetuple().tm_yday

# Define progress stages and colors
progress_stages = ["#b7efc5", "#6ede8a", "#25a244", "#1a7431", "#04471c"]

# Button list to store multiple buttons
buttons = []

months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
# functio to create roews of button for a week

def create_row(week):
    # display months label
    for i in range(0, 12):
        month = tk.Label(root, text=months[i],font=["Helvetica", 10], bg="#d8f3dc")
        month.grid(row=0,column=(1+i)*4, padx=2,pady=2)
        # Create buttons dynamically
    for i in range(1,8):  # Example: 5 buttons
        button = tk.Button(root, bg=progress_stages[0], width=1, height=0)
        button.bind("<Button-1>", change_button_color)
        button.grid(row=i, column=week, pady=2, padx=2)
        buttons.append(button)
        
    

# Function to handle button click and cycle through progress stages
def change_button_color(event):
    button = event.widget
    current_color = button.cget("background")
    try:
        next_color = progress_stages[(progress_stages.index(current_color) + 1) % len(progress_stages)]
        button.configure(bg=next_color)
    except ValueError:
        button.configure(bg=progress_stages[0])  # Start with the first color if no match

# Save button states to file
def save_buttons():
    with open("buttons_data.txt", "w") as file:
        for button in buttons:
            bg_color = button.cget("background")
            file.write(bg_color + "\n")


    
# Load button states from file
def load_buttons():
    try:
        with open("buttons_data.txt", "r") as file:
            colors = file.readlines()
        for i, button in enumerate(buttons):
            if i < len(colors):
                button.configure(bg=colors[i].strip())
            else:
                button.configure(bg=progress_stages[0])  # Default color for extra buttons
    except FileNotFoundError:
        # If the file doesn't exist, initialize buttons with default color
        for button in buttons:
            button.configure(bg=progress_stages[0])
            
# Reset all buttons to the initial color
def reset_buttons():
    for button in buttons:
        button.configure(bg=progress_stages[0])


# variable to track dit mode
edit = False

# function to toggle edit mode
def button_edit_on_off():
    global edit
    button_index = 0 
    if not edit:
        # enable edit mode
        for b in buttons:
            if button_index == day_of_year:
                button_index += 1
                bg_color = b.cget("background")
                if bg_color in progress_stages:
                    pass
                else:
                    b.configure(bg="#252422")
            else:
                b.configure(state="disabled")
                b.unbind("<Button-1>")
                button_index += 1
        edit = True # update edit mode
        
    else:
        # Disable edit mode
        for b in buttons:
            b.configure(state="normal")
            b.bind("<Button-1>")
        edit = False

load_buttons()  # Load button states at startup

# create_row()
for i in range(1,52):
    create_row(i)
    
# toggle edit mode
button_edit_on_off()

label_less = tk.Label(root, text="less", font=("Helvetica", 12), bg="#d8f3dc")
label_less.grid(row=9, column=0,padx=2, pady=2)
for index, stage_color in enumerate(progress_stages):
    example_color = tk.Button(root, state="disabled",background=stage_color, width=1, height=0)
    example_color.grid(row=9, column=index+1, padx=2, pady=2)


# Save and Load Buttons
save_button = tk.Button(root, text="Save", command=save_buttons, background="#f07167")
save_button.grid(row=9, column=53, pady=10)

reset_button = tk.Button(root, text="Reset", command=reset_buttons)
reset_button.grid(row=9, column=52, pady=10)

# button to toggle edit mode

edit_button = tk.Button(root, text="Edit", command=button_edit_on_off, background="#f07167")
edit_button.grid(row=9, column=54, pady=10)



    
# Start the Tkinter main loop
root.mainloop()
