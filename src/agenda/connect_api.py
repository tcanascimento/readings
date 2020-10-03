from requests import request


class ConnectApi:

    def __init__(self) -> None:
        super().__init__()
        self.url_base = "http://localhost:5000"

    def get_user(self, user=None):
        # response = request("GET", self.url_base+"/user/"+user)
        # print(response)
        # return response
        return "beatles"
