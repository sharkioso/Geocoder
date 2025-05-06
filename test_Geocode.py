from unittest.mock import patch, MagicMock
from Geocode import geocoding, reverse_geocoding


def test_geocoding_success():
    mock_response = MagicMock()
    mock_response.json.return_value = [{"lat": "55.7558", "lon": "37.6176"}]

    # Изменяем target для patch:
    with patch('requests.get', return_value=mock_response) as mock_get:
        result = geocoding("Москва")
        assert "Широта: 55.7558" in result
        assert "Долгота: 37.6176" in result
        mock_get.assert_called_once()


def test_geocoding_fail():
    mock_response = MagicMock()
    mock_response.json.return_value = []

    with patch('requests.get', return_value=mock_response):
        result = geocoding("Деревня Гадюкино")
        assert result == "Адрес не найден"


def test_reverse_geocoding_success():
    mock_response = MagicMock()
    mock_response.json.return_value = {"display_name": "Москва, Россия"}

    with patch('requests.get', return_value=mock_response):
        result = reverse_geocoding("55.7558", "37.6176")
        assert "Москва, Россия" in result


def test_reverse_geocoding_fail():
    with patch('requests.get', side_effect=Exception("Ошибка API")):
        result = reverse_geocoding("abc", "xyz")
        assert "Ошибка" in result
