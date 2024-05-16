import tkinter as tk
from weather_api import WeatherAPI
class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.weather_api = WeatherAPI()
        # Create GUI elements
        self.label = tk.Label(root, text="Weather App")
        self.label.pack()
        self.button = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.button.pack()
        self.weather_label = tk.Label(root, text="")
        self.weather_label.pack()
    def get_weather(self):
        # Retrieve weather information using the WeatherAPI class
        weather_info = self.weather_api.get_weather_info()
        # Update the weather label with the retrieved information
        self.weather_label.config(text=weather_info)
if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()