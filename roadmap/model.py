import base64
import roadmap

from requests import request


class Model(object):
    """
    Class comment
    """

    def __init__(self):
        pass

    def __make_request(self, method, path, data, success, error, is_local):
        url = path if is_local else "/v1" + path
        res = request(method, url=roadmap.api_base + url, data=data)

        if res is None:
            error(None, res.status_code)
        elif res.status_code is 200 or res.status_code is 201:
            if path.find(".json") > -1 or path.find(".html") > -1:
                success(res.text)
            else:
                success(res.json())

        elif res.status_code is 404 and method is "get":
            success(None)
        elif res.status_code is 403:
            error("permission denied", 403)
        elif res.body is not None:
            error(res, res.status_code)

    def get(self, path, success, error, is_local):
        self.__make_request("GET", path, None, success,
                            error, is_local is True)

    def put(self, path, data, success, error, is_local):
        self.__make_request("PUT", path, data, success,
                            error, is_local is True)

    def post(self, path, data, success, error, is_local):
        self.__make_request("POST", path, data, success,
                            error, is_local is True)

    def delete(self, path, data, success, error, is_local):
        self.__make_request("DELETE", path, data, success,
                            error, is_local is True)

    def compress_id(self, id, token):
        b64_bytes = base64.b64encode(id + "|" + token)
        return str(b64_bytes)
