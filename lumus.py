import pyautogui
import time
import math


def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m
#traco
#                pyautogui.press('capslock')
#                time.sleep(0.48)
#                pyautogui.press('capslock')
#pequeno
#                pyautogui.press('capslock')
#                time.sleep(0.18)
#                pyautogui.press('capslock')
print("Reading Secrect.txt")
with open("secret.txt", "r") as arquivo:
    for linha in arquivo:
        resp = toBinary(linha)
        print("Word : ", linha)
        for letra in resp:
            # Processa cada letra individualmente
            print("extracting set of letters with LED:", letra)
            for li in str(letra):
                print(li)
                if li == "1":
                    pyautogui.press('capslock')
                    time.sleep(0.18)
                    pyautogui.press('capslock')
                    time.sleep(1)             
                if li == "0":
                    pyautogui.press('capslock')
                    time.sleep(0.18)
                    pyautogui.press('capslock')
                    pyautogui.press('capslock')
                    time.sleep(0.18)
                    pyautogui.press('capslock')
                    time.sleep(1)
            print("waiting 3 seconds to represent the space bar.")
            time.sleep(3)