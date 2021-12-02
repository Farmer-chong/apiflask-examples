# -*- coding: utf-8 -*-
'''
    :file: __init__.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2021/12/02 10:29:27
'''

from apiflask import APIFlask
from app.schema import BaseResponse
from app.views import test_bp

def create_app(config:str='development') -> APIFlask:
    app = APIFlask(__name__)
    # 配置基础响应schema
    app.config['BASE_RESPONSE_SCHEMA'] = BaseResponse
    app.config['BASE_RESPONSE_DATA_KEY '] = 'data'

    registry_blueprints(app)
    return app

def registry_blueprints(app:APIFlask):
    app.register_blueprint(test_bp, url_prefix="/")