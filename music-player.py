import pygame.mixer as mixer
from tkinter import *
from tkinter import filedialog
import os 

root = Tk()
root.geometry("900x500")
root.title('Music Player')
song_list = []
paused = False
mixer.init()

def play_song(song_list):
	global paused
	name = song_list.get(ACTIVE)
	
	if not paused:
		mixer.music.load(os.path.join(root.directory, name))
		mixer.music.play()
	else:
		mixer.music.unpause()
		paused = False

def pause_music():
	global paused

	mixer.music.pause()
	paused = True
 
def list_mp3s():
	folder_path = filedialog.askdirectory()
	root.directory = folder_path

	if folder_path:
		for file in os.listdir(folder_path):
			if file.endswith(".mp3"):
				song_list.append(file)
				print(file)
				listbox.insert(END, file)

open_folder_btn = Button(root, text="Choose Folder", command=list_mp3s)
open_folder_btn.pack()

# Listbox of songs
listbox = Listbox(root, width=50, height=15)
listbox.pack()

play_btn = Button(root, text="Play", command=lambda: play_song(listbox))
pause_btn = Button(root, text="Pause", command=pause_music)
play_btn.pack()
pause_btn.pack()

root.resizable(False, False)
root.mainloop()