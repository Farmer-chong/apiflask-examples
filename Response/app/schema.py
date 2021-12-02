# -*- coding: utf-8 -*-
'''
    :file: schema.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2021/12/02 10:32:06
'''
from apiflask import Schema
from apiflask.fields import Integer, String, Field

HTTP_OK = 200


class BaseResponse(Schema):
    status_code = Integer()
    message = String()
    data = Field()

