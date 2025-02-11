import os

_screen_stack=[]

def NavigatorPush(screen):
   _screen_stack.append(screen)
   os.system('cls')
   NavigatorPrintPath()
   screen.display()
   
def NavigatorPushReplacement(screen):
   _screen_stack.pop()
   _screen_stack.append(screen)
   os.system('cls')
   NavigatorPrintPath()
   screen.display()
   
def NavigatorPop():
   _screen_stack.pop()
   os.system('cls')
   NavigatorPrintPath()
   _screen_stack[-1].display()   
   
def NavigatorPrintPath():
    path = "/ ".join(map(lambda x: type(x).__name__.replace("Screen", ''),_screen_stack))
    print("-"*35)
    print("Path: ",path)
    print("-"*35,"\n")
    
def NavigatorFlushTerminal():
   os.system('cls')
   NavigatorPrintPath()