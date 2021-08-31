from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.metrics import dp
import csv

# with open('film-data.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     for line in csv_reader:
#         print(line)

class BoxLayoutFrame(BoxLayout):
    pass

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with open('film-data.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            for line in csv_reader:
                a = Label(text=line["title"], size_hint=(.25, .2), pos_hint=(0, 0))
                b = Label(text=line["showtime"], size_hint=(.25, .2), pos_hint=(50, 50))
                c = Label(text=line["location"], size_hint=(.25, .2), pos_hint=(100, 100))
                d = Button(text="Buy", size_hint=(.25, .2), pos_hint=(150, 150))
                self.add_widget(a)
                self.add_widget(b)
                self.add_widget(c)
                self.add_widget(d)

class FilmScrapeApp(App):
    pass

FilmScrapeApp().run()

# csv_file.close()