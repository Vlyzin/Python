import tkinter as tk
from tkinter import ttk
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import csv
import os


print ("Diretorio Atual", os.getcwd())

states_cities = {}  # Caminho CSV com estados e cidades
with open('simplemaps_brazil_cities_basicv1.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        state = row['admin_name']
        city_name = row['city']
        if state not in states_cities:
            states_cities[state] = []
        states_cities[state].append(city_name)

def update_cities(event, city_combobox):
    state = event.widget.get()
    cities = states_cities.get(state, [])
    city_combobox['values'] = cities
    city_combobox.set('')

def calculate_days():
    try:
        origin_state = origin_state_combobox.get()
        origin_city = origin_city_combobox.get()
        destination_state = destination_state_combobox.get()
        destination_city = destination_city_combobox.get()
        speed = float(entry_speed.get())
        hours_per_day = 8

        origin = f"{origin_city}, {origin_state}"
        destination = f"{destination_city}, {destination_state}"

        geolocator = Nominatim(user_agent="travel_calculator")
        location_origin = geolocator.geocode(origin)
        location_destination = geolocator.geocode(destination)

        if location_origin and location_destination:
            coords_origin = (location_origin.latitude, location_origin.longitude)
            coords_destination = (location_destination.latitude, location_destination.longitude)
            distance = geodesic(coords_origin, coords_destination).kilometers
            days = distance / (speed * hours_per_day)
            if days < 1:
                hours = days * hours_per_day
                result_var.set(f"O veículo levará aproximadamente {hours:.2f} horas para percorrer {distance:.2f} km de {origin} a {destination} a {speed} km/h.")
            else:
                result_var.set(f"O veículo levará aproximadamente {days:.2f} dias para percorrer {distance:.2f} km de {origin} a {destination} a {speed} km/h.")
        else:
            result_var.set("Não foi possível encontrar uma ou ambas as localizações.")
    except ValueError:
        result_var.set("Por favor, insira valores válidos.")

root = tk.Tk()
root.geometry("800x800")
root.title("Calculadora de Dias de Viagem")


tk.Label(root, text="Estado de Origem:", font="label 12 bold").pack(pady=10)
origin_state_combobox = ttk.Combobox(root, values=list(states_cities.keys()), font="label 12")
origin_state_combobox.pack(pady=5)
origin_state_combobox.bind("<<ComboboxSelected>>", lambda event: update_cities(event, origin_city_combobox))

tk.Label(root, text="Cidade de Origem:", font="label 12 bold").pack(pady=10)
origin_city_combobox = ttk.Combobox(root, font="label 12")
origin_city_combobox.pack(pady=5)


tk.Label(root, text="Estado de Destino:", font="label 12 bold").pack(pady=10)
destination_state_combobox = ttk.Combobox(root, values=list(states_cities.keys()), font="label 12")
destination_state_combobox.pack(pady=5)
destination_state_combobox.bind("<<ComboboxSelected>>", lambda event: update_cities(event, destination_city_combobox))

tk.Label(root, text="Cidade de Destino:", font="label 12 bold").pack(pady=10)
destination_city_combobox = ttk.Combobox(root, font="label 12")
destination_city_combobox.pack(pady=5)


tk.Label(root, text="Velocidade (km/h):", font="label 12 bold").pack(pady=10)
entry_speed = tk.Entry(root, font="label 12")
entry_speed.pack(pady=5)


tk.Button(root, text="Calcular", font="label 12 bold", command=calculate_days).pack(pady=20)

result_var = tk.StringVar()
result_var.set("")
tk.Label(root, textvariable=result_var, font="label 12 bold", wraplength=500).pack(pady=10)

root.mainloop()
