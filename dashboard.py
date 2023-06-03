from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk #pip install pillow
from course import CourseClass
from student import studentClass
from result import ResultClass
from report import reportClass
from tkinter import messagebox
import os

from PIL import Image,ImageTk,ImageDraw #pip install pillow
from datetime import*
import time
from math import*
#import pymysql #pip install pymysql
import sqlite3


class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1520x780+0+0")
        self.root.config(bg="alice blue")
        #===icons===
        
        
        self.logo_dash=ImageTk.PhotoImage(file="image/analytics.png")
        
        #===title===
    
        title=Label(self.root,text="Student Result Management System",compound=LEFT,padx=10,
              image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
        
        #===menu====
        
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1500,height=80)
        
        
        
        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        
         
        btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=270,y=5,width=200,height=40)
        
         
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=520,y=5,width=200,height=40)
        
         
        btn_view=Button(M_Frame,text="View Student Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=770,y=5,width=200,height=40)
        
         
        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=1020,y=5,width=200,height=40)
        
         
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit_).place(x=1270,y=5,width=200,height=40)
        
        #===content_window====
        
        self.bg_img=Image.open("image/bg.png")
        self.bg_img=self.bg_img.resize((920,430),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=590,y=160,width=920,height=430)
        
        
        #===update_detail====
        
        self.lbl_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=590,y=600,width=300,height=100)
        
        self.lbl_student=Label(self.root,text="Total Students\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=900,y=600,width=300,height=100)
        
        
        self.lbl_result=Label(self.root,text="Total Results\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=1210,y=600,width=300,height=100)
        
        #============clock===============
        self.lbl=Label(self.root,text="Tic! Tic! Tic!",font=("\nBook Antiqua",25,"bold"),compound=BOTTOM,fg="white",bg="#081923",bd=0)
        self.lbl.place(x=115,y=205,height=450,width=350)
        #self.clock_image()
        self.working()
        
         #===footer===
    
        footer=Label(self.root,text="STUDENT RESULT MANAGEMENT SYSTEM\nA Team Project:- B.Tech CSE 4th Year\nBy : Prakhar Dev & Madhu Singh ",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
        
        self.update_details()
    #=========================
    def update_details(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]") 
            
            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")
            
            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")
            
            
            self.lbl_course.after(200,self.update_details)
            
            
       
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    
    
    
    
    
    
    
    
    
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
        
         
    #=================
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
        
    
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)
        
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)
        
        
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)
        
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)
    
    
    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")
            
    def exit_(self):
        op=messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.root)
        if op==True:
            self.root.destroy()
            
            
            
if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()