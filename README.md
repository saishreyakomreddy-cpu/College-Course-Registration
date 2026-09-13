# College Course Registration System

## 📌 Project Description

The **College Course Registration System** is a web-based application developed using **Python and Flask**. It allows students to enter their academic details and register for available college courses.

The system checks the student's **CGPA eligibility**, course availability, and duplicate registrations. Students can also drop courses and view their registered courses along with the total course fee.

## 🎯 Objectives

* Provide an easy way for students to register for courses.
* Validate student information before registration.
* Allow registration only when the student's CGPA is at least **7.5**.
* Prevent duplicate course registrations.
* Check course capacity before registration.
* Allow students to drop registered courses.
* Calculate the total fee for registered courses.

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **HTML**
* **Jinja2 Templates**
* **CSS**
* **Web Browser**

The Flask application uses `render_template()` and `request` to handle the web pages and form submissions.

## 📚 Modules Used

### 1. Flask

Flask is the main web framework used to create the application.

It is used for:

* Creating the web application
* Defining routes
* Handling GET and POST requests
* Rendering HTML templates

### 2. render_template

`render_template` is used to connect the Python backend with the HTML page.

It sends course and student information to `index.html`.

### 3. request

The `request` module is used to receive information submitted through the registration form, such as:

* Student ID
* Student Name
* Year
* Department
* Section
* CGPA
* Selected Course

## 🧩 Main Modules / Features

### 1. Student Information Module

Collects:

* Student ID
* Student Name
* Year
* Department
* Section
* CGPA

### 2. Course Management Module

The system contains six courses:

| Course | Capacity |   Fee |
| ------ | -------: | ----: |
| AI     |       50 | ₹5000 |
| ML     |       40 | ₹4500 |
| CN     |       45 | ₹4800 |
| APP    |       35 | ₹5200 |
| JAVA   |       30 | ₹4700 |
| DL     |       25 | ₹5300 |

These course details are stored in the Python `courses` dictionary.

### 3. Eligibility Module

The system checks the student's CGPA.

**Minimum required CGPA = 7.5**

If the CGPA is below 7.5, registration is rejected.

### 4. Course Registration Module

Students can register for a selected course if:

* All required details are entered.
* CGPA is at least 7.5.
* The course exists.
* The student is not already registered.
* The course has available seats.

### 5. Course Drop Module

Students can drop a course they have already registered for.

If the student is not registered for that course, the system displays a warning.

### 6. Fee Calculation Module

The system automatically calculates the total fee based on the student's registered courses.

### 7. Validation Module

The system validates:

* Empty fields
* CGPA
* Course selection
* Duplicate registration
* Course capacity

## 🔄 System Workflow

```text
Student
   ↓
Enter Student Details
   ↓
Enter CGPA
   ↓
CGPA ≥ 7.5?
   ↓
Select Course
   ↓
Check Course Capacity
   ↓
Check Duplicate Registration
   ↓
Register Course
   ↓
Calculate Total Fee
```

## ▶️ How to Run

### Step 1: Install Python

Make sure Python is installed on your system.

### Step 2: Install Flask

```bash
pip install flask
```

### Step 3: Run the Application

```bash
python app.py
```

### Step 4: Open in Browser

Open the local Flask address shown in the terminal, usually:

```text
http://127.0.0.1:5000/
```

## 📁 Project Structure

```text
College-Course-Registration/
│
├── app.py
├── README.md
├── .gitignore
│
└── templates/
    └── index.html
```

## ⭐ Advantages

* Simple and easy-to-use interface
* Automatic eligibility checking
* Prevents duplicate registrations
* Checks course capacity
* Calculates total fees
* Provides course dropping functionality

## 🚀 Future Enhancements

* Add a database such as MySQL or SQLite.
* Add student login and authentication.
* Add an admin dashboard.
* Store registration data permanently.
* Add payment functionality.
* Generate course registration receipts.
* Add timetable/conflict checking.

## 👩‍💻 Developed Using

**Python + Flask**

### Project

**College Course Registration System**
