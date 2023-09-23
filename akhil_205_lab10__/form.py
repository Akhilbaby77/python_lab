import tkinter as tk
from tkinter import messagebox
import re


def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_phone(phone):
    pattern = r'^\d{10}$'
    return re.match(pattern, phone) is not None

def validate_name(name):
    pattern = r'^[A-Za-z]{3,}$'
    return re.match(pattern, name) is not None
     

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    gender = gender_var.get()
    year_dob = year_spinbox.get()
    vehicle_type = vehicle_var.get()
    rental_period = rental_spinbox.get()

  
    if not validate_name(name):
        messagebox.showerror("Error", "Please enter a valid name (only letters and spaces allowed).")
        return


    if not validate_email(email):
        messagebox.showerror("Error", "Please enter a valid email.")
        return

  
    if not validate_phone(phone):
        messagebox.showerror("Error", "Please enter a valid phone number (10 digits).")
        return

    if not name or not email or not phone or not gender or not year_dob or not vehicle_type or not rental_period:
        messagebox.showerror("Error", "Please fill in all the fields.")
        return



    print("Name:", name)
    print("Email:", email)
    print("Phone:", phone)
    print("Gender:", gender)
    print("Year/DoB:", year_dob)
    print("Vehicle Type:", vehicle_type)
    print("Rental Period (days):", rental_period)


    messagebox.showinfo("Success", "Form submitted successfully!")


root = tk.Tk()
root.title("Vehicle Rental Management Form")


tk.Label(root, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Email:").grid(row=1, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1)

tk.Label(root, text="Phone Number:").grid(row=2, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=2, column=1)


tk.Label(root, text="Gender:").grid(row=3, column=0)
gender_options = ['Male', 'Female', 'Other']
gender_var = tk.StringVar(root)
gender_dropdown = tk.OptionMenu(root, gender_var, *gender_options)
gender_dropdown.grid(row=3, column=1)


tk.Label(root, text="Year/DoB:").grid(row=4, column=0)
year_spinbox = tk.Spinbox(root, from_=1900, to=2023)
year_spinbox.grid(row=4, column=1)


tk.Label(root, text="Vehicle Type:").grid(row=5, column=0)
vehicle_type_options = ['Sedan', 'SUV', 'Truck', 'Van', 'Motorcycle']
vehicle_var = tk.StringVar(root)
vehicle_dropdown = tk.OptionMenu(root, vehicle_var, *vehicle_type_options)
vehicle_dropdown.grid(row=5, column=1)


tk.Label(root, text="Rental Period (days):").grid(row=6, column=0)
rental_spinbox = tk.Spinbox(root, from_=1, to=30)
rental_spinbox.grid(row=6, column=1)

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=7, column=0, columnspan=2, pady=10)


root.mainloop()
