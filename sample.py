from tkinter import*
from PIL import Image,ImageTk,ImageDraw #pip install pillow
from datetime import*
import time
from math import*
#import pymysql #pip install pymysql
import sqlite3
import os



from tkinter import messagebox,ttk




class Choose_window:
    def __init__(self,root):
        self.root=root
        self.root.title("CHOOSE SYSTEM")
        self.root.geometry("1520x780+0+0")
        self.root.config(bg="#021e2f")
        
        #=============background colors==============================
        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=750)
        
        right_lbl=Label(self.root,bg="#031F3C",bd=0)
        right_lbl.place(x=750,y=0,relheight=1,relwidth=1)
       #=======frames================
        
        choose_frame=Frame(self.root,bg="white")
        choose_frame.place(x=340,y=150,width=800,height=500)
        
        self.lbl=Label(self.root,text="choose Window",font=("\nBook Antiqua",25,"bold"),compound=BOTTOM,fg="white",bg="#081923",bd=0)
        self.lbl.place(x=180,y=175,height=450,width=350)
        
        
        # Checkbutton for "Faculty"
        self.faculty_var = IntVar()
        faculty_checkbox = Checkbutton(
            choose_frame,
            text="Faculty",
            variable=self.faculty_var,
            font=("times new roman", 25),
            bg="white",
        )
        faculty_checkbox.place(x=400, y=180)

        # Checkbutton for "Student"
        self.student_var = IntVar()
        student_checkbox = Checkbutton(
            choose_frame,
            text="Student",
            variable=self.student_var,
            font=("times new roman", 25),
            bg="white",
        )
        student_checkbox.place(x=400, y=300)

        # Submit button
        submit_button = Button(
            choose_frame,
            text="Submit",
            font=("times new roman", 20),
            bg="white",
            command=self.submit_action,
        )
        submit_button.place(x=400, y=400)

        # Initialize selected value
        self.selected_value = None

        # Update selected value based on the checkbox selection
        self.faculty_var.trace("w", lambda *args: self.update_selected_value("faculty"))
        self.student_var.trace("w", lambda *args: self.update_selected_value("student"))
        
        
        #self.clock_image()
        self.working()

    def update_selected_value(self, value):
        self.selected_value = value

    def submit_action(self):
        if self.selected_value == "faculty":
            # Redirect to faculty dashboard section
           self.root.destroy()
           os.system("python dashboard.py")
          
           
        elif self.selected_value == "student":
            # Redirect to student report section
            self.root.destroy()
            os.system("python report.py")
        else:
            messagebox.showerror("Error", "Please select an option")  # Show error message if no option is selected

    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)
        #========for clock image===============
        bg=Image.open("image2/Frame.png")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        
        
        #formula to rotate the anticlock
        #angle_in_radians = angle_in_degrees * math.pi / 180
        #line_length=100
        #center_x=250
        #center_y=250
        #end_x=center_x + line_length * math.cos(angle_in_radians)
        #end_y=center_y - line_length * math.sin(angle_in_radians)
        
        clock.save("clock_new.png")    
        #=============hour line image===============
        #           x1,y1,x2,y2
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="black",width=4)
        clock.save("clock_new.png")   
        #=============minute line image===============
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="green",width=3)
        clock.save("clock_new.png")  
        #=============second line image===============
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="red",width=4)
        draw.ellipse((194,194,205,205),fill="red")
        clock.save("clock_new.png")
        
        
    def working(self):
         h=datetime.now().time().hour
         m=datetime.now().time().minute
         s=datetime.now().time().second
         
         hr=(h/12)*360
         min_=(m/60)*360
         sec_=(s/60)*360
         #print(h,m,s)
         #print(hr,min_,sec_)
         self.clock_image(hr,min_,sec_)
         self.img=ImageTk.PhotoImage(file="clock_new.png")
         self.lbl.config(image=self.img)
         self.lbl.after(200,self.working)
root=Tk()
obj=Choose_window(root)
root.mainloop()