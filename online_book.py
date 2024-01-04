import tkinter
from tkinter import ttk
import mysql.connector

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Online_Book"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

root=tkinter.Tk()
root.title("Online Book")

def enter_data():
    name= first_name_entry.get()
    phonenumber= phone_number_entry.get()
    book= book_combobox.get()
    age= age_spinbox.get()
    totalbook=int(numcourses_spinbox.get())

    if book=="Malay":
        price= int(30) 
    else:
        price= int(40)
        
    if int(totalbook) > 4:
        total_price=totalbook * price * 0.3
    else:
        total_price=totalbook * price

    print ("RM",total_price)
    output_label.config(text=f", Total Price: RM{total_price}")

    print("Name: ", name, "Phone number: ", phonenumber )
    print("Book:", book, "Age: ", age, "Total book: ", totalbook)
    print("Total Price:RM",total_price)

    # To insert your Data to your database, As for this example, you have 3 attributes. (2 Attributes from your selection (Package, Pack) and another attributes that derived from your attributes (price))
    sql = "INSERT INTO user_information (name, phone_number, book, age, total_book, total_price) VALUES (%s,%s,%s,%s,%s,%s)"
    val = (name, phonenumber, book, age, totalbook, total_price)
    mycursor.execute(sql, val)
    mydb.commit()

frame=tkinter.Frame(root)
frame.pack()

user_info_frame=tkinter.LabelFrame(frame, text="USER INFORMATION", font=("Consolas", 20,"bold"), foreground= "blue")
user_info_frame.grid(row=0, column=0)

first_name_label=tkinter.Label(user_info_frame, text="Name")
first_name_label.grid(row=0, column=0)
first_name_entry=tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)

phone_number_label=tkinter.Label(user_info_frame, text="Phone Number")
phone_number_label.grid(row=0,column=1)
phone_number_entry=tkinter.Entry(user_info_frame)
phone_number_entry.grid(row=1,column=1)

book_label=tkinter.Label(user_info_frame, text="Book") 
book_combobox=ttk.Combobox(user_info_frame,values=["Malay","English"])
book_label.grid(row=2,column=0)
book_combobox.grid(row=3,column=0)

age_label=tkinter.Label(user_info_frame, text="Age")
age_spinbox=tkinter.Spinbox(user_info_frame,from_=18,to=25)
age_label.grid(row=2,column=1)
age_spinbox.grid(row=3,column=1)

courses_frame=tkinter.LabelFrame(frame, text="BOOK PURCHASE", font=("Colonna MT", 20,"bold"), foreground="green")
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)

numcourses_label=tkinter.Label(courses_frame, text="Total Book")
numcourses_spinbox=tkinter.Spinbox(courses_frame, from_=0, to="Infinity")
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

button=tkinter.Button(root, text="Enter data",command=enter_data)
button.pack(pady=10)

label=tkinter.Label(root,text="Total Price")
label.pack(ipadx=10, ipady=10)
output_label=tkinter.Label(root, text="")
output_label.pack()

root.mainloop()



