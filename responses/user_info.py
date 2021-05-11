
from responses.response import Response

class User:
    def __init__(self) -> None:
        pass
    def __init__(self, response) -> None:
        self.id = response['id']
        self.name = response['user']
        self.premium = response['premium']
        self.color = response['color']

class UserResponse(Response):
    def __init__(self, json_response) -> None:
        super().__init__(json_response)

    def get_data(self) -> User:
        if self._status == True:
            return User(self._data)
        else:
            return User() # raise exceptions