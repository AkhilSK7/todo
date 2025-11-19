# TO DO App

A simple **TO DO application** built with **Django** to manage tasks. Users can **sign up, log in, and manage their personal tasks**. Each user has a separate task list, and tasks can be added, marked as done, or deleted.  

The UI is **responsive and modern**, using **Bootstrap 5**.

---

## Features

- **User Authentication**  
  - Sign up with username, email, and password.  
  - Log in and log out securely.  
  - Passwords are encrypted using Django’s built-in authentication.  

- **Task Management**  
  - Add new tasks with description and deadline.  
  - View all your tasks in a table format.  
  - Mark tasks as completed.  
  - Delete tasks when no longer needed.  
  - Filter tasks by deadline date.  

- **Responsive UI**  
  - Modern and clean design using **Bootstrap 5**.  
  - Home page with quick links to add or view tasks.  
  - Home and task pages accessible only after login.  

---

## Pages

1. **Home Page** (`home.html`)  
   - Accessible only after login.  
   - Quick links/buttons to **Add Task** and **View Tasks**.  

2. **Add Task** (`addtask.html`)  
   - Form to add a new task with description and deadline.  
   - Tasks are linked to the logged-in user.  
   - Success message shown after adding a task.  

3. **View Tasks** (`viewtask.html`)  
   - Displays all tasks of the logged-in user.  
   - Buttons to **mark tasks as done** or **delete tasks**.  
   - Filter tasks by a selected date.  

4. **Login Page** (`login.html`)  
   - Users can log in with their credentials.  

5. **Register Page** (`register.html`)  
   - New users can create an account.  

6. **Logout**  
   - Logs the user out and redirects to login page.  

---

## Technologies Used

- **Python 3** – Backend logic and task handling.  
- **Django** – Web framework for routing, views, models, and authentication.  
- **Bootstrap 5** – For responsive UI and styling.  
- **HTML / CSS** – Page structure and styling.  
- **SQLite** – Default database storing user accounts and tasks.  

---

## Updates

- Added **user authentication** (signup, login, logout).  
- Added **user-specific task lists**.  
- Added **login-required pages** for secure access.  
- Added **filter by deadline date**.  
- Updated UI with **icons for home and logout** buttons.  

---

