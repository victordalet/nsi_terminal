import pyautogui,time
def main():
    time.sleep(2)
    a = 0
    time_b = round(time.time())
    while 42:
        a += 1
        pyautogui.write("testV2")
        print(a , round(time.time()) - time_b)
        time.sleep(1) #pour les notifs donc a voir
        pyautogui.press('ENTER')
main()