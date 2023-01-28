from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
import pyodbc

user_helper = """
MDTextField:
    hint_text: 'Enter username'
    helper_text: 'or click forgot username'
    helper_text_mode: 'on_focus'
    icon_right: 'candy'
    icon_right_color: app.theme_cls.primary_palette
    pos_hint: {'center_x':0.5,'center_y':0.6}
    size_hint_x: None
    width: 300
"""

passwd_helper = """
MDTextField:
    hint_text: 'Enter password'
    icon_right: 'form-textbox-password'
    icon_right_color: app.theme_cls.primary_palette
    pos_hint: {'center_x':0.5,'center_y':0.5}
    size_hint_x: None
    width: 300
    password : True
"""
image_helper = '''
Image :
    source: 'shreck.png'
    pos_hint: {'center_x':0.5,'center_y':0.9}
'''


class DulceriaApp(MDApp):
    server = 'nombre-server'
    db = 'nombre-tabla'
    usuario = 'nombre-usuario'
    contrasena = 'contrasena'
    global conexion
    conexion = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + '; DATABASE=' + db + ';UID=' + usuario + '; PWD=' + contrasena,
        autocommit=True)
    def login(self,obj):
        btn_close = MDFlatButton(text='Close', on_release=self.dialog_close)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM login where username=? AND password=?",(self.user.text,self.passwd.text))
        row=cursor.fetchone()
        if self.user.text == '' and self.passwd.text == '':
            self.dialog = MDDialog(title='Login', text='You have to enter username and password',
                                   size_hint=(0.7, 1),
                                   buttons=[btn_close])
            self.dialog.open()
        elif row:
            self.dialog = MDDialog(title='Login', text='Login success',
                                   size_hint=(0.7, 1),
                                   buttons=[btn_close])
            self.dialog.open()
        else:
            self.dialog = MDDialog(title='Failed', text='Login Failed',
                                   size_hint=(0.7, 1),
                                   buttons=[btn_close])
            self.dialog.open()
        self.user.text = ""
        self.passwd.text = ""
        cursor.commit()
        cursor.close()

    def newUser(self,obj):
        btn_close = MDFlatButton(text='Close', on_release=self.dialog_close)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM login where username=? ", (self.user.text,))
        row = cursor.fetchone()
        if self.user.text == '' and self.passwd.text == '':
            self.dialog = MDDialog(title='User Created', text='You have to enter username and password',
                                   size_hint=(0.7, 1),
                                   buttons=[btn_close])
            self.dialog.open()
        elif row:
            self.dialog = MDDialog(title='User Created', text='User already exists',
                                   size_hint=(0.7, 1),
                                   buttons =[btn_close])
            self.dialog.open()
        else:
            cursor.execute("INSERT INTO login(username,password) VALUES(?,?)", (self.user.text, self.passwd.text))
            self.dialog = MDDialog(title='User Created', text='Successful',
                                   size_hint=(0.7, 1),
                                   buttons =[btn_close])
            self.dialog.open()
        self.user.text = ""
        self.passwd.text = ""
        cursor.commit()
        cursor.close()

    def delUser(self,obj):
        btn_close = MDFlatButton(text='Close', on_release=self.dialog_close)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM login where username=? ", (self.user.text,))
        row = cursor.fetchone()
        if self.user.text == '' and self.passwd.text == '':
            self.dialog = MDDialog(title='User Remove', text='You have to enter username and password',
                                   size_hint=(0.7, 1),
                                   buttons=[btn_close])
            self.dialog.open()
        elif row:
            cursor.execute("DELETE FROM login where username=?", (self.user.text,))
            self.dialog = MDDialog(title='User Remove', text='Successful',
                                   size_hint=(0.7, 1),
                                   buttons=[btn_close])
            self.dialog.open()
        else:
            self.dialog = MDDialog(title='User Remove', text='User Not Exists',
                                   size_hint=(0.7, 1)
                                   , buttons=[btn_close])
            self.dialog.open()
        self.user.text = ""
        self.passwd.text = ""
        cursor.commit()
        cursor.close()

    def userMod(self,obj):
        btn_close = MDFlatButton(text='Close', on_release=self.dialog_close)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM login where username=? ", (self.user.text,))
        row = cursor.fetchone()
        if self.user.text == '' and self.passwd.text == '':
            self.dialog = MDDialog(title='User Modify', text='You have to enter username and password',
                                   size_hint=(0.7, 1),
                                   buttons=[btn_close])
            self.dialog.open()
        elif row:
            cursor.execute("UPDATE login SET password=? WHERE username=?", (self.passwd.text, self.user.text))
            self.dialog = MDDialog(title='User Modify', text='Successful',
                                   size_hint=(0.7, 1),
                                   buttons=[btn_close])
            self.dialog.open()
        else:
            self.dialog = MDDialog(title='User Modify', text='User Not Exists',
                                   size_hint=(0.7, 1)
                                   , buttons=[btn_close])
            self.dialog.open()
        self.user.text = ""
        self.passwd.text = ""
        cursor.commit()
        cursor.close()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = 'BlueGray'
        screen = Screen()
        self.user = Builder.load_string(user_helper)
        self.passwd = Builder.load_string(passwd_helper)
        self.img = Builder.load_string(image_helper)
        user_btn = MDRectangleFlatButton(text='Show',pos_hint = {'center_x':0.5,'center_y':0.4},
                                         on_release= self.login)
        usern_btn = MDRectangleFlatButton(text='New user', pos_hint={'center_x': 0.37, 'center_y': 0.4},
                                          on_release=self.newUser)
        userd_btd = MDRectangleFlatButton(text='Remove user', pos_hint={'center_x': 0.63, 'center_y': 0.4},
                                          on_release=self.delUser)
        userm_btd = MDRectangleFlatButton(text='Modify user', pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                          on_release=self.userMod)

        screen.add_widget(self.user)
        screen.add_widget(self.passwd)
        screen.add_widget(self.img)
        screen.add_widget(user_btn)
        screen.add_widget(usern_btn)
        screen.add_widget(userd_btd)
        screen.add_widget(userm_btd)
        return screen

    def dialog_close(self,obj):
        self.dialog.dismiss()

DulceriaApp().run()