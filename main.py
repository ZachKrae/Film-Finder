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
            csv_reader = csv.reader(csv_file)
            
            for line in csv_reader:
                a = Label(text=line[0], size_hint=(.5, .5), pos_hint=(0, 0))
                b = Button(text=line[3], size_hint=(.5, .5), pos_hint=(100, 100))
                self.add_widget(a)
                self.add_widget(b)

class FilmScrapeApp(App):
    pass

FilmScrapeApp().run()

# csv_file.close()