import tkinter as tk
from weather import WeatherAPI
class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")
        self.geometry("400x300")
        self.weather_api = WeatherAPI()
        self.label = tk.Label(self, text="Enter city name:")
        self.label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.button = tk.Button(self, text="Get Weather", command=self.get_weather)
        self.button.pack()
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()
    def get_weather(self):
        city = self.entry.get()
        weather_data = self.weather_api.get_weather(city)
        self.result_label.config(text=weather_data)
def main():
    app = WeatherApp()
    app.mainloop()
if __name__ == "__main__":
    main()