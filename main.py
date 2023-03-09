import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.lang import Builder

#setting the app to resizable/fullscreen
Config.set('graphics', 'resizable', 1)
#Config.set('graphics', 'fullscreen', 1)
#Config.set('graphics', 'borderless', 1)

#new screenmanager
sm = ScreenManager()

class ReactionGridLayout(GridLayout):
    def button_pressed(self, num):
        print("Button " + str(num) + " pressed")

    def logout(self):
        print("logged out")
        self.parent.add_widget(NumpadGridLayout())
        self.parent.remove_widget(self)

#this is the logon 
class NumpadGridLayout(GridLayout):

    #function called on logon button pressed
    def sessionID(self, sessionID):
        if sessionID:
            try:
                #attempt to login, otherwise throw error
                print(sessionID)
                # replace the current grid layout with the ReactionGridLayout
                self.parent.add_widget(ReactionGridLayout())
                self.parent.remove_widget(self)
            except:
                self.display.text = 'ERROR'

#creating app class    
class SmileyApp(App):

    def build(self):
        print('building app....')
        try:
            print('loading the .kv file')
            Builder.load_file("main.kv")
            print('loading the .ttf file')
            Builder.load_file("Amasis_MT_")
        except Exception as e:
            print('failed to load .kv file. this is the error: ', e)

        # add a new screen and set it as the current screen
        main_screen = Screen(name='main')
        sm.add_widget(main_screen)
        sm.current = 'main'

        # add the numpad grid layout to the current screen
        numpad_grid_layout = NumpadGridLayout()
        main_screen.add_widget(numpad_grid_layout)

        return sm

smileyApp = SmileyApp()
smileyApp.run()
