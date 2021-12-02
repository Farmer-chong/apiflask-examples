# -*- coding: utf-8 -*-
'''
    :file: utils.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2021/12/02 10:34:56
'''

from typing import Union
from flask import make_response


def make_resp(payload: any,
              status_code: int = 200,
              http_status_code: int = 200,
              message: str = "ok") -> Union[dict, int]:
    """格式化响应

    Args:
        payload (any): 状态码
        status_code (int, optional): 消息内容. Defaults to 200.
        http_status_code (int, optional): http状态码. Defaults to 200.
        message (str, optional): 响应主体. Defaults to "ok".

    Returns:
        Union[dict, int]: 格式化后的响应体、http状态码
    """

    return {
        'status_code': status_code,
        'message': message,
        'data': payload
    }, http_status_code


class Result():
    status_code: int = 200
    message: str = "ok"
    data: any = None

    @classmethod
    def ok(self):
        result = Result()
        result.status_code = 200
        result.message = "ok"
        return result

    @classmethod
    def error(self):
        result = Result()
        result.status_code = 500
        result.message = "err"
        return result

    def setMessage(self, message: str):
        self.message = message
        return self

    def setCode(self, status_code: int):
        self.status_code = status_code
        return self

    def setData(self, data):
        self.data = data
        return self

    def to_dict(self) -> dict:
        return make_resp(self.data, self.status_code, self.message)
