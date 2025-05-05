import pytest
from Geocode import geocoding, reverse_geocoding
from unittest.mock import patch, MagicMock


def test_geocoding_successful_coordinates_lookup():
    """Тест успешного получения координат по адресу"""
    with patch('geocoding.requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = [{
            "lat": "55.7558",
            "lon": "37.6176"
        }]
        mock_get.return_value = mock_response

        result = geocoding("Москва, Красная площадь")
        assert "Широта: 55.7558" in result
        assert "Долгота: 37.6176" in result


def test_geocoding_address_not_found():
    """Тест случая, когда адрес не найден"""
    with patch('geocoding.requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = []
        mock_get.return_value = mock_response

        result = geocoding("Несуществующий адрес")
        assert result == "Адрес не найден"


def test_geocoding_network_error():
    """Тест обработки ошибки сети"""
    with patch('geocoding.requests.get') as mock_get:
        mock_get.side_effect = Exception("Ошибка соединения")

        result = geocoding("Москва")
        assert "Ошибка: Ошибка соединения" in result


def test_reverse_geocoding_successful_address_lookup():
    """Тест успешного получения адреса по координатам"""
    with patch('geocoding.requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "display_name": "Москва, Кремль"
        }
        mock_get.return_value = mock_response

        result = reverse_geocoding("55.7558", "37.6176")
        assert "Москва, Кремль" in result


def test_reverse_geocoding_invalid_coordinates():
    """Тест обработки некорректных координат"""
    result = reverse_geocoding("invalid", "coordinates")
    assert "Ошибка" in result or "не найдены" in result
