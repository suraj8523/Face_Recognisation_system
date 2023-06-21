from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        self.root.wm_iconbitmap("face.ico")
        
        #title
        title_lbl=Label(self.root,text="Face Recognition",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        # 1st image===
        img_top=Image.open("college_images/face_detector1.jpg")
        img_top=img_top.resize((650,700),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)
        # 2nd image====
        img_bottom=Image.open("college_images/aaa.jpg")
        img_bottom=img_bottom.resize((950,700),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)
        
        #button
        b1_1=Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",18),bg="darkgreen",fg="white")
        b1_1.place(x=365,y=620,width=200,height=40)
        
    #attandence====
    def mark_attaendance(self,i,r,n,d):
        with open("suraj.csv","r+",newline="\n") as f:
            mydataList=f.readlines()
            name_list=[]
            for line in mydataList:
                entry=line.split((","))
                name_list.append(entry[0])
            
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list) ):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},present")
                    
                
            
        
        
    
    
    
    
    #face regonition ========
    
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):  
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
            
           
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",username="root",password="admin123",database="face_recognition")
                my_curser=conn.cursor()
                
                my_curser.execute("select name from student where Student_id="+str(id))
                n=my_curser.fetchone()
                n="+".join(n)
                
                my_curser.execute("select Roll from student where Student_id="+str(id))
                r=my_curser.fetchone()
                r="+".join(r)
                
                my_curser.execute("select Dep from student where Student_id="+str(id))
                d=my_curser.fetchone()
                d="+".join(d)
                
                my_curser.execute("select Student_id from student where Student_id="+str(id))
                i=my_curser.fetchone()
                i="+".join(i)
                 
                
                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attaendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,h]
            return coord 
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
        clf=cv2.face.LBPHFaceRecognizer_create()   
        clf.read("classifier.xml")    
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade) 
            cv2.imshow("Welcome to face recognition",img)
            
            if cv2.waitKey(1000)==13:
                cv2.destroyAllWindows()
                video_cap.release()
            
            
            
            
            
            
                    
                    
                
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()       