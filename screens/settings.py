from kivymd.uix.screen import MDScreen

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel

from kivy.metrics import dp


class SettingsScreen(MDScreen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        layout = MDBoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(15)
        )


        title = MDLabel(
            text="⚙️ Налаштування",
            halign="center",
            font_style="H5",
            size_hint_y=None,
            height=dp(50)
        )

        layout.add_widget(title)



        # Тема

        theme_card = MDCard(

            orientation="vertical",
            padding=dp(15),
            radius=[20],
            size_hint_y=None,
            height=dp(130)

        )


        theme_card.add_widget(

            MDLabel(
                text="🌙 Тема",
                font_style="H6"
            )

        )


        theme_card.add_widget(

            MDLabel(
                text="Використовується темна тема",
                theme_text_color="Secondary"
            )

        )


        layout.add_widget(theme_card)



        # Одиниці


        units_card = MDCard(

            orientation="vertical",
            padding=dp(15),
            radius=[20],
            size_hint_y=None,
            height=dp(160)

        )


        units_card.add_widget(

            MDLabel(
                text="📏 Одиниці",
                font_style="H6"
            )

        )


        units_card.add_widget(

            MDLabel(
                text=
                "Сила: Ньютон (N)\n"
                "Маса: кілограми (kg)\n"
                "Швидкість: м/с"
            )

        )


        layout.add_widget(units_card)



        # Про програму


        about_card = MDCard(

            orientation="vertical",
            padding=dp(15),
            radius=[20],
            size_hint_y=None,
            height=dp(200)

        )


        about_card.add_widget(

            MDLabel(

                text=
                "🚀 Rocket Analyzer A-Series\n\n"
                "Версія: 1.0\n"
                "Python + KivyMD\n\n"
                "Програма для аналізу "
                "характеристик запусків ракет.\n\n"
                "© Mister-Atom2026"

            )

        )


        layout.add_widget(about_card)



        self.add_widget(layout)