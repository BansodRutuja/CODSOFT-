from tkinter import *
import tkinter as tnk
from PIL import Image, ImageTk  # Pillow is for image processing
import random
import sys

# Function to load images
def load_image(file_name, width=300, height=210):
    try:
        img = Image.open(file_name)
        img = img.resize((width, height))
        return ImageTk.PhotoImage(img)
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return None
    except Exception as e:
        print(f"Error loading image {file_name}: {e}")
        return None

# Create a class for the game to maintain image references
class RockPaperScissorsGame:
    def __init__(self, root):
        self.guiWindow = root
        self.guiWindow.title('Let\'s Play - Rock Paper Scissors')
        self.guiWindow.geometry('800x700')
        self.guiWindow.configure(bg='white')

        # Create a canvas
        self.canvas = Canvas(self.guiWindow, width=800, height=700, bg='white')
        self.canvas.grid(row=0, column=0)

        # Create labels for player and computer 
        self.l1 = Label(self.guiWindow, width=150,height=4,bg='#FCCB2F')
        self.l2 = Label(self.guiWindow, text='Ultimate Gesture Game', font=('Comic Sans MS', 30,'italic'),fg='black',bg='#FCCB2F')
        self.l3 = Label(self.guiWindow, text='You', font=('Comic Sans MS', 22,'bold'),bg='white',fg='#149B82')
        self.l4 = Label(self.guiWindow, text='Opponent', font=('Comic Sans MS', 22,'bold'),bg='white',fg='#149B82')

        # Placing the labels on the main window
        self.l1.place(x=0, y=2)
        self.l2.place(x=180, y=14)
        self.l3.place(x=100, y=100)
        self.l4.place(x=560, y=100)

        # Load images for hand gestures and selection
        print("Loading images...")

        # Load all images with consistent width and height
        self.rock_left = load_image("D:/CODSOFT/rps/images/rock-left.jpg", 350, 210)
        self.rock_right = load_image("D:/CODSOFT/rps/images/rock-right.jpg", 350, 210)
        self.paper_left = load_image("D:/CODSOFT/rps/images/paper-left.jpg", 350, 210)
        self.paper_right = load_image("D:/CODSOFT/rps/images/paper-right.jpg", 350, 210)
        self.scissor_left = load_image("D:/CODSOFT/rps/images/scissor-left.jpg", 350, 210)
        self.scissor_right = load_image("D:/CODSOFT/rps/images/scissor-right.jpg", 350, 210)
        self.img_s1 = load_image("D:/CODSOFT/rps/images/selection image.jpg", 280, 150)
        self.img_s2 = load_image("D:/CODSOFT/rps/images/selection image2.jpg", 280, 116)

        # Check if any image is missing
        if None in [self.rock_left, self.rock_right, self.paper_left, self.paper_right,
                    self.scissor_left, self.scissor_right, self.img_s1, self.img_s2]:
            print("One or more images are missing. Please check the file paths.")
            self.guiWindow.destroy()  # Exit if images are not loaded
            sys.exit(1)  # Use sys.exit to terminate with an error code

        print("Images loaded successfully.")

        # Placing selection image on canvas on specific coordinates
        self.canvas.create_image(0, 160, anchor=NW, image=self.rock_left)  # Set all images to y-coordinate 160
        self.canvas.create_image(500, 160, anchor=NW, image=self.rock_right)

        # Adjusted positioning for Paper and Scissor images
        self.canvas.create_image(0, 160, anchor=NW, image=self.paper_left)
        self.canvas.create_image(500, 160, anchor=NW, image=self.paper_right)
        self.canvas.create_image(0, 160, anchor=NW, image=self.scissor_left)
        self.canvas.create_image(500, 160, anchor=NW, image=self.scissor_right)

        # Placing selection images
        self.canvas.create_image(20, 450, anchor=NW, image=self.img_s2)  # Moved down by increasing y-coordinate
        self.canvas.create_image(490, 450, anchor=NW, image=self.img_s1)  # Moved down by increasing y-coordinate

        # Buttons for selecting rock, paper & scissor
        self.rock_b = Button(self.guiWindow, bg='white', text='Rock', font=('Comic Sans MS', 17, 'bold'), command=lambda: self.games(1), borderwidth=0, highlightthickness=0, relief='flat')
        self.rock_b.place(x=20, y=560)

        self.paper_b = Button(self.guiWindow, bg='white', text='Paper', font=('Comic Sans MS', 17, 'bold'), command=lambda: self.games(2), borderwidth=0, highlightthickness=0, relief='flat')
        self.paper_b.place(x=128, y=560)

        self.scissor_b = Button(self.guiWindow, bg='white', text='Scissor', font=('Comic Sans MS', 17, 'bold'), command=lambda: self.games(3), borderwidth=0, highlightthickness=0, relief='flat')
        self.scissor_b.place(x=230, y=560)

        # Button to clear output
        self.clear_b = Button(self.guiWindow, bg='#00BEAE',fg='white', text='Clear', font=('Comic Sans MS', 20, 'bold'), width=8, command=self.clear, borderwidth=0, highlightthickness=0, relief='flat')
        self.clear_b.place(x=346, y=550)

    # Function for game logic
    def games(self, players):
        select = [1, 2, 3]
        computer = random.choice(select)  # Assign random choice to computer

        # Clear previous images
        self.canvas.delete('player')
        self.canvas.delete('computer')
        self.canvas.delete('result')

        # Player side
        if players == 1:
            self.canvas.create_image(0, 160, anchor=NW, image=self.rock_left, tag='player')  # Set y-coordinate to 160
        elif players == 2:
            self.canvas.create_image(0, 160, anchor=NW, image=self.paper_left, tag='player')  # Set y-coordinate to 160
        else:
            self.canvas.create_image(0, 160, anchor=NW, image=self.scissor_left, tag='player')  # Set y-coordinate to 160

        # Computer side
        if computer == 1:
            self.canvas.create_image(500, 160, anchor=NW, image=self.rock_right, tag='computer')  # Set y-coordinate to 160
        elif computer == 2:
            self.canvas.create_image(500, 160, anchor=NW, image=self.paper_right, tag='computer')  # Set y-coordinate to 160
        else:
            self.canvas.create_image(500, 160, anchor=NW, image=self.scissor_right, tag='computer')  # Set y-coordinate to 160

        # Determine result
        if players == computer:
            res = 'Draw'
        elif (players == 1 and computer == 3) or (players == 2 and computer == 1) or (players == 3 and computer == 2):
            res = 'You Won'
        else:
            res = 'System Won'

        # Placing result on canvas
        self.canvas.create_text(400, 400, text='' + res, fill="#FF4D45", font=('Comic Sans MS', 32,'bold','italic'), tag='result')

    # Function for clear button
    def clear(self):
        self.canvas.delete('result')
        self.canvas.create_image(0, 160, anchor=NW, image=self.rock_left, tag='player')  # Set y-coordinate to 160
        self.canvas.create_image(500, 160, anchor=NW, image=self.rock_right, tag='computer')  # Set y-coordinate to 160

# Main function to run the game
def main():
    try:
        root = tnk.Tk()
        game = RockPaperScissorsGame(root)
        root.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
