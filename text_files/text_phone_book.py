import csv

from models.contact import Contact


def get_phone_book():
    contact_list = []
    with open("phone_book.csv") as csv_file:
        for line in csv_file.readlines():
            contact_info = line.split(",")
            contact = Contact(*contact_info)
            contact_list.append(contact)

    return contact_list

def add_to_phone_book(*new_contact):
    with open("phone_book.csv",mode="a",newline='') as csv_file:
        writer=csv.writer(csv_file)
        writer.writerow(*new_contact)

