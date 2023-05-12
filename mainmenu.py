import CallLMBot
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# from PIL import Image, ImageTk      ### pip install pillow

def chosejob():
    root = tk.Tk()
    root.geometry("400x150")    
    root.configure(background='#fafafa')
    root.title("Solar Modeling BOT")
    
    file_path=StringVar()
    jobname=StringVar()
    ft = (('text files','*.txt'))
    
    def exitfunc():
        root.destroy()
        SystemExit()

    def callbot():
        global file_path
        if jobname.get() == "Select a Process":
            jobname.set("SolarModelingAPI")
            jobmsg = "SolarModelingAPI (Default)"
        else:
            jobmsg = jobname.get()
        jobmsg = "Do you confirm the simulation for:\nJob Name: "+jobmsg+"\nJson File: "+str(file_path)+"?"
        confirm = messagebox.askokcancel("Confirm Simulation", message=jobmsg)
        if confirm:
            for item in file_path:
                CallLMBot.main(jobname.get(), item)

    def chosefile():
        global file_path
        file_path = filedialog.askopenfilenames(filetypes=[("json format", ".json")])
        label3=Label(root,text=file_path,fg="black",bg='#fafafa', font=("arial",10))
        label3.place(x=35,y=40)
                
        def choseprocess():
        ### Chose Job Name
            label2=Label(root,text="Process Name",fg="black",bg='#fafafa', font=("arial",10, "bold"))
            label2.place(x=40,y=80)
            joblist = ["SolarModelingAPI", "BOT 1", "BOT 2", "BOT 3"]
            droplist=OptionMenu(root,jobname,*joblist)
            jobname.set("Select a Process")
            droplist.config(width=15)
            droplist.place(x=135,y=75)

            Btnframe = Frame(root, width=400, height=40, bd=2, bg='#f5f5f5')
            Btnframe.place(x=0,y=110)

        ### Call Bot
            confirmBtn=Button(root, text="Confirm", font=("arial",10), bg="#3258EF", fg="white", command=callbot)
            confirmBtn.place(x=250,y=118)
            # confirmBtn['relief'] = 'solid'

        ### Cancel Job
            exitBtn=Button(root, text="Cancel", font=("arial",10), bg="#F73B3B", fg="white", command=exitfunc)
            exitBtn.place(x=320,y=118)
            # exitBtn['relief'] = 'solid'

        choseprocess()
        
### Chose Json File
    label1=Label(root,text="Json File", bg='#fafafa', font=("arial",10, "bold"))
    label1.place(x=35,y=10)
    fileBtn=Button(root, text="Chose a File", font=("arial",10), command=chosefile)
    fileBtn.place(x=130,y=10)

    root.mainloop()
    
if __name__ == "__main__":
    chosejob()