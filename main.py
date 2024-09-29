from tkinter import *
from tkinter import filedialog,messagebox
import subprocess

class IDLE:
    def __init__(self,root):
        # ============================== GUI ==============================
        self.root = root
        self.root.title("Python IDLE developed by Uttam Kumar")
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}+0+0")
        self.color,self.Bt_color,self.line_thick = 'white','black',self.height*0.006
        self.root.configure(bg=self.color,highlightthickness=self.line_thick,highlightcolor="pale green",highlightbackground="pale green")
        self.root.iconbitmap("icon.ico")
        # self.root.resizable(0,0)

        # ===================== Lines & Labels ====================
        Label(self.root,bg="pale green").place(x=self.width*0.055,width=self.line_thick,height=self.height)
        Label(self.root,text="",bg="pale green").place(x=self.width*0.058,y=self.height*0.06,height=self.line_thick,width=self.width)
        Label(self.root,text="",bg="pale green").place(x=self.width*0.658,width=self.line_thick,height=self.height)
        self.pythonIDELabel =Label(self.root,text="Python IDE",font=("Comic Sans MS",20,"bold"),fg="purple3",bg='yellow')
        self.pythonIDELabel.place(x=self.width*0.058,width=self.width*0.6,height=self.height*0.06)
        self.outputLabel = Label(self.root,text="Output",font=("Comic Sans MS",20,"bold"),fg="purple3",bg='yellow')
        self.outputLabel.place(x=self.width*0.661,width=self.width*0.333,height=self.height*0.06)

        # ====================== Image Buttons & Labels ====================
        self.Open = PhotoImage(file="open.png")
        self.file = PhotoImage(file="new_file.png")
        self.Save = PhotoImage(file="save.png")
        self.Run = PhotoImage(file="run.png")
        self.Reset = PhotoImage(file="reset.png")
        self.Mode = PhotoImage(file="mode.png")

        self.openButton = Button(self.root,text="Open",font=("lucida",10),image=self.Open,compound=TOP,bd=0,bg=self.color,fg=self.Bt_color,activebackground=self.color,command=self.open_file)
        self.openButton.place(x=1,y=10)
        self.fileButton = Button(self.root,text="New File",font=("lucida",10),image=self.file,compound=TOP,bd=0,bg=self.color,fg=self.Bt_color,activebackground=self.color,command=self.new_file)
        self.fileButton.place(x=1,y=self.height*0.15)
        self.saveButton = Button(self.root,text="Save",font=("lucida",10),image=self.Save,compound=TOP,bd=0,bg=self.color,fg=self.Bt_color,activebackground=self.color,command=self.save_file)
        self.saveButton.place(x=1,y=self.height*0.29)
        self.runButton = Button(self.root,text="Run",font=("lucida",10),image=self.Run,compound=TOP,bd=0,bg=self.color,fg=self.Bt_color,activebackground=self.color,command=self.run_code)
        self.runButton.place(x=1,y=self.height*0.43)
        self.resetButton = Button(self.root,text="Reset",font=("lucida",10),image=self.Reset,compound=TOP,bd=0,bg=self.color,fg=self.Bt_color,activebackground=self.color,command=self.reset)
        self.resetButton.place(x=1,y=self.height*0.57)
        self.modeButton = Button(self.root,text="Dark",font=("lucida",10),image=self.Mode,compound=TOP,bd=0,bg=self.color,fg=self.Bt_color,activebackground=self.color,command=self.light_dark)
        self.modeButton.place(x=1,y=self.height*0.71)
        self.more = Label(self.root,text="More",font=("Comic Sans MS",15,"bold"),fg=self.Bt_color,bg=self.color)
        self.more.place(x=6,y=self.height*0.85)

        # =================== Hover effect ====================
        self.pythonIDELabel.bind("<Enter>",lambda event:self.pythonIDELabel.configure(font=("Comic Sans MS",25,"bold")))
        self.pythonIDELabel.bind("<Leave>",lambda event:self.pythonIDELabel.configure(font=("Comic Sans MS",20,"bold")))
        self.outputLabel.bind("<Enter>",lambda event:self.outputLabel.configure(font=("Comic Sans MS",25,"bold")))
        self.outputLabel.bind("<Leave>",lambda event:self.outputLabel.configure(font=("Comic Sans MS",20,"bold")))
        self.openButton.bind("<Enter>",lambda event:self.openButton.configure(font=("lucida",12,"bold")))
        self.openButton.bind("<Leave>",lambda event:self.openButton.configure(font=("lucida",10)))
        self.fileButton.bind("<Enter>",lambda event:self.fileButton.configure(font=("lucida",11,"bold")))
        self.fileButton.bind("<Leave>",lambda event:self.fileButton.configure(font=("lucida",10)))
        self.saveButton.bind("<Enter>",lambda event:self.saveButton.configure(font=("lucida",12,"bold")))
        self.saveButton.bind("<Leave>",lambda event:self.saveButton.configure(font=("lucida",10)))
        self.runButton.bind("<Enter>",lambda event:self.runButton.configure(font=("lucida",12,"bold")))
        self.runButton.bind("<Leave>",lambda event:self.runButton.configure(font=("lucida",10)))
        self.resetButton.bind("<Enter>",lambda event:self.resetButton.configure(font=("lucida",12,"bold")))
        self.resetButton.bind("<Leave>",lambda event:self.resetButton.configure(font=("lucida",10)))
        self.modeButton.bind("<Enter>",lambda event:self.modeButton.configure(font=("lucida",12,"bold")))
        self.modeButton.bind("<Leave>",lambda event:self.modeButton.configure(font=("lucida",10)))
        self.more.bind("<Enter>",self.more_func_enter)
        self.more.bind("<Leave>",self.more_func_leave)

        # ======================== Shortcut keys controll =================
        self.root.bind("<Control-o>",lambda event:self.open_file())
        self.root.bind("<Control-O>",lambda event:self.open_file())
        self.root.bind("<Control-n>",lambda event:self.new_file())
        self.root.bind("<Control-N>",lambda event:self.new_file())
        self.root.bind("<Control-s>",lambda event:self.save_file())
        self.root.bind("<Control-S>",lambda event:self.save_file())
        self.root.bind("<Control-Alt-n>",lambda event:self.run_code())
        self.root.bind("<Control-Alt-N>",lambda event:self.run_code())
        self.root.bind("<Control-r>",lambda event:self.reset())
        self.root.bind("<Control-R>",lambda event:self.reset())
        self.root.bind("<Control-m>",lambda event:self.light_dark())
        self.root.bind("<Control-M>",lambda event:self.light_dark())
        self.root.bind("<Control-q>",lambda event:self.root.destroy())
        self.root.bind("<Control-Q>",lambda event:self.root.destroy())

        # =================== code input ===================
        self.code_input_frame = LabelFrame(root,bd=0,fg=self.color)
        self.scrollbarY1 = Scrollbar(self.code_input_frame,orient=VERTICAL)
        self.scrollbarX1 = Scrollbar(self.code_input_frame,orient=HORIZONTAL)
        self.scrollbarY1.pack(side=RIGHT,fill=Y)
        self.scrollbarX1.pack(side=BOTTOM,fill=X)
        self.code_input = Text(self.code_input_frame,font=("Comic Sans MS",15),fg="#4FC1FF",bg=self.color,bd=0,yscrollcommand=self.scrollbarY1.set,xscrollcommand=self.scrollbarX1.set,wrap="none")
        self.code_input.pack(fill=BOTH,expand=1)
        self.scrollbarY1.config(command=self.code_input.yview)
        self.scrollbarX1.config(command=self.code_input.xview)
        self.code_input_frame.place(x=self.width*0.058,y=self.height*0.066,width=self.width*0.6,height=self.height*0.896)
        
        # ================= code output ===================
        self.code_output_frame = LabelFrame(root,bd=0,fg=self.color)
        self.scrollbarY2 = Scrollbar(self.code_output_frame,orient=VERTICAL)
        self.scrollbarX2 = Scrollbar(self.code_output_frame,orient=HORIZONTAL)
        self.scrollbarY2.pack(side=RIGHT,fill=Y)
        self.scrollbarX2.pack(side=BOTTOM,fill=X)
        self.code_output = Text(self.code_output_frame,font=("Comic Sans MS",15),fg="purple3",bg=self.color,bd=0,yscrollcommand=self.scrollbarY2.set,xscrollcommand=self.scrollbarX2.set,wrap="none")
        self.code_output.pack(fill=BOTH,expand=1)
        self.scrollbarY2.config(command=self.code_output.yview)
        self.scrollbarX2.config(command=self.code_output.xview)
        self.code_output_frame.place(x=self.width*0.661,y=self.height*0.066,width=self.width*0.333,height=self.height*0.896)

        # some attributes related to the functionality part
        self.file_path = ""
        self.read_code = ""
        self.get_code = ""
        self.light = True

    # =============================== Functionality part ================================
    def set_file_path(self,path):
        self.file_path = path

    def open_file(self):
        path = filedialog.askopenfilename(filetypes=[("Python Files","*.py")],title="Open Python File")
        with open(path,'r') as file:
            self.read_code = file.read()
            self.code_input.delete(1.0,END)
            self.code_input.insert(1.0,self.read_code)
            self.set_file_path(path)

    def new_file(self):
        path = filedialog.asksaveasfilename(filetypes=[("Python Files","*.py")],defaultextension=".py",title="Create New Python File")
        with open(path,'w') as file:
            file.write("")
            self.set_file_path(path)

    def save_file(self):
        if self.file_path == "":
            messagebox.showerror("Python IDLE","Please create a new file or open an existing file")
            return
        if self.read_code != self.code_input.get(1.0,END):
            with open(self.file_path,'w') as file:
                self.get_code = self.code_input.get(1.0,END)
                file.write(self.get_code)
                messagebox.showinfo("Success","Changes save successfully")

    def run_code(self):
        if self.file_path == "":
            messagebox.showerror("Python IDLE","Please save your code")
            return
        if 'input(' in self.read_code or 'input(' in self.get_code:
            messagebox.showerror("Python IDLE","Please don't use input function in your code")
            return
        command = f'python "{self.file_path}"'
        process = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        output,error = process.communicate()
        self.code_output.delete(1.0,END)
        if error == b'':
            self.code_output.configure(fg='green2')
            self.code_output.insert(END,output)
        elif output == b'':
            self.code_output.configure(fg="red")
            self.code_output.insert(END,error)
        else:
            self.code_output.configure(fg="tomato")
            self.code_output.insert(END,output)
            self.code_output.insert(END,error)

    def reset(self):
        if self.file_path != "":self.file_path = ""
        self.code_input.delete(1.0,END)
        self.code_output.delete(1.0,END)

    def light_dark(self):
        self.color,self.Bt_color = self.Bt_color,self.color
        if self.light:
            self.modeButton.configure(text="Light")
            self.light = False
        else:
            self.modeButton.configure(text="Dark")
            self.light = True
        
        self.root.configure(bg=self.color)
        self.openButton.configure(bg=self.color,fg=self.Bt_color,activebackground=self.color,activeforeground=self.Bt_color)
        self.fileButton.configure(bg=self.color,fg=self.Bt_color,activebackground=self.color,activeforeground=self.Bt_color)
        self.saveButton.configure(bg=self.color,fg=self.Bt_color,activebackground=self.color,activeforeground=self.Bt_color)
        self.runButton.configure(bg=self.color,fg=self.Bt_color,activebackground=self.color,activeforeground=self.Bt_color)
        self.resetButton.configure(bg=self.color,fg=self.Bt_color,activebackground=self.color,activeforeground=self.Bt_color)
        self.modeButton.configure(bg=self.color,fg=self.Bt_color,activebackground=self.color,activeforeground=self.Bt_color)
        self.code_input.configure(bg=self.color)
        self.code_output.configure(bg=self.color)
        self.more.configure(bg=self.color,fg=self.Bt_color)

    def more_func_enter(self,event):
        self.more.configure(font=("Comic Sans MS",17,"bold"),fg="purple3")
        self.window = Tk()
        self.window.title("Shortcuts")
        self.window.geometry("300x240")
        self.window.resizable(0,0)
        self.window.configure(bg=self.color)
        self.window.iconbitmap("icon.ico")
        Label(self.window,text="Ctrl+O - Open\nCtrl+N - New File\nCtrl+S - Save\nCtrl+R - Reset\nCtrl+Alt+R - Run\nCtrl+M - Light/Dark\nCtrl+Q - Exit",font=("Comic Sans MS",15),bg=self.color,fg="purple3").pack()
        self.window.mainloop()

    def more_func_leave(self,event):
        self.window.destroy()
        self.more.configure(font=("Comic Sans MS",15,"bold"),fg=self.Bt_color)

root = Tk()
IDLE(root)
root.mainloop()