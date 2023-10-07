from tkinter import *

root = Tk()
root.title('ASCII Encrypter')
root.geometry('400x400')
root.configure(background = 'snow')

entWord = Entry(root)
entWord.place(relx = 0.5, rely = 0.3, anchor = CENTER)

lblAscii = Label(root, text = 'ASCII: ', bg = 'light blue', fg = 'black')
lblAscii.place(relx = 0.5, rely = 0.5, anchor = CENTER)
lblEncrypt = Label(root, text = 'Encrypted: ', bg = 'light blue', fg = 'black')
lblEncrypt.place(relx = 0.5, rely = 0.6, anchor = CENTER)

def asciiConvert():
    word = entWord.get()
    lblAscii['text'] = 'ASCII: '   
    lblEncrypt['text'] = 'Encrypted: ' 
    for i in range(len(word)):
        lblAscii['text'] += str(ord(word[i]))
        if i != len(word) - 1:
            lblAscii['text'] += ', '
    
    for i in range(len(word)):
        lblEncrypt['text'] += str(chr(int(ord(word[i])) - 1))

btnConvert = Button(root, text = 'Show ASCII Values', command = asciiConvert)
btnConvert.place(relx = 0.5, rely = 0.4, anchor = CENTER)

root.mainloop()