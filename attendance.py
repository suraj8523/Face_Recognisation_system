from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os 
import csv
from tkinter import filedialog




mydata=[]

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")
        
        #variable=======
        self.var_attend_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendance=StringVar()
        
        
        #== 1ST IMAGE===
        img=Image.open("college_images\har.jpg")
        img=img.resize((800,200),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)
        
        ###2nd image ===
        img1=Image.open("college_images/s.jpg")
        img1=img1.resize((800,200),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)
        
        
         #background image=====
        
        img3=Image.open("college_images/wp2551980.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img_lbl=Label(self.root,image=self.photoimg3)
        bg_img_lbl.place(x=0,y=200,width=1530,height=710)
        
        #title
        title_lbl=Label(bg_img_lbl,text="ATTANDENCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="green",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #frame=====        
        main_frame=Frame(bg_img_lbl,bd=2,relief=RIDGE,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)
        
        #left side label
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attandence Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)
        
        img_left=Image.open("college_images/s2.jpeg")
        img_left=img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=720,height=130)
        
        
        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=370)
        
        #labled entry===
        #Attandence Id===
        
        attendance_id_lbl=Label(left_inside_frame,text="Attendance ID",font=("times new roman",12,"bold"))
        attendance_id_lbl.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        attendance_id_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_id,font=("times new roman",13,"bold"))
        attendance_id_entry.grid(row=0,column=1,padx=10,sticky=W)
        
         #Roll Id===
        
        rollLabel=Label(left_inside_frame,text="Roll ",font=("times new roman",12,"bold"))
        rollLabel.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_roll,font=("times new roman",13,"bold"))
        atten_roll.grid(row=0,column=3,padx=10,sticky=W)
        
         #Name Id===
        
        nameLabel=Label(left_inside_frame,text="Name",font=("times new roman",12,"bold"))
        nameLabel.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_name,font=("times new roman",13,"bold"))
        atten_name.grid(row=1,column=1,padx=10,sticky=W)
        
         #Department Id===
        
        depLabel=Label(left_inside_frame,text="Department",font=("times new roman",12,"bold"))
        depLabel.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_dep,font=("times new roman",13,"bold"))
        atten_dep.grid(row=1,column=3,padx=10,sticky=W)
        
        #Time===
        
        timeLabel=Label(left_inside_frame,text="Time",font=("times new roman",12,"bold"))
        timeLabel.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_time,font=("times new roman",13,"bold"))
        atten_dep.grid(row=2,column=1,padx=10,sticky=W)
        
         #Date===
        
        dateLabel=Label(left_inside_frame,text="date",font=("times new roman",12,"bold"))
        dateLabel.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_date,font=("times new roman",13,"bold"))
        atten_date.grid(row=2,column=3,padx=10,sticky=W)
        
         #Attendance===
        
        attendanceLabel=Label(left_inside_frame,text="Attendance status",font=("times new roman",12,"bold"))
        attendanceLabel.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        self.atten_status=ttk.Combobox(left_inside_frame,font=("times new roman",12,"bold"),width=20,textvariable=self.var_attend_attendance,state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,padx=10,pady=8)  
        
        #button frame======
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=300,width=715,height=40)
        
        save_btn=Button(btn_frame,text="IMPORT CSV",command=self.importCSV,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="EXPORT CSV",command=self.exportcsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="UPDATE",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="RESET",width=17,command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
              
        
        
        
        #right side label
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attandence Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)
        
        table_frame=Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=0,width=650,height=445)
        
        #scrollbar====
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
    
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Ateendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        
        
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
    #fetch data===
    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
            
    #import csv====            
    def importCSV(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV File","*csv"),("All Files","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)    
            
            
    # export csv===
    def exportcsv(self):
        try:
            
            if len(mydata)<1:
                messagebox.showerror("No data","No data found export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV File","*csv"),("All Files","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data Exported to "+os.path.basename(fln)+"Successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)    
                         
    #get data===
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])  
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendance.set(rows[6])
        
    #reset data===
    def reset_data(self):
        self.var_attend_id.set("")  
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")
            
                          
                        
                        
                        
               
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()        