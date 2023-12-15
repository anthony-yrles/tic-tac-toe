from globals import *
from tkinter.messagebox import askyesno
from tkinter import messagebox as mb
import time

def gris_ou_roux(event, chat_gris, chat_roux):
    if image_gris_pos[0] <= event.pos[0] <= image_gris_pos[0] + image_gris.get_width() and \
        image_gris_pos[1] <= event.pos[1] <= image_gris_pos[1] + image_gris.get_height():
        if chat_roux == True or chat_gris == True:
            mb.showerror("Erreur", "You can only choose one warrior")
        else:
            choose_chat_gris = askyesno('Chat Gris selection','Confirm the selection of warrior name Mistrigri?')
            if choose_chat_gris == True:
                chat_gris = True
    return chat_gris

    
def roux_ou_gris(event, chat_gris, chat_roux):
    if image_roux_pos[0] <= event.pos[0] <= image_roux_pos[0] + image_roux.get_width() and \
        image_roux_pos[1] <= event.pos[1] <= image_roux_pos[1] + image_roux.get_height():
        if chat_roux == True or chat_gris == True:
            mb.showerror("Erreur", "You can only choose one warrior")
        else:
            choose_chat_roux = askyesno('Chat Gris selection','Confirm the selection of warrior name Roucky?')
            if choose_chat_roux == True:
                chat_roux = True
    return chat_roux
        
# def fight(event, chat_gris, chat_roux, fight_on):
#     if image_fight_pos[0] <= event.pos[0] <= image_fight_pos[0] + image_fight.get_width() and \
#         image_fight_pos[1] <= event.pos[1] <= image_fight_pos[1] + image_fight.get_height():
#         if chat_gris == False and chat_roux == False:
#             mb.showerror("Erreur", "Veuillez sélectionner un combattant avec de lancer le fight!!!")
#         elif chat_gris == True:
#             mb.askquestion("Fight", "Préparez-vous au combat Mistrigri!!!")
#             fight_on = True
#             return fight_on
#         elif chat_roux == True:
#             mb.askquestion("Fight", "Préparez-vous au combat Roucky!!!")
#             fight_on = True
#             return fight_on

def mouse_pos():
    mouseX, mouseY = Py.mouse.get_pos()
    if mouseX >= 520 and mouseX <= 880 and mouseY >= 220 and mouseY <= 700:
        row = (mouseY - 220) // 120
        col = (mouseX - 520) // 120
        return row, col
        