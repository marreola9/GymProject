
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Client:
    def __init__(self, name, age, interests, instructor):
        self.name = name
        self.age = age
        self.interests = interests
        self.instructor = instructor

class GymApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gym App")
        self.master.geometry("700x325")
        self.master.configure(bg="DarkGoldenrod3")
        
         # create label with the font
        label = tk.Label(self.master, text='Hello')

        self.show_clients_button = tk.Button(self.master, text="Show Clients", command=self.show_clients)
        self.show_clients_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Create a list of clients
        self.clients = []
        
        # Create a tuple of exercise types
        self.exercises = ("Weights", "Cardio", "Yoga")
        
        # Create a dictionary of clients' exercise preferences
        self.client_prefs = {}
        
        # Create a frame to hold the entry fields and labels
        self.entry_frame = tk.Frame(self.master)
        self.entry_frame.pack(padx=10, pady=10)
        
        # Create a label and entry for the client's name
        self.name_label = tk.Label(self.entry_frame, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.entry_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create a label and entry for the client's age
        self.age_label = tk.Label(self.entry_frame, text="Age:")
        self.age_label.grid(row=1, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(self.entry_frame)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)

        # Create a label and entry for the client's gender
        self.instructor_label = tk.Label(self.entry_frame, text="instructor:")
        self.instructor_label.grid(row=2, column=0, padx=5, pady=5)
        self.instructor_entry = tk.Entry(self.entry_frame)
        self.instructor_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Create a label and checkboxes for the client's exercise interests
        self.exercise_label = tk.Label(self.entry_frame, text="Exercise interests:")
        self.exercise_label.grid(row=3, column=0, padx=5, pady=5)
        
        self.weights_var = tk.IntVar()
        self.weights_check = tk.Checkbutton(self.entry_frame, text="Weights", variable=self.weights_var)
        self.weights_check.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)
        
        self.cardio_var = tk.IntVar()
        self.cardio_check = tk.Checkbutton(self.entry_frame, text="Cardio", variable=self.cardio_var)
        self.cardio_check.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)
        
        self.yoga_var = tk.IntVar()
        self.yoga_check = tk.Checkbutton(self.entry_frame, text="Yoga", variable=self.yoga_var)
        self.yoga_check.grid(row=5, column=1, sticky=tk.W, padx=5, pady=5)
        
        # Create a button to add the client
        self.add_button = tk.Button(self.master, text="Add client", command=self.add_client)
        self.add_button.pack(padx=10, pady=10)


        # Create a button to show the class schedule
        self.schedule_button = tk.Button(self.master, text="Class Schedule", command=self.clas_schedule)
        self.schedule_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Define the class schedule
        self.class_schedule = {
            "Monday": {
                "Weights": "10:00am - 11:00am",
                "Yoga": "11:00am - 12:00pm",
                "Cardio": "1:00pm - 2:00pm"
            },
            "Tuesday": {
                "Yoga": "10:00am - 11:00am",
                "Cardio": "11:00am - 12:00pm",
                "Weights": "1:00pm - 2:00pm"
            },
            "Wednesday": {
                "Cardio": "10:00am - 11:00am",
                "Weights": "11:00am - 12:00pm",
                "Yoga": "1:00pm - 2:00pm"
            },
            "Thursday": {
                "Weights": "10:00am - 11:00am",
                "Yoga": "11:00am - 12:00pm",
                "Cardio": "1:00pm - 2:00pm"
            },
            "Friday": {
                "Yoga": "10:00am - 11:00am",
                "Cardio": "11:00am - 12:00pm",
                "Weights": "1:00pm - 2:00pm"
            }
        }

    def clas_schedule(self):
        # Create a new window
        self.schedule_window = tk.Toplevel(self.master)
        self.schedule_window.title("Class Schedule")
        self.schedule_window.geometry("400x300")

        # Create a label to display the class schedule
        schedule_label = tk.Label(self.schedule_window, text="Class Schedule", font=("Arial", 14))
        schedule_label.pack(pady=10)

        # Create a treeview widget to display the class schedule
        schedule_treeview = ttk.Treeview(self.schedule_window)
        schedule_treeview['columns'] = ('Time')
        schedule_treeview.column('#0', width=150, anchor=tk.W)
        schedule_treeview.column('Time', width=150, anchor=tk.W)
        schedule_treeview.heading('#0', text='Day', anchor=tk.W)
        schedule_treeview.heading('Time', text='Time', anchor=tk.W)

        # Add each class to the treeview
        for day, classes in self.class_schedule.items():
            for exercise, time in classes.items():
                schedule_treeview.insert('', tk.END, text=day, values=(time, exercise))

        schedule_treeview.pack(pady=10)

    
    
    def add_client(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        instructor = self.instructor_entry.get()
        interests = []
        if self.weights_var.get():
            interests.append("weights")
        if self.cardio_var.get():
            interests.append("cardio")
        if self.yoga_var.get():
            interests.append("yoga")
        client = Client(name, age, interests, instructor)
        self.clients.append(client)
        
    
    
    def show_clients(self):
        # Create a new window
        self.clients_window = tk.Toplevel(self.master)
        self.clients_window.title("Clients")
        self.clients_window.geometry("500x275")
        

        # Create a treeview widget
        self.clients_treeview = ttk.Treeview(self.clients_window)

        # Define the columns to display in the treeview
        self.clients_treeview['columns'] = ('Name', 'Age', 'Instructor', 'Exercise Interests')
        self.clients_treeview.column('#0', width=0, stretch=tk.NO)
        self.clients_treeview.column('Name', width=100)
        self.clients_treeview.column('Age', width=50)
        self.clients_treeview.column('Instructor', width=100)
        self.clients_treeview.column('Exercise Interests', width=150)

        # Add headings for each column
        self.clients_treeview.heading('#0', text='', anchor=tk.CENTER)
        self.clients_treeview.heading('Name', text='Name', anchor=tk.CENTER)
        self.clients_treeview.heading('Age', text='Age', anchor=tk.CENTER)
        self.clients_treeview.heading('Instructor', text='Instructor', anchor=tk.CENTER)
        self.clients_treeview.heading('Exercise Interests', text='Exercise Interests', anchor=tk.CENTER)

        # Add each client to the treeview
        for i, client in enumerate(self.clients):
            interests = ', '.join(client.interests)
            self.clients_treeview.insert(parent='', index=i, text='', values=(client.name, client.age, client.instructor, interests))

        # Pack the treeview
        self.clients_treeview.pack(expand=True, fill=tk.BOTH)


root = tk.Tk()
app = GymApp(root)
root.mainloop()







