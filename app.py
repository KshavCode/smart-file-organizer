from tkinter import *
import tkinter.ttk as ttk 
from tkinter import filedialog
import tkinter.messagebox as mb
import terminal as m


root = Tk()
root.geometry("500x250")
root.title("File Organizer")


def NewWindow() :
    def Sorting2() :
        if choice_var.get() == 0 :
            mb.showerror("ERROR", "Kindly select the sorting option!")
        else :
            try :
                if len(FileDestination_Var.get())==29 :
                    mb.showerror("ERROR", f"Kindly enter the word which you want to focus on!")
                    root2.destroy()
                else :
                    m.sort2(FileDestination_Var.get(), choice_var.get(), word_var.get())
                    mb.showinfo("SUCCESS", "The folder has been organized!")
                    root2.destroy()
            except Exception as e : 
                mb.showerror("ERROR", f"Kindly check if you specified the folder destination correctly and it's button is green.\n{e}")
                root2.destroy()
            
    
    root2 = Toplevel(root)
    root2.geometry("250x250")
    
    word_var = StringVar()
    choice_var = IntVar()
    word_txt = Label(root2, text="Word to use :", font="corbel 13")
    word_input = Entry(root2,width=10, textvariable=word_var)
    
    check1 = Radiobutton(root2, text="Starts with", font="corbel 13", value=1, indicatoron=False, background="#ffbcae", variable=choice_var)
    check2 = Radiobutton(root2, text="Ends with", font="corbel 13", value=2, indicatoron=False, background="#ffbcae", variable=choice_var)
    check3 = Radiobutton(root2, text="Contains", font="corbel 13", value=3, indicatoron=False, background="#ffbcae", variable=choice_var)
    
    confirm_button = ttk.Button(root2, text="Confirm", command=Sorting2)
    
    word_txt.place(x=10, y=10)
    word_input.place(x=110, y=15)
    check1.place(x=75, y=50)
    check2.place(x=75, y=85)
    check3.place(x=75, y=120)
    confirm_button.place(x=85, y=170)

def OpenFolder() :
    FileDestination_Var.set(filedialog.askdirectory())
    FileDestination_Button.config(background="lightgreen", text="Click to Change", width=15)

def SortIt() :
    if OptionNumber.get()==0 :
        mb.showerror("ERROR", "Kindly select the type of Organize!")
    elif OptionNumber.get()==1 :
        m.sort1(FileDestination_Var.get())
        mb.showinfo("SUCCESS", "The folder has been organized!")
    elif OptionNumber.get() == 2 :
        NewWindow()
        

FileDestination_Var = StringVar()
OptionNumber = IntVar(value=0)

FileDestination_Text = Label(root, text="Select Folder : ", font="corbel 15")
FileDestination_Button = Button(root, text="Open", font="corbel 13", width=10, background="red", command=OpenFolder)
sort1check = Radiobutton(root, text="Organize by type", value=1, variable=OptionNumber, font="corbel 13")
sort2check = Radiobutton(root, text="Organize by word", value=2, variable=OptionNumber, font="corbel 13")
Done_Button = ttk.Button(root, text="Proceed", width=15, command=SortIt)

FileDestination_Text.place(x=10, y=50)
FileDestination_Button.place(x=140, y=50)
sort1check.place(x=140, y=120)
sort2check.place(x=140, y=150)
Done_Button.place(x=170, y=200)



root.mainloop()
