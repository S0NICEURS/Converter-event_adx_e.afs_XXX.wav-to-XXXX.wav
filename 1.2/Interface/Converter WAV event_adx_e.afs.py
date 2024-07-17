import ctypes
from tkinter import *
from tkinter import filedialog, messagebox
import os
import shutil

# Masquer la fenêtre de console
if __name__ == "__main__":
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def select_source_folder():
    folder_selected = filedialog.askdirectory()
    source_entry.delete(0, END)
    source_entry.insert(0, folder_selected)

def convert_files():
    source_folder = source_entry.get()
    
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    destination_folder = os.path.join(desktop_path, 'converted_wav_files')

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    for i in range(1, 2728):
        filename = f"event_adx_e.afs_{i:03d}.wav"
        source_file = os.path.join(source_folder, filename)
        if os.path.exists(source_file):
            destination_file = os.path.join(destination_folder, f"{i}.wav")
            shutil.copy(source_file, destination_file)

    messagebox.showinfo("Success", "Files converted successfully!")

# Création de la fenêtre principale Tkinter
fenetre = Tk()
fenetre.geometry('820x200')
fenetre.title('Converter event_adx_e.afs_XXXX.wav to XXXX.wav')
fenetre.configure(bg='#312b41')

source_label = Label(fenetre, text="Source Folder:", fg='white', bg='#312b41')
source_label.pack(pady=10)
source_entry = Entry(fenetre, width=85, font=('Arial', 12))
source_entry.pack(pady=5)
source_button = Button(fenetre, text="Browse", command=select_source_folder)
source_button.pack(pady=5)

convert_button = Button(fenetre, text="Convert", command=convert_files, font=('Arial', 14, 'bold'))
convert_button.pack(pady=20)

created_by_label = Label(fenetre, text="Created by Soniceurs", fg='white', bg='#312b41', font=('Arial', 10, 'italic'))
created_by_label.place(relx=1.0, rely=1.0, anchor='se')

fenetre.mainloop()