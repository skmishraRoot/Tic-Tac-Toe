from tkinter import *
from tkinter import messagebox


# Making window
window = Tk()
window.title("Tic Tac Toe")
window.geometry("400x400")
window.resizable(False, False)



# setting player
player=False
# player labels to show player one and two options
Label(window,text="Player 1 - X").place(x=50,y=50)
Label(window,text="Player 2 - O").place(x=300,y=50)


#score variables
x_score = 0
o_score = 0
# score label to show score on the screen
Label(window,text=f"X = {x_score}").place(x=100,y=10)
Label(window,text=f"O = {o_score}").place(x=280,y=10)


# Button click function
def clicked_button(button):
    # making player global to change this inside the function
    global player
    if player==False and button['text']=='':
        # changing text
        button['text'] = 'X'
        # changing font color
        button['fg']='red'
        # changing value of player from false to true
        player=True
        check_winner()
    elif player==True and button['text']=='':
        # changing text
        button['text'] = 'O'
        # changing font color
        button['fg']='green'
        # changing value of player from true to false
        player=False
        check_winner()



# Function to check anyone wins or not
def check_winner():
    # making score var to global which make use make change in them inside the function
    global x_score, o_score

    # checking first row
    if button_1['text'] == button_2['text'] == button_3['text'] == 'X':
        messagebox.showinfo('winner', "player one winner")
        x_score += 1
        Label(window,text=f"X = {x_score}").place(x=100,y=10)
        reset()
    elif button_1['text'] == button_2['text'] == button_3['text'] == 'O':
        messagebox.showinfo('winner', "player two winner")
        o_score += 1
        Label(window,text=f"O = {o_score}").place(x=280,y=10)
        reset()
    else:
        pass
    
    # checking second row
    if button_4['text'] == button_5['text'] == button_6['text'] == 'X':
        messagebox.showinfo('winner', "player one winner")
        x_score += 1
        Label(window,text=f"X = {x_score}").place(x=100,y=10)
        reset()
    elif button_4['text'] == button_5['text'] == button_6['text'] == 'O':
        messagebox.showinfo('winner', "player two winner")
        o_score += 1
        Label(window,text=f"O = {o_score}").place(x=280,y=10)
        reset()
    else:
        pass
    # checking third row
    if button_7['text'] == button_8['text'] == button_9['text'] == 'X':
        messagebox.showinfo('winner', "player one winner")
        x_score += 1
        Label(window,text=f"X = {x_score}").place(x=100,y=10)
        reset()
    elif button_7['text'] == button_8['text'] == button_9['text'] == 'O':
        messagebox.showinfo('winner', "player two winner")
        o_score += 1
        Label(window,text=f"O = {o_score}").place(x=280,y=10)
        reset()
    else:
        pass
    
    # checking first column
    if button_1['text'] == button_4['text'] == button_7['text'] == 'X':
        messagebox.showinfo('winner', "player one winner")
        x_score += 1
        Label(window,text=f"X = {x_score}").place(x=100,y=10)
        reset()
    elif button_1['text'] == button_4['text'] == button_7['text'] == 'O':
        messagebox.showinfo('winner', "player two winner")
        o_score += 1
        Label(window,text=f"O = {o_score}").place(x=280,y=10)
        reset()
    else:
        pass
    
    # checking second column
    if button_2['text'] == button_5['text'] == button_8['text'] == 'X':
        messagebox.showinfo('winner', "player one winner")
        x_score += 1
        Label(window,text=f"X = {x_score}").place(x=100,y=10)
        reset()
    elif button_2['text'] == button_5['text'] == button_8['text'] == 'O':
        messagebox.showinfo('winner', "player two winner")
        o_score += 1
        Label(window,text=f"O = {o_score}").place(x=280,y=10)
        reset()
    else:
        pass
    
    # checking third column
    if button_3['text'] == button_6['text'] == button_9['text'] == 'X':
        messagebox.showinfo('winner', "player one winner")
        x_score += 1
        Label(window,text=f"X = {x_score}").place(x=100,y=10)
        reset()
    elif button_3['text'] == button_6['text'] == button_9['text'] == 'O':
        messagebox.showinfo('winner', "player two winner")
        o_score += 1
        Label(window,text=f"O = {o_score}").place(x=280,y=10)
        reset()
    else:
        pass
    
    # checking left to right digonal
    if button_1['text'] == button_5['text'] == button_9['text'] == 'X':
        messagebox.showinfo('winner', "player one winner")
        x_score += 1
        Label(window,text=f"X = {x_score}").place(x=100,y=10)
        reset()
    elif button_1['text'] == button_5['text'] == button_9['text'] == 'O':
        messagebox.showinfo('winner', "player two winner")
        o_score += 1
        Label(window,text=f"O = {o_score}").place(x=280,y=10)
        reset()
    else:
        pass
    
    # checking right to left digonal
    if button_3['text'] == button_5['text'] == button_7['text'] == 'X':
        messagebox.showinfo('winner', "player one winner")
        x_score += 1
        Label(window,text=f"X = {x_score}").place(x=100,y=10)
        reset()
    elif button_3['text'] == button_5['text'] == button_7['text'] == 'O':
        messagebox.showinfo('winner', "player two winner")
        o_score += 1
        Label(window,text=f"O = {o_score}").place(x=280,y=10)
        reset()
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



# RESETING FOR NEW GAME
# list of buttons
ls_btn = [button_1,button_2, button_3, button_4, button_5, button_6, button_7,button_8, button_9]
# reset tiles
def reset():
    for i in ls_btn:
        i['text'] = ''

# reset score 
def reset_score():
    x_score = 0
    o_score = 0
    Label(window,text=f"X = {x_score}").place(x=100,y=10)
    Label(window,text=f"O = {o_score}").place(x=280,y=10)
    

# Button to reset all the button to reset
button_reset =Button(window, height=1,width=4, text='Reset', command=reset)
button_reset.place(x=10, y=10)

# Button to reset score
button_reset_score = Button(window, height=1, width=8, text='Reset Score', command=reset_score)
button_reset_score.place(x=170,y =10)

mainloop()
