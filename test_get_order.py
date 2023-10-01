import sender_stand_request
import data

# Функция - получение данных о заказе по треку

def test_get_order_info_by_track():
    track_number = sender_stand_request.get_order_info_by_track()
    assert track_number.status_code == 200

# Проверили, что код ответа равен 200