"""
KMS Easy
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, Pack, LEFT
from corekms import activationcore as accore


class KMSEasy(toga.App):
    def buttonpro(widget, e):
        accore(2)
    def buttonworkstation(widget,e ):
        accore(3)

    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        box = toga.Box()
        label = toga.Label("Select System Edition", style=Pack(text_align=LEFT))
        button = toga.Button("Pro", on_press=self.buttonpro)
        button1 = toga.Button("Pro Workstation", on_press=self.buttonworkstation)
        box.add(label)
        box.add(button)
        box.add(button1)
        box.style.update(direction=COLUMN, padding=10)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = box
        self.main_window.show()
    

def main():
    return KMSEasy()
