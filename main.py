import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.lang import Builder

#setting the app to resizable
Config.set('graphics', 'resizable', 1)
Config.set('graphics', 'fullscreen', 1)
Config.set('graphics', 'borderless', 1)


class NumpadGridLayout(GridLayout):

    #function called on logon button pressed
    def logon(self, logon):
        if logon:
            try:
                #attempt to login, otherwise throw error
                print(logon)
            except:
                self.display.text = 'ERROR'

#creating app class    
class SmileyApp(App):

    def build(self):
        print('building app....')
        try:
            print('loading the .kv file')
            Builder.load_file("main.kv")
        except Exception as e:
            print('failed to load .kv file. this is the error: ', e)
        return NumpadGridLayout()

smileyApp = SmileyApp()
smileyApp.run()