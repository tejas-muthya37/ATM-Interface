import tkinter.font as font
from random import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import *
root = Tk()
root.title("State Bank of India")
root.iconbitmap('c:/Python/sbi.ico')
canvas = Canvas(root, height = 770, width = 1200)
canvas.pack()


def languageScreen():
    languageFrame = Frame(root, bg = "#019EEC")
    languageFrame.place(relheight = 1, relwidth = 1)

    myFont3 = font.Font(family='Courier', weight = 'bold', size = 35)

    languageLabel = Label(languageFrame, text = "Please select a language.", bg = "#019EEC", fg = "Black")
    languageLabel.place(relx = 0, rely = 0.4, relheight = 0.2, relwidth = 1)
    languageLabel['font'] = myFont3

    myFont = font.Font(family='.AppleSystemUIFont', weight = 'bold', size = 30)

    englishButton = Button(languageFrame, text = "English", bg="#FFB600", fg = "black", command = serviceScreen)
    englishButton['font'] = myFont
    englishButton.place(relx = 0.75, rely = 0.2, relheight = 0.1, relwidth = 0.25)

    hindiButton = Button(languageFrame, text = "Hindi", bg="#FFB600", fg = "black")
    hindiButton['font'] = myFont
    hindiButton.place(relx = 0.75, rely = 0.8, relheight = 0.1, relwidth = 0.25)


# def pinScreen():
#     pinFrame = Frame(root, bg = "#019EEC")
#     pinFrame.place(relheight = 1, relwidth = 1)

#     myFont3 = font.Font(family='Courier', weight = 'bold', size = 35)

#     pinLabel = Label(pinFrame, text = "Please enter your PIN.", bg = "#019EEC", fg = "Black")
#     pinLabel.place(relx = 0, rely = 0.45, relheight = 0.05, relwidth = 1)
#     pinLabel['font'] = myFont3

#     pinEntry = Entry(pinFrame, show="*", font = myFont3, justify = CENTER, bd = 2, bg = "gray", fg = "black")
#     pinEntry.place(relx = 0.3, rely = 0.55, relheight = 0.08, relwidth = 0.4)

#     myFont = font.Font(family='.AppleSystemUIFont', weight = 'bold', size = 30)

#     pinButton = Button(pinFrame, text = "Continue", bg="#FFB600", fg = "black", command = serviceScreen)
#     pinButton['font'] = myFont
#     pinButton.place(relx = 0.75, rely = 0.2, relheight = 0.1, relwidth = 0.25)

#     reEnterButton = Button(pinFrame, text = "Re-Enter PIN", bg="#FFB600", fg = "black", command = pinScreen)
#     reEnterButton['font'] = myFont
#     reEnterButton.place(relx = 0.75, rely = 0.8, relheight = 0.1, relwidth = 0.25)


def serviceScreen():
    serviceFrame = Frame(root, bg = "#019EEC")
    serviceFrame.place(relheight = 1, relwidth = 1)

    myFont3 = font.Font(family='Courier', weight = 'bold', size = 35)

    serviceLabel = Label(serviceFrame, text = "Select your services.", bg = "#019EEC", fg = "Black")
    serviceLabel.place(relx = 0, rely = 0.45, relheight = 0.05, relwidth = 1)
    serviceLabel['font'] = myFont3

    withdrawalButton = Button(serviceFrame, text = "Withdrawal", bg="#FFB600", fg = "black", command = accountScreen)
    withdrawalButton['font'] = myFont
    withdrawalButton.place(relx = 0.75, rely = 0.2, relheight = 0.1, relwidth = 0.25)

    balanceButton = Button(serviceFrame, text = "Balance Enquiry", bg="#FFB600", fg = "black")
    balanceButton['font'] = myFont
    balanceButton.place(relx = 0.75, rely = 0.4, relheight = 0.1, relwidth = 0.25)

    statementButton = Button(serviceFrame, text = "Mini Statement", bg="#FFB600", fg = "black")
    statementButton['font'] = myFont
    statementButton.place(relx = 0.75, rely = 0.6, relheight = 0.1, relwidth = 0.25)

    pinChangeButton = Button(serviceFrame, text = "PIN Change", bg="#FFB600", fg = "black")
    pinChangeButton['font'] = myFont
    pinChangeButton.place(relx = 0.75, rely = 0.8, relheight = 0.1, relwidth = 0.25)


def accountScreen():
    accountFrame = Frame(root, bg = "#019EEC")
    accountFrame.place(relheight = 1, relwidth = 1)

    myFont3 = font.Font(family='Courier', weight = 'bold', size = 35)

    accountLabel = Label(accountFrame, text = "Select account type.", bg = "#019EEC", fg = "Black")
    accountLabel.place(relx = 0, rely = 0.45, relheight = 0.05, relwidth = 1)
    accountLabel['font'] = myFont3

    savingsButton = Button(accountFrame, text = "Savings", bg="#FFB600", fg = "black", command = amountScreen)
    savingsButton['font'] = myFont
    savingsButton.place(relx = 0.75, rely = 0.2, relheight = 0.1, relwidth = 0.25)

    currentButton = Button(accountFrame, text = "Current", bg="#FFB600", fg = "black")
    currentButton['font'] = myFont
    currentButton.place(relx = 0.75, rely = 0.5, relheight = 0.1, relwidth = 0.25)

    creditButton = Button(accountFrame, text = "Balance", bg="#FFB600", fg = "black")
    creditButton['font'] = myFont
    creditButton.place(relx = 0.75, rely = 0.8, relheight = 0.1, relwidth = 0.25)


def amountScreen():
    amountFrame = Frame(root, bg = "#019EEC")
    amountFrame.place(relheight = 1, relwidth = 1)

    myFont3 = font.Font(family='Courier', weight = 'bold', size = 35)

    amountLabel = Label(amountFrame, text = "Please enter the amount.", bg = "#019EEC", fg = "Black")
    amountLabel.place(relx = 0, rely = 0.45, relheight = 0.05, relwidth = 1) 
    amountLabel['font'] = myFont3

    amountEntry = Entry(amountFrame, font = myFont3, justify = CENTER, bd = 0, bg = "#019EEC", fg = "black")
    amountEntry.place(relx = 0.3, rely = 0.55, relheight = 0.08, relwidth = 0.4)
    amountEntry.focus()

    myFont = font.Font(family='.AppleSystemUIFont', weight = 'bold', size = 30)

    confirmButton = Button(amountFrame, text = "Continue", bg="#FFB600", fg = "black", command = confirmScreen)
    confirmButton['font'] = myFont
    confirmButton.place(relx = 0.75, rely = 0.2, relheight = 0.1, relwidth = 0.25)

    reEnter1Button = Button(amountFrame, text = "Re-Enter Amount", bg="#FFB600", fg = "black", command = amountScreen)
    reEnter1Button['font'] = myFont
    reEnter1Button.place(relx = 0.75, rely = 0.8, relheight = 0.1, relwidth = 0.25)

def confirmScreen():
    confirmFrame = Frame(root, bg = "#019EEC")
    confirmFrame.place(relheight = 1, relwidth = 1)

    myFont3 = font.Font(family='Courier', weight = 'bold', size = 35)

    amountLabel = Label(confirmFrame, text = "Your transaction is being processed ...", bg = "#019EEC", fg = "Black")
    amountLabel.place(relx = 0, rely = 0.45, relheight = 0.05, relwidth = 1) 
    amountLabel['font'] = myFont3



homeFrame = Frame(root, bg = "#019EEC")
homeFrame.place(relheight = 1, relwidth = 1)

myFont3 = font.Font(family='Courier', weight = 'bold', size = 35)

introLabel = Label(homeFrame, text = "Welcome to State Bank of India.\n\nPress Enter to get started.", bg = "#019EEC", fg = "Black")
introLabel.place(relx = 0, rely = 0.4, relheight = 0.2, relwidth = 1)
introLabel['font'] = myFont3

myFont = font.Font(family='.AppleSystemUIFont', weight = 'bold', size = 30)

logoButton = Button(homeFrame, text = "Enter", bg="#FFB600", fg = "black", command=languageScreen)
logoButton['font'] = myFont
logoButton.place(relx = 0.75, rely = 0.2, relheight = 0.1, relwidth = 0.25)

root.mainloop()