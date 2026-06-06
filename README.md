# Student Management System

A simple Student Management System built using **Python Flask**, **SQLite**, and **Bootstrap 5**.

## Features

- Add Student
- View Students
- Edit Student
- Delete Student
- Dashboard with Total Students Count
- Responsive Bootstrap UI
- SQLite Database Integration

## Technologies Used

- Python
- Flask
- SQLite
- Bootstrap 5
- HTML5
- CSS3
- Jinja2 Templates

## Project Structure

```text
Student_Management/
│
├── app.py
├── student.db
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add_student.html
│   ├── edit_student.html
│   └── students.html
│
```

## Database Schema

### Students Table

| Column | Type                              |
| ------ | --------------------------------- |
| id     | INTEGER PRIMARY KEY AUTOINCREMENT |
| name   | TEXT                              |
| age    | INTEGER                           |
| course | TEXT                              |
| email  | TEXT                              |

## Installation

### Clone Project

```bash
git clone <repository-url>
cd Student_Management
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install flask
```

### Run Project

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

## Screens

- Dashboard
- Add Student Page
- Students List Page
- Edit Student Page

## CRUD Operations

### Create

Add new students to the database.

### Read

View all students in a table.

### Update

Edit existing student information.

### Delete

Remove students from the database.

## Future Improvements

- Login System
- MySQL Database
- Export to Excel
- Student Profile Page
- Pagination
- Flash Messages

## Author

Lakshit Suthar

## License

This project is for learning and educational purposes.
