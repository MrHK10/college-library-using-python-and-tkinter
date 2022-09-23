#kanchu 
from cProfile import label
from cgitb import text
from logging import root
from msilib.schema import BindImage, ListBox
from multiprocessing.sharedctypes import Value
from textwrap import fill
from tkinter import*
from tkinter import ttk
from tkinter.font import ROMAN
# from tkinter.tix import MAIN
from turtle import width
# from certifi import contents
# from colorama import Cursor
# from pip import main
import mysql.connector
from tkinter import messagebox
import datetime
# from mysqlx import RowResult
import tkinter







class kanchu_Library_system:
    def __init__(self,root):
        self.root=root
        self.root.title("Computer Department Library System")
        self.root.geometry("1360x768+0+0")
        
        
        self.member_var=StringVar()
        self.due_date_var=StringVar()
        self.Rollno_var=StringVar()
        self.First_name_var=StringVar()
        self.Last_name_var=StringVar()
        self.address_var=StringVar()
        self.mobile_no_var=StringVar()
        self.book_id_var=StringVar()
        self.book_title_var=StringVar()
        self.auther_name_var=StringVar()
        self.borrowed_date_var=StringVar()
        self.book_price_var=StringVar()

        
        
        
        
        
        


        lb1=Label(self.root,text="Computer Department Library System",bg="pink",fg="black",bd=18,relief=RIDGE,font=("times new roman",50,"bold","italic"),padx=2,pady=6)
        lb1.pack(side=TOP,fill=X)

        frame=Frame(self.root,relief=RIDGE,padx=20,bg="pink")
        frame.place(x=0,y=200,width=1430,height=400)

        dataFrameLeft=LabelFrame(frame,text="Library Membership information",bg="pink",fg="black",bd=12,relief=RIDGE,font=("times new roman",12,"italic","bold"))
        dataFrameLeft.place(x=0,y=5,width=850,height=370)

        member1=Label(dataFrameLeft,bg="pink",text="Member type",font=("times new roman",15,"bold","italic"),padx=2,pady=6)
        member1.grid(row=0,column=0,sticky=W)  

        comMember=ttk.Combobox(dataFrameLeft,textvariable=self.member_var,font=("times new roman",15,"bold","italic"),width=18,state="readonly")
        comMember["value"]=("Admin staff","student")
        comMember.grid(row=0,column=1)
        
        # member2=Label(dataFrameLeft,bg="powder blue",text="PRN NO",font=("times new roman",15,"bold","italic"),padx=2,pady=6)
        # member2.grid(row=1,column=0,sticky=W)
        # txt_PRN_NO=Entry(dataFrameLeft,font=("times new roman",15),width=20)
        # txt_PRN_NO.grid(row=1,column=1)
    
         
        member2roll_no=Label(dataFrameLeft,bg="pink",text="Roll_no:",font=("times new roman",15,"bold","italic"),padx=2,pady=6)
        member2roll_no.grid(row=1,column=0,sticky=W)
        txt_PRN_NO=Entry(dataFrameLeft,font=("times new roman",15),textvariable=self.Rollno_var,width=20)
        txt_PRN_NO.grid(row=1,column=1)
    

        member2firstname=Label(dataFrameLeft,bg="pink",text="Name:",font=("times new roman",15,"bold","italic"),padx=2,pady=6)
        member2firstname.grid(row=2,column=0,sticky=W)
        txt_PRN_NO=Entry(dataFrameLeft,font=("times new roman",15),textvariable=self.First_name_var,width=20)
        txt_PRN_NO.grid(row=2,column=1)


        # member2lastname=Label(dataFrameLeft,bg="powder blue",text="Last_name:",font=("times new roman",15,"bold","italic"),padx=2,pady=6)
        # member2lastname.grid(row=3,column=0,sticky=W)
        # txt_PRN_NO=Entry(dataFrameLeft,font=("times new roman",15),width=20)
        # txt_PRN_NO.grid(row=3,column=1)


        member2address=Label(dataFrameLeft,bg="pink",text="Enter your address:",font=("times new roman",15,"bold","italic"),padx=2,pady=6)
        member2address.grid(row=3,column=0,sticky=W)
        txt_PRN_NO=Entry(dataFrameLeft,font=("times new roman",15),textvariable=self.address_var,width=20)
        txt_PRN_NO.grid(row=3,column=1)


        
        member2mobile=Label(dataFrameLeft,bg="pink",text="Enter mobile_No:",font=("times new roman",15,"bold","italic"),padx=2,pady=6)
        member2mobile.grid(row=5,column=0,sticky=W)
        txt_PRN_NO=Entry(dataFrameLeft,font=("times new roman",15),textvariable=self.mobile_no_var,width=20)
        txt_PRN_NO.grid(row=5,column=1)


          
        member2Book_Id=Label(dataFrameLeft,bg="pink",text="Enter Book_Id:",font=("times new roman",15,"bold","italic"),padx=2,pady=6)
        member2Book_Id.grid(row=6,column=0,sticky=W)
        txt_PRN_NO=Entry(dataFrameLeft,font=("times new roman",15),textvariable=self.book_id_var,width=20)
        txt_PRN_NO.grid(row=6,column=1)



        member2Book_Title=Label(dataFrameLeft,bg="pink",text="Enter Book_Title:",font=("times new roman",15,"bold","italic"),padx=2,pady=6)
        member2Book_Title.grid(row=7,column=0,sticky=W)
        txt_PRN_NO=Entry(dataFrameLeft,font=("times new roman",15),textvariable=self.book_title_var,width=20)
        txt_PRN_NO.grid(row=7,column=1)

        member2author=Label(dataFrameLeft,bg="pink",text="Enter Auther_name:",font=("times new roman",15,"bold","italic"),padx=2,pady=6)
        member2author.grid(row=0,column=2,sticky=W)
        txt_PRN_NO=Entry(dataFrameLeft,font=("times new roman",15),textvariable=self.auther_name_var,width=18)
        txt_PRN_NO.grid(row=0,column=3)


        member2dateborrowed=Label(dataFrameLeft,bg="pink",text="Enter Borrowed_Date:",font=("times new roman",15,"bold","italic"),padx=2,pady=6)
        member2dateborrowed.grid(row=1,column=2,sticky=W)
        txt_PRN_NO=Entry(dataFrameLeft,font=("times new roman",15),textvariable=self.borrowed_date_var,width=18)
        txt_PRN_NO.grid(row=1,column=3)



        member2author=Label(dataFrameLeft,bg="pink",text="enter due_date:",font=("times new roman",15,"bold","italic"),padx=2,pady=6)
        member2author.grid(row=2,column=2,sticky=W)
        txt_PRN_NO=Entry(dataFrameLeft,font=("times new roman",15),textvariable=self.due_date_var,width=18)
        txt_PRN_NO.grid(row=2,column=3)


        member2book_price=Label(dataFrameLeft,bg="pink",text="enter Book_price:",font=("times new roman",15,"bold","italic"),padx=2,pady=6)
        member2book_price.grid(row=3,column=2,sticky=W)
        txt_PRN_NO=Entry(dataFrameLeft,font=("times new roman",15),textvariable=self.book_price_var,width=18)
        txt_PRN_NO.grid(row=3,column=3)




        dataFrameright=LabelFrame(frame,text="book details",bg="pink",fg="black",bd=12,relief=RIDGE,font=("times new roman",12,"italic","bold"))
        dataFrameright.place(x=860,y=5,width=600,height=370)

        self.textbox=Text(dataFrameright,bg="pink",font=("times new roman",12,"italic","bold"),width=30,height=16,padx=2,pady=6)
        self.textbox.grid(row=0,column=2)
           
        listscrollbar=Scrollbar(dataFrameright)
        listscrollbar.grid(row=0,column=1,sticky="ns")
        listBooks=['English communication skill',
'English communication skill - 2',
'Essay learning to internet',
'English literary skill -1',
'English literary skill -2',
'General english ',
'MBD english guide',
'General english ',
'English communication skill(sem 3)',
'English communication skill(sem 4)',
'Hi tech literary skill- 2',
'Modern information system ',
'internet concept application',
'A simplified approached to internet and java',
'Fundamental of analog and digital electronics',
'fundamental of information technology',
'pc software',
'web desiging using html and dhtml ',
'system analysis and design',
'management information system ',
'structure system analysis and design',
'web technology',
'Data structure',
'artificial intelligence',
'office automation',
'computer networks',
'Business management',
'vector calculous and different geometry ',
'Design and analysis of algorithem',
'operating system concept ',
'Analysis and design of algorthems',
'Linux administration',
'Simplified approach to visual basic',
'Linux ',
'Web technology',
'system software',
'web desiging using html and dhtml ',
'Computer graphics',
'Fundamentals of internet applications',
'Computer networks',
'Information technology',
'Digital electronics',
'E-commerce',
'Computer networks',
'Visual Basic',
'Information technology',
'Digital electronics',
'Computer application in business',
'Computer network and internet programming',
'Management information system ',
'Simplified approach to DBMS',
'system analysis and design',
'Internet and world wide web',
'computer graphics & multimedia',
'Digital electronics',
'Digital electronics',
'ABC of digital electronics',
'Computer fundamental',
'Computer for business',
'Computer application in business',
'Basic of information technology',
'Fumdamentals of information technology',
'Data and files structures',
'Java programming ',
'Information technology and ms office ',
'Programming in java',
'information systen and design',
'system software',
'structure system analysis and design',
'window based computer coursec',
'Web designing HTML ',
'Medicinal chemistry - 1',
'Fundamentals of E - business',
'system analysis and design',
'Programming core java',
'International Politics  theory',
'Windoe based computer course',
'Communication and networking',
'Traning',
'Business Economics - 1',
'DBMS with MS-Access',
'DBMS',
'RDBMS with oracle',
'DBMS',
'RDBMS with oracle',
'DBMS',
'Database management and oracle programming',
'DBMS',
'COA',
'COA',
'COA',
'COA',
'COA',
'COA',
'Mathematical foundation of computer science',
'Discreate mathematics',
'Mathematical foundation of computer science',
'Fundamentals and programming in C',
'Programming Fundamentals using C',
'Programming using c++',
'Programming using c++',
'Data structure in c',
'Mathematical foundation of computer science',
'Mathematical foundation of computer science',
'Basic mathematics',
'Basic mathematics',
'Computer oriented numerical & statistical methods',
'Programming Fundamentals using C',
'Object oriented Design and c++',
'Object oriented programming  using c++',
'Java programming ',
'Computer programming & problem solving through "c"',
'Object oriented programming  using c++',
'Programming in c',
'Object oriented and c++',
'Programming Fundamentals using C',
'let us c',
'Object oriented Design and c++',
'Programming in c++',
'computernprograms of numerical and statical techniqunes using c and c++',
'problem solving using c',
'Big basics of computer',
'programmming in core java',
'office automation and productivity tools',
'Computer application in business',
'Business studies -1',
'Office automation tools',
'Business statistics',
'principle of management',
'Computer oriented methods',
'Data communication and networking',
'Programming using c++',
'Priogramming using c',
]
        
        
        
        def SelectBook(event=""):
           value=str(listbox.get(listbox.curselection()))
           x=value
           if (x=="English communication skill"):
               self.book_id_var.set("BK1")
               self.book_title_var.set("english book")
               self.auther_name_var.set("kanchu")
               d1=datetime.datetime.today()
               d2=datetime.timedelta(days=15)
               d3=d1+d2
               self.borrowed_date_var.set(d1)
               self.due_date_var.set(d3)
            #    self.daysonbook.set(15)
               self.due_date_var.set("No")
               self.book_price_var.set("Rs.780")
               
               
                        

        listbox=Listbox(dataFrameright,bg="pink",font=("times new roman",12,"italic"),width=26,height=16)
        listbox.bind("<<ListboxSelect>>",SelectBook)
        listbox.grid(row=0,column=0,padx=4)
        listscrollbar.config(command=listbox.yview)

        for item in listBooks:
            listbox.insert(END,item)

    
        Framebutton=Frame(self.root,relief=RIDGE,padx=20,bg="pink",bd=12)
        Framebutton.place(x=0,y=130,width=1430,height=70)


        btnadData=Button(Framebutton,text="Add Data",command=self.adda_data,font=("times new roman",12,"italic","bold"),width=20,bg="light green",fg="black",borderwidth = 4)
        btnadData.grid(row=0,column=0)

        btnadData=Button(Framebutton,text="Show data",command=self.show_data,font=("times new roman",12,"italic","bold"),width=20,bg="light green",fg="black" ,borderwidth = 4)
        btnadData.grid(row=0,column=1) 

        btnadData=Button(Framebutton,text="Update",command=self.update,font=("times new roman",12,"italic","bold"),width=20,bg="light green",fg="black", borderwidth = 4)
        btnadData.grid(row=0,column=2)


        btnadData=Button(Framebutton,text="Delete",command=self.delete,font=("times new roman",12,"italic","bold"),width=20,bg="light green",fg="black", borderwidth = 4)
        btnadData.grid(row=0,column=3)


        btnadData=Button(Framebutton,text="Reset",command=self.reset_r,font=("times new roman",12,"italic","bold"),width=20,bg="light green",fg="black",borderwidth=4)
        btnadData.grid(row=0,column=4)

        btnadData=Button(Framebutton,text="Exit",command=self.kanexit,font=("times new roman",12,"italic","bold"),width=24,bg="light green",fg="black",borderwidth=4)
        btnadData.grid(row=0,column=5)


        frameinfo=Frame(self.root,bd=18,relief=RIDGE,padx=20,bg="pink")
        frameinfo.place(x=0,y=600,width=1430,height=250)

        Table_frame=Frame(frameinfo,bd=0,relief=RIDGE,bg="pink")
        Table_frame.place(x=0,y=4,width=1350,height=200)

        xscroll=Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,columns=("membertype","Roll_no","First_name","Last_name","address","mobile_no","book_id","book_title","auther_name","borrowed_date","book_price","due date"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview) 

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("Roll_no",text="Roll_no")
        self.library_table.heading("First_name",text="Firstname")
        self.library_table.heading("Last_name",text="Lastname")
        self.library_table.heading("address",text="Address")
        self.library_table.heading("mobile_no",text="Mobile_No")
        self.library_table.heading("book_id",text="Book_ID")
        self.library_table.heading("book_title",text="Book_Title")
        self.library_table.heading("auther_name",text="Auther_name")
        self.library_table.heading("borrowed_date",text="Borrowed_Date")
        self.library_table.heading("book_price",text="Book_price")
        self.library_table.heading("due date",text="Due date")
        
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("Roll_no",width=100)
        self.library_table.column("First_name",width=100)
        self.library_table.column("Last_name",width=100)
        self.library_table.column("address",width=100)
        self.library_table.column("mobile_no",width=100)
        self.library_table.column("book_id",width=100)
        self.library_table.column("book_title",width=100)
        self.library_table.column("auther_name",width=100)
        self.library_table.column("borrowed_date",width=100)
        self.library_table.column("book_price",width=100)
        self.library_table.column("due date",width=100)


        self.fetch_data() 
        self.library_table.bind("<ButtonRelease-1>",self.get_kanchu)



    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="kanchu",database="sys")
        mycursor=conn.cursor()
        mycursor.execute("insert into library2 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.member_var.get(),
            self.Rollno_var.get(),
            self.First_name_var.get(),
            self.Last_name_var.get(),
            self.address_var.get(),
            self.mobile_no_var.get(),
            self.book_id_var.get(),
            self.book_title_var.get(),
            self.auther_name_var.get(),
            self.borrowed_date_var.get(),
            self.book_price_var.get(),
            self.due_date_var.get(),
            ))

        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("sucess","member has been added successfully")
        
        
        
    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="kanchu",database="sys")
        mycursor=conn.cursor()
        mycursor.execute("update library2 set member=%s, First_name=%s, Last_name=%s, address=%s, mobile_no=%s, book_id=%s, book_title=%s, auther_name=%s, borrowed_date=%s, book_price=%s, due_date=%s where Rollno=%s",(
                    self.member_var.get(),
                    self.First_name_var.get(),
                    self.Last_name_var.get(),
                    self.address_var.get(),
                    self.mobile_no_var.get(),
                    self.book_id_var.get(),
                    self.book_title_var.get(),
                    self.auther_name_var.get(),
                    self.borrowed_date_var.get(),
                    self.book_price_var.get(),
                    self.due_date_var.get(),
                    self.Rollno_var.get(),
        ))
        conn.commit()
        self.fetch_data()
        self.reset_r()
        conn.close()
        
        messagebox.showinfo("success","your data has been successfull updated")
        
    

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="kanchu",database="sys")
        mycursor=conn.cursor()
        mycursor.execute("select * from library2")
        rows=mycursor.fetchall()
        
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,value=i)
            conn.commit()
        conn.close()     
        
        
    def get_kanchu(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values'] 
        self.member_var.set(row[0])
        self.Rollno_var.set(row[1])
        self.First_name_var.set(row[2])
        self.Last_name_var.set(row[3])
        self.address_var.set(row[4])
        self.mobile_no_var.set(row[5])
        self.book_id_var.set(row[6])
        self.book_title_var.set(row[7])
        self.auther_name_var.set(row[8])
        self.borrowed_date_var.set(row[9])
        self.book_price_var.set([row[10]])
        self.due_date_var.set(row[11])
        
                   
        
    


    def show_data(self):
        self.textbox.insert(END,"Member Type\t\t"+self.member_var.get()+"\n")
        self.textbox.insert(END,"Roll_no\t\t"+self.Rollno_var.get()+"\n")
        self.textbox.insert(END,"First_name\t\t"+self.First_name_var.get()+"\n")
        self.textbox.insert(END,"Last_name\t\t"+self.Last_name_var.get()+"\n")
        self.textbox.insert(END,"Address\t\t"+self.address_var.get()+"\n")
        self.textbox.insert(END,"Mobile_no\t\t"+self.mobile_no_var.get()+"\n")
        self.textbox.insert(END,"Book_id\t\t"+self.book_id_var.get()+"\n")
        self.textbox.insert(END,"Book_Title\t\t"+self.book_title_var.get()+"\n")
        self.textbox.insert(END,"Auther_name\t\t"+self.auther_name_var.get()+"\n")
        self.textbox.insert(END,"Borrowed_date\t\t"+self.borrowed_date_var.get()+"\n")
        self.textbox.insert(END,"Book_price\t\t"+self.book_price_var.get()+"\n")
        self.textbox.insert(END,"Due date\t\t"+self.due_date_var.get()+"\n")
        
        
        
        
    def reset_r(self):
        self.member_var.set(""),   
        self.Rollno_var.set("") ,  
        self.due_date_var.set(""),
        self.First_name_var.set(""),
        self.Last_name_var.set(""),
        self.address_var.set(""),
        self.mobile_no_var.set(""),
        self.book_id_var.set(""),
        self.book_id_var.set(""),
        self.borrowed_date_var.set(""),
        self.book_price_var.set(""),
        self.textbox.delete("1.0",END)
        
        
        
    def kanexit(self):
        kanexit=tkinter.messagebox.askyesno("Library management","Do you want to exit")
        if kanexit>0:
         self.root.destroy()
         return
     
     
     

    def delete(self):
        if self.Rollno_var.get()=="" or self.mobile_no_var.get()=="":
          messagebox.showerror("Error","First select the Member")
        else:
          conn=mysql.connector.connect(host="localhost",username="root",password="kanchu",database="sys")
          mycursor=conn.cursor()    
          query="delete from library2 where Rollno=%s"
          value=(self.Rollno_var.get(),)
          mycursor.execute(query,value)
          
          conn.commit()
          self.fetch_data()
          self.reset_r()
          conn.close()


          messagebox.showinfo("Success","Member has been Deleted")




if __name__=="__main__":
    root=Tk()
    obj= kanchu_Library_system(root)
    root.mainloop()



                                    