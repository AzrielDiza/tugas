from tkinter import *
import pygame
import os
from mutagen.mp3 import MP3
from tkinter import filedialog
from ttkwidgets import Scale

class MusicPlayer:
    # Defining Constructor
    def __init__(self, root):
        self.root = root
        # Title of the window
        self.root.title("Music Player")
        # Window Geometry
        self.root.geometry("800x400+200+200")
        # Initiating Pygame
        pygame.init()
        # Initiating Pygame Mixer
        pygame.mixer.init()
        # Declaring track Variable
        self.track = StringVar()
        # Declaring Status Variable
        self.status = StringVar()
        # Creating Track Frame for Song label & status label
        trackframe = LabelFrame(self.root, text="Song Track", font=(
            "times new roman", 15, "bold"), bg="grey", fg="white", bd=5, relief=GROOVE)
        trackframe.place(x=0, y=0, width=600, height=100)
        # Inserting Song Track Label
        songtrack = Label(trackframe, textvariable=self.track, width=20, font=(
            "times new roman", 24, "bold"), bg="grey", fg="gold").grid(row=0, column=0, padx=10, pady=5)
        # Inserting Status Label
        trackstatus = Label(trackframe, textvariable=self.status, font=(
            "times new roman", 24, "bold"), bg="grey", fg="gold").grid(row=0, column=1, padx=10, pady=5)
        # Creating Button Frame
        buttonframe = LabelFrame(self.root, text="Control Panel", font=(
            "times new roman", 15, "bold"), bg="grey", fg="white", bd=5, relief=GROOVE)
        buttonframe.place(x=0, y=100, width=600, height=100)
        # Inserting Play Button
        playbtn = Button(buttonframe, text="PLAY", command=self.play, width=10, height=1, font=(
            "times new roman", 16, "bold"), fg="navyblue", bg="gold").grid(row=0, column=0, padx=10, pady=5)
        # Inserting Pause Button
        pausebtn = Button(buttonframe, text="PAUSE", command=self.pause, width=10, height=1, font=(
            "times new roman", 16, "bold"), fg="navyblue", bg="gold").grid(row=0, column=1, padx=10, pady=5)
        # Inserting Resume Button
        resumebtn = Button(buttonframe, text="RESUME", command=self.resume, width=10, height=1, font=(
            "times new roman", 16, "bold"), fg="navyblue", bg="gold").grid(row=0, column=2, padx=10, pady=5)
        # Inserting Stop Button
        stopbtn = Button(buttonframe, text="STOP", command=self.stop, width=10, height=1, font=(
            "times new roman", 16, "bold"), fg="navyblue", bg="gold").grid(row=0, column=3, padx=10, pady=5)
        # Inserting Load Button
        loadbtn = Button(buttonframe, text="LOAD", command=self.load, width=10, height=1, font=(
            "times new roman", 16, "bold"), fg="navyblue", bg="gold").grid(row=0, column=4, padx=10, pady=5)
        # Creating Progress Bar Frame
        progressframe = LabelFrame(self.root, text="Progress Bar", font=(
            "times new roman", 15, "bold"), bg="grey", fg="white", bd=5, relief=GROOVE)
        progressframe.place(x=0, y=200, width=600, height=100)
        # Inserting Progress Bar
        self.progress = Scale(progressframe, from_=0, to=100, orient=HORIZONTAL, length=500, command=self.change)
        self.progress.grid(row=0, column=0, padx=10, pady=5)
        # Inserting Volume Slider
        self.volume = Scale(progressframe, from_=0, to=100, orient=VERTICAL, length=80, command=self.change)
        self.volume.grid(row=0, column=1, padx=10, pady=5)
        # Setting default volume
        self.volume.set(50)
        # Initializing mixer volume
        pygame.mixer.music.set_volume(0.5)

    # Defining Play function
    def play(self):
        # Displaying Selected Song title
        self.track.set(self.playlist.get(ACTIVE))
        # Displaying Status
        self.status.set("-Playing")
        # Loading Selected Song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        # Playing Selected Song
        pygame.mixer.music.play()
        # Getting Song Length
        song = MP3(self.playlist.get(ACTIVE))
        # Getting Total Length Formatted
        total_length = song.info.length
        mins, secs = divmod(total_length, 60)
        mins = round(mins)
        secs = round(secs)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        self.status.set("Playing - " + timeformat)
        # Moving Progress Bar
        self.update()

    # Defining Pause function
    def pause(self):
        # Displaying Status
        self.status.set("-Paused")
        # Pausing Music
        pygame.mixer.music.pause()

    # Defining Resume function
    def resume(self):
        # Displaying Status
        self.status.set("-Playing")
        # Resuming Music
        pygame.mixer.music.unpause()

    # Defining Stop function
    def stop(self):
        # Displaying Status
        self.status.set("-Stopped")
        # Stopping Music
        pygame.mixer.music.stop()

    # Defining Load function
    def load(self):
        # Asking for Music File
        self.filename = filedialog.askopenfilename()
        # Updating Playlist
        self.playlist.insert(END, self.filename)

    # Defining Update function
    def update(self):
        # Getting Current Song Position
        current_pos = pygame.mixer.music.get_pos() // 1000
        # Moving Progress Bar
        self.progress.set(current_pos)
        # Updating Progress Bar
        self.progress.after(2, self.update)

    # Defining Change function
    def change(self, event):
        # Getting Slider Position
        slider_pos = self.progress.get()
        # Setting Volume
        pygame.mixer.music.set_volume(self.volume.get() / 100)
        # Jumping to Song Position
        pygame.mixer.music.play(loops=0, start=slider_pos)

# Creating TK Container
root = Tk()
# Passing Root to MusicPlayer Class
MusicPlayer(root)
# Root Window Looping
root.mainloop()
