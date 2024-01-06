# WARNING

- For development, go to backend folder and use `flask run` command.
- For deployment, run this backend app **only on root folder**, not in this backend folder.

```bash
# For debug
cd backend
flask run --reload

# For deployment
gunicorn -c backend/gunicorn.conf.py backend.wsgi:app
```