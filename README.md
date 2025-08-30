ECHO is on.
# Task Manager Project

A full-featured Django Task Management app with:

- User authentication (login, logout, register)
- CRUD for tasks and categories
- Task priority and due date
- Filter/search tasks
- Email notifications & reminders (if configured)
- Nice Bootstrap-based UI

## Setup Instructions

1. Clone the repository:
git clone https://github.com/yourusername/task_manager.git

2. Install dependencies:
pip install -r requirements.txt

3. Apply migrations:
python manage.py migrate

4. Create superuser:
python manage.py createsuperuser

5. Run the server:
python manage.py runserver

## Usage

- Sign up or log in
- Add, update, delete tasks
- Filter and search tasks

## License

MIT
Optionally, create requirements.txt:
pip freeze > requirements.txt
