from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognisation_System


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()
    

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("ChatBot")
        self.root.geometry("1550x800+0+0")
        #self.root.wm_iconbitmap("face.ico")
        
        self.bg=ImageTk.PhotoImage(file="college_images/un.jpg")
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        
        img1=Image.open("college_images/LoginIconAppl.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.Photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.Photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),bg="black",fg="white")
        get_str.place(x=95,y=100)
        
        #label1===
        username_lbl=Label(frame,text="Username",font=("times new roman",15),fg="white",bg="black")
        username_lbl.place(x=70,y=155)
        
        self.txtuser=ttk.Entry(frame,font=("times new roman",15))
        self.txtuser.place(x=40,y=180,width=270)
        
        password_lbl=Label(frame,text="Password",font=("times new roman",15),fg="white",bg="black")
        password_lbl.place(x=70,y=225)
        
        self.txtpass=ttk.Entry(frame,font=("times new roman",15))
        self.txtpass.place(x=40,y=250,width=270)
        
        #icon Images=================
        
        img2=Image.open("LoginIconAppl.png")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.Photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.Photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=323,width=25,height=25)
        
        
        img3=Image.open("college_images/lock-512.png")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.Photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.Photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=395,width=25,height=25)
        
        #login button=====
        
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        #register buttton==
        registerbtn=Button(frame,text="New user register",command=self.rigister_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)
        
        passbtn=Button(frame,text="Forget Password",command=self.forget_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        passbtn.place(x=10,y=370,width=160)
    
    
    def rigister_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
            
        
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All FIELDS REQUIRED")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="skr":
            messagebox.showinfo("Success","welcome to you ")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="admin123",database="mydat")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Inavlid username and password")
            else:
                open_main=messagebox.askyesno("YesNO","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognisation_System(self.new_window)  
                else:
                    if not open_main:
                        return   
            conn.commit()
            conn.close()
            
            
    #reset passwor===
    def reset_pass(self):
        if self.combo_security_q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="admin123",database="mydat")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityq=%s and securitya=%s")
            value=(self.txtuser.get(),self.combo_security_q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                quer=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(quer,value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password has been reset",parent=self.root2)  
                self.root2.destroy()
                
            
                    
            
                    
            
    #forget password======        
    def forget_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","please enter email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="admin123",database="mydat")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter a valid user name ")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget password")
                self.root2.geometry("340x450+610+170")  
                
                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1) 
                
                security_q=Label(self.root2,text="Security QUE",font=("times new roman",20,"bold"),bg="white")
                security_q.place(x=50,y=80)
                
                self.combo_security_q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),width=17,state="readonly")
                self.combo_security_q["values"]=("Select","Your birth place","Your pet name","Your college name")
                self.combo_security_q.current(0)
                self.combo_security_q.place(x=50,y=110,width=250)
                
                security_a=Label(self.root2,text="Security Answer",font=("times new roman",20,"bold"),bg="white")
                security_a.place(x=50,y=150)
                
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)
                
                new_password=Label(self.root2,text="New Password",font=("times new roman",20,"bold"),bg="white")
                new_password.place(x=50,y=220)
                
                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250) 
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)
                
                
            
                        
            
                      
            
            
            
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
        self.bg=ImageTk.PhotoImage(file="college_images/u.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        #left image===== 
        self.bg1=ImageTk.PhotoImage(file="college_images/ac.jpg")
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
        img=Image.open("college_images/register-now-button1.jpg")
        img=img.resize((200,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=10,y=420,width=300)
        
        img1=Image.open("college_images/loginpng.png")
        img1=img1.resize((200,50),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",bg="white")
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
    
    
    def return_login(self):
        self.root.destroy()
                
  

                
                
                    
            
            
                
        
        
        
        
        
        
if __name__=="__main__":
    main()      