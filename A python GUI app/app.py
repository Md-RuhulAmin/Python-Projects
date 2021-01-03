import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.title("Application Loader")
apps = [] #To append all the applications

# Loading up the text file and removing the extra comma
# also reading all the files that was saved before.
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

#Defing a function to fetch the applicatio from the system.
def addApps ():
    for widget in frame.winfo_children():
        widget.destroy()
    
    fileName = filedialog.askopenfilename(initialdir="/", title= "Select File",
                filetypes =(("executables","*.exe"), ("all files", "*.*")))
    apps.append(fileName)
    print(fileName)
    for app in apps:
        label = tk.Label(frame, text= app, bg="gray")
        label.pack()

#Defining another function to execute thpse application that are on the list
def runApps ():
    for app in apps:
        os.startfile(app)

#Creating a canvas by giving an exact size and background color
canvas = tk.Canvas(root, height= 500, width = 500, bg = '#263D42')
canvas.pack() #This pack() module will attach the canvas to the root

#Making a frame to the canvas
frame = tk.Frame(root, bg ="white")
frame.place(relwidth = 0.8, relheight = 0.7, relx= 0.1, rely=0.1)

#Creating a button to open the folder and select an executable file
openFile = tk.Button(root, text= "Open File", padx=10, pady=5, 
    fg="white", bg="#263D42", command = addApps)
openFile.pack()

#Creating "run apps" button to run the apps
runApps = tk.Button(root, text="Run apps", padx= 10, pady=5, 
    fg="white", bg="#263D42", command = runApps)
runApps.pack()

#To get the existing applications are saved on the save.txt file
for app in apps:
    label = tk.Label(frame, text =app)
    label.pack()

#Calling the root mainloop()
root.mainloop()

#Creating a txt file to keep the apps listed 
# and to get those back when need.
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')