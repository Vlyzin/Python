import tkinter as tk
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def calculate_days():
    try:
        origin = entry_origin.get()
        destination = entry_destination.get()
        speed = float(entry_speed.get())
        hours_per_day = 8

        geolocator = Nominatim(user_agent="travel_calculator")
        location_origin = geolocator.geocode(origin)
        location_destination = geolocator.geocode(destination)

        if location_origin and location_destination:
            coords_origin = (location_origin.latitude, location_origin.longitude)
            coords_destination = (location_destination.latitude, location_destination.longitude)
            distance = geodesic(coords_origin, coords_destination).kilometers
            days = distance / (speed * hours_per_day)
            result_var.set(f"O veículo levará aproximadamente {days:.2f} dias para percorrer {distance:.2f} km de {origin} a {destination} a {speed} km/h.")
        else:
            result_var.set("Não foi possível encontrar uma ou ambas as localizações.")
    except ValueError:
        result_var.set("Por favor, insira valores válidos.")

root = tk.Tk()
root.geometry("600x400")
root.title("Calculadora de Dias de Viagem")

tk.Label(root, text="Cidade e Estado de Origem:", font="lucida 12 bold").pack(pady=10)
entry_origin = tk.Entry(root, font="lucida 12")
entry_origin.pack(pady=5)

tk.Label(root, text="Cidade e Estado de Destino:", font="lucida 12 bold").pack(pady=10)
entry_destination = tk.Entry(root, font="lucida 12")
entry_destination.pack(pady=5)

tk.Label(root, text="Velocidade (km/h):", font="lucida 12 bold").pack(pady=10)
entry_speed = tk.Entry(root, font="lucida 12")
entry_speed.pack(pady=5)

tk.Button(root, text="Calcular", font="lucida 12 bold", command=calculate_days).pack(pady=20)

result_var = tk.StringVar()
result_var.set("")
tk.Label(root, textvariable=result_var, font="lucida 12 bold", wraplength=500).pack(pady=10)

root.mainloop()