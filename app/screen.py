from abc import ABC
import time
import msvcrt

class Screen(ABC):
    @staticmethod
    def display(self):
        pass
            
    def print(self,*txt,sep=' ',end='\n'):
        print(*txt, sep=sep,end=end)
            
    def printAnimated(self,txt,end='\n'):
        for i in txt:
            print(i,sep='',end='')
            time.sleep(0.005)
        print('',end=end)
    
    def printMenu(self,list):
        for i,j in enumerate(list):
            print(f"{i} -> {str(j).capitalize()}")
            time.sleep(0.1)
    
    def scanIntRange(self,max,title=None,min=0):
        if title == None:
            title = f'Input({min}:{max}): ' 
    
        num = max
        while num not in range(min,max):
            num = int(input(title))
            if num not in range(min,max):
                print(f"ERROR: input must be >={min} and <{max}")
        return num
    
    def scanStr(self,title):
        s = ''
        while(len(s.strip())==0):
            try:
                s =  input(title)
            except:
                s=''
        return s
    
    def scanInt(self,title):
        n = 0
        while(True):
            try:
                n =  int(input(title))
                break
            except:
                pass
        return n
        
    def load(self, seconds):
        symbols = ['■','□']
        count_of_100ml = int(seconds/0.1)
        
        for i in range(count_of_100ml):
            print('\r'+''*20,end='')
            percent =int(((i+1)/count_of_100ml)*100)
            
            print("loading: ",end='')
            for j in range(10):
                print(symbols[int(j*10 >percent) ]  ,end='')
            print(f" {percent}%",end='') 
            time.sleep(0.1)
        print('') 
    
    def wait(self, seconds):
        time.sleep(seconds)
        
    def waitKeyToContinue(self,title = "Press any key to continue..."):
        print(title)
        msvcrt.getch()

    def waitKeyToReturn(self,title = "Press any key to return screen..."):
        print(title)
        msvcrt.getch()
        
    def waitKey(self):
        return msvcrt.getch()
        
    
        