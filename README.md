# Expense Tracker Web Application

A simple Flask-based web application to track personal expenses with user authentication (login and registration).


## Features

- User registration and login
- Dashboard displaying welcome message and navigation
- Expense listing page (to be implemented)
- Secure user validation (currently in-memory dictionary)
- Responsive design using Bootstrap 5


## Technologies Used

- Python 3
- Flask (Micro web framework)
- Jinja2 (Templating engine)
- Bootstrap 5 (Front-end styling)
- HTML, CSS (Basic styling and layout)


## Installation & Setup

1. Clone the repository:
   git clone https://github.com/abhimakulshrestha/Expense_App_py.git
   cd expense-tracker

2. Create and activate a virtual environment:   
python -m venv .venv
source .venv/bin/activate    # Linux/Mac
.venv\Scripts\activate       # Windows

3. Install dependencies:
pip install -r requirements.txt

4. Run the application:
flask run

5. Open your browser and visit:
http://127.0.0.1:5000/login

## Usage
-> Register a new user using the Register page.
-> Login with your credentials.
-> After login, you will be redirected to the Dashboard.
-> Navigate to view expenses (feature under development).

## User Credentials for Testing
Use this to quickly test the login functionality:
| Username             | Password |
| [user@gmail.com]     | password |


## Project Structure
expense-tracker/
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│
├── static/
│   └── css/
│       └── style.css
│
├── main.py             
├── requirements.txt     
└── README.md

## Future Improvements
-> Store users and expenses in a database (e.g., SQLite)
-> Add password hashing for security
-> Add user session management
->Implement expense CRUD operations with categories and charts
->Add logout functionality

## Contact
For questions or suggestions, please contact [abhimakulshrestha2004@gmail.com]


