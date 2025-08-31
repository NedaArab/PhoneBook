from models.contact import Contact


class PhoneBook:
    def __init__(self,contact_list=None):
        if contact_list:
            self.contact_list=contact_list
        else:
            self.contact_list=[]

        self.show_contact_list=self.contact_list.copy()

    def get_contact_with_id(self):
        pass

    def search(self,text_search):
        self.show_contact_list.clear()
        for contact in self.contact_list:
            if text_search in contact.firstname or text_search in contact.lastname or text_search in contact.email:
                self.show_contact_list.append(contact)
        return self.show_contact_list




    def create_contact(self,firstname,lastname,phone,email):
        new_contact=Contact(firstname, lastname, phone, email)
        self.show_contact_list.append(new_contact)



    def delete(sel,firstname):
        pass



