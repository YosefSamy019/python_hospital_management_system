from app.screen import *
from app.navigator import *
import app

class ScreenSettings(Screen):
    def display(self):
        super().print("Nothing here...")
        super().waitKeyToReturn()
        NavigatorPop()
   