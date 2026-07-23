import json
import os


from kivymd.uix.screen import MDScreen

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView

from kivy.metrics import dp



FILE = "data/launches.json"



class HistoryScreen(MDScreen):


    def __init__(self, **kwargs):

        super().__init__(**kwargs)


        root = MDBoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(15)
        )


        title = MDLabel(

            text="📚 Історія запусків",

            halign="center",

            font_style="H5",

            size_hint_y=None,

            height=dp(50)

        )


        root.add_widget(title)



        scroll = MDScrollView()



        self.list_box = MDBoxLayout(

            orientation="vertical",

            spacing=dp(10),

            size_hint_y=None

        )


        self.list_box.bind(

            minimum_height=self.list_box.setter("height")

        )



        scroll.add_widget(
            self.list_box
        )


        root.add_widget(scroll)



        self.add_widget(root)



        self.load_history()




    def load_history(self):


        self.list_box.clear_widgets()



        if not os.path.exists(FILE):

            self.add_card(
                "🚀 Поки запусків немає"
            )

            return



        with open(
            FILE,
            "r",
            encoding="utf-8"
        ) as file:

            launches = json.load(file)



        if len(launches) == 0:

            self.add_card(
                "🚀 Поки запусків немає"
            )

            return



        for launch in launches:


            text = (

                f"🚀 {launch['name']}\n\n"

                f"📏 Висота: {launch['height']} м\n"

                f"⚡ Тяга: {launch.get('thrust_kg', 0)} кгс\n"

                f"🚀 TWR: {launch['twr']}\n"

            )


            self.add_card(text)




    def add_card(self, text):


        card = MDCard(

            padding=dp(15),

            radius=[20],

            size_hint_y=None,

            height=dp(140)

        )


        label = MDLabel(

            text=text

        )


        card.add_widget(label)


        self.list_box.add_widget(card)