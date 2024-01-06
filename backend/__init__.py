from flask import Flask
from flask_restx import Api
from werkzeug.middleware.proxy_fix import ProxyFix
from backend.home import home_template
from backend.modules.api.v1 import ns as api_v1_ns

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route("/")
def home(): 
    return home_template

api = Api(
    app,
    version='1.0',
    title='Projectopia API',
    description='WARNING: DO NOT USE THIS IF YOU ARE NOT PROJECTOPIA INTERNAL DEVELOPER',
    doc='/docs',
) 

api.add_namespace(api_v1_ns)
