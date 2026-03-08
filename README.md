# Student Notes Manager

A simple web application built using Django as part of my learning journey in web development.

---

## About This Project

This is a basic CRUD (Create, Read, Update, Delete) web application where students can manage their notes.
I built this project to practice Python and Django for the first time.
The project was done as part of my coursework and guided by my teacher.

---

## What I Learned

- How to set up a Django project from scratch
- How to create models, views, forms, and URLs in Django
- How CRUD operations work in a web application
- How to use HTML templates in Django
- How to use Git and push a project to GitHub

---

## Features

- Add a new student note with name, subject, and content
- View all notes in a table
- Edit any existing note
- Delete a note with a confirmation page

---

## Technologies Used

- Python
- Django
- HTML and CSS
- SQLite (default Django database)
- Git and GitHub

---

## How to Run This Project

Step 1 - Make sure Python and Django are installed

```
pip install django
```

Step 2 - Clone this repository

```
git clone https://github.com/Nair-Adhithyan-Vijaykumar/student-notes-manager.git
cd student-notes-manager
```

Step 3 - Run the migrations

```
python manage.py migrate
```

Step 4 - Start the server

```
python manage.py runserver
```

Step 5 - Open your browser and go to

```
http://127.0.0.1:8000
```

---

## Project Structure

```
notes_project/
    notes/
        templates/
            notes/
                base.html
                note_list.html
                note_form.html
                note_confirm_delete.html
        models.py
        views.py
        forms.py
        urls.py
    notes_project/
        settings.py
        urls.py
    manage.py
```

---

## About Me

I am a student currently learning Python and Django web development.
This project is one of my first hands-on projects where I applied what I learned in class.

---

## Note

This is a beginner level project made for learning purposes only.
It is not meant for production use.
