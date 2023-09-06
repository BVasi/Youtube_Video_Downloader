import pyautogui as pyg

messageToSpam = input("Enter the message you want to spam: ")

while True:
    pyg.write(messageToSpam)
    pyg.press("Enter")