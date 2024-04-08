import os
import pyautogui
import time



account_name = "cyber"


coord_list = [
1661, 742,
1664, 838,
2114, 644,
2107, 745,
2122, 845,
]


class main:
    def __init__(self):
        ordner_name = pyautogui.prompt(text='Folder name?', title='Ready' , default='continue')
        hero_set = ordner_name
        path = f'{account_name}/{hero_set}/'
        self.is_folder(path)
        self.screenshotsMachen(path)
        
        
    def screenshotsMachen(self, path):
        for i in range(0, 10, 2 ):
            dateiname = f"{path}my_screenshot{i}.png"
            pyautogui.moveTo(coord_list[i], coord_list[i+1] )
            pyautogui.click()
            time.sleep(0.35)
            pyautogui.screenshot(dateiname, region=(1730,625,320,295))
            time.sleep(0.25)
            print("screenshot taken")


    
    def is_folder(self, ziel):
        try:
            os.chdir(ziel)
        except FileNotFoundError:
               os.makedirs(ziel)
               print("folder created")
        except Exception as e:
               print("other problem")
              
              
    def start(self):
        while True:
            test = pyautogui.prompt(text='Done with current Hero?', title='Ready' , default='continue')
            if test == "DONE":
                break
            elif test == "NEXT":
                folder_name = pyautogui.prompt(text='New Char Name', title='Ready' , default='continue')
                hero_set = folder_name
                path = f'test/{hero_set}/'
                self.is_folder(path)
                self.screenshotsMachen(path)
                        
        

if __name__ == "__main__":
    main_instance = main()
    main_instance.start()