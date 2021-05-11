

class Response:
    def __init__(self, json_response) -> None:

        if json_response['status'] == 'ok':
            self._status = True
            self._data = json_response['data']
        else:
            self._status = False
            self._error_code = json_response['errorcode']
            self._error_message = json_response['error']
        self.resp = json_response

    def __repr__(self) -> str:
        return str(self.resp)

    def is_ok(self) -> bool:
        return self._status

    def get_data(self) -> dict:
        if self._status == True:
            return self._data
        else:
            return {}  # todo raise exceptions..

    def get_error_code(self) -> int:
        if self._status == False:
            return self._error_code
        else:
            return -1  # todo raise exceptions..

    def get_error_message(self) -> str:
        if self._status == False:
            return self._error_message
        else:
            return ''  # todo raise exceptions..
