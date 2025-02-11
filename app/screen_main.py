from app.screen import *
from app.navigator import *
import app
import app.screen_home

class ScreenMain(Screen):
    def display(self):
        logo = """
  _    _                 _ _        _    _____           _                 
 | |  | |               (_) |      | |  / ____|         | |                
 | |__| | ___  ___ _ __  _| |_ __ _| | | (___  _   _ ___| |_ ___ _ __ ___  
 |  __  |/ _ \/ __| '_ \| | __/ _` | |  \___ \| | | / __| __/ _ \ '_ ` _ \ 
 | |  | | (_) \__ \ |_) | | || (_| | |  ____) | |_| \__ \ ||  __/ | | | | |
 |_|  |_|\___/|___/ .__/|_|\__\__,_|_| |_____/ \__, |___/\__\___|_| |_| |_|
                  | |                           __/ |                      
                  |_|                          |___/                       
        """
    
        super().printAnimated(logo)
        
        
        
        
        super().load(3)
        super().waitKeyToContinue()
        NavigatorPush(app.screen_home.ScreenHome())