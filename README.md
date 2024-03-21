# Centralized
centralized system to manage tasks and projects
# Centralized Project

Overview
This Django application provides a RESTful API for managing tasks. Each task can have associated details such as due date, priority level, and assigned team members.

Features
- Create, read, update, and delete tasks
- Real-time chatroom (optional)

#Setup Instructions
1. Clone this repository.
2. Create a virtual environment and activate it.
3. Install dependencies using `pip install -r requirements.txt`.
4. Configure your database settings in `settings.py`.
5. Run migrations: `python manage.py makemigrations` and `python manage.py migrate`.
6. Create a superuser: `python manage.py createsuperuser`.
7. Start the development server: `python manage.py runserver`.
8. Access the API at [http://127.0.0.1:8000/api/tasks/](http://127.0.0.1:8000/api/tasks/).

#API Endpoints
- List tasks: GET `/api/tasks/`
- Create a task: POST `/api/tasks/`
- Retrieve a task: GET `/api/tasks/{task_id}/`
- Update a task: PUT `/api/tasks/{task_id}/`
- Delete a task: DELETE `/api/tasks/{
