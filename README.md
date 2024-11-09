
# Interactive CRUD Application with Sorting and Validation

This project is a web-based CRUD (Create, Read, Update, Delete) application built using Flask, MySQL, jQuery, and AJAX. The application allows users to add, update, delete, and search records with a user-friendly interface. It also includes sorting functionality on table headers and frontend validation for input fields.

## Features
- **CRUD Operations**: Add, view, edit, and delete user records.
- **Search**: Real-time search functionality to filter user records.
- **Sorting**: Clickable table headers for sorting records.
- **Validation**: Frontend validation for email and 10-digit phone number.
- **AJAX**: Asynchronous operations to update the page dynamically without full reloads.

## Project Structure
The project follows a simple structure, organized for scalability and clarity:

```
├── app.py                 # Main Flask application file with view logic and models fields
├── templates
│   └── index.html         # Main HTML template
├── static
│   └── style.css          # Custom styles for the application
├── README.md              # Project README file
└── requirements.txt       # Python dependencies
```

## Prerequisites
- Python 3.6 or higher
- MySQL
- Virtual environment (optional, recommended)

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/crud-app.git
cd crud-app
```

### 2. Set Up a Virtual Environment (Optional)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL Database
Create a MySQL database named `crud_db` and configure the following table:

```sql
CREATE DATABASE crud_db;

USE crud_db;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(10) NOT NULL
);
```

Update the database configuration in `app.py`:

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_mysql_username'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DB'] = 'crud_db'
```

### 5. Run the Application

```bash
python app.py
```

The application should now be running on `http://127.0.0.1:5000/`.

## Usage
1. Open a browser and navigate to `http://127.0.0.1:5000/`.
2. Use the form to add new user records.
3. Click on the table headers to sort records by name, email, or phone.
4. Search for records using the search input box.
5. Update or delete records using the action buttons in each row.

## API Endpoints

- **GET /get_users**: Retrieve all user records.
- **POST /submit**: Add a new user.
- **PUT /update_user/<int:id>**: Update an existing user.
- **DELETE /delete_user/<int:id>**: Delete a user.


## Acknowledgments
- [Flask](https://flask.palletsprojects.com/) - Python web framework.
- [MySQL](https://www.mysql.com/) - Database for storing user data.
- [jQuery](https://jquery.com/) - Simplifies AJAX requests and DOM manipulation.

