# -*-coding:utf-8-*-
import json

class BytesEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o,bytes):
            return o.decode()
        return json.JSONEncoder.default(self, o)