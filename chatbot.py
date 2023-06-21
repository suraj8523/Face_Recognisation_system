from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Chatbot:
    def __init__(self,root):
        self.root=root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>',self.enter_func)
        
        main_frame=Frame(self.root,bd=4,bg="powder blue",width=610)
        main_frame.pack()
        
        img_chat=Image.open("college_images/chat.jpg")
        img_chat=img_chat.resize((200,70),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img_chat)
        
        Title_label=Label(main_frame,bd=3,relief=RIDGE,compound=LEFT,anchor='nw',width=730,image=self.photoimg,text="CHAT ME",font=("times new roman",30,"bold"),fg="green",bg="white")
        Title_label.pack(side=TOP)
        
        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RIDGE,font=("times new roman",14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()
        
        btn_frame=Frame(self.root,bd=4,bg="white",width=730)
        btn_frame.pack()
        
        label1=Label(btn_frame,text="Type Something",font=("times new roman",14,"bold"),fg="green",bg="white")
        label1.grid(row=0,column=0,padx=5,sticky=W)
        
        self.entry=StringVar()
        self.entry1=Entry(btn_frame,font=("times new roman",16,"bold"),textvariable=self.entry,width=30)
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)
        
        
        self.send=Button(btn_frame,text="Send",command=self.send_data,font=("times new roman",14,"bold"),width=8,bg="green")
        self.send.grid(row=0,column=2,padx=5,sticky=W)
        
        self.clear=Button(btn_frame,text="Clear Data",command=self.clear,font=("times new roman",14,"bold"),width=8,bg="red",fg="white")
        self.clear.grid(row=1,column=0,padx=5,sticky=W)
        
        self.msg=''
        self.label1_1=Label(btn_frame,text=self.msg,font=("times new roman",14,"bold"),fg="green",bg="white")
        self.label1_1.grid(row=1,column=1,padx=5,sticky=W)
        
        
    #function=====
    
    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')
        
    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')   
    
    
    
    def send_data(self):
        send='\t\t\t'+'You:'+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)
        
        if(self.entry.get()==''):
            self.msg='Please enter some input'
            self.label1_1.config(text=self.msg,fg="red")
        else:
            self.msg=''
            self.label1_1.config(text=self.msg,fg="red")
            
        if (self.entry.get()=="hello"):
            self.text.insert(END,'\n\n'+'Bot: Hi')
            
        elif (self.entry.get()=="hi"):
            self.text.insert(END,'\n\n'+'Bot: Hello')
            
        elif (self.entry.get()=="How are you"):
            self.text.insert(END,'\n\n'+'Bot: I am Fine ')
            
        
        elif (self.entry.get()=="I am also fine"):
            self.text.insert(END,'\n\n'+'Bot: Great')
        
        elif (self.entry.get()=="what is your name"):
            self.text.insert(END,'\n\n'+'Bot: Group MC2039')
        
        elif (self.entry.get()=="who developed you"):
            self.text.insert(END,'\n\n'+'Bot: group MC2039')
        
        elif (self.entry.get()=="bye"):
            self.text.insert(END,'\n\n'+'Bot: See You Thanku||')
        else:
            self.text.insert(END,"\n\n"+"Bot: Sorry I didn't get it")    
                            
                
                
        
                
        
        
        
        
        
        
if __name__=='__main__':
    root=Tk()
    obj=Chatbot(root)
    root.mainloop()
            
        
        
        