from tkinter import *
from tkinter import filedialog, messagebox
import os
import shutil

def select_source_folder():
    folder_selected = filedialog.askdirectory()
    source_entry.delete(0, END)
    source_entry.insert(0, folder_selected)

def convert_files():
    source_folder = source_entry.get()
    
    # Obtenir le chemin du bureau de l'utilisateur
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
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
fenetre.title('Converter event_adx_e.afs_XXX.wav to XXXX.wav')
fenetre.configure(bg='#312b41')

# Champ de saisie pour le dossier source
source_label = Label(fenetre, text="Source Folder:", fg='white', bg='#312b41')
source_label.pack(pady=10)
source_entry = Entry(fenetre, width=85, font=('Arial', 12))  # Agrandir le champ de texte et changer la police
source_entry.pack(pady=5)
source_entry.insert(0, "C:/Users/Soniceurs/Desktop/Source-Folder/(event_adx_e.afs_001.wav, vent_adx_e.afs_002.wav...)")
source_button = Button(fenetre, text="Browse", command=select_source_folder)
source_button.pack(pady=5)

# Bouton pour convertir les fichiers
convert_button = Button(fenetre, text="Convert", command=convert_files, font=('Arial', 14, 'bold'))  # Agrandir et rendre le texte en gras
convert_button.pack(pady=20)

# Texte en bas à droite
created_by_label = Label(fenetre, text="Created by Soniceurs", fg='white', bg='#312b41', font=('Arial', 10, 'italic'))
created_by_label.place(relx=1.0, rely=1.0, anchor='se')  # Positionner en bas à droite

# Boucle principale de l'application Tkinter
fenetre.mainloop()
