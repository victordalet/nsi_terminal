import pyautogui,time
def main():
    a = 0
    time_b = round(time.time())
    while 42:
        a += 1
        pyautogui.write("non viens pas please")
        print(a , round(time.time()) - time_b)
        pyautogui.press('ENTER')
main()