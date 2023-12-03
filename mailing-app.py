import tkinter as tk
import webbrowser

master = tk.Tk()

def clear_fields():
    name_input.delete(0, 'end')
    address_input.delete(0, 'end')
    phone_input.delete(0, 'end')
    email_input.delete(0, 'end')

def save_entry():
    myfile = open('contacts', mode = 'a')
    myfile.write(str(name_input.get()))
    myfile.write(str(address_input.get()))
    myfile.write(str(phone_input.get()))
    myfile.write(str(email_input.get()) + '\n')
    myfile.close()

def delete_entry():
    myfile = open('contacts', mode = 'r')
    file = myfile.readlines()
    myfile.close()
    myfile = open('contacts', mode = 'w')
    for r in file:
        if str(name_input.get()) in r:
            continue
        myfile.write(str(r))
    myfile.close()    

def find_address():
    url = 'https://www.google.com/maps/search/?api=1&'
    par = list(str(address_input.get()))
    for j in range(len(par)):
        if par[j] == ' ':
            par[j] = '+'
        continue
    new_url = url+'query='+''.join(par)
    webbrowser.open(new_url)
            


#def send_email():
    


tk.Label(master, text = "Name").grid(row = 0)
name_input = tk.Entry(master)
name_input.grid(row = 0, column = 1)

tk.Label(master, text = "Address").grid(row = 1)
address_input = tk.Entry(master)
address_input.grid(row = 1, column = 1)

tk.Label(master, text = "Phone Number").grid(row = 2)
phone_input = tk.Entry(master)
phone_input.grid(row = 2, column = 1)

tk.Label(master, text = "Email Adress").grid(row = 3)
email_input = tk.Entry(master)
email_input.grid(row = 3, column = 1)

tk.Label(master, text = "View Contacts").grid(row = 5)
contacts = tk.Text(master)


tk.Button(master, text = "Clear", command = clear_fields).grid(row = 4, column = 1)

tk.Button(master, text = "Save", command = save_entry).grid(row = 4, column = 0)

tk.Button(master, text = "Delete", command = delete_entry).grid(row = 4, column = 2)

tk.Button(master, text = "Map", command = find_address).grid(row = 2 , column = 2)

#tk.Button(master, text = "Send Email", command = send_email).grid(row = 3, column = 2) 


