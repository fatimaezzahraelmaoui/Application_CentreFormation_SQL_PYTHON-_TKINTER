import tkinter as tk
from tkinter import ttk
from subprocess import call
from tkinter import messagebox
import mysql.connector
import pymysql

win =tk.Tk()
win .geometry("1350x700+0+0")
win.title("Student Management Syteme")

title_lab = tk.Label(win,text="Systeme De Gestion Des Etudiants",font=("Arial",30,"bold"),border=13,relief=tk.GROOVE,bg="red",foreground="yellow")
title_lab.pack(side=tk.TOP)

de_frame = tk.LabelFrame(win ,text="Entre les information",font=("Arial",24),bg="white",fg="green")
de_frame.place(x=25,y=80,width=420,height=590)

da_frame = tk.LabelFrame(win,bd=12,bg="white",relief=tk.GROOVE)
da_frame.place(x=460,y=90,width=860,height=565)

num = tk.StringVar()
nomp = tk.StringVar()
gen = tk.StringVar()
con = tk.StringVar()
ema = tk.StringVar()
yea = tk.StringVar()
ni = tk.StringVar()
fil = tk.StringVar()

rol_lbl = tk.Label(de_frame,text="NumEtu :",font=("Arial",18),fg="blue")
rol_lbl.grid(row=0,column=0,padx=2,pady=2)

rol_ent = tk.Entry(de_frame,bd=7,font=("Arial",18),textvariable=num)
rol_ent.grid(row=0,column=1,padx=2,pady=2)

rol1_lbl = tk.Label(de_frame,text="Nom Prenom :",font=("Arial",18),fg="blue")
rol1_lbl.grid(row=1,column=0,padx=2,pady=2)

rol1_ent = tk.Entry(de_frame,bd=7,font=("Arial",18),textvariable=nomp)
rol1_ent.grid(row=1,column=1,padx=2,pady=2)

rol6_lbl = tk.Label(de_frame,text="Genre :",font=("Arial",18),fg="blue")
rol6_lbl.grid(row=2,column=0,padx=2,pady=2)

sear_ten = ttk.Combobox(de_frame,font=("Arial",18),state="readonly",textvariable=gen)
sear_ten['values'] = ('Fille','Garçon')
sear_ten.grid(row=2,column=1,padx=12,pady=2)

rol2_lbl = tk.Label(de_frame,text="Contact :",font=("Arial",18),fg="blue")
rol2_lbl.grid(row=3,column=0,padx=2,pady=2)

rol2_ent = tk.Entry(de_frame,bd=7,font=("Arial",18),textvariable=con)
rol2_ent.grid(row=3,column=1,padx=2,pady=2)

rol3_lbl = tk.Label(de_frame,text="Email :",font=("Arial",18),fg="blue")
rol3_lbl.grid(row=4,column=0,padx=2,pady=2)

rol3_ent = tk.Entry(de_frame,bd=7,font=("Arial",18),textvariable=ema)
rol3_ent.grid(row=4,column=1,padx=2,pady=2)

rol4_lbl = tk.Label(de_frame,text="Year :",font=("Arial",18),fg="blue")
rol4_lbl.grid(row=5,column=0,padx=2,pady=2)

rol4_ent = tk.Entry(de_frame,bd=7,font=("Arial",18),textvariable=yea)
rol4_ent.grid(row=5,column=1,padx=2,pady=2)

rol5_lbl = tk.Label(de_frame,text="Niveau :",font=("Arial",18),fg="blue")
rol5_lbl.grid(row=6,column=0,padx=2,pady=2)

rol5_ent = tk.Entry(de_frame,bd=7,font=("Arial",18),textvariable=ni)
rol5_ent.grid(row=6,column=1,padx=2,pady=2)

rol7_lbl = tk.Label(de_frame,text="Filiere :",font=("Arial",18),fg="blue")
rol7_lbl.grid(row=7,column=0,padx=2,pady=2)

sear_enT = ttk.Combobox(de_frame,font=("Arial",18),state="readonly",textvariable=fil)
sear_enT['values'] = ('Français','Englais','physique','math')
sear_enT.grid(row=7,column=1,padx=12,pady=2)


def fetch():
    com = pymysql.connect(host="localhost",user="root",password="fatima1234567",database="sms1")
    cor = com.cursor()
    cor.execute("SELECT * FROM data")
    rows = cor.fetchall()
    if len(rows)!=0:
        table.delete(*table.get_children())
    for row in rows :
        table.insert('',tk.END,values=row)
    com.close()
    

fetch()

def get_data(event):
    cor_row = table.focus()
    cont = table.item(cor_row)
    row = cont['values']
    num.set(row[0])
    nomp.set(row[1])
    gen.set(row[2])
    con.set(row[3])
    ema.set(row[4])
    yea.set(row[5])
    ni.set(row[6])
    fil.set(row[7])

def clear():
    num.set("")
    nomp.set("")
    gen.set("")
    con.set("")
    ema.set("")
    yea.set("")
    ni.set("")
    fil.set("")

def Ajouter():
    if num.get() == "" or nomp.get() == "" or gen.get() == "":
        messagebox.showerror("information", "student Ajouter avec succès :)")
    else:
        com = pymysql.connect(host="localhost",user="root",password="fatima1234567",database="sms1")
        meConnect = com.cursor()
        meConnect.execute("INSERT INTO data (NumEtu, Nom_Prenom,Genre, Contact, Email, Year, Niveau,Filiere) VALUES (%s, %s, %s, %s, %s,%s, %s, %s)",(num.get(),
    nomp.get(),
    gen.get(),
    con.get(),
    ema.get() ,
    yea.get() ,
    ni.get() ,
    fil.get() ))
        com.commit()
        com.close()


def Modifer():
    nume = num.get()
    nom = nomp.get()
    gene = gen.get()
    conc = con.get()
    Email  = ema.get() 
    Ema = yea.get() 
    Enl  = ni.get() 
    rsl  = fil.get() 
    

    com = pymysql.connect(host="localhost",user="root",password="fatima1234567",database="sms1")
    meConnect = com.cursor()

    try:
        sql = "update data set  Nom_Prenom=%s,Genre= %s, Contact= %s, Email= %s, Year= %s, Niveau= %s, Filiere= %s where NumEtu= %s "
        val = (nume,nom,gene,conc,Email,Ema,Enl,rsl )
        meConnect.execute(sql, val)
        com.commit()
        derniereMatricule = meConnect.lastrowid
        messagebox.showinfo("information", "evennement modifier")
        win.destroy()
        call(["python", "student.py"])

    except Exception as e:
        print(e)
        #retour
        com.rollback()
        com.close()



def Supprimer():
    nume = num.get()

    com = pymysql.connect(host="localhost",user="root",password="fatima1234567",database="sms1")
    meConnect = com.cursor()

    try:
        sql = "delete from data where NumEtu= %s "
        val = (nume)
        meConnect.execute(sql, val)
        com.commit()
        derniereMatricule = meConnect.lastrowid
        messagebox.showinfo("information", "student supprimer :)")
        win.destroy()
        call(["python", "student.py"])

    except Exception as e:
        print(e)
        #retour
        com.rollback()
        com.close()




      

btn_frame = tk.Frame(de_frame,bg="lightgrey",bd=10,relief=tk.GROOVE)
btn_frame.place(x=18,y=390,width=430,height=140)

add_btn = tk.Button(btn_frame,bg="lightgrey",text="Add",bd=7,font=("Arial",18),width=12,command=Ajouter)
add_btn.grid(row=0,column=0,padx=2,pady=2)

upp_btn = tk.Button(btn_frame,bg="lightgrey",text="Update",bd=7,font=("Arial",18),width=12,command=Modifer)
upp_btn.grid(row=0,column=1,padx=3,pady=2)

del_btn = tk.Button(btn_frame,bg="lightgrey",text="Delete",bd=7,font=("Arial",18),width=12,command=Supprimer)
del_btn.grid(row=1,column=0,padx=2,pady=2)

cle_btn = tk.Button(btn_frame,bg="lightgrey",text="Clear",bd=7,font=("Arial",18),width=12,command=clear)
cle_btn.grid(row=1,column=1,padx=3,pady=2)
 
 
 
 
rol8_lbl = tk.Label(da_frame,text="Search :",font=("Arial",18),fg="deeppink")
rol8_lbl.grid(row=0,column=0,padx=12,pady=2)

sear_en = ttk.Combobox(da_frame,font=("Arial",18),state="readonly")
sear_en['values'] = ('NumEtu','Nom Prenom','Genre','Contact','Email','Year','Niveau','Filiere')
sear_en.grid(row=0,column=1,padx=12,pady=2)

sel_btn = tk.Button(da_frame,bg="lightgrey",text="Seatch",bd=7,font=("Arial",18),width=10)
sel_btn.grid(row=0,column=2,padx=3,pady=2)

se_btn = tk.Button(da_frame,bg="lightgrey",text="Show All",bd=7,font=("Arial",18),width=10)
se_btn.grid(row=0,column=3,padx=3,pady=2)

table = ttk. Treeview(da_frame, columns = (1, 2, 3, 4, 5, 6, 7,8), height = 5, show = "headings")

table.place(x = 0,y = 100, width = 770, height = 450)

#Entete

table.heading(1, text = "NumEtu")

table.heading(2, text = "Nom Prenom")

table.heading(3, text = "Genre")

table.heading(4, text = "Contact")

table.heading(5, text = "Email")

table.heading(6, text = "Year")

table.heading(7, text = "Niveau")

table.heading(8, text = "Filiere")

table.column(1,width = 30)

table.column(2,width = 70)

table.column(3,width = 50)

table.column(4,width = 80)

table.column(5,width = 90)

table.column(6,width = 60)

table.column(7,width = 60)

table.column(8,width = 60)

fetch()

table.bind("<ButtonRelease-1>",get_data)

win.mainloop()   
