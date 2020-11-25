'''
Application example using build() + return
==========================================
An application can be built if you return a widget on build(), or if you set
self.root.
'''
import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.storage.jsonstore import JsonStore
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.uix.popup import Popup
import json
import datetime
  
store = JsonStore('hell.json')

nameper = ObjectProperty(None)
pname = ObjectProperty(None)
pername = ObjectProperty(None)
addinormation = ObjectProperty(None)
clock = ObjectProperty(None)
alrm_name = ObjectProperty(None)
alrm_time = ObjectProperty(None)

class Manager(ScreenManager):
    main_screen= ObjectProperty(None)
    second_screen= ObjectProperty(None) #WELCOME
    third_screen= ObjectProperty(None)
    fourth_screen= ObjectProperty(None)
    fifth_screen= ObjectProperty(None) #NewUser
    sixth_screen= ObjectProperty(None) #Alarms

class MainWindow(Screen):  
    clk = StringProperty()
    def on_enter(self):
        ct = str(datetime.datetime.now())
        self.dt = ct[:10]
        self.clk = ct[10:19]

    def btn(self):
        a = len(self.nameper.text)
        if a == 0:
            self.manager.current = "main"
        else:
            if store.exists(self.nameper.text):
                ThirdWindow.login_id = self.nameper.text
                self.manager.current = "second"

            else:
                self.manager.current = "fifth"
        #clear input
        self.nameper.text = ""

    def pop(self):
        help_text= '                                                            Tutorial on how to navigate through app. \n \n              1.On the main page, enter your name into the white box next to, "Type your name:"\n\n              2. If you are a NEW User, enter the information being asked when redirected to a new window. \n\n                  Hit submit afterwards.\n\n              3. If you are a returning user, you are redirected to a different window where you can modify or  \n\n                  add more perscriptions and alarms. \n\n CLICK ANYWHERE OUTSIDE THE POPUP TO EXIT HELP'
      
        popup = Popup(title='Help: How to Navigate App', content=Label(text=help_text),size_hint=(None, None), size=(760, 400))
        popup.open()

class SecondWindow(Screen): #WElcomeMenu
    def btn(self):
        store.put(self.pname.text, name=self.pname.text, perscription=self.pername.text, addinfo= self.addinormation.text)
        print(store.get(self.pname.text)['name'])
        self.manager.current = "main"
    

class ThirdWindow(Screen): #CurrPresc
    namee = StringProperty()
    perscription = StringProperty()
    addinfo = StringProperty()
    login_id = ""

    def on_enter(self):
        self.namee = store.get(self.login_id)['name']
        self.perscription = store.get(self.login_id)['perscription']
        self.addinfo = store.get(self.login_id)['addinfo']

class FourthWindow(Screen): #AddPresc
    def btn(self):
        store.put(self.pname.text, name=self.pname.text, perscription=self.pername.text,
                  addinfo=self.addinormation.text)
                  
        print(store.get(self.pname.text)['name'])
        #clear input
        self.pname.text = ""
        self.pername.text = ""
        self.addinormation.text = ""
        
class FifthWindow(Screen):
    def btn(self):
        store.put(self.pname.text, name=self.pname.text, perscription=self.pername.text, addinfo= self.addinormation.text)
        print(store.get(self.pname.text)['name'])
        print(store.get(self.pname.text)['perscription'])
        print(store.get(self.pname.text)['addinfo'])

        #clear input
        self.pname.text = ""
        self.pername.text = ""
        self.addinormation.text = ""
        
class SixthWindow(Screen):
    def save_alrm(self):
      self.a_name = self.alrm_name.text
      self.a_time = self.alrm_time.text
      self.alrm_name.text = ""
      self.alrm_time.text = ""

    def pop(self):
        pop_text1 = "Alarm Name: %s" %self.a_name
        pop_text2 = "Time: %s" %self.a_time
        full_pop_text = str(pop_text1+pop_text2)
        popup = Popup(title='Current Alarms', content=Label(text=full_pop_text),size_hint=(None, None), size=(400, 400))
        popup.open()

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

class MyApp(App):
    def build(self):
        Window.clearcolor = (0.5, 0.8, 0.2, 1)
        return kv

if __name__=="__main__":
    MyApp().run()

