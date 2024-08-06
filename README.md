# To-Do List Manager as  *To_do.py*

## Description

The **To-Do List Manager** is a simple yet efficient application designed to help users keep track of their daily tasks. With a user-friendly interface built using Tkinter, this application allows users to add, delete, and manage their tasks with ease. The application uses SQLite to store tasks persistently, ensuring that your to-do list remains intact even after closing the application.

## Features

- **Add Tasks:** Quickly add new tasks to your to-do list.
- **Delete Tasks:** Remove tasks that are completed or no longer needed.
- **Clear All Tasks:** Delete all tasks at once if required.
- **Persistent Storage:** Uses SQLite database to store tasks persistently.
- **User-Friendly Interface:** Easy-to-use GUI with buttons and list display.

**CODE EXPLANATION**

#Main Window Setup: The application initializes the main Tkinter window with a specific size, title, and background color. It includes two primary frames for header and functions.

#Database Connection: A connection to an SQLite database is established, where tasks are stored in a table named tasks. This ensures task persistence.

#Functions:
**job_add**: Adds a new task to the list and database.
**list_update**: Updates the task list in the UI.
**delete_job**: Removes the selected task from the list and database.
**delete_all_jobs**: Clears all tasks from the list and database.
**clear_list**: Clears the displayed list of tasks.
**close**: Closes the application and commits changes to the database.
**dbs_recover**: Recovers tasks from the database on startup.
**GUI Elements**: Buttons, labels, and list boxes are used for task management, with various font styles and colors for a pleasant user experience.
**Main Loop**: The application runs using mainloop() to keep the window responsive.

**Technologies Used**
#Python: The primary programming language for the application.
#Tkinter: For creating the graphical user interface.
#SQLite3: For persistent storage of tasks.

**************************************************************************************************************************************************************************************************************************************************************************************

### 2. Password Generator AS *pss.py*

## Description

**Password Generator** application provides a secure way to create random passwords based on user-defined length. It uses a mix of uppercase letters, lowercase letters, numbers, and special characters to ensure robust password creation. This tool is particularly useful for enhancing security in online accounts by generating strong passwords.

## Features

**Customizable Length:** Choose password lengths from 4 to 16 characters.
**Random Generation:** Generates a random password each time with a mix of characters.
**User-Friendly Interface:** Intuitive GUI to select password length and generate passwords.
**Reset Option:** Easily reset the selection to generate a new password.

**Code Explanation**
***Main Window Setup***: Initializes the main Tkinter window with specific dimensions, title, and background color. The interface is divided into frames for layout management.

***Password Generation Logic***:
The gen_pass function creates a password using a combination of uppercase letters, lowercase letters, numbers, and special characters.
The random.sample method is used to select a random set of characters based on the chosen length.
Dropdown for Length Selection: Uses Tkinter's OptionMenu to allow users to select password length, updating the application state accordingly.

***Buttons and Labels***: Provides buttons for generating and resetting passwords, with labels displaying results.

***Main Loop***: The application runs using mainloop() to keep the window responsive.

**Technologies Used**
*Python*: The primary programming language for the application.
*Tkinter*: For creating the graphical user interface.
*Random Module*: For generating random selections of characters.

************************************************************************************************************************************************************************************************************************************************************************************************************************************

### 3.Rock Paper Scissors Game  As **rps.py**

## Description
The **Rock Paper Scissors Game** brings the classic hand game to your computer screen with a fun and interactive graphical interface. Built using Python and Tkinter, this application allows you to play against the computer, testing your strategy skills in this timeless game.

## Features

- **Interactive Gameplay:** Play Rock, Paper, Scissors against the computer.
- **Visual Feedback:** Displays hand gesture images for both player and computer selections.
- **Randomized Opponent:** The computer makes random selections, making each game unique.
- **Clear Results:** Displays the outcome of each match (win, lose, or draw).
- **User-Friendly Interface:** Designed for easy interaction and enjoyment.
- 

**Code Explanation**

***Main Window Setup***: Initializes the main Tkinter window with specific dimensions, title, and background color. The interface is divided into frames for layout management.

***Password Generation Logic***:
The gen_pass function creates a password using a combination of uppercase letters, lowercase letters, numbers, and special characters.
The random.sample method is used to select a random set of characters based on the chosen length.
Dropdown for Length Selection: Uses Tkinter's OptionMenu to allow users to select password length, updating the application state accordingly.

***Buttons and Labels***: Provides buttons for generating and resetting passwords, with labels displaying results.

***Main Loop***: The application runs using mainloop() to keep the window responsive.

**Technologies Used**
*Python*: The primary programming language for the application.
*Tkinter*: For creating the graphical user interface.
*Random Module*: For generating random selections of characters.
