import os
import tkinter as tk
from tkinter import PhotoImage
from pygame import mixer
from videoTest import liveVideoTest

### Create the main windows that is music player
class Player(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        mixer.init()
        
        
        self.current = 0
        self.paused = True
        self.played = False
        
        ### Call the createFrames function 
        self.createFrames()
        self.trackWidgets()
        self.controlWidgets()
        
    ### Function to create the frame inside the window
    def createFrames(self):
        ### First frame
        self.track = tk.LabelFrame(self, text=f'Emotion Detection', font=("times new roman", "20", "bold"), bg="grey", fg="white", bd=5, relief=tk.GROOVE)
        self.track.configure(width=700, height=500)
        self.track.grid(row=0, column=0, padx=10)
        
        ### Second frame
        self.controls = tk.LabelFrame(self, font=("times new roman", "15", "bold"), bg="white", fg="white", bd=4, relief=tk.GROOVE)
        self.controls.configure(width=700, height=100)
        self.controls.grid(row=1, column=0, pady=10, padx=10)
    
    def trackWidgets(self):
        self.canvas = tk.Label(self.track, image=img)
        self.canvas.configure(width=700, height=530)
        self.canvas.grid(row=0, column=0)
        
        self.songTrack = tk.Label(self.track, font=("times new roman", "15", "bold"), bg='white', fg='dark blue')
        self.songTrack['text'] = 'Facial Emotion Detection System'
        self.songTrack.configure(width=30, height=1)
        self.songTrack.grid(row=1, column=0)
    
    def controlWidgets(self):
        self.loadSongs = tk.Button(self.controls, bg='green', fg='white', font=("times new roman", "15", "bold"))
        self.loadSongs['text'] = "Detect Emotion"
        self.loadSongs['command'] = self.retrieveEmotions
        self.loadSongs.grid(row=0, column=0, padx=10, pady=5)
    
    def retrieveEmotions(self):
        self.songlist = []
        result = liveVideoTest()
        self.track['text'] = f'Emotion Detected: {result}'

root = tk.Tk()
root.geometry('750x670')
root.wm_title('Facial Emotion Detection System')
root.resizable(width=0, height=0)

img = PhotoImage(file='images/music.gif')

### Call the main window class
app = Player(master=root)
app.mainloop()