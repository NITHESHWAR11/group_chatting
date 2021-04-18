from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import requests


class WelcomeScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class SignIn(Screen):
    pass


class Signup(Screen):
    pass


se = ScreenManager()
se.add_widget(SignIn(name='sign in'))
se.add_widget(Signup(name='sign up'))
se.add_widget(WelcomeScreen(name='WelcomeScreen'))
se.add_widget(MainScreen(name='mainScreen'))


class Chatting(MDApp):
    firebase_url = "https://chatting-application-a964d-default-rtdb.firebaseio.com/.json"

    def build(self):
        return Builder.load_file('kv/style.kv')

    def show_data(self):
        name = self.root.get_screen('sign in').ids.username.text
        password = self.root.get_screen('sign in').ids.Password.text
        email_id = self.root.get_screen('sign in').ids.Email.text
        data = {
            name: {
                "name": name,
                "Password": password,
                "Email Id": email_id,
            }
        }
        e = requests.post(url=self.firebase_url, json=data)


if __name__ == '__main__':
    Chatting().run()

