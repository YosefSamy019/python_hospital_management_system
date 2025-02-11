import app.screen_main
from data.storage import *
from data.models import *
from app.screen import *
from app.navigator import *
import app

def main():
    Storage.reload()
    NavigatorPush(app.screen_main.ScreenMain())

if __name__ == "__main__":
    main()
    