import configuration
import requests
import data

# 1. Функция - запрос на создание заказа
def create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json = order_body)

# 2. Функция - сохранение номера трека заказа
def save_order_track():
    track_response = create_order(data.order_body)
    return track_response.json()["track"]

# 3. Функция - выполнить запрос на получения заказа по треку заказа
# (номеру отслеживания)
def get_order_info_by_track():
    track = save_order_track()
    par = {"t": track}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO_BY_TRACK_PATH,
                        params = par)
