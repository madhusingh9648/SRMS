from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3
import os
import re


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
          #=============background colors==============================
        left_lbl=Label(self.root,bg="#031F3C",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=750)
        
        right_lbl=Label(self.root,bg="#08A3D2",bd=0)
        right_lbl.place(x=750,y=0,relheight=1,relwidth=1)

        #=====left Image======
        self.left=Image.open("image/left.png")
        self.left=ImageTk.PhotoImage(self.left)
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)
        #=======Register Frame====
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)
        #======title=======
        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
        #=======row1=====
        
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_f_name=Entry(frame1,font=("times new roman",15,),bg='lightgray')
        self.txt_f_name.place(x=50,y=130,width=250)

        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_l_name=Entry(frame1,font=("times new roman",15,),bg='lightgray')
        self.txt_l_name.place(x=370,y=130,width=250)

        #==========Row2======== 
        contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15,),bg='lightgray')
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15,),bg='lightgray')
        self.txt_email.place(x=370,y=200,width=250)
        
        #==========Row3========
        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name","In what city or town was your first job?","What elementary school/high school did you attend?","What is your favorite movie?","What was your favorite sport in high school? ","What was the first exam you failed? ","What is your best friend name?")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)
        
        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15,),bg='lightgray')
        self.txt_answer.place(x=370,y=270,width=250)
        
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15,),bg='lightgray')
        self.txt_password.place(x=50,y=340,width=250)
        
        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15,),bg='lightgray')
        self.txt_cpassword.place(x=370,y=340,width=250)


         #============terms==============
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)
        
        btn_register=Button(frame1,text='Register',font=("times new roman",16),bg="green",fg="white",cursor="hand2",command=self.register_data).place(x=150,y=430,width=150,height=40)
        btn_login=Button(frame1,text='Sign In',command=self.login_window,font=("times new roman",16),bg="blue",fg="white",cursor="hand2").place(x=380,y=430,width=150,height=40)
   
    
    def login_window(self):
        self.root.destroy()
        os.system("python login.py")
        
        
    def clear(self):
        self.txt_f_name.delete(0,END)
        self.txt_l_name.delete(0,END)    
        self.txt_contact.delete(0,END)    
        self.txt_email.delete(0,END)    
        self.txt_password.delete(0,END)    
        self.txt_cpassword.delete(0,END)
        self.txt_answer.delete(0,END)    
            
        self.txt_cpassword.delete(0,END)    
        self.cmb_quest.current(0)    
        
    def validate_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email)

      
     


    def register_data(self):
        if self.txt_f_name.get() == "" or self.txt_contact.get() == "" or self.txt_email.get() == "" or self.cmb_quest.get() == "Select" or self.txt_answer.get() == "" or self.txt_password.get() == "" or self.txt_cpassword.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif len(self.txt_contact.get()) != 10:
            messagebox.showerror("Error", "Contact number should be 10 digits", parent=self.root)
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror("Error", "Password and Confirm Password should be the same", parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms and conditions", parent=self.root)
        elif not self.validate_email(self.txt_email.get()):
            messagebox.showerror("Error", "Invalid email format", parent=self.root)
        else:
            password = self.txt_password.get()
            cpassword = self.txt_cpassword.get()

        # Check password constraints
        if not re.search(r'[A-Z]', password):
            messagebox.showerror("Error", "Password should contain at least one uppercase letter", parent=self.root)
        elif not re.search(r'[a-z]', password):
            messagebox.showerror("Error", "Password should contain at least one lowercase letter", parent=self.root)
        elif not re.search(r'\d', password):
            messagebox.showerror("Error", "Password should contain at least one digit", parent=self.root)
        elif not re.search(r'[\W_]', password):
            messagebox.showerror("Error", "Password should contain at least one special character", parent=self.root)
        elif len(password) < 8:
            messagebox.showerror("Error", "Password should be at least 8 characters long", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM employee WHERE email=?", (self.txt_email.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "User already exists. Please try with another email", parent=self.root)
                else:
                    cur.execute("INSERT INTO employee(f_name, l_name, contact, email, question, answer, password) VALUES(?, ?, ?, ?, ?, ?, ?)",
                                (self.txt_f_name.get(),
                                self.txt_l_name.get(),
                                self.txt_contact.get(),
                                self.txt_email.get(),
                                self.cmb_quest.get(),
                                self.txt_answer.get(),
                                self.txt_password.get()
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Registration successful", parent=self.root)
                    self.clear()
                    self.login_window()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)



                   
      




root=Tk()
obj=Register(root)
root.mainloop()