# ALX Intranet Clone

## Authors

Namwamba Marvin Jealous Matsikachando

## Description

This project is a clone of our school intranet dashboard, providing a centralized platform for students and teachers to access information such as projects, servers, planning, sandboxes, and grades. The dashboard is designed to be user-friendly and customizable, providing a seamless experience for users.

## Features

- User authentication and role-based access control
- Course management functionality for teachers
- Assignment submission and grading system
- Announcements and notifications for important updates
- Personalized dashboard with widgets and customization options

## Technologies Used

- **Front-end:** jQuery, Bootstrap 5, CSS3, Font Awesome icons, HTML5
- **Back-end:** Python 3, Django 3.2.12
- **Database:** SQLite3
- **Development Tools:** Visual Studio Code, Figma (for mockups), Trello (for project scheduling)
- **Version Control:** GitHub
- **Deployment:** AWS EC2

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/pasej5/alx-intranet_clone.git
   ```

   Navigate to the project directory: cd alx-intranet_clone
   Navigate to the WebstackPortfolio directory: cd WebstackPortfolio
   Install the necessary dependencies. Ensure you have a virtual environment set up: python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

   The requirements.txt file should contain the following dependencies:

   Django==3.2.12
   django-cors-headers==4.3.1
   djangorestframework
   Jinja2==2.11.3
   MarkupSafe==2.1.1
   more-itertools==8.10.0
   msgpack==1.0.7
   netifaces==0.10.9
   parameterized==0.8.1
   pbr==6.0.0
   pep8==1.7.1
   pillow==10.3.0
   pip==22.0.2
   platformdirs==2.1.0
   PyAudio==0.2.11
   pycodestyle==2.7.0

Set up a local server to run the application:
python3 manage.py migrate
python3 manage.py runserver

Start the server:

bash
Copy code
python3 manage.py runserver
Access the dashboard through your web browser by navigating to the server address specified in the console (e.g., http://localhost:8000).

Log in with your credentials to explore the dashboard features.
Contributing
If you would like to contribute to the project, please fork the repository, make your changes, and submit a pull request. Your contributions are greatly appreciated
