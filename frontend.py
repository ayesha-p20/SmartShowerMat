#GUI
from tkinter import *
from tkinter import ttk
from database import *

#add threshold
def createBioObj(age, height, weight):
    bioObj = {
        'age': age,
        'height': height,
        'weight': weight
        }
    
    return bioObj

def createUserObj(fname, lname, phone, email, ename, relation, ephone, eemail):
    userObj = {
    'fname':fname,
    'lname':lname,
    'phone':phone,
    'email':email,
    'eContactName': ename,
    'relation': relation,
    'eContactPhone': ephone,
    'eContactEmail': eemail
    }
    return userObj

    

def onClickSubmit(config, age, height, weight):
    print("Submitted!")

    #create an object for biometric info
    bioObj = createBioObj(age,height,weight)

    #store biometric data in db
    bio_instance = writeBiometrics(bioObj)
    readBiometrics(bioInstance)

    
    #frame to print prompt to stand on mat
    frame_threshold = ttk.Frame(config, width =100)
    frame_threshold.columnconfigure(0,weight=1)
    frame_threshold.grid(row=2,column=0)

    #label
    label_threshold = Label(frame_threshold, text = "Please stand on the mat for initial pressure reading")

    #placing label
    label_threshold.grid(row = 0, column = 0, pady = 25, padx = 5, sticky='NSEW')

def onClickNext(fname, lname, phone, email, ename, relation, ephone, eemail):
    print("Clicked!")

    #create an object to store in db
    userObj = createUserObj(fname, lname, phone, email, ename, relation, ephone, eemail)

    #write to db
    writeUser(userObj)

    #create pop up window
    config = Toplevel()
    config.title("Smart Shower Mat - Initial Configuration")
    config.resizable(0,0)
    
    # upper frame
    frame_text = ttk.Frame(config) 
    frame_text.columnconfigure(0,weight=1)
    frame_text.grid(row=0,column=0)

    #labels
    label_age = Label(frame_text, text = "Age")
    label_height = Label(frame_text, text = "Height (inches)")
    label_weight = Label(frame_text, text = "Weight (pounds)")

    #placing labels
    label_age.grid(row = 0,column = 0,pady = 15, padx = 5, sticky='NSEW')
    label_height.grid(row = 0,column = 1,pady = 15, padx = 5, sticky='NSEW')
    label_weight.grid(row = 0,column = 2,pady = 15, padx = 5, sticky='NSEW')

    #text entry boxes
    entry_age = Entry(frame_text, width = 25)
    entry_height = Entry(frame_text, width = 25)
    entry_weight = Entry(frame_text, width = 25)

    #placing entry boxes
    entry_age.grid(row = 1,column = 0, padx = 5, sticky='W')
    entry_height.grid(row = 1,column = 1, padx = 5, sticky='W')
    entry_weight.grid(row = 1,column = 2, padx = 5, sticky='W')

    #button frame
    frame_btnSubmit = ttk.Frame(config)
    frame_btnSubmit.columnconfigure(0,weight=1)
    frame_btnSubmit.grid(row=1,column=0)

    #button
    btn_submit = Button(frame_btnSubmit, text = "Submit", width = 10, command=lambda: [onClickSubmit(config,entry_age.get(),entry_height.get(),entry_weight.get())])
    btn_submit .grid(row = 0, column = 0, pady = 15,  sticky = 'E')

def mainWin():
    root = Tk()
    root.title("Smart Shower Mat - User Details")

    pc_width = root.winfo_screenwidth()
    pc_height = root.winfo_screenheight() 
    #root.geometry("%dx%d"%(pc_width,pc_height))
    root.resizable(0,0)

    #left frame
    frame_labels = ttk.Frame(root)
    frame_labels.columnconfigure(0,weight=1)
    frame_labels.grid(row=0,column=0)

    #labels
    label_fname = Label(frame_labels, text = "First Name")
    label_lname = Label(frame_labels, text = "Last Name")
    label_phone = Label(frame_labels, text = "Phone")
    label_email = Label(frame_labels, text = "Email")
    label_ename = Label(frame_labels, text = "Emergency Contact Name")
    label_relation = Label(frame_labels, text = "Contact's Relation to User")
    label_eemail = Label(frame_labels, text = "Contact Email")
    label_ephone = Label(frame_labels, text = "Contact Phone")

    #placing labels
    label_fname.grid(row = 0, column = 0, pady = 7, padx = 5, sticky='W')
    label_lname.grid(row = 1, column = 0, pady = 7, padx = 5, sticky='W')
    label_phone.grid(row = 2, column = 0, pady = 7, padx = 5, sticky='W')
    label_email.grid(row = 3, column = 0, pady = 7, padx = 5, sticky='W')
    label_ename.grid(row = 4, column = 0, pady = 7, padx = 5, sticky='W')
    label_relation.grid(row = 5, column = 0, pady = 7, padx = 5, sticky='W')
    label_ephone.grid(row = 6, column = 0, pady = 7, padx = 5, sticky='W')
    label_eemail.grid(row = 7, column = 0, pady = 7, padx = 5, sticky='W')

    #right frame
    frame_entry = ttk.Frame(root)
    frame_entry.columnconfigure(0, weight=1)
    frame_entry.columnconfigure(0, weight=3)
    frame_entry.grid(row = 0, column = 1)

    #entry boxes
    entry_fname = Entry(frame_entry, width = 54)
    entry_lname = Entry(frame_entry, width = 54)
    entry_phone = Entry(frame_entry, width = 54)
    entry_email = Entry(frame_entry, width = 54)
    entry_ename = Entry(frame_entry, width = 54)
    entry_relation = Entry(frame_entry, width = 54)
    entry_eemail = Entry(frame_entry, width = 54)
    entry_ephone = Entry(frame_entry, width = 54)

    #highlight entry box when user is typing
    entry_fname.focus()
    entry_lname.focus()
    entry_phone.focus()
    entry_email.focus()
    entry_ename.focus()
    entry_relation.focus()
    entry_ephone.focus()
    entry_eemail.focus()

    #placing entry boxes
    entry_fname.grid(row = 0, column = 0, pady = 7, padx = 5)
    entry_lname.grid(row = 1, column = 0, pady = 7, padx = 5)
    entry_phone.grid(row = 2, column = 0, pady = 7, padx = 5)
    entry_email.grid(row = 3, column = 0, pady = 7, padx = 5)
    entry_ename.grid(row = 4, column = 0, pady = 7, padx = 5)
    entry_relation.grid(row = 5, column = 0, pady = 7, padx = 5)
    entry_ephone.grid(row = 6, column = 0, pady = 7, padx = 5)
    entry_eemail.grid(row = 7, column = 0, pady = 7, padx = 5)

    #next button frame
    frame_btnNext = ttk.Frame(root,width = 100)
    frame_btnNext.columnconfigure(1, weight=0)
    frame_btnNext.grid(row = 8, column = 0)

    #next button
    btn_next = Button(frame_btnNext, text = "Next", width = 10, command= lambda:[onClickNext(entry_fname.get(), entry_lname.get(), entry_phone.get(), entry_email.get(), entry_ename.get(), entry_relation.get(), entry_ephone.get(), entry_eemail.get())])
    btn_next.grid(row = 8, column = 0, pady = 7,  sticky = 'E')



    root.mainloop()















