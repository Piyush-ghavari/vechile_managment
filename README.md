# Vehicle Management System

This project is a **Vehicle Management System** built using Python's `Tkinter` for the graphical user interface (GUI) and `MySQL` for data storage. The system allows users to add, display, and store vehicles of different types (Car, Truck, Motorcycle) in a MySQL database.

## Features

- Add new vehicles to the system.
- Select vehicle type (Car, Truck, Motorcycle) and provide specific details for each type (e.g., number of doors, load capacity, or engine capacity).
- Store vehicle data in a MySQL database.
- Display a list of vehicles in the application.
- Exit the application with a simple click.

## Technologies Used

- **Python**: Programming language used for building the application.
- **Tkinter**: Python library used for creating the GUI.
- **MySQL**: Database system used to store vehicle information.

## Installation

### Prerequisites

Before running the application, make sure you have the following installed:

1. Python 3.x
2. Tkinter (comes pre-installed with Python, but if not, you can install it using your package manager).
3. MySQL Server
4. `mysql-connector-python` library for Python (can be installed via pip).

You can install `mysql-connector-python` by running:

```bash
pip install mysql-connector-python
```

## Usage
### 1. Add a Vehicle:

- Fill out the required fields:
- License Plate: The unique license plate of the vehicle.
- Make: The brand or manufacturer of the vehicle.
- Model: The model of the vehicle.
- Year: The manufacturing year of the vehicle.
- Choose the vehicle type (Car, Truck, or Motorcycle) from the dropdown menu.
- Based on the selected vehicle type, additional fields will appear:
- Car: Enter the number of doors.
- Truck: Enter the load capacity in kilograms.
- Motorcycle: Enter the engine capacity in cubic centimeters (cc).
- Click the "Add Vehicle" button to save the vehicle to the database and display it in the vehicle list.

### 2.Vehicle List:

- The list of vehicles will be displayed in the Listbox on the main screen. Each vehicle's details (License Plate, Make, Model, Year, and Specific Details) will be shown.
### 3 Exit:

- To exit the application, simply click the "Exit" button.
### Screenshots
- Here are some screenshots of the application interface:
- 
1.![Screenshot 2025-01-09 172949](https://github.com/user-attachments/assets/bf86c28c-bc29-42e9-b6bc-6849bdd813bf)

2.![Screenshot 2025-01-09 173225](https://github.com/user-attachments/assets/2e5ebd13-8f75-49cc-a256-b38bb7002b4b)

3.![Screenshot 2025-01-09 172927](https://github.com/user-attachments/assets/d59d343b-df76-4faa-9400-c367156d0068)

4.![Screenshot 2025-01-09 173338](https://github.com/user-attachments/assets/65142668-e02f-48e0-9b72-04bf677906b1)


## Acknowledgements
- Tkinter for the GUI.
- MySQL for the database.
- Python community for their support and libraries.
