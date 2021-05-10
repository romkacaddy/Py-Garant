import requests

# https://online-garant.net/doc
class PyGarant():
    authority = 'https://api.online-garant.net/'

    def __init__(self, token, app_id=10):
        self.token = token
        self.app_id = app_id

    def _get_default_params(self) -> dict:
        return {
            'appid': self.app_id,
            'token': self.token
        }

    def _make_request(self, action, params) -> dict:
        resp = requests.get(self.authority + action, params=params)
        return resp.json()

    def get_user_info(self) -> dict:
        '''
        Получение информации о пользователе
        '''
        params = self._get_default_params()
        return self._make_request('userinfo', params)

    def sell_account(self, server, login, password, account_description, price, notify, onlymoney,  sellmsg=None, test=1) -> dict:
        '''
        Продажа аккаунта

        appid - ID приложения
        token - Токен пользователя
        server - IP сервера либо код сервиса (wot, steam, psn)
        login - Логин продаваемого аккаунта
        password - Пароль продаваемого аккаунта
        text - Описание аккаунта
        sellermsg - Сообщение от продавца. Необязательный параметр
        price - Цена в рублях
        notify - Уведомление о продаже. 1 либо 0
        onlymoney - Показывать только деньги при проверке. 1 либо 0
        test - Указывайте этот параметр, если хотите протестировать своё приложение и не выкладывать аккаунт на продажу.
        '''
        params = self._get_default_params()
        params.update(
            {
                'server': server,
                'login': login,
                'password': password,
                'text': account_description,
                'price': price,
                'notify': notify,
                'onlymoney': onlymoney,
                'test': test
            }
        )
        if sellmsg != None:
            params.update({'sellmsg': sellmsg})

        return self._make_request('sell', params)

    def set_money_information(self, isauto, servercodes, price=None, avail=0, min_order=None) -> dict:
        '''
        Объявление о продаже

        Для работы этого метода, сначала нужно вручную создать объявления о продаже, если их не было раньше.
        В режиме автоматической выдачи, объявление будет в списке всегда, даже если продавец оффлайн.

        Параметры
        isauto - Обязательный. 1 - Автоматический режим, 0 - ручной режим.
        servercode[] - Обязательный. Может быть указан несколько раз в одном запросе. Должен содержать код сервера. (см. ниже).
        price - Цена за 1кк. Цена должна быть не самой низкой. Необязательный.
        min - Минимальное количество для заказа. Больше 9999. Необязательный.
        avail - Сколько есть в наличии. 0 - снять с продажи. Необязательный.
        '''

        params = self._get_default_params()
        params.update(
            {
                'act': 'setInfo',
                'isauto': isauto,
                'servercodes': servercodes,
                'avail': avail
            }
        )
        if price != None:
            params.update({'price': price})
        if min_order != None:
            params.update({'min': min_order})

        return self._make_request('money', params)

    def get_orders(self) -> dict:
        '''
        Метод возвращает все незавершённые сделки, для которых была включена автоматическая выдача
        '''
        params = self._get_default_params()
        params.update(
            {
                'act': 'getOrders'
            }
        )
        print(params)
        return self._make_request('money', params)

    def accept_deal(self, deal_id) -> dict:
        '''
        Принять сделку. Должен отправляться тогда, когда бот начинает работу по выдаче заказа
        '''
        params = self._get_default_params()
        params.update(
            {
                'dealid': deal_id,
                'act': 'acceptDeal'
            }
        )
        return self._make_request('money', params)

    def cancel_deal(self, deal_id) -> dict:
        '''
        Отменить сделку
        '''
        params = self._get_default_params()
        params.update(
            {
                'dealid': deal_id,
                'act': 'cancelDeal'
            }
        )
        return self._make_request('money', params)

    def done_deal(self, deal_id) -> dict:
        '''
        Завершить сделку
        '''
        params = self._get_default_params()
        params.update(
            {
                'dealid': deal_id,
                'act': 'doneDeal'
            }
        )
        return self._make_request('money', params)

    def send_message(self, deal_id, message_body) -> dict:
        '''
        Отправить сообщение
        '''
        params = self._get_default_params()
        params.update(
            {
                'dealid': deal_id,
                'msg': message_body
            }
        )
        return self._make_request('sendMessage', params)
