# Hotel Reservation Management System 

In this app services like multiple Bookings in certain hotels are carried out. In each hotel there are multiple tasks about specific rooms. So basically a customer can book a room in the respected hotel.

### Processes and services:
 1. Room is booked by a Customer with an option to vacate on the desired date.
 2. If a new customer is trying to book a specific room which is already booked by some other customer then the new customer                 				will be alerted with an error and the room will not be available until the existing customer vacates it.
 3. I have implemented the concept of post_save so that as soon the room is vacated and the room is shown available for the 					upcoming booking customers.
 4. A customer can book only one room at a time.
 
 To run this in your system:
 
 Clone this repo in your system:
 ```
 git clone https://github.com/rub9542/Hotel-Reservation-management-system.git
 ```
 Get inside the repo, type this is terminal:
 ```
 cd Hotel-Reservation-management-system
 ```
 Create a virtual environment inside the repo:
 ```
 python3 -m venv .venv
 ```
 After that activate the virtual environment by typing:
 ```
 source .venv/bin/activate
 ```
 Next step is to install all the dependencies into your virtual environment:
 ```
 pip3 install 
Django==3.0.1
django-jsonfield==1.4.0
 ```
 Next get into the project directory by typing:
 ```
 cd hrms
 ```
 Type 3 commands in order before for the project to run:
 ```
 python3 manage.py makemigrations
 python3 manage.py migrate
 ```
 Now to access the admin page before running the server create a superuser:
 ```
 python3 manage.py createsuperuser
 fill the details :
 username: <ur choice>
 email: <optional>
 password: <password>
 confirm password: <confirm the password>
 ```
 After filling all these to run the project:
 ```
 python3 manage.py runserver
 ```
 
 
 
