from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
import json,glob
from datetime import datetime
from pathlib import Path
import random
from hoverable import HoverBehavior
from kivy.uix.image import Image
import time
from kivy.uix.behaviors import ButtonBehavior

Builder.load_file("frontend.kv")

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"
    def login(self,user,passw):
        with open("users.json") as file:
            usern = json.load(file)
        if user in usern and usern[user]["password"] == passw:
            self.manager.current = "login_screen_success" 
        else:
            self.ids.wrong.text = "Wrong username or password!"
    def go_to_forgot_password(self):
        self.manager.current = "forgot_pass"

class rootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def add_value(self,user,passw):
        with open("users.json") as file:
            users = json.load(file)
        
        users[user] = {"username":user,"password":passw,"created":datetime.now().strftime("%Y-%m-%d %H-%M-%S")}

        with open("users.json","w") as file:
            json.dump(users,file)

        self.manager.current = "sign_up_page_success"
    

class SignUpScreenSuccess(Screen):
    def main_page(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"
    def get_quote(self,feel):
        feel = feel.lower()
        available_feelings = glob.glob("quotes/*txt")
        available_feelings = [Path(filename).stem for filename in available_feelings]
        if feel in available_feelings:
            with open("quotes/" + str(feel) + ".txt",encoding="utf8") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another feeling"

class ImageButton(ButtonBehavior,HoverBehavior,Image):
    pass

class ForgotPassword(Screen):
    def change_password(self,user_name, new_pass):
        with open("users.json") as file:
            users = json.load(file)       
        users[user_name] = {'username':user_name, 'password':new_pass, 'created': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        
        if users[user_name]['username'] == user_name:
            with open("users.json", "w") as file:
                users[user_name]['password'] = new_pass
                json.dump(users, file)
            self.ids.password_status.text = "Password changed successfully"
            time.sleep(1)
            self.manager.transition.direction = "right"
            self.manager.current="login_screen"
        else:
            self.ids.password_status.text = "Try Again"

class MainApp(App):
    def build(self):
        return rootWidget()

if __name__ == "__main__":
    MainApp().run()