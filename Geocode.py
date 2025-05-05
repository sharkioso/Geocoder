import requests
from urllib.parse import quote


def geocoding(address):
    """Ищет координаты по адресу (возвращает строку с широтой/долготой)"""
    url = f"https://nominatim.openstreetmap.org/search?q={quote(address)}&format=json"
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        data = response.json()
        if data:
            return f"Широта: {data[0]['lat']}\nДолгота: {data[0]['lon']}"
        return "Адрес не найден"
    except Exception as e:
        return f"Ошибка: {e}"


def reverse_geocoding(lat, lon):
    """Ищет адрес по координатам (возвращает строку с адресом)"""
    url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        data = response.json()
        return data.get("display_name", "Координаты не найдены")
    except Exception as e:
        return f"Ошибка: {e}"
