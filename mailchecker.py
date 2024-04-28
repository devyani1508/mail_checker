from tkinter import*
from tkinter import ttk

root=Tk()
root.title('MAIL CHECKER!')
root.geometry('800x600+150+50')
# root.wm_iconbitmap("c:\Users\devya\Downloads\ramji-3.ico")
check=0
def getmail():
    email=etry.get()
    k,j,d=0,0,0
    if len(email)>=6:
        if email[0].isalpha():
            if ("@" in email) and (email.count("@")==1):
                if (email[-4]==".") ^ (email[-3]=="."):
                    for i in email:
                        if i==" ":
                            k=1
                        elif i.isalpha():
                            if i==i.upper:
                                j==1
                        elif i.isdigit():
                            continue
                        elif i=="_" or i=="." or i=="@":
                            continue
                        else:
                            d=1
                    
                    if k==1 or j==1 or d==1:
                        check=1
                    else:
                        check=0
                else:
                    check=1
            else:
                check=1
        else:
            check=1
    else:
        check=1
        

    if check==0:
        lbl2=Label(root,text="submitted succesfully",font=("arial",15,"bold"))
        lbl2.place(x=320,y=380)
    else:
        lbl2=Label(root,text="check your your mail",font=("arial",15,"bold"))
        lbl2.place(x=320,y=380)

    

frame=Frame(root,bd=3,relief=RIDGE,bg='white')
frame.place(x=40,y=30,width=700,height=300)

btn=Button(root,text='SUBMIT',font=20,bg='light blue',fg='dark blue',activebackground='red',command=getmail)
btn.place(x=320,y=350,relwidth=0.10)


lbl1=Label(frame,text='ENTER YOUR MAIL',font=('algebraic',15,'bold'),fg='blue',bg='light blue',relief=SUNKEN)
lbl1.place(x=250,y=50,relwidth=0.29)

etry=Entry(frame,width=50,font=30,bg='white')
etry.place(x=60,y=100,relheight=0.10)

root.mainloop()

