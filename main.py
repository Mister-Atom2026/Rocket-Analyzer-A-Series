from kivy.core.window import Window

# 📱 Тестовий екран телефону 16:9
Window.size = (360, 640)


from kivymd.app import MDApp

from kivy.uix.screenmanager import ScreenManager

from kivymd.uix.screen import MDScreen
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.bottomnavigation import MDBottomNavigationItem

from screens.calculator import CalculatorScreen
from screens.history import HistoryScreen
from screens.graphs import GraphsScreen
from screens.settings import SettingsScreen



class RocketAnalyzerApp(MDApp):

    def build(self):

        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark"


        navigation = MDBottomNavigation()



        # 🚀 Розрахунок

        calc_item = MDBottomNavigationItem(
            name="calc",
            text="Розрахунок",
            icon="rocket"
        )

        calc_item.add_widget(
            CalculatorScreen()
        )


        navigation.add_widget(calc_item)



        # 📚 Історія

        history_item = MDBottomNavigationItem(
            name="history",
            text="Історія",
            icon="history"
        )

        history_item.add_widget(
            HistoryScreen()
        )


        navigation.add_widget(history_item)



        # 📊 Графіки

        graph_item = MDBottomNavigationItem(
            name="graphs",
            text="Графіки",
            icon="chart-line"
        )

        graph_item.add_widget(
            GraphsScreen()
        )


        navigation.add_widget(graph_item)



        # ⚙️ Налаштування

        settings_item = MDBottomNavigationItem(
            name="settings",
            text="Налаштування",
            icon="cog"
        )

        settings_item.add_widget(
            SettingsScreen()
        )


        navigation.add_widget(settings_item)



        return navigation




RocketAnalyzerApp().run()