# To-Do List Application

A simple to-do list application developed using Python and Tkinter. This application allows users to register, login, and manage their tasks with basic CRUD operations.

## Features

- **User Authentication:** Register and login with username and password.
- **Task Management:** Add, update, and delete tasks.
- **Persistent Storage:** Tasks are stored persistently using SQLite.
- **GUI:** User-friendly graphical interface using Tkinter.

## Requirements

- Python 3.6 or higher
- Tkinter (included with most Python installations)

## Installation

# Clone the repository
```bash
git clone https://github.com/yourusername/todo-app.git
cd todo-app
```

# Create a virtual environment
```bash
python -m venv venv
```

# Activate the virtual environment
# On Windows
```bash
venv\Scripts\activate
```
# On macOS/Linux
```bash
source venv/bin/activate
```

# Run the application
```bash
python main.py
```

## File Structure
- **main.py:** The entry point of the application. Initializes the database and starts the login window.
- **auth.py:** Handles user registration and login functionality.
- **crud.py:** Contains CRUD operations for tasks.
- **db.py:** Manages database connection and table creation.
- **ui.py:** Defines the graphical user interface using Tkinter.
- **utils.py:** Contains utility functions for input validation and message display.

## Screenshots
(Include screenshots of the application here)

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- **Tkinter** for the GUI
- **hashlib** for password hashing
- **SQLite3** for database