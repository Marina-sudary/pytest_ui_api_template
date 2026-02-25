import json

my_file = open('test_data.json')
global_data = json.load(my_file)

class DataProvider:

    def __init__(self) -> None:
        self.data = global_data

    # можно делать общие методы
    def get(self, prop: str) -> str:
        return self.data.get(prop)
    
    def get(self, prop: str) -> int:
        val = self.data.get(prop)
        return int(val)
    
    #можно делать специфичные методы
    def get_token(self) -> str:
        return self.data.get("token")