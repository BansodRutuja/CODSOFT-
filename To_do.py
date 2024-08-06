import tkinter as tnk
from tkinter import messagebox
import sqlite3 as sql3

# Initialize the main window
guiWindow = tnk.Tk()
guiWindow.title("My Task Manager : RB")
guiWindow.geometry("550x550+750+250")
guiWindow.resizable(0, 0)
guiWindow.configure(bg="#FFCCD5")

job =[]

# Function to add job or task in list
def job_add():
    get_a_job = job_field.get()
    if len(get_a_job) == 0:
        messagebox.showinfo('Error', 'Empty Field')
    else:
        job.append(get_a_job)
        cursor.execute('insert into tasks values (?)', (get_a_job,))
        list_update()
        job_field.delete(0, 'end')

# Function to update list
def list_update():
    clear_list()
    for x in job:
        job_Lbox.insert('end', x)

# Function to delete the selected job
def delete_job():
    try:
        job_to_delete = job_Lbox.get(job_Lbox.curselection())
        if job_to_delete in job:
            job.remove(job_to_delete)
        list_update()
        cursor.execute('delete from tasks where title = ?', (job_to_delete,))
    except:
        messagebox.showinfo('No Task Selected', 'Please select task to delete.')

# Function to delete all the jobs
def delete_all_jobs():
    display_msg = messagebox.askyesno('Clear All.', 'Are you sure?')
    if display_msg:
        while len(job) != 0:
            job.pop()
            cursor.execute('delete from tasks')
        list_update()

# Function to clear the list
def clear_list():
    job_Lbox.delete(0, 'end')

# Function to close application
def close():
    print(job)
    connection.commit()
    cursor.close()
    guiWindow.destroy()

# Function to recover the database
def dbs_recover():
    while len(job) != 0:
        job.pop()
    for row in cursor.execute('select title from tasks'):
        job.append(row[0])

# Main function
if __name__ == "__main__":
    # Connecting database to application
    connection = sql3.connect('listOfTasks.db')
    cursor = connection.cursor()
    cursor.execute('create table if not exists tasks (title text)')

    # Adding frames
    header_frame = tnk.Frame(guiWindow, bg="#FF659D")
    functions_frame = tnk.Frame(guiWindow, bg="#FEDCDB")

    # Packing frames
    header_frame.pack(fill="both")
    functions_frame.pack(side="left", expand=True, fill="both")

    # Adding header label
    header_label = tnk.Label(
        header_frame,
        text="The To-Do List",
        font=("Comic Sans Ms", "30"),
        background="#FF659D",
        foreground="#FFFFFF"
    )
    header_label.pack(padx=20, pady=10)

    # Adding job label
    job_label = tnk.Label(
        functions_frame,
        text="Enter the Task:",
        font=("Serif", "13", "bold"),
        background="#FFFFFF",
        foreground="#000000"
    )
    job_label.place(x=238, y=20)

    # Adding job entry field
    job_field = tnk.Entry(
        functions_frame,
        font=("Serif", "12", "bold"),
        width=18,
        background="#FFFFFF",
        foreground="#D90166"
    )
    job_field.place(x=220, y=60)

    # Adding buttons
    add_button = tnk.Button(
        functions_frame,
        text="Add Task",
        width=24,
        font=("Comic Sans Ms Italic", "9", "bold"),
        background="#CCABDB",
        foreground="#000000",
        command=job_add
    )
    del_button = tnk.Button(
        functions_frame,
        text="Delete Task",
        width=24,
        font=("Comic Sans Ms Italic", "9", "bold"),
        background="#FFDD94",
        foreground="#000000",
        command=delete_job
    )
    del_all_button = tnk.Button(
        functions_frame,
        text="Delete All Tasks",
        width=24,
        font=("Comic Sans Ms Italic", "9", "bold"),
        background="#FA897B",
        foreground="#000000",
        command=delete_all_jobs
    )
    exit_button = tnk.Button(
        functions_frame,
        text="Exit",
        width=24,
        font=("Comic Sans Ms Italic", "9", "bold"),
        background="#86A3CE",
        foreground="#000000",
        command=close
    )

    # Placing buttons
    add_button.place(x=20, y=120)
    del_button.place(x=80, y=180)
    del_all_button.place(x=20, y=240)
    exit_button.place(x=80, y=300)

    # Styling task list container
    job_Lbox = tnk.Listbox(
        functions_frame,
        width=26,
        height=13,
        font=("Serif", "12", "bold"),
        selectmode='SINGLE',
        background="#FFFFFF",
        foreground="#000000",
        selectbackground="#FF8DB7",
        selectforeground="#FFFFFF"
    )
    job_Lbox.place(x=300, y=180)

    # Calling database and list update function
    dbs_recover()
    list_update()

    # Using the mainloop() method to run the application
    guiWindow.mainloop()

    # Closing the database connection after the main loop
    connection.commit()
    cursor.close()
    connection.close()
