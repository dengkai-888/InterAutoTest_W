import requests
from utils.RequestsUtils import RequestUtils


# 定义测试数据
url_get = "https://timc.sinoxk.cn/lingtong-service/app/drug/selectSort"
url_post = "https://timc.sinoxk.cn/lingtong-service/app/people/peopleBase"
headers = {
    "content-type": "application/json;charset=UTF-8",
    "token": "TSmCjLjvMUvLpO5fu8eD1IitvRcvehgq+8oKQ15+f3Xqz4hgOKGoreGubmieT8JHHglJemTkczHAzyyYG70s+w=="
}
post_data = {"brand":"华润三九医药-三九胃泰胶囊"}


def test_get():
    h = RequestUtils()
    r = h.request_get(url=url_get, method="get", headers=headers)
    print(r)
    print("-------------------------")


def test_post():
    # r = request_post(url=url_post, headers=headers, json=post_data)
    # print(r)
    pass



if __name__ == '__mani__':
    test_get()
