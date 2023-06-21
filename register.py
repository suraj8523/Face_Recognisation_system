from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        
        
        #variable====
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityq=StringVar()
        self.var_securitya=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        

        
       
       #bg image===== 
        self.bg=ImageTk.PhotoImage(file="u.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        #left image===== 
        self.bg1=ImageTk.PhotoImage(file="ac.jpg")
        bg1_lbl=Label(self.root,image=self.bg1)
        bg1_lbl.place(x=50,y=100,width=470,height=550)
        
        #frane==
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        
        register_lbl=Label(frame,text="Register Here",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)
        
        #label and entry field=====
        
        #row 1====
        fname=Label(frame,text="First Name",font=("times new roman",20,"bold"),bg="white")
        fname.place(x=50,y=100)
        
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)
        
        lname=Label(frame,text="Last Name",font=("times new roman",20,"bold"),bg="white")
        lname.place(x=370,y=100)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)
        
        #rwo2====
        
        contact=Label(frame,text="Contact",font=("times new roman",20,"bold"),bg="white")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame,text="Email",font=("times new roman",20,"bold"),bg="white")
        email.place(x=370,y=170)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)
        
        #row3======
        
        security_q=Label(frame,text="Security QUE",font=("times new roman",20,"bold"),bg="white")
        security_q.place(x=50,y=240)
        
        self.combo_security_q=ttk.Combobox(frame,textvariable=self.var_securityq,font=("times new roman",15,"bold"),width=17,state="readonly")
        self.combo_security_q["values"]=("Select","Your birth place","Your pet name","Your college name")
        self.combo_security_q.current(0)
        self.combo_security_q.place(x=50,y=270,width=250)
        
        security_a=Label(frame,text="Security Answer",font=("times new roman",20,"bold"),bg="white")
        security_a.place(x=370,y=240)
        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securitya,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)
        
        #row4=====
        pswd=Label(frame,text="Password",font=("times new roman",20,"bold"),bg="white")
        pswd.place(x=50,y=310)
        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)
        
        confirm_pswd=Label(frame,text=" Confirm Password",font=("times new roman",20,"bold"),bg="white")
        confirm_pswd.place(x=370,y=310)
        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_pswd.place(x=370,y=340,width=250)
        
        #check button===
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree term and condition",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)
        
        #buttons====
        img=Image.open("register-now-button1.jpg")
        img=img.resize((200,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=10,y=420,width=300)
        
        img1=Image.open("loginpng.png")
        img1=img1.resize((200,50),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=330,y=420,width=300)
    
    #function====
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityq.get()=="Select":
            messagebox.showerror("Error","All field are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm password not same")    
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree all term & condition")
        else:
            #messagebox.showinfo("Success","Welcome Friends")   
            conn=mysql.connector.connect(host="localhost",username="root",password="admin123",database="mydat")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()  
            if row!=None:
                messagebox.showerror("Error","User already exist please try another email") 
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityq.get(),
                    self.var_securitya.get(),
                    self.var_pass.get()
                    
                            ))  
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","register Successfully")
            
            
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()         
        