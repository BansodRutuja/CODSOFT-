import tkinter as tnk
import random                           
from tkinter import messagebox
import sqlite3 as sql3
from tkinter import *
guiWindow = tnk.Tk()  


#function for randomly generating password
def gen_pass(len):
    "this function accept len and in return give randomly generated password"


    #variable that holds all cahracters required to generate the password.
    listofchar = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*()?/~"

    #returing char from list according to len obtain.
    char_select = random.sample(listofchar,len)

    char_string = "".join(char_select)                               #converting char from list into string.

    char_label.config(text=char_string)                              #displaying generated password string.

    print("Generatd Password : ",char_string)     

#function for cheking user choice from option.
def selection():
        len = length_var.get()  

        if len!=0:
            gen_pass(len)
        
        else:
            messagebox.showerror("Invalid Selection","Plz. Select Length Of Password")


#function for printing length of password.
def print_length():
        print("Selected length password :",length_var.get(),"Characters")      


#function to reset the generator.
def reset():
        length_var.set(0)    

        char_label.config(text="")


#main function.
if __name__=="__main__":

        #guiWindow = tnk.TK()
        guiWindow.title("Password Generator - RB")
        guiWindow.geometry("500x400+400+200")
        guiWindow.config(bg="#FFE082")


#adding  frames.
heading_frame = Frame(guiWindow, bg = "#7E57C2",width=20)  
dropdown_frame = Frame(guiWindow, bg = "#B39DDB")  
button_frame = Frame(guiWindow, bg = "#FFE082")  
result_frame = Frame(guiWindow, bg = "#B39DDB")


#using pack()method to place frames in gui.
heading_frame.pack(fill = "both") 
dropdown_frame.pack(pady= 20,padx=60,side=tnk.TOP)  
button_frame.pack(padx=70,pady = 40,side=tnk.LEFT)  
result_frame.pack(padx=0,pady = 0,side=tnk.LEFT)


#adding label for header.
heading = tnk.Label(  
    heading_frame,  
    text = "SecureString  Generator",  
    font = ("Comic Sans Ms", "20"),  
    bg = "#7E57C2",  
    fg = "#FFFFFF"  
    )  

subheading = tnk.Label(                                                  #label for subheader. 
    text = "Customize the Length :",  
    font = ("Bahnschrift SemiBold", "14","bold"),  
    bg = "#FFE082",  
    fg = "#BA0F30"  
    ) 


#using pack() method placing above label in gui. 
heading.pack(pady = 25)  
subheading.place(x=10,y=110)

#instanctiating  IntVar() variable
length_var = IntVar()
length_var.set(0)                                                           #setting initial value of object of IntVar().


#defining the  length of list.
length_options = [4, 6, 8, 10, 12, 16]


#variable that holds dropdown menu.
dropdown_menu = tnk.OptionMenu(  
    dropdown_frame,  
    length_var,  
    *length_options,  
    command=lambda x: print_length()  
)


#adding dropdown menu in gui.
dropdown_menu.config(font=("Times New Roman", "12"), bg="#00968A")
dropdown_menu.pack(padx=0,pady=0)

#adding buttons for generate password and reset.
get_pass = tnk.Button(  
        button_frame,  
        text="Get Password",  
        font=("Bahnschrift SemiBold", "12"),  
        width=16,  
        bg="#EC407A",  
        fg="#FFFFFF",  
        activebackground="#006400",  
        activeforeground="#FFFFFF",  
        relief=GROOVE,  
        command=selection  
    )  
# button to clear everything  
clear_all = tnk.Button(  
        button_frame,  
        text="Reset",  
        font=("Bahnschrift SemiBold", "12"),  
        width=16,  
        bg="#29B6F6",
        fg="#FFFFFF",  
        activebackground="#8B0000",  
        activeforeground="#FFFFFF",  
        relief=GROOVE,  
        command=reset  
)


# using the grid() method to set the position of the above buttons in grid format      
get_pass.grid(row=0, column=0, padx=0, pady=30) 
clear_all.grid(row=2, column=0, padx=0, pady=10) 


char_label = tnk.Label(  
        result_frame,  
        text="",  
        width=17,
        font=("Consolas", "15", "bold"),  
        bg="#E6E6FA",  
        fg="#000000" 
         
)  
#placing label in gui.
char_label.pack() 



#using mainloop() method to run application.ss
guiWindow.mainloop()

