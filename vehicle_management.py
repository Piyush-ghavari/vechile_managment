import tkinter as tk
from tkinter import messagebox
import mysql.connector

# MySQL connection setup
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # Replace with your MySQL username
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
        self.root.geometry("700x600")
        self.root.configure(bg="#F0F8FF")  # Light blue background
        
        # Initialize the list of vehicles
        self.vehicles = []

        # Create the form labels and entry fields
        self.create_widgets()

    def create_widgets(self):
        # Common vehicle fields with colors and padding
        tk.Label(self.root, text="License Plate:", font=("Arial", 12, "bold"), bg="#F0F8FF", fg="#2F4F4F").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        self.license_plate_entry = tk.Entry(self.root, font=("Arial", 12), width=20, relief="solid", bd=2, highlightbackground="#B0C4DE")
        self.license_plate_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Make:", font=("Arial", 12, "bold"), bg="#F0F8FF", fg="#2F4F4F").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        self.make_entry = tk.Entry(self.root, font=("Arial", 12), width=20, relief="solid", bd=2, highlightbackground="#B0C4DE")
        self.make_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Model:", font=("Arial", 12, "bold"), bg="#F0F8FF", fg="#2F4F4F").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        self.model_entry = tk.Entry(self.root, font=("Arial", 12), width=20, relief="solid", bd=2, highlightbackground="#B0C4DE")
        self.model_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Year:", font=("Arial", 12, "bold"), bg="#F0F8FF", fg="#2F4F4F").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        self.year_entry = tk.Entry(self.root, font=("Arial", 12), width=20, relief="solid", bd=2, highlightbackground="#B0C4DE")
        self.year_entry.grid(row=3, column=1, padx=10, pady=5)

        # Type of vehicle selection with a nice dropdown style
        self.vehicle_type_label = tk.Label(self.root, text="Vehicle Type:", font=("Arial", 12, "bold"), bg="#F0F8FF", fg="#2F4F4F")
        self.vehicle_type_label.grid(row=4, column=0, sticky="e", padx=10, pady=5)

        self.vehicle_type_var = tk.StringVar(value="Car")
        self.vehicle_type_menu = tk.OptionMenu(self.root, self.vehicle_type_var, "Car", "Truck", "Motorcycle")
        self.vehicle_type_menu.config(font=("Arial", 12), width=18, bg="#ADD8E6", relief="raised")
        self.vehicle_type_menu.grid(row=4, column=1, padx=10, pady=5)

        # Specific fields based on vehicle type
        self.specific_fields_frame = tk.Frame(self.root, bg="#F0F8FF")
        self.specific_fields_frame.grid(row=5, columnspan=2, pady=10)

        # Add Vehicle Button with style
        self.add_vehicle_button = tk.Button(self.root, text="Add Vehicle", font=("Arial", 12, "bold"), bg="#32CD32", fg="white", command=self.add_vehicle, relief="raised", bd=3)
        self.add_vehicle_button.grid(row=6, columnspan=2, pady=10)

        # Vehicle listbox with a clean style
        self.vehicles_listbox = tk.Listbox(self.root, width=50, height=10, font=("Arial", 12), bg="#F7F7F7", selectmode=tk.SINGLE, relief="sunken", bd=2)
        self.vehicles_listbox.grid(row=7, columnspan=2, padx=10, pady=10)

        # Update specific fields when the vehicle type changes
        self.vehicle_type_var.trace("w", self.update_specific_fields)

        self.load_vehicles_from_db()

        # Exit Button with aesthetic design
        self.exit_button = tk.Button(self.root, text="Exit", font=("Arial", 12, "bold"), bg="#FF6347", fg="white", command=self.exit_app, relief="raised", bd=3)
        self.exit_button.grid(row=8, columnspan=2, pady=10)

    def update_specific_fields(self, *args):
        # Clear the previous specific fields
        for widget in self.specific_fields_frame.winfo_children():
            widget.destroy()

        vehicle_type = self.vehicle_type_var.get()

        if vehicle_type == "Car":
            tk.Label(self.specific_fields_frame, text="Number of Doors:", font=("Arial", 12, "bold"), bg="#F0F8FF", fg="#2F4F4F").grid(row=0, column=0, padx=10, pady=5)
            self.num_doors_entry = tk.Entry(self.specific_fields_frame, font=("Arial", 12), width=20, relief="solid", bd=2, highlightbackground="#B0C4DE")
            self.num_doors_entry.grid(row=0, column=1, padx=10, pady=5)

        elif vehicle_type == "Truck":
            tk.Label(self.specific_fields_frame, text="Load Capacity (kg):", font=("Arial", 12, "bold"), bg="#F0F8FF", fg="#2F4F4F").grid(row=0, column=0, padx=10, pady=5)
            self.load_capacity_entry = tk.Entry(self.specific_fields_frame, font=("Arial", 12), width=20, relief="solid", bd=2, highlightbackground="#B0C4DE")
            self.load_capacity_entry.grid(row=0, column=1, padx=10, pady=5)

        elif vehicle_type == "Motorcycle":
            tk.Label(self.specific_fields_frame, text="Engine Capacity (cc):", font=("Arial", 12, "bold"), bg="#F0F8FF", fg="#2F4F4F").grid(row=0, column=0, padx=10, pady=5)
            self.engine_capacity_entry = tk.Entry(self.specific_fields_frame, font=("Arial", 12), width=20, relief="solid", bd=2, highlightbackground="#B0C4DE")
            self.engine_capacity_entry.grid(row=0, column=1, padx=10, pady=5)

    def add_vehicle(self):
        # Retrieve data from entry fields
        license_plate = self.license_plate_entry.get()
        make = self.make_entry.get()
        model = self.model_entry.get()
        year = self.year_entry.get()

        if not (license_plate and make and model and year):
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        vehicle_type = self.vehicle_type_var.get()

        if vehicle_type == "Car":
            num_doors = self.num_doors_entry.get()
            if not num_doors:
                messagebox.showerror("Input Error", "Please provide the number of doors.")
                return
            vehicle = Car(license_plate, make, model, year, num_doors)

        elif vehicle_type == "Truck":
            load_capacity = self.load_capacity_entry.get()
            if not load_capacity:
                messagebox.showerror("Input Error", "Please provide the load capacity.")
                return
            vehicle = Truck(license_plate, make, model, year, load_capacity)

        elif vehicle_type == "Motorcycle":
            engine_capacity = self.engine_capacity_entry.get()
            if not engine_capacity:
                messagebox.showerror("Input Error", "Please provide the engine capacity.")
                return
            vehicle = Motorcycle(license_plate, make, model, year, engine_capacity)

        self.vehicles.append(vehicle)
        self.save_vehicle_to_db(vehicle)
        self.update_vehicle_list()

    def update_vehicle_list(self):
        self.vehicles_listbox.delete(0, tk.END)
        for vehicle in self.vehicles:
            self.vehicles_listbox.insert(tk.END, vehicle.display_info())

    def save_vehicle_to_db(self, vehicle):
        connection = get_db_connection()
        cursor = connection.cursor()

        vehicle_type = vehicle.__class__.__name__  # Corrected to get class name
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

    def load_vehicles_from_db(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM vehicles")
        rows = cursor.fetchall()
        
        for row in rows:
            vehicle_type = row[5]
            if vehicle_type == "Car":
                vehicle = Car(row[1], row[2], row[3], row[4], row[6])
            elif vehicle_type == "Truck":
                vehicle = Truck(row[1], row[2], row[3], row[4], row[7])
            elif vehicle_type == "Motorcycle":
                vehicle = Motorcycle(row[1], row[2], row[3], row[4], row[8])
            
            self.vehicles.append(vehicle)

        self.update_vehicle_list()
        cursor.close()
        connection.close()

    def exit_app(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = VehicleManagementApp(root)
    root.mainloop()
