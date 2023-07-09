# from time import sleep
# import pyautogui


# pyautogui.PAUSE = 0.5
# ID = 451, 48
# CHOOSE_FILE = 547, 744
# DOWNLOADS = 360, 400
# SELECT = 1033, 225
# CONTINUAR_EDITANDO = 649, 692

# sleep(10)

# for i in range(1, 124):
#     # selecionar o id
#     pyautogui.moveTo(ID[0], ID[1])
#     pyautogui.click(clicks=2)
#     pyautogui.write(str(i))
#     pyautogui.press('enter')

#     # selecionar imagem
#     pyautogui.moveTo(CHOOSE_FILE[0], CHOOSE_FILE[1])
#     pyautogui.click()
#     pyautogui.moveTo(DOWNLOADS[0], DOWNLOADS[1])
#     pyautogui.click()
#     pyautogui.moveTo(SELECT[0], SELECT[1])
#     pyautogui.click()

#     # salvar
#     pyautogui.scroll(-5)
#     pyautogui.moveTo(CONTINUAR_EDITANDO[0], CONTINUAR_EDITANDO[1])
#     pyautogui.click()
