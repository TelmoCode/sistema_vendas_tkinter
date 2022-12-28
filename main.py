from tkinter import *
import time
import datetime
import pygame,sys, random

pygame.init()

root = Tk()
root.title("Sistema de Vendas")
root.geometry('1352x720+0+0')

root.configure(background='yellow')

framePrinc = Frame(root,bg='blue', bd=10, relief= RIDGE)
framePrinc.grid()

frameP1 = Frame(root,bg='blue', bd=10, relief= RIDGE)
frameP1.grid()


root.mainloop()