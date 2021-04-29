import pyautogui as pag
import pyperclip as pyp
#Directions, open anki and go to add card field. Select the topmost portion 
#from...whatever, just read your own damm code Ted.
pag.PAUSE = 1


text_file = open("Anki_Auto_Entry.txt","r", encoding="utf-8")
L = text_file.read().split("\n")

pag.keyDown('alt')
pag.press('tab')
pag.keyUp('alt')   

for string in L:
    pag.PAUSE = 1
    pyp.copy(string)
    pag.hotkey('ctrl', 'v')   
    #entry process
    pag.press('tab')
    pag.hotkey('ctrl', 'enter')   
  

"""
CODE FOR TEXT SPACE PROCESSING

y = list(string)
for i in range(len(y)-2):
    j = i+1
    if y[i] ==  '\n':
        if y[j]!='\n':
            y[i] = None
    
y = [i for i in y if i] 

print("".join(y))

"""