import sqlite3
import webbrowser
import os
from tkinter import *
from tkinter import messagebox
    
root=Tk()
root.title("E-VOTING")
root.geometry("1500x1000")
canvas = Canvas(root,width = 1000, height = 1000,bg="black")
img = PhotoImage(file="image.png")      
canvas.create_image(0,0, anchor=NW, image=img)

id=canvas.create_text(400,300,text="E-VOTING",font=('arial',55),fill="lightblue")
id=canvas.create_text(1300,675,text="*T & C apply",font=('arial',12),fill="white")
id=canvas.create_text(95,650,text='''Be Digitally Smart!!!''',font=('arial',16,'italic'),fill="cyan")
id=canvas.create_text(400,375,text='''\n"VOTING\nis not only your right - it is your power"''',font=('arial',20,'italic'),fill="blue")

conn=sqlite3.connect('E_VOTINGS.db')
cur=conn.cursor()

cur.execute('''create table if NOT EXISTS Voters(Id INT UNIQUE, pswd VARCHAR(30))''')
print("Table Voters created...")
conn.commit()



print("E-Voting executing...")

view_id=StringVar()
v_id=IntVar()
v_pass=StringVar()

def ShowRailways():
    Railways= Toplevel(bg="yellow")
    Railways.title("E-Voting")
    width = 600
    height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Railways.resizable(0, 0)
    Railways.geometry("%dx%d+%d+%d" % (width, height, x, y))
    
    l=Label(Railways, text="LOGIN", font=('arial',20),relief=RAISED)
    l.pack()
    la=Label(Railways, text="Enter User ID:", font=('arial',15))
    la.pack()
    ea=Entry(Railways, textvariable=view_id)
    ea.pack()
    lb=Label(Railways, text="Enter Password:", font=('arial',15))
    lb.pack()
    eb=Entry(Railways, textvariable=v_pass)
    eb.pack()
    

    
    def execute():
        os.system("start cmd /c cd Desktop & cd pragati_final & cd election & npm run dev")
##        query='select pswd from Voters where Id=%d' %view_id.get()
##        cur.execute(query)
##        n3=StringVar()
##        n3=cur.fetchone()
##        print(n3)
##        def hello():
##            os.system("start cmd /c cd Desktop & cd pragati_final & cd election & npm run dev")
##        if str(v_pass.get()) == str(n3):
##            
##            hello()
##        
##        else:
##            messagebox.showinfo("Message", '''Invalid Password or ID!!''')
##        
    button=Button(Railways, text="\n   BOOK   \n",command=execute)
    button.pack()
    Railways()

def ShowCall():
    calls= Toplevel(bg="black")
    calls.title("Contact Details")
    width = 500
    height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    calls.resizable(0, 0)
    calls.geometry("%dx%d+%d+%d" % (width, height, x, y))
    label=Label(calls, text="  CONTACT DETAILS  ", font=('arial',20), relief=RAISED)
    label.pack()
    text=Text(calls)
    text.insert(INSERT,'''\n->PHONE NO:02288653872\n->MOBILE NO:9675235460\n->MOBILE NO:9565429990\n->FAX NO:022234876509''')
    text.pack()
    calls()
def ShowEmail():
    e= Toplevel(bg="black")
    e.title("Contact Details")
    width = 500
    height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    e.resizable(0, 0)
    e.geometry("%dx%d+%d+%d" % (width, height, x, y))
    label=Label(e, text="  CONTACT DETAILS  ", font=('arial',20), relief=RAISED)
    label.pack()
    text=Text(e)
    text.insert(INSERT,'''\n->EMAIL ID :gov@gmail.com''')
    text.pack()
    e()
def ShowTerms():
    Terms= Toplevel(bg="black")
    Terms.title("Guidelines")
    width = 800
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Terms.resizable(0, 0)
    Terms.geometry("%dx%d+%d+%d" % (width, height, x, y))

    
    label=Label(Terms, text="  GUIDELINES  ", font=('arial',20), relief=RAISED)
    label.pack()
    text=Text(Terms)
    text.insert(INSERT,'''\n Here are a set of steps to help you cast your vote conviniently:
    \n
    \n-> Menubar-> Login
    \n-> Enter your Voter ID and Password
    \n-> Provide Face recognition
    \n-> After voter authentication, you will be directed to the Voting Page
    \n-> Select the candidate your wish to vote for
    \n-> Click on the vote button
    \n-> BOOM!!! You're done Voting! ''')
    text.pack()
    Terms()


im = PhotoImage(file="i1.png")
im1=PhotoImage(file="i2.png")
im2=PhotoImage(file="i3.png")
im3=PhotoImage(file="i4.png")
im4=PhotoImage(file="i5.png")
im5=PhotoImage(file="i6.png")
im6=PhotoImage(file="i7.png")
menubar1=Menu(root)
root.configure(menu=menubar1)
fmenu=Menu(menubar1,tearoff=0)
menubar1.add_cascade(label="Login",menu=fmenu)
fmenu.add_command(label="Login Now!",command=ShowRailways,image=im5,compound=LEFT)
tmenu=Menu(menubar1,tearoff=0)
menubar1.add_cascade(label="Guidelines",menu=tmenu)
tmenu.add_command(label="Read",command=ShowTerms)
amenu=Menu(menubar1,tearoff=0)
menubar1.add_cascade(label="Contact",menu=amenu)
amenu.add_command(label="Call",command=ShowCall,image=im3,compound=LEFT)
amenu.add_command(label="Email",command=ShowEmail,image=im4,compound=LEFT)

canvas.pack(expand = 1, fill=BOTH)
root.mainloop()
