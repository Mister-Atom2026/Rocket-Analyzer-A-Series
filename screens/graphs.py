import json
import os

from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

from matplotlib.figure import Figure


class GraphsScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = MDBoxLayout(
            orientation="vertical"
        )

        layout.add_widget(
            MDLabel(
                text="📊 TWR ракет",
                halign="center",
                size_hint_y=None,
                height=50
            )
        )

        layout.add_widget(
            self.create_graph()
        )

        self.add_widget(layout)



    def create_graph(self):

        path = "data/launches.json"


        fig = Figure()

        ax = fig.add_subplot(111)



        if not os.path.exists(path):

            ax.text(
                0.5,
                0.5,
                "Немає даних",
                ha="center"
            )

            return FigureCanvasKivyAgg(fig)



        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            launches = json.load(f)



        names = [
            x.get("name", "Без назви")
            for x in launches
        ]


        values = [
            x.get("twr", 0)
            for x in launches
        ]



        ax.bar(
            names,
            values
        )



        ax.set_title(
            "Порівняння TWR"
        )


        ax.set_ylabel(
            "TWR"
        )

        if not values:
            values = [0]

        ax.set_ylim(
            0,
            max(values) + 1
        )


        ax.grid(
            axis="y"
        )


        return FigureCanvasKivyAgg(fig)