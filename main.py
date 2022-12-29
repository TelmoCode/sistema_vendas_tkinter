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

frameP1 = Frame(framePrinc,bg='blue', bd=10, relief= RIDGE)
frameP1.grid(row=0,column=0,columnspan=4, sticky=W)

frameP2 = Frame(framePrinc,bg='blue', bd=10, relief= RIDGE)
frameP2.grid(row=1,column=0, sticky=W)

frameP3 = Frame(framePrinc,bg='blue', bd=10, relief= RIDGE)
frameP3.grid(row=1,column=1, sticky=W)

frameP4 = Frame(framePrinc,bg='blue', bd=10, relief= RIDGE)
frameP4.grid(row=1,column=2, sticky=W)

frameP5 = Frame(frameP4,bg='blue', bd=10, relief= RIDGE)
frameP5.grid(row=0,column=0, sticky=W)

frameP5 = Frame(frameP4,bg='blue', bd=10, relief= RIDGE)
frameP5.grid(row=1,column=0,columnspan=4, sticky=W)

lblDate = Label(frameP1,text="\tDate\t",font=('arial',30,'bold'),
                padx=9,pady=9,bd=14,bg='Cadet Blue', fg='Cornsilk',
                justify=CENTER
                ).grid(row=0,column=0)


root.mainloop()