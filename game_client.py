#I have finally decided, that I will do a Game! (Multiplayer with every PC in your Local Network)
#Importing Modules
from tools import *
from tkinter import *
import pygame
from pygame.locals import *

class start_client:
    def __init__(self):
        self.username = ""
        self.winlist = []
    def create_player(self):
        FILE = class_read_write("player.txt")
        try:
            [self.username,self.winlist] = FILE.read()
            GAME = game(self.username, self.winlist)
            GAME.start()
        except FileNotFoundError:

            def create():
                self.username = entry_username.get()
                if self.username != "":
                    self.winlist = []
                    locallist = []
                    locallist.append(self.username)
                    locallist.append(self.winlist)
                    FILE.write(locallist)
                    GAME = game(self.username,self.winlist)
                    GAME.start()
                    window.quit()

            window = Tk()
            label_username = Label(window, text="Username")
            label_username.pack()
            entry_username = Entry(window)
            entry_username.pack()
            button_create = Button(window, text="Create!", command=lambda : create())
            button_create.pack()
            window.mainloop()

#TODO create user data, If not exsisting

#TODO connect to server

#TODO send user data

#TODO retrieve opponent data

#TODO make "place" function or class, that places on a field and sends the Data to the Server

#TODO make "checkwin" function or class, that checks, If one player has won

#TODO make "drawgamefield" function or class, that draws the game Field
class game:
    def __init__(self,username,winlist):
        self.username = username
        self.winlist = winlist
    def start(self):
        pygame.init()
        pygame.display.set_mode((800,600))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.update()

CLIENT = start_client()
CLIENT.create_player()