import tkinter as tk
from tkinter import messagebox, Listbox
from PIL import Image, ImageTk
import requests
import io
from datetime import datetime
from weather import get_weather_data
from storage import save_weather_data

# Türkiye'deki 81 ilin tam listesi
CITIES = [
    "Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin",
    "Aydın", "Balıkesir", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa",
    "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Edirne", "Elazığ", "Erzincan",
    "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay",
    "Isparta", "Mersin", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli",
    "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş",
    "Mardin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Rize", "Sakarya", "Samsun",
    "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Şanlıurfa",
    "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman", "Kırıkkale",
    "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis",
    "Osmaniye", "Düzce"
]

def clear_placeholder(event):
    if city_entry.get() == "Örnek: İstanbul":
        city_entry.delete(0, tk.END)
        city_entry.config(fg="black")

def set_placeholder(event):
    if not city_entry.get():
        city_entry.insert(0, "Örnek: İstanbul")
        city_entry.config(fg="gray")

def fetch_weather():
    city = city_entry.get().strip()
    if not city or city == "Örnek: İstanbul":
        messagebox.showwarning("Uyarı", "Lütfen bir şehir adı girin.")
        return

    try:
        data = get_weather_data(city)
    except Exception as e:
        messagebox.showerror("Hata", f"Hava durumu alınırken hata oluştu:\n{e}")
        return

    if data:
        result_label.config(text=f"{data['city']} için hava durumu", fg="#333")
        temperature_label.config(text=f"🌡 Sıcaklık: {data['temperature']}°C")
        description_label.config(text=f"📝 Açıklama: {data['description'].capitalize()}")
        humidity_label.config(text=f"💧 Nem: %{data['humidity']}")
        time_label.config(text="")

        icon_code = data.get("icon")
        if icon_code:
            icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
            icon_response = requests.get(icon_url)
            if icon_response.status_code == 200:
                image_data = icon_response.content
                image = Image.open(io.BytesIO(image_data))
                photo = ImageTk.PhotoImage(image)
                icon_label.config(image=photo)
                icon_label.image = photo
        else:
            icon_label.config(image='')
            icon_label.image = None

        save_weather_data(data)
    else:
        messagebox.showerror("Hata", "Hava durumu alınamadı.")

# Autocomplete fonksiyonu
def update_listbox(event):
    typed = city_entry.get()
    listbox.delete(0, tk.END)
    if typed:
        suggestions = [city for city in CITIES if city.lower().startswith(typed.lower())]
        for city in suggestions:
            listbox.insert(tk.END, city)
        listbox.place(x=city_entry.winfo_x(), y=city_entry.winfo_y() + city_entry.winfo_height())
    else:
        listbox.place_forget()

def fill_city_from_listbox(event):
    selected = listbox.get(tk.ACTIVE)
    city_entry.delete(0, tk.END)
    city_entry.insert(0, selected)
    listbox.place_forget()

# Arayüz
window = tk.Tk()
window.title("🌤 Hava Durumu Uygulaması")
window.geometry("420x500")
window.configure(bg="#e6f0fa")

tk.Label(window, text="Şehir Adı Girin", font=("Arial", 14), bg="#e6f0fa").pack(pady=10)

city_entry = tk.Entry(window, width=30, font=("Arial", 12), fg="gray")
city_entry.pack(pady=5)
city_entry.insert(0, "Örnek: İstanbul")
city_entry.bind("<FocusIn>", clear_placeholder)
city_entry.bind("<FocusOut>", set_placeholder)
city_entry.bind("<KeyRelease>", update_listbox)

listbox = Listbox(window, width=30, font=("Arial", 11))
listbox.bind("<<ListboxSelect>>", fill_city_from_listbox)

fetch_button = tk.Button(window, text="Hava Durumunu Getir", command=fetch_weather,
                         font=("Arial", 12), bg="#4682b4", fg="white", activebackground="#315f91")
fetch_button.pack(pady=10)

icon_label = tk.Label(window, bg="#e6f0fa")
icon_label.pack()

result_label = tk.Label(window, text="", font=("Arial", 14, "bold"), bg="#e6f0fa")
result_label.pack(pady=5)

temperature_label = tk.Label(window, text="", font=("Arial", 12), bg="#e6f0fa")
temperature_label.pack()

description_label = tk.Label(window, text="", font=("Arial", 12), bg="#e6f0fa")
description_label.pack()

humidity_label = tk.Label(window, text="", font=("Arial", 12), bg="#e6f0fa")
humidity_label.pack()

time_label = tk.Label(window, text="", font=("Arial", 10, "italic"), bg="#e6f0fa", fg="#555")
time_label.pack(pady=(5, 0))

window.mainloop()
