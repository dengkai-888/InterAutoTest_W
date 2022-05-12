import requests


class RequestUtils:
    # 定义公共方法
    def request_api(self, url, method, headers=None, json=None):
        if method == "get":
            r = requests.get(url, headers=headers)
        elif method == "post":
            r = requests.post(url=url, headers=headers, json=json)
        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        res = dict()
        res["code"] = code
        res["body"] = body
        return res  # 返回字典

    # 重构get方法
    def request_get(self, url, method, **kwargs):
        self.request_api(url, method, **kwargs)

    # 重构post方法
    def request_post(self, url, method, **kwargs):
        self.request_api(url, method, **kwargs)


if __name__ == "__main__":
    pass
