import requests
from urllib.parse import quote
import tkinter as tk
from tkinter import ttk, messagebox

def geocode(address):
    """Ищет координаты по адресу"""
    url = f"https://nominatim.openstreetmap.org/search?q={quote(address)}&format=json"
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        data = response.json()
        if data:
            return f"Широта: {data[0]['lat']}\nДолгота: {data[0]['lon']}"
        return "Адрес не найден"
    except Exception as e:
        return f"Ошибка: {e}"

def reverse_geocode(lat, lon):
    """Ищет адрес по координатам"""
    url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        data = response.json()
        return data.get("display_name", "Координаты не найдены")
    except Exception as e:
        return f"Ошибка: {e}"

def on_search():
    """Кнопка 'Найти адрес'"""
    address = entry_address.get()
    if address:
        result = geocode(address)
        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, result)
    else:
        messagebox.showwarning("Ошибка", "Введите адрес")

def on_reverse():
    """Кнопка 'Найти по координатам'"""
    lat = entry_lat.get()
    lon = entry_lon.get()
    if lat and lon:
        result = reverse_geocode(lat, lon)
        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, result)
    else:
        messagebox.showwarning("Ошибка", "Введите координаты")

root = tk.Tk()
root.title("Геокодер для своих")
root.geometry("500x400")

frame_address = ttk.Frame(root)
frame_address.pack(pady=10)

ttk.Label(frame_address, text="Адрес:").pack(side=tk.LEFT)
entry_address = ttk.Entry(frame_address, width=40)
entry_address.pack(side=tk.LEFT, padx=5)
ttk.Button(frame_address, text="Найти", command=on_search).pack(side=tk.LEFT)

frame_coords = ttk.Frame(root)
frame_coords.pack(pady=10)

ttk.Label(frame_coords, text="Широта:").pack(side=tk.LEFT)
entry_lat = ttk.Entry(frame_coords, width=15)
entry_lat.pack(side=tk.LEFT, padx=5)

ttk.Label(frame_coords, text="Долгота:").pack(side=tk.LEFT)
entry_lon = ttk.Entry(frame_coords, width=15)
entry_lon.pack(side=tk.LEFT, padx=5)
ttk.Button(frame_coords, text="Найти адрес", command=on_reverse).pack(side=tk.LEFT)

text_result = tk.Text(root, height=10, width=60)
text_result.pack(pady=20)

root.mainloop()