from tkinter import *
from tkinter import messagebox


# Making window
window = Tk()
window.title("Tic Tac Toe")
window.geometry("400x400")
window.resizable(False, False)

Label(window,text="Player 1 - X").place(x=50,y=50)
Label(window,text="Player 2 - O").place(x=300,y=50)

# setting player
player=False



# Button click function
def clicked_button(button):
    global player
    if player==False and button['text']=='':
        button['text'] = 'X'
        button['fg']='red'
        player=True
        check_winner()
    elif player==True and button['text']=='':
        button['text'] = 'O'
        button['fg']='green'
        player=False
        check_winner()



# Function to check anyone wins or not
def check_winner():

    # checking first row
    if button_1['text'] == button_2['text'] == button_3['text'] == 'X':
        messagebox.showinfo('winner', "player one winner")
    elif button_1['text'] == button_2['text'] == button_3['text'] == 'O':
        messagebox.showinfo('winner', "player two winner")
    else:
        pass
    
    # checking second row
    if button_4['text'] == button_5['text'] == button_6['text'] == 'X':
        messagebox.showinfo('winner', "player one winner")
    elif button_4['text'] == button_5['text'] == button_6['text'] == 'O':
        messagebox.showinfo('winner', "player two winner")
    else:
        pass
    # checking third row
    if button_7['text'] == button_8['text'] == button_9['text'] == 'X':
        messagebox.showinfo('winner', "player one winner")
    elif button_7['text'] == button_8['text'] == button_9['text'] == 'O':
        messagebox.showinfo('winner', "player two winner")
    else:
        pass
    
    # checking first column
    if button_1['text'] == button_4['text'] == button_7['text'] == 'X':
        messagebox.showinfo('winner', "player one winner")
    elif button_1['text'] == button_4['text'] == button_7['text'] == 'O':
        messagebox.showinfo('winner', "player two winner")
    else:
        pass
    
    # checking second column
    if button_2['text'] == button_5['text'] == button_8['text'] == 'X':
        messagebox.showinfo('winner', "player one winner")
    elif button_2['text'] == button_5['text'] == button_8['text'] == 'O':
        messagebox.showinfo('winner', "player two winner")
    else:
        pass
    
    # checking third column
    if button_3['text'] == button_6['text'] == button_9['text'] == 'X':
        messagebox.showinfo('winner', "player one winner")
    elif button_3['text'] == button_6['text'] == button_9['text'] == 'O':
        messagebox.showinfo('winner', "player two winner")
    else:
        pass
    
    # checking left to right digonal
    if button_1['text'] == button_5['text'] == button_9['text'] == 'X':
        messagebox.showinfo('winner', "player one winner")
    elif button_1['text'] == button_5['text'] == button_9['text'] == 'O':
        messagebox.showinfo('winner', "player two winner")
    else:
        pass
    
    # checking right to left digonal
    if button_3['text'] == button_5['text'] == button_7['text'] == 'X':
        messagebox.showinfo('winner', "player one winner")
    elif button_3['text'] == button_5['text'] == button_7['text'] == 'O':
        messagebox.showinfo('winner', "player two winner")
    else:
        pass



    
# Making buttons on which we play our game

# first row of button
button_1 = Button(window, height=4, width=8, bg='grey',text='', command=lambda: clicked_button(button_1))
button_1.place(x=100,y=80)
button_2 = Button(window, height=4, width=8,  bg='grey', text='', command=lambda: clicked_button(button_2))
button_2.place(x=170,y=80)
button_3 = Button(window, height=4, width=8 ,  bg='grey',text='', command=lambda: clicked_button(button_3))
button_3.place(x=240,y=80)

# second row of buttons
button_4 = Button(window, height=4, width=8,  bg='grey',text='', command=lambda: clicked_button(button_4))
button_4.place(x=100,y=160)
button_5 = Button(window, height=4, width=8,  bg='grey',text='', command=lambda: clicked_button(button_5))
button_5.place(x=170,y=160)
button_6 = Button(window, height=4, width=8,  bg='grey',text='', command=lambda: clicked_button(button_6))
button_6.place(x=240,y=160)

# third row of button
button_7 = Button(window, height=4, width=8,  bg='grey',text='', command=lambda: clicked_button(button_7))
button_7.place(x=100,y=240)
button_8 = Button(window, height=4, width=8, bg='grey',text='', command=lambda: clicked_button(button_8))
button_8.place(x=170,y=240)
button_9 = Button(window, height=4, width=8, bg='grey',text='', command=lambda: clicked_button(button_9))
button_9.place(x=240,y=240)


# Button to quit the game
button_0 = Button(window, height=2, width=12, text="Quit", command=window.destroy)
button_0.place(x=150,y=340)

# list of buttons
ls_btn = [button_1,button_2, button_3, button_4, button_5, button_6, button_7,button_8, button_9]

def reset():
    for i in ls_btn:
        i['text'] = ''

# Button to reset all the button to reset
button_11 =Button(window, height=2,width=5, text='Reset', command=reset)
button_11.place(x=10, y=10)

mainloop()
