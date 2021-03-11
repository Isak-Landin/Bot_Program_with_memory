import cv2, time, pyautogui, PIL, json, pyperclip, importlib
import pytesseract
from Testing import *

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


class Clients:
    def __init__(self):
        self.regions = list(pyautogui.locateAllOnScreen('open_screen.png', confidence=0.95))

    def find_each_region(self):
        return self.regions


class Accounts:
    def __init__(self, accounts, regions):
        self.accounts = accounts
        self.regions = regions
        self.counter = 0
        self.account_memory = []
        """
        for i in self.regions:
            self.center = pyautogui.center(i)
            pyautogui.moveTo(self.center)
        """

    def execute_logins(self):

        for specific_region in self.regions:
            print(specific_region)
            print(self.accounts[self.counter])
            existing_user = list(pyautogui.locateOnScreen('existing_user.png', region=specific_region, confidence=0.95))
            center_existing_user = pyautogui.center(existing_user)

            pyautogui.moveTo(center_existing_user, duration=0.5)
            pyautogui.click()

            pyautogui.write(self.accounts[self.counter][0], interval=0.1)
            pyautogui.hotkey('altright', '2')
            pyautogui.write(self.accounts[self.counter][1], interval=0.1)

            pyautogui.press('tab')
            pyautogui.write(self.accounts[self.counter][2], interval=0.1)
            pyautogui.press('enter')

            print(self.accounts[self.counter][1])


            account_location = [self.accounts[self.counter][0] + "@" + self.accounts[self.counter][1], specific_region]
            self.account_memory.append(account_location)

            self.counter += 1

    def click_to_play(self):
        self.location_click_to_play = pyautogui.locateAllOnScreen('click_to_play.png', confidence=0.95)

        for i in self.location_click_to_play:
            center = pyautogui.center(i)

            pyautogui.moveTo(center, duration=0.4)
            pyautogui.click()



clients_var = Clients()
saved_client_regions = clients_var.find_each_region()
print(saved_client_regions)

list_of_accounts = [["yaatahatah", "gmail.com", "8DDDOg"], ["pippisnegerslavar", "gmail.com", "Thekilling2"]]
Acc2 = Accounts(list_of_accounts, saved_client_regions)
Acc2.execute_logins()
print(Acc2.account_memory)
pyautogui.moveTo((1, 1), duration=0.2)

# testing_var = testing(saved_client_regions)
# print(testing_var.return_region())
# print(testing_var.return_region())
# print(testing_var.return_region())

breaker_condition = 0

while True:
    click_to_play_buttons_active = list(pyautogui.locateAllOnScreen('click_to_play.png', confidence=0.95))

    if len(saved_client_regions) == len(click_to_play_buttons_active) or breaker_condition > 200:
        for i in click_to_play_buttons_active:
            click_to_play_buttons_active_center = pyautogui.center(i)
            pyautogui.moveTo(click_to_play_buttons_active_center, duration=0.2)
            pyautogui.click()
        break

    breaker_condition += 1
    print(breaker_condition)
