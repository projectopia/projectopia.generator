# backend/modules/root/__init__.py

from flask_restx import Namespace, Resource
from .utils import hello
ns = Namespace('api/v1/', description='Root API operations')

@ns.route('/hello')
class RootResource(Resource):
    def get(self):
        result = hello()
        return {
            'message': f'{result}'
        }, 200