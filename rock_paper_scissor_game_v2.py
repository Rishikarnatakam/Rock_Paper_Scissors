import random
from tkinter import *
from PIL import ImageTk,Image
import customtkinter as ctk
import os


playerscore=0
compscore=0
root = ctk.CTk()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(current_dir, "rock_paper_scissor_game_imgs")


#images
rock_img = ctk.CTkImage(Image.open(os.path.join(images_dir, "rock.png")), size=(200,200))
paper_img = ctk.CTkImage(Image.open(os.path.join(images_dir, "paper.png")), size=(200,200))
scissor_img = ctk.CTkImage(Image.open(os.path.join(images_dir, "scissor.png")), size=(200,200))
quit_img = ctk.CTkImage(Image.open(os.path.join(images_dir, "quit2.png")), size=(20,20))


#buttons
rock_button = ctk.CTkButton(master=root,text="",image=rock_img,command=lambda: userInput("rock"))
paper_button = ctk.CTkButton(master=root,text="",image=paper_img,command=lambda: userInput("paper"))
scissor_button = ctk.CTkButton(master=root,text="",image=scissor_img,command=lambda: userInput("scissor"))
#quit_button = ctk.CTkButton(master=root,text="",image=quit_img,command=lambda: userInput("quit"),width=20,height=20,fg_color="transparent",hover_color="dark grey")
rock_button.grid(row=2,column=0,padx=40,pady=30)
paper_button.grid(row=2,column=1,padx=40,pady=30)
scissor_button.grid(row=2,column=2,padx=40,pady=30)
#quit_button.grid(row=0,column=3)


#resultbox
result_box = ctk.CTkLabel(master=root,text = "result",font=("Arial",50))
result_box.grid(row=1,columnspan=4)


#gamebox
user_choice = ctk.CTkLabel(master=root,text="USER",image=rock_img,compound=BOTTOM,font=("Arial",40))
user_choice.grid(row=0,column=2,padx=40,pady=20)
comp_choice = ctk.CTkLabel(master=root,text="COMPUTER",image=rock_img,compound=BOTTOM,font=("Arial",40))
comp_choice.grid(row=0,column=0,padx=40,pady=20)


#scoreframe
scoreframe=ctk.CTkFrame(master=root,width=200,height=100)
scoreframe.grid(row=0,column=1)


#compscore
comp_score = ctk.CTkLabel(master=scoreframe,text="COMP : "+str(compscore),width=70,height=80,font=("Arial",20))
comp_score.grid(row=0,column=0,padx=20)
player_score = ctk.CTkLabel(master=scoreframe,text="YOU : "+str(playerscore),width=70,height=80,font=("Arial",20))
player_score.grid(row=0,column=1,padx=20)


#display_choice
def display_choice(comp,player):
    if comp=="rock":comp_img=rock_img
    if comp=="paper":comp_img=paper_img
    if comp=="scissor":comp_img=scissor_img
    if player=="rock":player_img=rock_img
    if player=="paper":player_img=paper_img
    if player=="scissor":player_img=scissor_img
    user_choice.configure(image=player_img)
    comp_choice.configure(image=comp_img)


#title
root.title("Rock paper sciccor Game")


#icon
root.iconbitmap(os.path.join(images_dir, "rock_paper_scissor_icon.ico"))


#result_display function
def result(string,result_int):
    global playerscore
    global compscore
    result_box.configure(text=string)
    if result_int==1:
        playerscore+=1
        player_score.configure(text="YOU : "+str(playerscore))
    elif result_int==0:
        compscore+=1
        comp_score.configure(text="COMP : "+str(compscore))
    else :
        pass


#game_code
def userInput(choice):
    player = choice
    possible = ('rock','paper','scissor')
    comp = random.choice(possible)
    display_choice(comp, player)
    if player == "quit":
        root.destroy()
    if comp == player :
        result("Tie",2)
    elif comp=="rock" and player=="paper":
        result("You Won",1)
    elif comp=="paper" and player=="scissor":
        result("You Won",1)
    elif comp=="scissor" and player=="rock":
        result("You Won",1)
    else:
        result("You Lost",0)

   
root.mainloop()