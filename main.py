import webbrowser
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class SimpleBrowser(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        youtube = Button(text="Open YouTube")
        google = Button(text="Open Google")
        exit_button = Button(text="Exit")

        youtube.bind(
            on_press=lambda x: webbrowser.open(
                "https://www.youtube.com"
            )
        )

        google.bind(
            on_press=lambda x: webbrowser.open(
                "https://www.google.com"
            )
        )

        exit_button.bind(on_press=self.stop)

        layout.add_widget(youtube)
        layout.add_widget(google)
        layout.add_widget(exit_button)

        return layout


SimpleBrowser().run()