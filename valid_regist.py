import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3
import re
from tkinter.ttk import Combobox


#-----------------------squlite

d=sqlite3.connect("validregistration3.db")
c=d.cursor()

q=("create table if not exists Student1(Name text, Email text,Password text,Contact text,Age integer,City text)")
c.execute(q)
d.commit()
d.close()






#-------------------------------------------------------------------------


def checkname(name):

    if name.isalnum():
        return True
    if name == "":
            return True
    else:
        messagebox.showwarning("Invalid","Not allowed "+ name[-1])
        return False


def checkpaswd(paswd):
    if len(paswd)<=20:
                if re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z](?=.*[^a-bA-B0-9]))",paswd):
                        return True


                messagebox.showwarning("Invalid","PASSWORD must contain 1 Upper case, 1 Lower case,1 Num,1 special character")
                return False
    else:
        messagebox.showwarning("Invalid","Length try to exceed")
        return False


def checkcontact(contact):
    if contact.isdigit():
        return True

    if len(str(contact))==0:
        return True

    if len(str(contact))<10:
        return False

    else:
        messagebox.showwarning("INVALID",'ENTER A VALID Contact')

        return False

def checkemail(email):
    if len(email)>7:
        if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",email):
            return True


        else:
            messagebox.showwarning("Alert","Invalid E-mail enter by user")
            return False


    else:
        messagebox.showwarning("Alert","Email length is too small")


#------------------------validate
def validate():

    if entry_name.get()=="":
        messagebox.showwarning("INVALID","ENTER A VALID NAME")

    elif entry_email.get()=="":
        messagebox.showwarning("INVALID","ENTER A VALID EMAIL")

    elif entry_paswd.get()=="":
        messagebox.showwarning("INVALID","ENTER A VALID PASSWORD")

    elif entry_contact.get()=="":
        messagebox.showwarning("INVALID","ENTER A VALID contact")

    elif entry_age.get()=="" or entry_age.get()== 0:
        messagebox.showwarning("INVALID","ENTER A VALID AGE")

    elif entry_city.get()=="" or entry_city.get() == "choose your city":
        messagebox.showwarning("INVALID","ENTER A VALID city")

    elif check1.get()==0 and check2.get()==0 and check3.get()==0:
        messagebox.showwarning("INVALID","ENTER A VALID LANGUAGE")

    elif entry_email.get()!= None and entry_paswd.get()!=None and entry_contact.get()!=None:
        x=checkemail(entry_email.get())
        y=checkpaswd(entry_paswd.get())
        z=checkcontact(entry_contact.get())
        print(x,y,z)



        if x== True and y==True:
            messagebox.askokcancel("DATA REGISTERED","DATA ENTERED SUCCESSFULLY")
            d=sqlite3.connect("validregistration3.db")
            c=d.cursor()

            q=("create table if not exists Student1(Name text, Email text,Password text,Contact text,Age integer,City text)")
            c.execute(q)
            c.execute("insert into Student1(Name , Email ,Password ,Contact ,Age ,City )values(?,?,?,?,?,?)",(entry_name.get(),entry_email.get(),entry_paswd.get(),entry_contact.get(),entry_age.get(),entry_city.get()))

            # c.execute("insert into Student1(Name, Email ,Password ,Contact ,Age ,City ,Language )values(?,?,?,?,?,?,?)",(name,email,paswd,contact,age,city,language))

            d.commit()
            d.close()




#---------------------------------------------verify
def verify():
    global screen1
    screen1=Toplevel(screen)
    screen1.geometry("500x500")
    screen1.config(bg='white')

    label_tiltle=Label(screen1,bg='PINK',font=('bold',25),text='REGISTRATION FORM')
    label_tiltle.place(x=220,y=50)

    Label_name=Label(screen1,bg='white',font=('bold',25),text='Name     :           '+ entry_name.get() )
    Label_name.place(x=150,y=150)

    Label_email=Label(screen1,bg='white',font=('bold',25),text='Email         :       '+entry_email.get())
    Label_email.place(x=150,y=200)

    Label_password=Label(screen1,bg='white',font=('bold',25),text='Password     :       '+entry_paswd.get())
    Label_password.place(x=150,y=250)

    Label_contact=Label(screen1,bg='white',font=('bold',25),text='Contact           :       '+entry_contact.get())
    Label_contact.place(x=150,y=300)

    Label_age=Label(screen1,bg='white',font=('bold',25),text='Age        :       '+entry_age.get())
    Label_age.place(x=150,y=350)

    Label_city=Label(screen1,bg='white',font=('bold',25),text='City         :       '+entry_city.get())
    Label_city.place(x=150,y=400)

    if Radio1.get()==1:
        Label_Gender=Label(screen1,bg='white',font=('bold',25),text='Gender         :       Male')
        Label_Gender.place(x=150,y=450)
    elif Radio1.get()==2:
        Label_Gender=Label(screen1,bg='white',font=('bold',25),text='Gender         :       Female')
        Label_Gender.place(x=150,y=450)

    elif Radio1.get()==3:
        Label_Gender=Label(screen1,bg='white',font=('bold',25),text='Gender          :       OTHERS')
        Label_Gender.place(x=150,y=450)

    if check1.get()==1 and check2.get()==1 and check3.get()==1:
        Label_language=Label(screen1,bg='white',font=('bold',25),text='Language         :       PTYHON, JAVA , C+')
        Label_language.place(x=150,y=500)

    if check1.get()==1 and check2.get()==1 and check3.get()==0:
        Label_language=Label(screen1,bg='white',font=('bold',25),text='Language         :       Python , JAVA')
        Label_language.place(x=150,y=500)

    if check1.get()==1 and check2.get()==0 and check3.get()==1:
        Label_language=Label(screen1,bg='white',font=('bold',25),text='Language      :       PYTHON , C+')
        Label_language.place(x=150,y=500)

    if check1.get()==1 and check2.get()==0 and check3.get()==0:
        Label_language=Label(screen1,bg='white',font=('bold',25),text='Language         :       PYTHON')
        Label_language.place(x=150,y=500)

    if check1.get()==0 and check2.get()==1 and check3.get()==1:
        Label_language=Label(screen1,bg='white',font=('bold',25),text='Language         :       JAVA , C+')
        Label_language.place(x=150,y=500)

    if check1.get()==0 and check2.get()==1 and check3.get()==0:
        Label_language=Label(screen1,bg='white',font=('bold',25),text='Language         :       JAVA ')
        Label_language.place(x=150,y=500)

    if check1.get()==0 and check2.get()==0 and check3.get()==1:
        Label_language=Label(screen1,bg='white',font=('bold',25),text='Language         :        C+')
        Label_language.place(x=150,y=500)


#-r----------------------------------clear

def clear():
    entry_name.delete(0,END)
    entry_email.delete(0,END)
    entry_paswd.delete(0,END)
    entry_contact.delete(0,END)
    entry_age.delete(0,END)
    entry_city.set("choose your city")
    Radio1.set(0)
    check1.set(0)
    check2.set(0)
    check3.set(0)





#---------------------------------------------------------------------


# gui

def mainscreen():
    global screen
    screen=tk.Tk()
    screen.title("REGISTRATION FORM")
    screen.config(bg='orange')
    screen.geometry("1000x700")


    label_tiltle=Label(screen,bg='grey',font=('bold',25),text='REGISTRATION FORM')
    label_tiltle.place(x=220,y=50)

    Label_name=Label(screen,bg='white',font=('bold',25),text='Name')
    Label_name.place(x=150,y=150)

    Label_email=Label(screen,bg='white',font=('bold',25),text='Email')
    Label_email.place(x=150,y=200)

    Label_password=Label(screen,bg='white',font=('bold',25),text='Password')
    Label_password.place(x=150,y=250)

    Label_contact=Label(screen,bg='white',font=('bold',25),text='Contact')
    Label_contact.place(x=150,y=300)

    Label_age=Label(screen,bg='white',font=('bold',25),text='Age')
    Label_age.place(x=150,y=350)

    Label_city=Label(screen,bg='white',font=('bold',25),text='City')
    Label_city.place(x=150,y=400)


    Label_Gender=Label(screen,bg='white',font=('bold',25),text='Gender')
    Label_Gender.place(x=150,y=450)

    Label_language=Label(screen,bg='white',font=('bold',25),text='Language')
    Label_language.place(x=150,y=500)

    global entry_name,entry_email,entry_paswd,entry_contact,entry_age,entry_city,Radio1,check1,check2,check3



    entry_name=Entry(screen,width=30,bd=10)
    entry_name.place(x=300,y=150)
    validate_name=screen.register(checkname)
    entry_name.config(validate='key',validatecommand=(validate_name,"%P"))

    entry_email=Entry(screen,width=30,bd=10)
    entry_email.place(x=300,y=200)


    entry_paswd=Entry(screen,width=30,bd=10)
    entry_paswd.place(x=300,y=250)

    entry_contact=Entry(screen,width=30,bd=10)
    entry_contact.place(x=300,y=300)
    validate_contact=screen.register(checkcontact)
    entry_contact.config(validate='key',validatecommand=(validate_contact,"%P"))

    entry_age=Spinbox(screen,from_=0, to=100,bd=10,width=30)
    entry_age.place(x=300,y=350)


    valcity=['South Delhi','North Delhi','Centrel Delhi','West Delhi','East Delhi']
    entry_city=Combobox(screen,value=valcity,width=30)
    entry_city.place(x=300,y=400)
    entry_city.set("choose your city")

    Radio1=IntVar()
    RadioM=Radiobutton(screen,text='Male',font=('bold'),variable=Radio1,value=1,bg='brown')
    RadioM.place(x=300,y=450)

    RadioF=Radiobutton(screen,text='Female',font=('bold'),variable=Radio1,value=2,bg='brown')
    RadioF.place(x=400,y=450)

    RadioO=Radiobutton(screen,text='Others',font=('bold'),variable=Radio1,value=3,bg='brown')
    RadioO.place(x=500,y=450)

    check1=IntVar()
    check2=IntVar()
    check3=IntVar()

    checkP=Checkbutton(screen,text='PYTHON',bg='white',font=('bold'),variable=check1,onvalue=1)
    checkP.place(x=350,y=500)

    checkJ=Checkbutton(screen,text=' JAVA ',bg='white',font=('bold'),variable=check2,onvalue=1)
    checkJ.place(x=450,y=500)

    checkC=Checkbutton(screen,text=' C+ ',bg='white',font=('bold'),variable=check3,onvalue=1)
    checkC.place(x=550,y=500)

    button_submit=Button(screen,text='SUBMIT',font=('bold',20),relief=RAISED,command=validate)
    button_submit.place(x=300,y=600)

    button_clear=Button(screen,text='CLEAR',font=('bold',20),relief=RAISED,command=clear)
    button_clear.place(x=150,y=600)

    button_verify=Button(screen,text='VERIFY',font=('bold',20),relief=RAISED,command=verify)
    button_verify.place(x=450,y=600)

    # global entry_name,entry_email,entry_paswd,entry_contact,entry_age,entry_city,Radio1,check1,check2,check3

    global name
    name=entry_name.get()

    global paswd
    paswd=entry_paswd.get()

    global email
    email=entry_email.get()

    global contact
    contact=entry_contact.get()

    global age
    age=entry_age.get()

    global city
    city=entry_city.get()

    global language
    language=check1.get(),check2.get(),check3.get()
    language=str(language)



    screen.mainloop()
mainscreen()
