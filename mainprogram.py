from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
import pickle as p
import random as r


#------------------------- Command Functions --------------------------------

#----- Add New Book -----

def addbook():
   global bkaddpage
   bkaddpage = Tk()
   bkaddpage.title('Add Book')
   bkaddpage.geometry('767x548')
   bkaddpage.configure(bg = '#1A2A29')
   additionicon = PhotoImage(file = 'images/Addicon.png')
   bkaddpage.iconphoto(False,additionicon)
   
   def add_click():
      b_id = (e1.get()).upper()
      bname = (e2.get()).upper()
      bauthor = (e3.get()).upper()
      bcat = (e4.get()).upper()
      record = [b_id, bname, bauthor, bcat, 'AVAILABLE', '-']
      f = open("files/BookRoughCopy.dat", 'rb+')
      bk_rec = p.load(f)
      book_ids = [i[0] for i in bk_rec]
      book_names = [i[1] for i in bk_rec]
      if '' in record:
         messagebox.showwarning("Error", "Field Empty Input Not Valid")
      elif b_id in book_ids:
         messagebox.showwarning("Error", "Book with this Id already exists")
      elif bname in book_names:
         messagebox.showwarning("Error", "Book with same name already exists")
      else:
         bk_rec.insert(r.randrange(len(bk_rec)),record)
         f.truncate(0)
         f.seek(0)
         p.dump(bk_rec, f)
         messagebox.showinfo("Addition Success", "Book Added")
         f.close()
         e1.delete(0, END)
         e2.delete(0, END)
         e3.delete(0, END)
         e4.delete(0, END)

   def backtomenu():
      bkaddpage.destroy()
      Menuscreen()

   #labels, entries and buttons
      
   addframe = LabelFrame(bkaddpage, padx=100, pady=50, bg='#F5F5F5', borderwidth=10)
   addframe.place(x=35, y=35)

   addlabel = Label(addframe, text='ENTER BOOK DETAILS', bg='#F5F5F5',
                    font=('Times New Roman','15'))
   addlabel.grid(row=0, column=1, columnspan=3)

   idlabel = Label(addframe, text='Book ID', bg='#F5F5F5', font=('Helvetica','12'))
   namelabel = Label(addframe, text='Book Name', bg='#F5F5F5', font=('Helvetica','12'))
   authorlabel = Label(addframe, text='Book Author', bg='#F5F5F5', font=('Helvetica','12'))
   categorylabel = Label(addframe, text='Book Category', bg='#F5F5F5', font=('Helvetica','12'))
   idlabel.grid(row=2, column=1, columnspan=2, sticky=W)
   namelabel.grid(row=3, column=1, columnspan=2, sticky=W)
   authorlabel.grid(row=4, column=1, columnspan=2, sticky=W)
   categorylabel.grid(row=5, column=1, columnspan=2, sticky=W)

   e1 = Entry(addframe, width=35, borderwidth=2, font=('Helvetica','12'))
   e2 = Entry(addframe, width=35, borderwidth=2, font=('Helvetica','12'))
   e3 = Entry(addframe, width=35, borderwidth=2, font=('Helvetica','12'))
   e4 = Entry(addframe, width=35, borderwidth=2, font=('Helvetica','12'))
   e1.grid(row=2, column=3, sticky=E)
   e2.grid(row=3, column=3, sticky=E)
   e3.grid(row=4, column=3, sticky=E)
   e4.grid(row=5, column=3, sticky=E)

   space1 = Label(addframe, text='      ', bg='#F5F5F5')
   space2 = Label(addframe, text='      ', bg='#F5F5F5')
   space3 = Label(addframe, text='      ', bg='#F5F5F5')
   space4 = Label(addframe, text='      ', bg='#F5F5F5')
   space1.grid(row=1, column=1)
   space2.grid(row=6, column=1)
   space3.grid(row=7, column=1)
   space4.grid(row=9, column=1)
   
   addbutton = Button(addframe, text='Add Book', fg='white', width=40, padx=10, borderwidth=7,
                    pady=10, bg='#1A2A29', font=('Calibri','16'), command = add_click)
   addbutton.grid(row=8, column=1, columnspan=3)

   backbutton = Button(addframe, text='Back to Menu', fg='white', width=40, padx=10, borderwidth=7,
                    pady=10, bg='#1A2A29', font=('Calibri','16'), command = backtomenu)
   backbutton.grid(row = 10, column=1, columnspan=3)
   
   bkaddpage.mainloop()









#----- Delete Book -----
   
def delbook():
   global bkdelpage
   bkdelpage = Tk()
   bkdelpage.title('Delete Book')
   bkdelpage.geometry('768x478')
   bkdelpage.configure(bg='#1A2A29')
   deleteicon = PhotoImage(file = 'images/Delicon.png')
   bkdelpage.iconphoto(False,deleteicon)
   
   def del_click():
      b_id = (e1.get()).upper()
      f = open("files/BookRoughCopy.dat",'rb+')
      bk_rec = p.load(f)
      book_ids = [i[0] for i in bk_rec]
      if b_id == '':
         messagebox.showwarning("Error","Field Empty Input Not Valid")
         e1.delete(0,END)
      elif b_id not in book_ids:
         messagebox.showwarning("Error","Book with this Id does not exist")
         e1.delete(0,END)
      else:
         for i in bk_rec:
            if b_id==i[0]:
               bk_rec.remove(i)
         f.truncate(0)
         f.seek(0)
         p.dump(bk_rec,f)
         messagebox.showinfo("Deletion Success","Book Deleted")
         f.close()
         e1.delete(0,END)

   def backtomenu():
      bkdelpage.destroy()
      Menuscreen()

   #labels, entries and buttons
      
   delframe = LabelFrame(bkdelpage,padx=100,pady=50,bg='#F5F5F5',borderwidth=10)
   delframe.place(x=35, y=35)

   dellabel = Label(delframe, text='ENTER BOOK ID', bg='#F5F5F5',
                    font=('Times New Roman','15'))
   dellabel.grid(row=0, column=1, columnspan=3)

   idlabel = Label(delframe, text='Book ID', bg='#F5F5F5', font=('Helvetica','12'))
   idlabel.grid(row=2, column=1, columnspan=2, sticky='W')

   e1 = Entry(delframe, width=35, borderwidth=2, font=('Helvetica','12'))
   e1.grid(row=2,column=3, sticky='E')

   space1 = Label(delframe, text='      ', bg='#F5F5F5')
   space2 = Label(delframe, text='      ', bg='#F5F5F5')
   space3 = Label(delframe, text='      ', bg='#F5F5F5')
   space4 = Label(delframe, text='      ', bg='#F5F5F5')
   space1.grid(row=1, column=1)
   space2.grid(row=6, column=1)
   space3.grid(row=7, column=1)
   space4.grid(row=9, column=1)
   
   delbutton = Button(delframe, text='Delete Book', fg='white', width=40, padx=10, borderwidth=7,
                    pady=10, bg='#1A2A29', font=('Calibri','16'), command=del_click)
   delbutton.grid(row=8,column=1, columnspan=3)

   backbutton = Button(delframe, text='Back to Menu', fg='white', width=40, padx=10, borderwidth=7,
                    pady=10, bg='#1A2A29', font=('Calibri','16'), command=backtomenu)
   backbutton.grid(row=10,column=1, columnspan=3)
   
   bkdelpage.mainloop()









#----- Display All Book Details -----
   
def disbook():
   global bkdispage
   bkdispage = Tk()
   bkdispage.title('Display All Book Details')
   bkdispage.geometry('1150x660')
   bkdispage.configure(bg = '#1A2A29')
   displayicon = PhotoImage(file = 'images/Listicon.png')
   bkdispage.iconphoto(False,displayicon)

   bkdisframe=LabelFrame(bkdispage,padx=20,pady=20,bg='#F5F5F5',borderwidth=10)
   bkdisframe.place(x=35, y=35)

   #creating a book details display as a box
   
   bkdisscroll= Scrollbar(bkdisframe)

   bkdisplay = ttk.Treeview(bkdisframe, yscrollcommand=bkdisscroll.set)

   bkdisscroll.configure(command= bkdisplay.yview)

   style = ttk.Style()
   style.configure("Treeview.Heading", font=('Times New Roman', 11))
   style.configure('Treeview', rowheight=35)

   bkdisplay['columns'] = ('Book ID','Book Name','Book Author',
                           'Book Category','Status','Issued to')

   bkdisplay.column('#0', width=0, stretch=NO)
   bkdisplay.column('Book ID', anchor=E, width=100)
   bkdisplay.column('Book Name', anchor=E, width=200)
   bkdisplay.column('Book Author', anchor=E, width=200)
   bkdisplay.column('Book Category', anchor=E, width=200)
   bkdisplay.column('Status', anchor=E, width=100)
   bkdisplay.column('Issued to', anchor=E, width=200)

   bkdisplay.heading('#0', text='', anchor=E)
   bkdisplay.heading('Book ID', text='Book ID', anchor=E)
   bkdisplay.heading('Book Name', text='Book Name', anchor=E)
   bkdisplay.heading('Book Author', text='Book Author', anchor=E)
   bkdisplay.heading('Book Category', text='Book Category', anchor=E)
   bkdisplay.heading('Status', text='Status', anchor=E)
   bkdisplay.heading('Issued to', text='Issued to (Member ID)', anchor=E)

   bkdisscroll.pack(side=RIGHT, fill=Y)
   bkdisplay.pack()

   #taking the records from binary file and displaying them
   
   backmnframe=LabelFrame(bkdispage, padx=291, pady=20, bg='#F5F5F5', borderwidth=10)
   backmnframe.place(x=35, y=505)

   f = open("files/BookRoughCopy.dat", 'rb')
   bk_rec = p.load(f)
   count=0
   for i in bk_rec:
      bkdisplay.insert(parent='', index='end', iid=count, text='',
                             values=(i[0], i[1], i[2], i[3], i[4], i[5]+'  '))
      count+=1

   f.close()

   def backtomenu():
      bkdispage.destroy()
      Menuscreen()

   backbutton = Button(backmnframe, text='Back to Menu', fg='white', width=40, padx=10, borderwidth=7,
                    pady=3, bg='#1A2A29', font=('Calibri','16'), command=backtomenu)
   backbutton.grid(row=0, column=0)
   
   bkdispage.mainloop()









#----- Search by Book No -----

def searchbook():
   global bksearchpage
   bksearchpage = Tk()
   bksearchpage.title('Search by Book ID')
   bksearchpage.geometry('1150x713')
   bksearchpage.configure(bg = '#1A2A29')
   displayicon = PhotoImage(file = 'images/Listicon.png')
   bksearchpage.iconphoto(False,displayicon)

   bksearchframe=LabelFrame(bksearchpage,padx=20,pady=20,bg='#F5F5F5',borderwidth=10)
   bksearchframe.place(x=35, y=35)

   #creating a book details display as a box
   
   bksearchscroll= Scrollbar(bksearchframe)

   bkdisplay = ttk.Treeview(bksearchframe, yscrollcommand=bksearchscroll.set)

   bksearchscroll.configure(command= bkdisplay.yview)

   style = ttk.Style()
   style.configure("Treeview.Heading", font=('Times New Roman', 11))
   style.configure('Treeview', rowheight=35)

   bkdisplay['columns'] = ('Book ID','Book Name','Book Author',
                           'Book Category','Status','Issued to')

   bkdisplay.column('#0', width=0, stretch=NO)
   bkdisplay.column('Book ID', anchor=E, width=100)
   bkdisplay.column('Book Name', anchor=E, width=200)
   bkdisplay.column('Book Author', anchor=E, width=200)
   bkdisplay.column('Book Category', anchor=E, width=200)
   bkdisplay.column('Status', anchor=E, width=100)
   bkdisplay.column('Issued to', anchor=E, width=200)

   bkdisplay.heading('#0', text='', anchor=E)
   bkdisplay.heading('Book ID', text='Book ID', anchor=E)
   bkdisplay.heading('Book Name', text='Book Name', anchor=E)
   bkdisplay.heading('Book Author', text='Book Author', anchor=E)
   bkdisplay.heading('Book Category', text='Book Category', anchor=E)
   bkdisplay.heading('Status', text='Status', anchor=E)
   bkdisplay.heading('Issued to', text='Issued to (Member ID)', anchor=E)

   bksearchscroll.pack(side=RIGHT, fill=Y)
   bkdisplay.pack()

   #taking the records from binary file and displaying them
   
   selectframe=LabelFrame(bksearchpage, padx=28,pady=20,bg='#F5F5F5',borderwidth=10)
   selectframe.place(x=35, y=505)

   def displayrec():
      f=open("files/BookRoughCopy.dat", 'rb')
      bk_rec=p.load(f)
      f.close()
      book_ids = [i[0] for i in bk_rec]
      b_id = (searchent.get()).upper()
      
      if b_id == '':
         messagebox.showwarning("Error", "Field Empty Input Not Valid")
         searchent.delete(0, END)
      elif b_id not in book_ids:
         messagebox.showwarning("Error", "Book with this Id does not exist")
         searchent.delete(0, END)
         
      else:
         for record in bkdisplay.get_children():
            bkdisplay.delete(record)
         count=0
         for i in bk_rec:
            if b_id ==i[0]:
               bkdisplay.insert(parent='', index='end', iid=count, text='',
                             values=(i[0], i[1], i[2], i[3], i[4], i[5]+'  '))
               count+=1
         searchent.delete(0, END)
         
   def backtomenu():
      bksearchpage.destroy()
      Menuscreen()

   searchlabel=Label(selectframe, text='Enter Book ID', bg='#F5F5F5',
                    font=('Helvetica','12'))
   searchlabel.grid(row=0, column=0)
   
   searchent = Entry(selectframe, width=35, borderwidth=2, font=('Helvetica','12'))
   searchent.grid(row=0, column=1, columnspan=2)

   space1=Label(selectframe, text='      ', bg='#F5F5F5')
   space2=Label(selectframe, text='      ', bg='#F5F5F5')
   space3=Label(selectframe, text='      ', bg='#F5F5F5')
   space1.grid(row=1, column=1)
   space2.grid(row=2, column=2)
   space3.grid(row=2, column=3)

   selectbutton = Button(selectframe, text='Display Book Details', fg='white', width=40, padx=10, borderwidth=7,
                    pady=3, bg='#1A2A29', font=('Calibri','16'), command=displayrec)
   selectbutton.grid(row=2, column=0, columnspan=2)
   
   backbutton = Button(selectframe, text='Back to Menu', fg='white', width=40, padx=10, borderwidth=7,
                    pady=3, bg='#1A2A29', font=('Calibri','16'), command=backtomenu)
   backbutton.grid(row=2, column=4)
   
   bksearchpage.mainloop()









#----- View by Category -----

def discat():
   global bkcatpage
   bkcatpage = Tk()
   bkcatpage.title('View by Category')
   bkcatpage.geometry('1150x713')
   bkcatpage.configure(bg = '#1A2A29')
   displayicon = PhotoImage(file = 'images/Listicon.png')
   bkcatpage.iconphoto(False,displayicon)

   bkcatframe=LabelFrame(bkcatpage,padx=20,pady=20,bg='#F5F5F5',borderwidth=10)
   bkcatframe.place(x=35, y=35)

   #creating a book details display as a box
   
   bkcatscroll= Scrollbar(bkcatframe)

   bkdisplay = ttk.Treeview(bkcatframe, yscrollcommand=bkcatscroll.set)

   bkcatscroll.configure(command= bkdisplay.yview)

   style = ttk.Style()
   style.configure("Treeview.Heading", font=('Times New Roman', 11))
   style.configure('Treeview', rowheight=35)

   bkdisplay['columns'] = ('Book ID','Book Name','Book Author',
                           'Book Category','Status','Issued to')

   bkdisplay.column('#0', width=0, stretch=NO)
   bkdisplay.column('Book ID', anchor=E, width=100)
   bkdisplay.column('Book Name', anchor=E, width=200)
   bkdisplay.column('Book Author', anchor=E, width=200)
   bkdisplay.column('Book Category', anchor=E, width=200)
   bkdisplay.column('Status', anchor=E, width=100)
   bkdisplay.column('Issued to', anchor=E, width=200)

   bkdisplay.heading('#0', text='', anchor=E)
   bkdisplay.heading('Book ID', text='Book ID', anchor=E)
   bkdisplay.heading('Book Name', text='Book Name', anchor=E)
   bkdisplay.heading('Book Author', text='Book Author', anchor=E)
   bkdisplay.heading('Book Category', text='Book Category', anchor=E)
   bkdisplay.heading('Status', text='Status', anchor=E)
   bkdisplay.heading('Issued to', text='Issued to (Member ID)', anchor=E)

   bkcatscroll.pack(side=RIGHT, fill=Y)
   bkdisplay.pack()

   # Creating frame for selecting Category

   selectframe=LabelFrame(bkcatpage, padx=28,pady=20,bg='#F5F5F5',borderwidth=10)
   selectframe.place(x=35, y=505)

   def displayrec():
      for record in bkdisplay.get_children():
         bkdisplay.delete(record)
      count=0
      for i in bk_rec:
         if clicked1.get()==i[3]:
            bkdisplay.insert(parent='', index='end', iid=count, text='',
                             values=(i[0], i[1], i[2], i[3], i[4], i[5]+'  '))
            count+=1
         
   def backtomenu():
      bkcatpage.destroy()
      Menuscreen()

   catoptions=[]
   f=open("files/BookRoughCopy.dat", 'rb')
   bk_rec=p.load(f)
   f.close()
   for i in bk_rec:
      if i[3] not in catoptions:
         catoptions.append(i[3])

   clicked1=StringVar()
   clicked1.set(r.choice(catoptions))

   catlabel=Label(selectframe, text='Select Category', bg='#F5F5F5',
                    font=('Helvetica','12'))
   catlabel.grid(row=0, column=0)
   
   catdrop=OptionMenu(selectframe, clicked1, *catoptions)
   catdrop.grid(row=0, column=1)

   space1=Label(selectframe, text='      ', bg='#F5F5F5')
   space2=Label(selectframe, text='      ', bg='#F5F5F5')
   space3=Label(selectframe, text='      ', bg='#F5F5F5')
   space4=Label(selectframe, text='      ', bg='#F5F5F5')
   space5=Label(selectframe, text='      ', bg='#F5F5F5')
   space1.grid(row=1, column=1)
   space2.grid(row=2, column=2)
   space3.grid(row=2, column=3)

   selectbutton = Button(selectframe, text='Display Book Details', fg='white', width=40, padx=10, borderwidth=7,
                    pady=3, bg='#1A2A29', font=('Calibri','16'), command=displayrec)
   selectbutton.grid(row=2, column=0, columnspan=2)
   
   backbutton = Button(selectframe, text='Back to Menu', fg='white', width=40, padx=10, borderwidth=7,
                    pady=3, bg='#1A2A29', font=('Calibri','16'), command=backtomenu)
   backbutton.grid(row=2, column=4)
   
   bkcatpage.mainloop()









#----- View by Author -----

def disaut():
   global bkautpage
   bkautpage = Tk()
   bkautpage.title('View by Author')
   bkautpage.geometry('1150x713')
   bkautpage.configure(bg = '#1A2A29')
   displayicon = PhotoImage(file = 'images/Listicon.png')
   bkautpage.iconphoto(False,displayicon)

   bkautframe=LabelFrame(bkautpage,padx=20,pady=20,bg='#F5F5F5',borderwidth=10)
   bkautframe.place(x=35, y=35)

   #creating a book details display as a box
   
   bkautscroll= Scrollbar(bkautframe)

   bkdisplay = ttk.Treeview(bkautframe, yscrollcommand=bkautscroll.set)

   bkautscroll.configure(command= bkdisplay.yview)

   style = ttk.Style()
   style.configure("Treeview.Heading", font=('Times New Roman', 11))
   style.configure('Treeview', rowheight=35)

   bkdisplay['columns'] = ('Book ID','Book Name','Book Author',
                           'Book Category','Status','Issued to')

   bkdisplay.column('#0', width=0, stretch=NO)
   bkdisplay.column('Book ID', anchor=E, width=100)
   bkdisplay.column('Book Name', anchor=E, width=200)
   bkdisplay.column('Book Author', anchor=E, width=200)
   bkdisplay.column('Book Category', anchor=E, width=200)
   bkdisplay.column('Status', anchor=E, width=100)
   bkdisplay.column('Issued to', anchor=E, width=200)

   bkdisplay.heading('#0', text='', anchor=E)
   bkdisplay.heading('Book ID', text='Book ID', anchor=E)
   bkdisplay.heading('Book Name', text='Book Name', anchor=E)
   bkdisplay.heading('Book Author', text='Book Author', anchor=E)
   bkdisplay.heading('Book Category', text='Book Category', anchor=E)
   bkdisplay.heading('Status', text='Status', anchor=E)
   bkdisplay.heading('Issued to', text='Issued to (Member ID)', anchor=E)

   bkautscroll.pack(side=RIGHT, fill=Y)
   bkdisplay.pack()

   # Creating frame for selecting Category

   selectframe=LabelFrame(bkautpage, padx=28,pady=20,bg='#F5F5F5',borderwidth=10)
   selectframe.place(x=35, y=505)

   def displayrec():
      for record in bkdisplay.get_children():
         bkdisplay.delete(record)
      count=0
      for i in bk_rec:
         if clicked1.get()==i[2]:
            bkdisplay.insert(parent='', index='end', iid=count, text='',
                             values=(i[0], i[1], i[2], i[3], i[4], i[5]+'  '))
            count+=1
         
   def backtomenu():
      bkautpage.destroy()
      Menuscreen()

   autoptions=[]
   f=open("files/BookRoughCopy.dat", 'rb')
   bk_rec=p.load(f)
   f.close()
   for i in bk_rec:
      if i[2] not in autoptions:
         autoptions.append(i[2])

   clicked1=StringVar()
   clicked1.set(r.choice(autoptions))

   autlabel=Label(selectframe, text='Select Author', bg='#F5F5F5',
                    font=('Helvetica','12'))
   autlabel.grid(row=0, column=0)
   
   autdrop=OptionMenu(selectframe, clicked1, *autoptions)
   autdrop.grid(row=0, column=1)

   space1=Label(selectframe, text='      ', bg='#F5F5F5')
   space2=Label(selectframe, text='      ', bg='#F5F5F5')
   space3=Label(selectframe, text='      ', bg='#F5F5F5')
   space4=Label(selectframe, text='      ', bg='#F5F5F5')
   space5=Label(selectframe, text='      ', bg='#F5F5F5')
   space1.grid(row=1, column=1)
   space2.grid(row=2, column=2)
   space3.grid(row=2, column=3)

   selectbutton = Button(selectframe, text='Display Book Details', fg='white', width=40, padx=10, borderwidth=7,
                    pady=3, bg='#1A2A29', font=('Calibri','16'), command=displayrec)
   selectbutton.grid(row=2, column=0, columnspan=2)
   
   backbutton = Button(selectframe, text='Back to Menu', fg='white', width=40, padx=10, borderwidth=7,
                    pady=3, bg='#1A2A29', font=('Calibri','16'), command=backtomenu)
   backbutton.grid(row=2, column=4)
   
   bkautpage.mainloop()









#----- View by Status ------

def disbkstat():
   global bkstatpage
   bkstatpage = Tk()
   bkstatpage.title('View by Status')
   bkstatpage.geometry('1150x713')
   bkstatpage.configure(bg = '#1A2A29')
   displayicon = PhotoImage(file = 'images/Listicon.png')
   bkstatpage.iconphoto(False,displayicon)

   bkstatframe=LabelFrame(bkstatpage,padx=20,pady=20,bg='#F5F5F5',borderwidth=10)
   bkstatframe.place(x=35, y=35)

   #creating a book details display as a box
   
   bkstatscroll= Scrollbar(bkstatframe)

   bkdisplay = ttk.Treeview(bkstatframe, yscrollcommand=bkstatscroll.set)

   bkstatscroll.configure(command= bkdisplay.yview)

   style = ttk.Style()
   style.configure("Treeview.Heading", font=('Times New Roman', 11))
   style.configure('Treeview', rowheight=35)

   bkdisplay['columns'] = ('Book ID','Book Name','Book Author',
                           'Book Category','Status','Issued to')

   bkdisplay.column('#0', width=0, stretch=NO)
   bkdisplay.column('Book ID', anchor=E, width=100)
   bkdisplay.column('Book Name', anchor=E, width=200)
   bkdisplay.column('Book Author', anchor=E, width=200)
   bkdisplay.column('Book Category', anchor=E, width=200)
   bkdisplay.column('Status', anchor=E, width=100)
   bkdisplay.column('Issued to', anchor=E, width=200)

   bkdisplay.heading('#0', text='', anchor=E)
   bkdisplay.heading('Book ID', text='Book ID', anchor=E)
   bkdisplay.heading('Book Name', text='Book Name', anchor=E)
   bkdisplay.heading('Book Author', text='Book Author', anchor=E)
   bkdisplay.heading('Book Category', text='Book Category', anchor=E)
   bkdisplay.heading('Status', text='Status', anchor=E)
   bkdisplay.heading('Issued to', text='Issued to (Member ID)', anchor=E)

   bkstatscroll.pack(side=RIGHT, fill=Y)
   bkdisplay.pack()

   # Creating frame for selecting Category

   selectframe=LabelFrame(bkstatpage, padx=28,pady=20,bg='#F5F5F5',borderwidth=10)
   selectframe.place(x=35, y=505)

   def displayrec():
      for record in bkdisplay.get_children():
         bkdisplay.delete(record)
      count=0
      for i in bk_rec:
         if clicked1.get()==i[4]:
            bkdisplay.insert(parent='', index='end', iid=count, text='',
                             values=(i[0], i[1], i[2], i[3], i[4], i[5]+'  '))
            count+=1
         
   def backtomenu():
      bkstatpage.destroy()
      Menuscreen()

   statoptions=[]
   f=open("files/BookRoughCopy.dat", 'rb')
   bk_rec=p.load(f)
   f.close()
   for i in bk_rec:
      if i[4] not in statoptions:
         statoptions.append(i[4])

   clicked1=StringVar()
   clicked1.set(r.choice(statoptions))

   statlabel=Label(selectframe, text='Select Status', bg='#F5F5F5',
                    font=('Helvetica','12'))
   statlabel.grid(row=0, column=0)
   
   statdrop=OptionMenu(selectframe, clicked1, *statoptions)
   statdrop.grid(row=0, column=1)

   space1=Label(selectframe, text='      ', bg='#F5F5F5')
   space2=Label(selectframe, text='      ', bg='#F5F5F5')
   space3=Label(selectframe, text='      ', bg='#F5F5F5')
   space4=Label(selectframe, text='      ', bg='#F5F5F5')
   space5=Label(selectframe, text='      ', bg='#F5F5F5')
   space1.grid(row=1, column=1)
   space2.grid(row=2, column=2)
   space3.grid(row=2, column=3)

   selectbutton = Button(selectframe, text='Display Book Details', fg='white', width=40, padx=10, borderwidth=7,
                    pady=3, bg='#1A2A29', font=('Calibri','16'), command=displayrec)
   selectbutton.grid(row=2, column=0, columnspan=2)
   
   backbutton = Button(selectframe, text='Back to Menu', fg='white', width=40, padx=10, borderwidth=7,
                    pady=3, bg='#1A2A29', font=('Calibri','16'), command=backtomenu)
   backbutton.grid(row=2, column=4)
   
   bkstatpage.mainloop()










#----- Issue Book -----

def issuebook():
   global bkisspage
   bkisspage = Tk()
   bkisspage.title('Issue Book')
   bkisspage.geometry('767x500')
   bkisspage.configure(bg = '#1A2A29')
   additionicon = PhotoImage(file = 'images/Addicon.png')
   bkisspage.iconphoto(False,additionicon)
   
   def issue_click():
      b_id = (e1.get()).upper()
      mem_id = (e2.get()).upper()
      
      f1 = open("files/BookRoughCopy.dat", 'rb+')
      f2 = open("files/MemberRoughCopy.dat", 'rb+')
      
      bk_rec = p.load(f1)
      mem_rec = p.load(f2)
      book_ids = [i[0] for i in bk_rec]
      member_ids = [i[0] for i in mem_rec]
      
      if b_id == '' or mem_id == '':
         messagebox.showwarning("Error", "Field Empty Input Not Valid")
      elif b_id not in book_ids:
         messagebox.showwarning("Error", "Book with this Id does not exist")
      elif mem_id not in member_ids:
         messagebox.showwarning("Error", "Member with this Id does not exist")
      else:
         for i in bk_rec:
            if b_id==i[0]:
               if i[4]=='ISSUED':
                  messagebox.showwarning("Error", "Book already Issued. Not Available")
               else:
                  for j in mem_rec:
                     if mem_id==j[0]:
                        if j[4]=='BORROWED':
                           messagebox.showwarning("Error",
                                                  "Member has already borrowed a book")
                        else:
                           i[4]='ISSUED'
                           j[4]='BORROWED'
                           i[5]=mem_id
                           j[5]=b_id
                           messagebox.showinfo("Issue Success", "Book Issued Successfully")

         f1.truncate(0)
         f1.seek(0)
         f2.truncate(0)
         f2.seek(0)
         p.dump(bk_rec, f1)
         p.dump(mem_rec, f2)
         f1.close()
         f2.close()
         e1.delete(0, END)
         e2.delete(0, END)
                                        
   def backtomenu():
      bkisspage.destroy()
      Menuscreen()

   #labels, entries and buttons
      
   issueframe = LabelFrame(bkisspage, padx=100, pady=50, bg='#F5F5F5', borderwidth=10)
   issueframe.place(x=35, y=35)

   issuelabel = Label(issueframe, text='ENTER BOOK ID & MEMBER ID', bg='#F5F5F5',
                    font=('Times New Roman','15'))
   issuelabel.grid(row=0, column=1, columnspan=3)

   bidlabel = Label(issueframe, text='Book ID', bg='#F5F5F5', font=('Helvetica','12'))
   memidlabel = Label(issueframe, text='Member ID', bg='#F5F5F5', font=('Helvetica','12'))
   bidlabel.grid(row=2, column=1, columnspan=2, sticky=W)
   memidlabel.grid(row=3, column=1, columnspan=2, sticky=W)

   e1 = Entry(issueframe, width=35, borderwidth=2, font=('Helvetica','12'))
   e2 = Entry(issueframe, width=35, borderwidth=2, font=('Helvetica','12'))
   e1.grid(row=2, column=3, sticky=E)
   e2.grid(row=3, column=3, sticky=E)

   space1 = Label(issueframe, text='      ', bg='#F5F5F5')
   space2 = Label(issueframe, text='      ', bg='#F5F5F5')
   space3 = Label(issueframe, text='      ', bg='#F5F5F5')
   space4 = Label(issueframe, text='      ', bg='#F5F5F5')
   space1.grid(row=1, column=1)
   space2.grid(row=4, column=1)
   space3.grid(row=5, column=1)
   space4.grid(row=7, column=1)
   
   issuebutton = Button(issueframe, text='Issue Book', fg='white', width=40, padx=10, borderwidth=7,
                    pady=10, bg='#1A2A29', font=('Calibri','16'), command = issue_click)
   issuebutton.grid(row=6, column=1, columnspan=3)

   backbutton = Button(issueframe, text='Back to Menu', fg='white', width=40, padx=10, borderwidth=7,
                    pady=10, bg='#1A2A29', font=('Calibri','16'), command = backtomenu)
   backbutton.grid(row = 8, column=1, columnspan=3)
   
   bkisspage.mainloop()









#----- Return Book -----

def returnbook():
   global bkretpage
   bkretpage = Tk()
   bkretpage.title('Return Book')
   bkretpage.geometry('767x475')
   bkretpage.configure(bg = '#1A2A29')
   additionicon = PhotoImage(file = 'images/Addicon.png')
   bkretpage.iconphoto(False,additionicon)
   
   def return_click():
      b_id = (e1.get()).upper()
      
      f1 = open("files/BookRoughCopy.dat", 'rb+')
      f2 = open("files/MemberRoughCopy.dat", 'rb+')
      
      bk_rec = p.load(f1)
      mem_rec = p.load(f2)
      book_ids = [i[0] for i in bk_rec]
      
      if b_id == '' :
         messagebox.showwarning("Error", "Field Empty Input Not Valid")
      elif b_id not in book_ids:
         messagebox.showwarning("Error", "Book with this Id does not exist")
         e1.delete(0, END)
      else:
         for i in bk_rec:
            if b_id==i[0]:
               if i[4]=='AVAILABLE':
                  messagebox.showwarning("Error", "Book has not been issued")
               else:
                  mem_id=i[5]
                  for j in mem_rec:
                     if mem_id==j[0]:
                        i[4]='AVAILABLE'
                        j[4]='RETURNED'
                        i[5]='-'
                        j[5]='-'
                        messagebox.showinfo("Return Success", "Book Returned Successfully")

         f1.truncate(0)
         f1.seek(0)
         f2.truncate(0)
         f2.seek(0)
         p.dump(bk_rec, f1)
         p.dump(mem_rec, f2)
         f1.close()
         f2.close()
         e1.delete(0, END)            
                   
   def backtomenu():
      bkretpage.destroy()
      Menuscreen()

   #labels, entries and buttons
      
   returnframe = LabelFrame(bkretpage, padx=100, pady=50, bg='#F5F5F5', borderwidth=10)
   returnframe.place(x=35, y=35)

   returnlabel = Label(returnframe, text='ENTER BOOK ID', bg='#F5F5F5',
                    font=('Times New Roman','15'))
   returnlabel.grid(row=0, column=1, columnspan=3)

   bidlabel = Label(returnframe, text='Book ID', bg='#F5F5F5', font=('Helvetica','12'))
   bidlabel.grid(row=2, column=1, columnspan=2, sticky=W)

   e1 = Entry(returnframe, width=35, borderwidth=2, font=('Helvetica','12'))
   e1.grid(row=2, column=3, sticky=E)

   space1 = Label(returnframe, text='      ', bg='#F5F5F5')
   space2 = Label(returnframe, text='      ', bg='#F5F5F5')
   space3 = Label(returnframe, text='      ', bg='#F5F5F5')
   space4 = Label(returnframe, text='      ', bg='#F5F5F5')
   space1.grid(row=1, column=1)
   space2.grid(row=3, column=1)
   space3.grid(row=4, column=1)
   space4.grid(row=6, column=1)
   
   returnbutton = Button(returnframe, text='Return Book', fg='white', width=40, padx=10, borderwidth=7,
                    pady=10, bg='#1A2A29', font=('Calibri','16'), command = return_click)
   returnbutton.grid(row=5, column=1, columnspan=3)

   backbutton = Button(returnframe, text='Back to Menu', fg='white', width=40, padx=10, borderwidth=7,
                    pady=10, bg='#1A2A29', font=('Calibri','16'), command = backtomenu)
   backbutton.grid(row = 7, column=1, columnspan=3)
   
   bkretpage.mainloop()









#----- Add Member -----

def addmember():
   global memaddpage
   memaddpage = Tk()
   memaddpage.title('Add Member')
   memaddpage.geometry('767x548')
   memaddpage.configure(bg = '#1A2A29')
   additionicon = PhotoImage(file = 'images/Addicon.png')
   memaddpage.iconphoto(False,additionicon)
   
   def add_click():
      mem_id = (e1.get()).upper()
      memname = (e2.get()).upper()
      phno = e3.get()
      email = e4.get()
      record = [mem_id, memname, phno, email, 'RETURNED', '-']
      f = open("files/MemberRoughCopy.dat", 'rb+')
      mem_rec = p.load(f)
      member_ids = [i[0] for i in mem_rec]
      member_names = [i[1] for i in mem_rec]
      if '' in record:
         messagebox.showwarning("Error", "Field Empty Input Not Valid")
      elif mem_id in member_ids:
         messagebox.showwarning("Error", "Member with same Id already exists")
      elif memname in member_names:
         messagebox.showwarning("Error", "Member with same name already exists")
      else:
         mem_rec.insert(r.randrange(len(mem_rec)),record)
         f.truncate(0)
         f.seek(0)
         p.dump(mem_rec, f)
         messagebox.showinfo("Addition Success", "Member Added")
         f.close()
         e1.delete(0, END)
         e2.delete(0, END)
         e3.delete(0, END)
         e4.delete(0, END)

   def backtomenu():
      memaddpage.destroy()
      Menuscreen()

   #labels, entries and buttons
      
   addframe = LabelFrame(memaddpage, padx=100, pady=50, bg='#F5F5F5', borderwidth=10)
   addframe.place(x=35, y=35)

   addlabel = Label(addframe, text='ENTER MEMBER DETAILS', bg='#F5F5F5',
                    font=('Times New Roman','15'))
   addlabel.grid(row=0, column=1, columnspan=3)

   idlabel = Label(addframe, text='Member ID', bg='#F5F5F5', font=('Helvetica','12'))
   namelabel = Label(addframe, text='Member Name', bg='#F5F5F5', font=('Helvetica','12'))
   phnolabel = Label(addframe, text='Phone No', bg='#F5F5F5', font=('Helvetica','12'))
   emaillabel = Label(addframe, text='Email', bg='#F5F5F5', font=('Helvetica','12'))
   idlabel.grid(row=2, column=1, columnspan=2, sticky=W)
   namelabel.grid(row=3, column=1, columnspan=2, sticky=W)
   phnolabel.grid(row=4, column=1, columnspan=2, sticky=W)
   emaillabel.grid(row=5, column=1, columnspan=2, sticky=W)

   e1 = Entry(addframe, width=35, borderwidth=2, font=('Helvetica','12'))
   e2 = Entry(addframe, width=35, borderwidth=2, font=('Helvetica','12'))
   e3 = Entry(addframe, width=35, borderwidth=2, font=('Helvetica','12'))
   e4 = Entry(addframe, width=35, borderwidth=2, font=('Helvetica','12'))
   e1.grid(row=2, column=3, sticky=E)
   e2.grid(row=3, column=3, sticky=E)
   e3.grid(row=4, column=3, sticky=E)
   e4.grid(row=5, column=3, sticky=E)

   space1 = Label(addframe, text='      ', bg='#F5F5F5')
   space2 = Label(addframe, text='      ', bg='#F5F5F5')
   space3 = Label(addframe, text='      ', bg='#F5F5F5')
   space4 = Label(addframe, text='      ', bg='#F5F5F5')
   space1.grid(row=1, column=1)
   space2.grid(row=6, column=1)
   space3.grid(row=7, column=1)
   space4.grid(row=9, column=1)
   
   addbutton = Button(addframe, text='Add Member', fg='white', width=40, padx=10, borderwidth=7,
                    pady=10, bg='#1A2A29', font=('Calibri','16'), command = add_click)
   addbutton.grid(row=8, column=1, columnspan=3)

   backbutton = Button(addframe, text='Back to Menu', fg='white', width=40, padx=10, borderwidth=7,
                    pady=10, bg='#1A2A29', font=('Calibri','16'), command = backtomenu)
   backbutton.grid(row = 10, column=1, columnspan=3)
   
   memaddpage.mainloop()









#----- Delete Member -----

def delmember():
   global memdelpage
   memdelpage = Tk()
   memdelpage.title('Delete Member')
   memdelpage.geometry('768x478')
   memdelpage.configure(bg='#1A2A29')
   deleteicon = PhotoImage(file = 'images/Delicon.png')
   memdelpage.iconphoto(False,deleteicon)
   
   def del_click():
      mem_id = (e1.get()).upper()
      f = open("files/MemberRoughCopy.dat",'rb+')
      mem_rec = p.load(f)
      member_ids = [i[0] for i in mem_rec]
      if mem_id == '':
         messagebox.showwarning("Error","Field Empty Input Not Valid")
         e1.delete(0,END)
      elif mem_id not in member_ids:
         messagebox.showwarning("Error","Member with this Id does not exist. Cannot delete")
         e1.delete(0,END)
      else:
         for i in mem_rec:
            if mem_id==i[0]:
               mem_rec.remove(i)
         f.truncate(0)
         f.seek(0)
         p.dump(mem_rec,f)
         messagebox.showinfo("Deletion Success","Book Deleted")
         f.close()
         e1.delete(0,END)

   def backtomenu():
      memdelpage.destroy()
      Menuscreen()

   #labels, entries and buttons
      
   delframe = LabelFrame(memdelpage,padx=100,pady=50,bg='#F5F5F5',borderwidth=10)
   delframe.place(x=35, y=35)

   dellabel = Label(delframe, text='ENTER MEMBER ID', bg='#F5F5F5',
                    font=('Times New Roman','15'))
   dellabel.grid(row=0, column=1, columnspan=3)

   idlabel = Label(delframe, text='Member ID', bg='#F5F5F5', font=('Helvetica','12'))
   idlabel.grid(row=2, column=1, columnspan=2, sticky='W')

   e1 = Entry(delframe, width=35, borderwidth=2, font=('Helvetica','12'))
   e1.grid(row=2,column=3, sticky='E')

   space1 = Label(delframe, text='      ', bg='#F5F5F5')
   space2 = Label(delframe, text='      ', bg='#F5F5F5')
   space3 = Label(delframe, text='      ', bg='#F5F5F5')
   space4 = Label(delframe, text='      ', bg='#F5F5F5')
   space1.grid(row=1, column=1)
   space2.grid(row=6, column=1)
   space3.grid(row=7, column=1)
   space4.grid(row=9, column=1)
   
   delbutton = Button(delframe, text='Delete Member', fg='white', width=40, padx=10, borderwidth=7,
                    pady=10, bg='#1A2A29', font=('Calibri','16'), command=del_click)
   delbutton.grid(row=8,column=1, columnspan=3)

   backbutton = Button(delframe, text='Back to Menu', fg='white', width=40, padx=10, borderwidth=7,
                    pady=10, bg='#1A2A29', font=('Calibri','16'), command=backtomenu)
   backbutton.grid(row=10,column=1, columnspan=3)
   
   memdelpage.mainloop()









#----- View All Member Details -----

def viewmember():
   global memdispage
   memdispage = Tk()
   memdispage.title('Display All Member Details')
   memdispage.geometry('1150x660')
   memdispage.configure(bg = '#1A2A29')
   displayicon = PhotoImage(file = 'images/Listicon.png')
   memdispage.iconphoto(False,displayicon)

   memdisframe=LabelFrame(memdispage,padx=20,pady=20,bg='#F5F5F5',borderwidth=10)
   memdisframe.place(x=35, y=35)

   #creating a book details display as a box
   
   memdisscroll = Scrollbar(memdisframe)

   memdisplay = ttk.Treeview(memdisframe, yscrollcommand=memdisscroll.set)

   memdisscroll.configure(command= memdisplay.yview)

   style = ttk.Style()
   style.configure("Treeview.Heading", font=('Times New Roman', 11))
   style.configure('Treeview', rowheight=35)

   memdisplay['columns'] = ('Member ID','Member Name','Phone No',
                           'Email','Status','Book Issued')

   memdisplay.column('#0', width=0, stretch=NO)
   memdisplay.column('Member ID', anchor=E, width=100)
   memdisplay.column('Member Name', anchor=E, width=200)
   memdisplay.column('Phone No', anchor=E, width=200)
   memdisplay.column('Email', anchor=E, width=200)
   memdisplay.column('Status', anchor=E, width=100)
   memdisplay.column('Book Issued', anchor=E, width=200)

   memdisplay.heading('#0', text='', anchor=E)
   memdisplay.heading('Member ID', text='Member ID', anchor=E)
   memdisplay.heading('Member Name', text='Member Name', anchor=E)
   memdisplay.heading('Phone No', text='Phone No', anchor=E)
   memdisplay.heading('Email', text='Email', anchor=E)
   memdisplay.heading('Status', text='Status', anchor=E)
   memdisplay.heading('Book Issued', text='Book Issued (Book ID)', anchor=E)

   memdisscroll.pack(side=RIGHT, fill=Y)
   memdisplay.pack()

   #taking the records from binary file and displaying them
   
   backmnframe=LabelFrame(memdispage, padx=291, pady=20, bg='#F5F5F5', borderwidth=10)
   backmnframe.place(x=35, y=505)

   f = open("files/MemberRoughCopy.dat", 'rb')
   mem_rec = p.load(f)
   count=0
   for i in mem_rec:
      memdisplay.insert(parent='', index='end', iid=count, text='',
                             values=(i[0], i[1], i[2], i[3], i[4], i[5]+'  '))
      count+=1

   f.close()

   def backtomenu():
      memdispage.destroy()
      Menuscreen()

   backbutton = Button(backmnframe, text='Back to Menu', fg='white', width=40, padx=10, borderwidth=7,
                    pady=3, bg='#1A2A29', font=('Calibri','16'), command=backtomenu)
   backbutton.grid(row=0, column=0)
   
   memdispage.mainloop()









#----- Search by Membership No. -----

def searchmember():
   global memsearchpage
   memsearchpage = Tk()
   memsearchpage.title('Search by Book No.')
   memsearchpage.geometry('1150x713')
   memsearchpage.configure(bg = '#1A2A29')
   displayicon = PhotoImage(file = 'images/Listicon.png')
   memsearchpage.iconphoto(False,displayicon)

   memsearchframe=LabelFrame(memsearchpage,padx=20,pady=20,bg='#F5F5F5',borderwidth=10)
   memsearchframe.place(x=35, y=35)

   #creating a book details display as a box
   
   memdisscroll = Scrollbar(memsearchframe)

   memdisplay = ttk.Treeview(memsearchframe, yscrollcommand=memdisscroll.set)

   memdisscroll.configure(command= memdisplay.yview)

   style = ttk.Style()
   style.configure("Treeview.Heading", font=('Times New Roman', 11))
   style.configure('Treeview', rowheight=35)

   memdisplay['columns'] = ('Member ID','Member Name','Phone No',
                           'Email','Status','Book Issued')

   memdisplay.column('#0', width=0, stretch=NO)
   memdisplay.column('Member ID', anchor=E, width=100)
   memdisplay.column('Member Name', anchor=E, width=200)
   memdisplay.column('Phone No', anchor=E, width=200)
   memdisplay.column('Email', anchor=E, width=200)
   memdisplay.column('Status', anchor=E, width=100)
   memdisplay.column('Book Issued', anchor=E, width=200)

   memdisplay.heading('#0', text='', anchor=E)
   memdisplay.heading('Member ID', text='Member ID', anchor=E)
   memdisplay.heading('Member Name', text='Member Name', anchor=E)
   memdisplay.heading('Phone No', text='Phone No', anchor=E)
   memdisplay.heading('Email', text='Email', anchor=E)
   memdisplay.heading('Status', text='Status', anchor=E)
   memdisplay.heading('Book Issued', text='Book Issued (Book ID)', anchor=E)

   memdisscroll.pack(side=RIGHT, fill=Y)
   memdisplay.pack()

   #taking the records from binary file and displaying them
   
   selectframe=LabelFrame(memsearchpage, padx=28,pady=20,bg='#F5F5F5',borderwidth=10)
   selectframe.place(x=35, y=505)

   def displayrec():
      f=open("files/MemberRoughCopy.dat", 'rb')
      mem_rec=p.load(f)
      f.close()
      member_ids = [i[0] for i in mem_rec]
      mem_id = searchent.get()
      
      if mem_id == '':
         messagebox.showwarning("Error", "Field Empty Input Not Valid")
         searchent.delete(0, END)
      elif mem_id not in member_ids:
         messagebox.showwarning("Error", "Member with this Id does not exist")
         searchent.delete(0, END)
         
      else:
         for record in memdisplay.get_children():
            memdisplay.delete(record)
         count=0
         for i in mem_rec:
            if mem_id ==i[0]:
               memdisplay.insert(parent='', index='end', iid=count, text='',
                             values=(i[0], i[1], i[2], i[3], i[4], i[5]+'  '))
               count+=1
         searchent.delete(0, END)
         
   def backtomenu():
      memsearchpage.destroy()
      Menuscreen()

   searchlabel=Label(selectframe, text='Enter Member ID', bg='#F5F5F5',
                    font=('Helvetica','12'))
   searchlabel.grid(row=0, column=0)
   
   searchent = Entry(selectframe, width=35, borderwidth=2, font=('Helvetica','12'))
   searchent.grid(row=0, column=1, columnspan=2)
   
   space1=Label(selectframe, text='      ', bg='#F5F5F5')
   space2=Label(selectframe, text='      ', bg='#F5F5F5')
   space3=Label(selectframe, text='      ', bg='#F5F5F5')
   space1.grid(row=1, column=1)
   space2.grid(row=2, column=2)
   space3.grid(row=2, column=3)

   selectbutton = Button(selectframe, text='Display Member Details', fg='white', width=40, padx=10, borderwidth=7,
                    pady=3, bg='#1A2A29', font=('Calibri','16'), command=displayrec)
   selectbutton.grid(row=2, column=0, columnspan=2)
   
   backbutton = Button(selectframe, text='Back to Menu', fg='white', width=40, padx=10, borderwidth=7,
                    pady=3, bg='#1A2A29', font=('Calibri','16'), command=backtomenu)
   backbutton.grid(row=2, column=4)
   
   memsearchpage.mainloop()










#----- View Members who have borrowed a book -----

def viewmemstat():
   global memstatpage
   memstatpage = Tk()
   memstatpage.title('View by Status')
   memstatpage.geometry('1150x713')
   memstatpage.configure(bg = '#1A2A29')
   displayicon = PhotoImage(file = 'images/Listicon.png')
   memstatpage.iconphoto(False,displayicon)

   memstatframe=LabelFrame(memstatpage,padx=20,pady=20,bg='#F5F5F5',borderwidth=10)
   memstatframe.place(x=35, y=35)

   #creating a book details display as a box
   
   memstatscroll= Scrollbar(memstatframe)

   memdisplay = ttk.Treeview(memstatframe, yscrollcommand=memstatscroll.set)

   memstatscroll.configure(command= memdisplay.yview)

   style = ttk.Style()
   style.configure("Treeview.Heading", font=('Times New Roman', 11))
   style.configure('Treeview', rowheight=35)

   memdisplay['columns'] = ('Member ID','Member Name','Phone No',
                           'Email','Status','Book Issued')

   memdisplay.column('#0', width=0, stretch=NO)
   memdisplay.column('Member ID', anchor=E, width=100)
   memdisplay.column('Member Name', anchor=E, width=200)
   memdisplay.column('Phone No', anchor=E, width=200)
   memdisplay.column('Email', anchor=E, width=200)
   memdisplay.column('Status', anchor=E, width=100)
   memdisplay.column('Book Issued', anchor=E, width=200)

   memdisplay.heading('#0', text='', anchor=E)
   memdisplay.heading('Member ID', text='Member ID', anchor=E)
   memdisplay.heading('Member Name', text='Member Name', anchor=E)
   memdisplay.heading('Phone No', text='Phone No', anchor=E)
   memdisplay.heading('Email', text='Email', anchor=E)
   memdisplay.heading('Status', text='Status', anchor=E)
   memdisplay.heading('Book Issued', text='Book Issued (Book ID)', anchor=E)

   memstatscroll.pack(side=RIGHT, fill=Y)
   memdisplay.pack()

   # Creating frame for selecting Category

   selectframe=LabelFrame(memstatpage, padx=28,pady=20,bg='#F5F5F5',borderwidth=10)
   selectframe.place(x=35, y=505)

   def displayrec():
      for record in memdisplay.get_children():
         memdisplay.delete(record)
      count=0
      for i in st_rec:
         if clicked1.get()==i[4]:
            memdisplay.insert(parent='', index='end', iid=count, text='',
                             values=(i[0], i[1], i[2], i[3], i[4], i[5]+'  '))
            count+=1
         
   def backtomenu():
      memstatpage.destroy()
      Menuscreen()

   statoptions=[]
   f=open("files/MemberRoughCopy.dat", 'rb')
   st_rec=p.load(f)
   f.close()
   for i in st_rec:
      if i[4] not in statoptions:
         statoptions.append(i[4])

   clicked1=StringVar()
   clicked1.set(r.choice(statoptions))

   statlabel=Label(selectframe, text='Select Status', bg='#F5F5F5',
                    font=('Helvetica','12'))
   statlabel.grid(row=0, column=0)
   
   statdrop=OptionMenu(selectframe, clicked1, *statoptions)
   statdrop.grid(row=0, column=1)

   space1=Label(selectframe, text='      ', bg='#F5F5F5')
   space2=Label(selectframe, text='      ', bg='#F5F5F5')
   space3=Label(selectframe, text='      ', bg='#F5F5F5')
   space4=Label(selectframe, text='      ', bg='#F5F5F5')
   space5=Label(selectframe, text='      ', bg='#F5F5F5')
   space1.grid(row=1, column=1)
   space2.grid(row=2, column=2)
   space3.grid(row=2, column=3)

   selectbutton = Button(selectframe, text='Display Member Details', fg='white', width=40, padx=10, borderwidth=7,
                    pady=3, bg='#1A2A29', font=('Calibri','16'), command=displayrec)
   selectbutton.grid(row=2, column=0, columnspan=2)
   
   backbutton = Button(selectframe, text='Back to Menu', fg='white', width=40, padx=10, borderwidth=7,
                    pady=3, bg='#1A2A29', font=('Calibri','16'), command=backtomenu)
   backbutton.grid(row=2, column=4)
   
   memstatpage.mainloop()










#----------------------------- Login and Menu ------------------------------

#----- Menu -----

def Menuscreen():
   global menu
   menu=Tk()
   menu.title("Local Library")
   menu.geometry('1390x710')
   menuicon=PhotoImage(file='images/Libico.png')
   menu.iconphoto(False,menuicon)

   #background
   bgimg=PhotoImage(file='images/LibraryBG.png')
   bgcanvas=Canvas(menu, width=1390, height=710)
   bgcanvas.pack(fill="both", expand=True)
   bgcanvas.create_image(0,0, image=bgimg, anchor='nw')

   def bookexecute():
      option=clicked1.get()
      if option=='Add New Book':
         menu.destroy()
         addbook()
         
      elif option=='Delete Book':
         menu.destroy()
         delbook()
         
      elif option=='Display All Book Details':
         menu.destroy()
         disbook()
         
      elif option=='Search by Book ID':
         menu.destroy()
         searchbook()
         
      elif option=='View by Category':
         menu.destroy()
         discat()
         
      elif option=='View by Author':
         menu.destroy()
         disaut()
         
      elif option=='View by Status':
         menu.destroy()
         disbkstat()
         
      elif option=='Issue Book':
         menu.destroy()
         issuebook()
         
      elif option=='Return Book':
         menu.destroy()
         returnbook()
            
   def memberexecute():
      option=clicked2.get()
      if option=='Add Member':
         menu.destroy()
         addmember()
         
      elif option=='Delete Member':
         menu.destroy()
         delmember()
         
      elif option=='View All Member Details':
         menu.destroy()
         viewmember()
         
      elif option=='Search by Member ID':
         menu.destroy()
         searchmember()
         
      elif option=='View by Status':
         menu.destroy()
         viewmemstat()

   #Available options in both drop-down menus
   
   bookoptions=['Add New Book',
                'Delete Book',
                'Display All Book Details',
                'Search by Book ID',
                'View by Category',
                'View by Author',
                'View by Status',
                'Issue Book',
                'Return Book']

   memberoptions=['Add Member',
                  'Delete Member',
                  'View All Member Details',
                  'Search by Member ID',
                  'View by Status']

   clicked1 = StringVar()
   clicked1.set('Display All Book Details')
   clicked2 = StringVar()
   clicked2.set('View All Member Details')

   #drop-down menus and buttons
                
   bookdrop=OptionMenu(menu, clicked1, *bookoptions)
   memberdrop=OptionMenu(menu, clicked2, *memberoptions)

   bgcanvas.create_window(100, 300, window=bookdrop, anchor='nw')
   bgcanvas.create_window(500, 300, window=memberdrop, anchor='nw')

   bkexecute=Button(menu, text='Execute Command', padx=10,
                    pady=10, command=bookexecute)
   mbexecute=Button(menu, text='Execute Command', padx=10,
                    pady=10, command=memberexecute)
   
   bgcanvas.create_window(100, 500, window=bkexecute, anchor='nw')
   bgcanvas.create_window(500, 500, window=mbexecute, anchor='nw')
   
   menu.mainloop()









#----- Login -----
   
def Loginscreen():
   log=Tk()
   log.title('Login')
   log.geometry('1030x483')
   log.configure(bg='#1A2A29')
   loginicon=PhotoImage(file='images/Lockico.png')
   log.iconphoto(False,loginicon)

   logframe=LabelFrame(log,padx=100,pady=75,bg='#F5F5F5',borderwidth=10)
   logframe.place(x=35, y=35)

   #login conditions
   
   def log_click():
      username=e1.get()
      password=e2.get()
      if username=='030115':
         if password=='030115':
            log.destroy()
            Menuscreen()
         else:
            messagebox.showwarning("Login Error","Invalid Username and Password")
            e1.delete(0,END)
            e2.delete(0,END)
            
    
      else:
         messagebox.showwarning("Login Error","Invalid Username and Password")
         e1.delete(0,END)
         e2.delete(0,END)

   #labels, entries and buttons
         
   loginlabel=Label(logframe, text='ADMIN LOGIN', bg='#F5F5F5',
                    font=('Times New Roman','15'))
   loginlabel.grid(row=0, column=2, columnspan=2)
   
   adphoto=PhotoImage(file='images/Admin.png')
   adminphoto=Label(logframe, image=adphoto, borderwidth=0)
   adminphoto.grid(row=0, column=0, rowspan=7)
   
   userlabel=Label(logframe, text='Username', bg='#F5F5F5', font=('Helvetica','12'))
   passlabel=Label(logframe, text='Password', bg='#F5F5F5', font=('Helvetica','12'))
   userlabel.grid(row=2, column=2, sticky=W)
   passlabel.grid(row=3, column=2, sticky=W)

   e1=Entry(logframe, width=35, borderwidth=2, font=('Helvetica','12'))
   e2=Entry(logframe, show='*', width=35, borderwidth=2, font=('Helvetica','12'))
   e1.grid(row=2,column=3, sticky=E)
   e2.grid(row=3,column=3, sticky=E)

   space1=Label(logframe, text='      ', bg='#F5F5F5')
   space2=Label(logframe, text='      ', bg='#F5F5F5')
   space3=Label(logframe, text='      ', bg='#F5F5F5')
   space4=Label(logframe, text='      ', bg='#F5F5F5')
   space5=Label(logframe, text='      ', bg='#F5F5F5')
   space1.grid(row=2, column=1)
   space2.grid(row=3, column=1)
   space3.grid(row=1, column=2)
   space4.grid(row=4, column=2)
   space5.grid(row=5, column=2)
   
   logbutton=Button(logframe, text='Log In', fg='white', width=40, padx=10, borderwidth=7,
                    pady=10, bg='#1A2A29', font=('Calibri','16'), command=log_click)
   logbutton.grid(row=6,column=2, columnspan=2)

   log.mainloop()

Loginscreen()

