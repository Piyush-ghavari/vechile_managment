import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog  # Correct import for simpledialog
import mysql.connector

# MySQL connection setup
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="password",  # Replace with your MySQL password
        database="vehicle_management"
    )

class Vehicle:
    def __init__(self, license_plate, make, model, year):
        self.license_plate = license_plate
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"License Plate: {self.license_plate}\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}"

class Car(Vehicle):
    def __init__(self, license_plate, make, model, year, num_doors):
        super().__init__(license_plate, make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        return super().display_info() + f"\nNumber of Doors: {self.num_doors}"

class Truck(Vehicle):
    def __init__(self, license_plate, make, model, year, load_capacity):
        super().__init__(license_plate, make, model, year)
        self.load_capacity = load_capacity

    def display_info(self):
        return super().display_info() + f"\nLoad Capacity: {self.load_capacity} kg"

class Motorcycle(Vehicle):
    def __init__(self, license_plate, make, model, year, engine_capacity):
        super().__init__(license_plate, make, model, year)
        self.engine_capacity = engine_capacity

    def display_info(self):
        return super().display_info() + f"\nEngine Capacity: {self.engine_capacity} cc"

class VehicleManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vehicle Management System")
        
        # Create a container for both pages
        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        # Initialize the pages
        self.page1()

    def page1(self):
        # Page 1 - Vehicle Type Selection
        self.clear_page()

        # Set the background color for the page
        self.container.config(bg="lightblue")

        # Title label with a font color
        tk.Label(self.container, text="Select Vehicle Type", font=("Arial", 14), bg="lightblue", fg="darkblue").pack(pady=20)

        # Button to select vehicle type
        select_button = tk.Button(self.container, text="Select Vehicle Type", font=("Arial", 12), command=self.select_vehicle)
        select_button.pack(pady=10)

        # Exit button
        exit_button = tk.Button(self.container, text="Exit", font=("Arial", 12), command=self.exit_app)
        exit_button.pack(pady=10)

    def select_vehicle(self):
        # Page 1 - After selecting vehicle type
        vehicle_type = self.ask_vehicle_type()

        if vehicle_type:
            self.vehicle_type = vehicle_type
            self.page2()

    def ask_vehicle_type(self):
        # This function will allow the user to select a vehicle type (Car, Truck, Motorcycle)
        vehicle_type = tkinter.simpledialog.askstring("Select Vehicle", "Enter Vehicle Type (Car, Truck, Motorcycle):")
        
        if vehicle_type not in ["Car", "Truck", "Motorcycle"]:
            messagebox.showerror("Input Error", "Please select a valid vehicle type (Car, Truck, or Motorcycle).")
            return None
        return vehicle_type

    def page2(self):
        # Page 2 - Vehicle Details Form
        self.clear_page()

        # Set the background color for the page
        self.container.config(bg="lightyellow")

        # Title label with a font color
        tk.Label(self.container, text="Enter Vehicle Details", font=("Arial", 14), bg="lightyellow", fg="darkgreen").pack(pady=20)

        # Common fields for all vehicles
        tk.Label(self.container, text="License Plate:", font=("Arial", 12), bg="lightyellow", fg="darkgreen").pack(pady=5)
        self.license_plate_entry = tk.Entry(self.container, font=("Arial", 12))
        self.license_plate_entry.pack(pady=5)

        tk.Label(self.container, text="Make:", font=("Arial", 12), bg="lightyellow", fg="darkgreen").pack(pady=5)
        self.make_entry = tk.Entry(self.container, font=("Arial", 12))
        self.make_entry.pack(pady=5)

        tk.Label(self.container, text="Model:", font=("Arial", 12), bg="lightyellow", fg="darkgreen").pack(pady=5)
        self.model_entry = tk.Entry(self.container, font=("Arial", 12))
        self.model_entry.pack(pady=5)

        tk.Label(self.container, text="Year:", font=("Arial", 12), bg="lightyellow", fg="darkgreen").pack(pady=5)
        self.year_entry = tk.Entry(self.container, font=("Arial", 12))
        self.year_entry.pack(pady=5)

        # Specific fields based on vehicle type
        if self.vehicle_type == "Car":
            tk.Label(self.container, text="Number of Doors:", font=("Arial", 12), bg="lightyellow", fg="darkgreen").pack(pady=5)
            self.num_doors_entry = tk.Entry(self.container, font=("Arial", 12))
            self.num_doors_entry.pack(pady=5)
        elif self.vehicle_type == "Truck":
            tk.Label(self.container, text="Load Capacity (kg):", font=("Arial", 12), bg="lightyellow", fg="darkgreen").pack(pady=5)
            self.load_capacity_entry = tk.Entry(self.container, font=("Arial", 12))
            self.load_capacity_entry.pack(pady=5)
        elif self.vehicle_type == "Motorcycle":
            tk.Label(self.container, text="Engine Capacity (cc):", font=("Arial", 12), bg="lightyellow", fg="darkgreen").pack(pady=5)
            self.engine_capacity_entry = tk.Entry(self.container, font=("Arial", 12))
            self.engine_capacity_entry.pack(pady=5)

        # Submit button to add the vehicle
        submit_button = tk.Button(self.container, text="Submit", font=("Arial", 12), command=self.add_vehicle)
        submit_button.pack(pady=10)

        # Exit button
        exit_button = tk.Button(self.container, text="Exit", font=("Arial", 12), command=self.exit_app)
        exit_button.pack(pady=10)

    def clear_page(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def add_vehicle(self):
        # Retrieve data from entry fields
        license_plate = self.license_plate_entry.get()
        make = self.make_entry.get()
        model = self.model_entry.get()
        year = self.year_entry.get()

        if not (license_plate and make and model and year):
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        if self.vehicle_type == "Car":
            num_doors = self.num_doors_entry.get()
            if not num_doors:
                messagebox.showerror("Input Error", "Please provide the number of doors.")
                return
            vehicle = Car(license_plate, make, model, year, num_doors)

        elif self.vehicle_type == "Truck":
            load_capacity = self.load_capacity_entry.get()
            if not load_capacity:
                messagebox.showerror("Input Error", "Please provide the load capacity.")
                return
            vehicle = Truck(license_plate, make, model, year, load_capacity)

        elif self.vehicle_type == "Motorcycle":
            engine_capacity = self.engine_capacity_entry.get()
            if not engine_capacity:
                messagebox.showerror("Input Error", "Please provide the engine capacity.")
                return
            vehicle = Motorcycle(license_plate, make, model, year, engine_capacity)

        self.save_vehicle_to_db(vehicle)
        messagebox.showinfo("Success", "Vehicle added successfully!")

        # Go back to the first page after vehicle is added
        self.page1()

    def save_vehicle_to_db(self, vehicle):
        connection = get_db_connection()
        cursor = connection.cursor()

        vehicle_type = vehicle.__class__.__name__
        if isinstance(vehicle, Car):
            num_doors = vehicle.num_doors
            cursor.execute("INSERT INTO vehicles (license_plate, make, model, year, vehicle_type, num_doors) VALUES (%s, %s, %s, %s, %s, %s)", 
                           (vehicle.license_plate, vehicle.make, vehicle.model, vehicle.year, vehicle_type, num_doors))
        elif isinstance(vehicle, Truck):
            load_capacity = vehicle.load_capacity
            cursor.execute("INSERT INTO vehicles (license_plate, make, model, year, vehicle_type, load_capacity) VALUES (%s, %s, %s, %s, %s, %s)", 
                           (vehicle.license_plate, vehicle.make, vehicle.model, vehicle.year, vehicle_type, load_capacity))
        elif isinstance(vehicle, Motorcycle):
            engine_capacity = vehicle.engine_capacity
            cursor.execute("INSERT INTO vehicles (license_plate, make, model, year, vehicle_type, engine_capacity) VALUES (%s, %s, %s, %s, %s, %s)", 
                           (vehicle.license_plate, vehicle.make, vehicle.model, vehicle.year, vehicle_type, engine_capacity))

        connection.commit()
        cursor.close()
        connection.close()

    def exit_app(self):
        # Show thank you message before exiting
        messagebox.showinfo("Exit", "Thank you for visiting!")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = VehicleManagementApp(root)
    root.mainloop()
