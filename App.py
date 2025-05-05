import tkinter as tk
from tkinter import ttk, messagebox
from Geocode import geocoding, reverse_geocoding  # Импорт функций из Geocode.py

def on_search():
    """Кнопка 'Найти адрес'"""
    address = entry_address.get()
    if address:
        result = geocoding(address)
        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, result)
    else:
        messagebox.showwarning("Ошибка", "Введите адрес")

def on_reverse():
    """Кнопка 'Найти по координатам'"""
    lat = entry_lat.get()
    lon = entry_lon.get()
    if lat and lon:
        result = reverse_geocoding(lat, lon)
        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, result)
    else:
        messagebox.showwarning("Ошибка", "Введите координаты")

# Создание окна
root = tk.Tk()
root.title("Геокодер")
root.geometry("500x400")

# Поле для ввода адреса
frame_address = ttk.Frame(root)
frame_address.pack(pady=10)
ttk.Label(frame_address, text="Адрес:").pack(side=tk.LEFT)
entry_address = ttk.Entry(frame_address, width=40)
entry_address.pack(side=tk.LEFT, padx=5)
ttk.Button(frame_address, text="Найти", command=on_search).pack(side=tk.LEFT)

# Поля для координат
frame_coords = ttk.Frame(root)
frame_coords.pack(pady=10)
ttk.Label(frame_coords, text="Широта:").pack(side=tk.LEFT)
entry_lat = ttk.Entry(frame_coords, width=15)
entry_lat.pack(side=tk.LEFT, padx=5)
ttk.Label(frame_coords, text="Долгота:").pack(side=tk.LEFT)
entry_lon = ttk.Entry(frame_coords, width=15)
entry_lon.pack(side=tk.LEFT, padx=5)
ttk.Button(frame_coords, text="Найти адрес", command=on_reverse).pack(side=tk.LEFT)

# Поле для вывода результата
text_result = tk.Text(root, height=10, width=60)
text_result.pack(pady=20)

root.mainloop()