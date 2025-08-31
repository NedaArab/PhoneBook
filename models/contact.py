import requests


class Contact:
    def __init__(self,firstname,lastname,phone,email=None):
        self.firstname=firstname
        self.lastname=lastname
        self.phone=phone
        self.email=email

    def get_full_name(self):
        return f"{self.firstname} {self.lastname}"

    def edit_contact(self,new_firstname,new_lastname,new_phone,new_email):
        self.firstname=new_firstname
        self.lastname=new_lastname
        self.phone=new_phone
        self.email=new_email

    def call(self,text_mesage):
        pass

    def sms(self):
        url="https://app.snapp.taxi/api/api-passenger-oauth/v3/mutotp"

        pass

    def send_email(self):
        pass

