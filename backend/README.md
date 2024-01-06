# WARNING

- For development, go to backend folder and use `flask run` command.

```bash
cd backend

# For debug
flask run --reload

# For deployment
gunicorn -c gunicorn.conf.py wsgi:app
```