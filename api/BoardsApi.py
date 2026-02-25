import requests

class BoardApi:
    base_url = "https://trello.com/ru"
    
    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token

    def get_all_boards_by_org_id(self, org_id: str) -> list:
        path = ("{trello}/organizations/{id}?boards=open&board_fields=all&fields=boards".
                format(trello=self.base_url, id=org_id))
        cookie = {"token": self.token} #значение ключа из данных взять"}
        resp = requests.get(path, cookies=cookie)

        return resp.json().get("boards")

    def creat_board(self, name: str, default_list = True)-> dict:
        body = {
            'defaultLists': default_list,
            'name': name,
            "token": self.token
        }
        cookie = {"token": self.token} #значение ключа из данных взять"}
        path = "{trello}/boards/".format(trello = self.base_url)
        resp = requests.post(path, json=body, cookies=cookie)

        return resp.json()
    
    def delete_board_by_id(self, id: str):
        path = "{trello}/boards/".format(trello = self.base_url)
        cookie = {"token": self.token} #значение ключа из данных взять"}
        resp = requests.delete(path, json=cookie, cookies=cookie)

        return resp.json()
    