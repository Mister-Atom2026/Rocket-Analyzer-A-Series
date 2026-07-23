import json
import os
from datetime import datetime

from kivymd.uix.screen import MDScreen

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton

from kivy.metrics import dp

from calculator import calculate_thrust



def number(text):
    return float(text.replace(",", "."))



class CalculatorScreen(MDScreen):


    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        layout = MDBoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(15)
        )


        title = MDLabel(
            text="🚀 A-Series Calculator",
            halign="center",
            font_style="H5",
            size_hint_y=None,
            height=dp(50)
        )

        layout.add_widget(title)



        card = MDCard(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(10),
            radius=[20],
            size_hint_y=None,
            height=dp(330)
        )


        card.add_widget(
            MDLabel(
                text="⚙️ Дані ракети",
                font_style="H6"
            )
        )

        self.rocket_name = MDTextField(
            hint_text="🚀 Назва ракети (A6, A7...)"
        )

        self.rocket_name = MDTextField(
            hint_text="🚀 Назва ракети",
        )

        self.dry = MDTextField(
            hint_text="⚖️ Суха маса (г)",
            input_filter="float"
        )


        self.fuel = MDTextField(
            hint_text="⛽ Паливо (г)",
            input_filter="float"
        )

        self.height_input = MDTextField(
            hint_text="📏 Висота (м)",
            input_filter="float"
        )


        self.time = MDTextField(
            hint_text="⏱ Час (с)",
            input_filter="float"
        )



        card.add_widget(self.rocket_name)
        card.add_widget(self.dry)
        card.add_widget(self.fuel)
        card.add_widget(self.height_input)
        card.add_widget(self.time)



        layout.add_widget(card)



        button = MDRaisedButton(
            text="🚀 РОЗРАХУВАТИ",
            size_hint_x=1
        )


        button.bind(
            on_press=self.calculate
        )


        layout.add_widget(button)



        result_card = MDCard(
            padding=dp(20),
            radius=[20],
            size_hint_y=None,
            height=dp(220)
        )


        self.result = MDLabel(
            text="📊 Очікую запуск...",
            halign="center"
        )


        result_card.add_widget(
            self.result
        )


        layout.add_widget(result_card)



        self.add_widget(layout)




    def calculate(self, button):

        try:

            result = calculate_thrust(

                number(self.dry.text),

                number(self.fuel.text),

                number(self.height_input.text),

                number(self.time.text)

            )


            twr = result["twr"]


            if twr < 1:
                status = "🔴 Не стартує"

            elif twr < 2:
                status = "🟡 Слабкий старт"

            elif twr < 4:
                status = "🟢 Хороший старт"

            else:
                status = "🚀 Потужна ракета"



            self.result.text = (

                "🚀 Результат\n\n"

                f"Маса: {result['mass']:.3f} кг\n"

                f"Тяга: {result['thrust_kg']:.2f} кгс\n"

                f"TWR: {twr:.2f}:1\n\n"

                f"{status}"

            )
            # 💾 Збереження запуску

            rocket_name = self.rocket_name.text.strip()

            if rocket_name == "":
                rocket_name = "Без назви"

            launch = {
                "name": rocket_name,
                "date": datetime.now().strftime("%d.%m.%Y %H:%M"),

                "dry_mass": number(self.dry.text),
                "fuel_mass": number(self.fuel.text),

                "height": number(self.height_input.text),
                "time": number(self.time.text),

                "thrust_N": round(result["thrust_N"], 2),
                "thrust_kg": round(result["thrust_kg"], 2),

                "twr": round(result["twr"], 2)
            }

            file_path = "data/launches.json"

            try:

                with open(file_path, "r", encoding="utf-8") as file:
                    launches = json.load(file)

            except:

                launches = []

            launches.append(launch)

            with open(file_path, "w", encoding="utf-8") as file:

                json.dump(
                    launches,
                    file,
                    indent=4,
                    ensure_ascii=False
                )


        except Exception as error:

            self.result.text = (
                "❌ Помилка\n"
                f"{error}"
            )