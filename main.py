import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.config import Config
from kivy.lang import Builder
import pymysql.cursors
import time
import configparser
import os


class ReactionGridLayout(GridLayout):

    def __init__(self, cursor, connection, roomcode, **kwargs):
        super(ReactionGridLayout, self).__init__(**kwargs)
        self.cursor = cursor
        self.connection = connection
        self.roomcode = roomcode

    def button_pressed(self, num):
        print("Button " + str(num) + " pressed")
        if num == 1:
            sql = "UPDATE db.feedback SET veryUnsatisfied = veryUnsatisfied + 1  WHERE sessionID = %s;"
            self.cursor.execute(sql, self.roomcode)
            self.cursor.connection.commit()
        elif num == 2:
            sql = "UPDATE db.feedback SET unsatisfied = unsatisfied + 1  WHERE sessionID = %s;"
            self.cursor.execute(sql, self.roomcode)
            self.cursor.connection.commit()
        elif num == 3:
            sql = "UPDATE db.feedback SET neutral = neutral + 1  WHERE sessionID = %s;"
            self.cursor.execute(sql, self.roomcode)
            self.cursor.connection.commit()
        elif num == 4:
            sql = "UPDATE db.feedback SET satisfied = satisfied  + 1  WHERE sessionID = %s;"
            self.cursor.execute(sql, self.roomcode)
            self.cursor.connection.commit()
        elif num == 5:
            sql = "UPDATE db.feedback SET verySatisfied = verySatisfied + 1  WHERE sessionID = %s;"
            self.cursor.execute(sql, self.roomcode)
            self.cursor.connection.commit()

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
                connection = pymysql.connect(
                    host=database_host,
                    port=database_port,
                    user=database_user,
                    password=database_password,
                )
                cursor = connection.cursor()
                sql = "SELECT * FROM db.roomcodes WHERE roomcode = %s"
                cursor.execute(sql, sessionID)
                row = cursor.fetchone()

                if row:
                    # get current time
                    curr_date = time.strftime("%Y-%m-%d %H:%M:%S")
                    print(curr_date)

                    # insert initial row
                    sql = "INSERT INTO db.feedback (roomCode, curr_date, veryUnsatisfied, unsatisfied, neutral, satisfied, verySatisfied) VALUES (%s, %s, 0, 0, 0, 0, 0)"
                    data = (sessionID, curr_date)
                    cursor.execute(sql, data)
                    # commit the changes to the DB
                    connection.commit()

                    # get the index number
                    sql = "SELECT sessionID FROM db.feedback WHERE roomCode = %s ORDER BY sessionID DESC LIMIT 1;"
                    cursor.execute(sql, sessionID)
                    temp = cursor.fetchone()
                    print(temp)
                    roomcode = temp[0]

                    # replace the current grid layout with the ReactionGridLayout
                    #(change windows)
                    self.parent.add_widget(ReactionGridLayout(cursor, connection, roomcode))
                    self.parent.remove_widget(self)
                else:
                    #make an error title popup
                    popup = Popup(title='Login Failed',
                                  content=Label(text="Incorrect Session ID"),
                                  size_hint=(None,None), size=(400,400))
                    popup.open()
            except Exception as e:
                print(e)

#creating app class    
class SmileyApp(App):

    def build(self):
        print('building app....')
        try:
            print('loading the .kv file')
            Builder.load_file("main.kv")
            print('loading the .ttf file')
            Builder.load_file("Amasis_MT_Std_Black.ttf")
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

#set windows specifically for DEBUG purposes
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '800')

#setting the app to resizable/fullscreen
Config.set('graphics', 'resizable', 1)
#Config.set('graphics', 'fullscreen', 'auto')
#Config.set('graphics', 'borderless', 1)

#new screenmanager
sm = ScreenManager()

encryption_key = os.environ.get('MY_ENCRYPTION_KEY')

config = configparser.ConfigParser()
config.read('config.ini')

database_host = config.get('database', 'host')
database_port = config.getint('database', 'port')
database_user = config.get('database', 'user')
database_password = config.get('database', 'password')

global cursor
global roomcode
global connection
smileyApp = SmileyApp()
smileyApp.run()
