from globals import *
from tkinter.messagebox import askyesno
from tkinter import messagebox as mb

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

def choice_human(event, human, computer, chat_gris, chat_roux):
    if image_vs_player_pos[0] <= event.pos[0] <= image_vs_player_pos[0] + image_vs_player.get_width() and \
        image_vs_player_pos[1] <= event.pos[1] <= image_vs_player_pos[1] + image_vs_player.get_height():
        if human == True or computer == True:
            mb.showerror("Erreur", "You have already choice your opponent")
        else:
            if chat_gris == True or chat_roux == True:
                choice = askyesno('Human selection','Confirm that you want to play versus human?')
                if choice == True:
                    human = True
            else:
                mb.showerror("Erreur", "You have to select your warrior first")
    return human

def choice_computer(event, computer, human, chat_gris, chat_roux):
    if image_vs_cpu_pos[0] <= event.pos[0] <= image_vs_cpu_pos[0] + image_vs_cpu.get_width() and \
        image_vs_cpu_pos[1] <= event.pos[1] <= image_vs_cpu_pos[1] + image_vs_cpu.get_height():
        if human == True or computer == True:
            mb.showerror("Erreur", "You have already choice your opponent")
        else:
            if chat_gris == True or chat_roux == True:
                choice = askyesno('Human selection','Confirm that you want to play versus computer?')
                if choice == True:
                    computer = True
            else:
                mb.showerror("Erreur", "You have to select your warrior first")
    return computer

def mouse_pos():
    mouseX, mouseY = Py.mouse.get_pos()
    if mouseX >= 520 and mouseX <= 880 and mouseY >= 220 and mouseY <= 700:
        row = (mouseY - 220) // 120
        col = (mouseX - 520) // 120
        return row, col
        