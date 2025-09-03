from tkinter import Tk,Label,Button,Entry
from text_files.text_phone_book import get_phone_book,add_to_phone_book
from models.phone_book import PhoneBook

window=Tk()
window.title("Phone Book")

data=get_phone_book()
phone_book=PhoneBook(data)

def contact_form():
    contact_form_window=Tk()
    contact_form_window.title("New Contact")

    firstname_lable=Label(contact_form_window,text="First Name")
    firstname_lable.grid(row=0,column=0,padx=5,pady=5)

    firstname_entry=Entry(contact_form_window,width=30)
    firstname_entry.grid(row=0,column=1,padx=5,pady=5)

    lastname_lable = Label(contact_form_window, text="Last Name")
    lastname_lable.grid(row=1, column=0, padx=5, pady=5)

    lastname_entry = Entry(contact_form_window, width=30)
    lastname_entry.grid(row=1, column=1, padx=5, pady=5)

    phone_lable = Label(contact_form_window, text="Phone Number")
    phone_lable.grid(row=2, column=0, padx=5, pady=5)

    phone_entry = Entry(contact_form_window, width=11)
    phone_entry.grid(row=2, column=1, padx=5, pady=5)

    email_lable = Label(contact_form_window, text="Email Address")
    email_lable.grid(row=3, column=0, padx=5, pady=5)

    email_entry = Entry(contact_form_window, width=30)
    email_entry.grid(row=3, column=1, padx=5, pady=5)

    def submit():
        firstname=firstname_entry.get()
        lastname=lastname_entry.get()
        phone=phone_entry.get()
        email=email_entry.get()

        phone_book.create_contact(firstname,lastname,phone,email)
        add_to_phone_book([firstname,lastname,phone,email])

        create_table_body()

        contact_form_window.destroy()
    submit_button=Button(contact_form_window,text="Submit",command=submit)
    submit_button.grid(row=4, column=1, padx=5, pady=5)

    contact_form_window.mainloop()

new_contact_button=Button(window,text="New Contact",command=contact_form)
new_contact_button.grid(row=0,column=1,padx=5,pady=5)

search_entry=Entry(window,width=40)
search_entry.grid(row=0,column=2,padx=0,pady=5,columnspan=2,sticky="e")

def search():
    text=search_entry.get()
    phone_book.search(text)

    create_table_body()

search_button=Button(window,text="Search",command=search)
search_button.grid(row=0,column=4,padx=5,pady=5,sticky="w")


def create_header_table():
    row_label=Label(window,text="NO")
    row_label.grid(row=1,column=0,padx=(5,2),pady=5)

    firstname_label = Label(window, text="First Name")
    firstname_label.grid(row=1, column=1, padx=2, pady=5)

    lastname_label = Label(window, text="Last Name")
    lastname_label.grid(row=1, column=2, padx=2, pady=5)

    phone_label = Label(window, text="Phone Number")
    phone_label.grid(row=1, column=3, padx=2, pady=5)

    email_label = Label(window, text="Email Address")
    email_label.grid(row=1, column=4, padx=2, pady=5)

create_header_table()

entry_list=[]

def create_table_body():

    for entry in entry_list:
        entry.destroy()
    entry_list.clear()

    row_number = 1
    for contact in phone_book.show_contact_list:
        row_entry=Entry(window,width=4)
        row_entry.insert(0,str(row_number))
        row_entry.config(state="readonly")
        row_entry.grid(row=row_number+1, column=0, padx=2, pady=1)
        entry_list.append(row_entry)

        firstname_entry = Entry(window, width=20)
        firstname_entry.insert(0, contact.firstname)
        firstname_entry.config(state="readonly")
        firstname_entry.grid(row=row_number+1, column=1, padx=2, pady=1)
        entry_list.append(firstname_entry)

        lastname_entry = Entry(window, width=30)
        lastname_entry.insert(0, contact.lastname)
        lastname_entry.config(state="readonly")
        lastname_entry.grid(row=row_number + 1, column=2,pady=1)
        entry_list.append(lastname_entry)

        phone_entry = Entry(window, width=11)
        phone_entry.insert(0, contact.phone)
        phone_entry.config(state="readonly")
        phone_entry.grid(row=row_number + 1, column=3, pady=1)
        entry_list.append(phone_entry)

        email_entry = Entry(window, width=30)
        email_entry.insert(0, contact.email)
        email_entry.config(state="readonly")
        email_entry.grid(row=row_number + 1, column=4, padx=2, pady=1)
        entry_list.append(email_entry)



        row_number+=1

create_table_body()



window.mainloop()