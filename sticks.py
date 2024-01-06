from tkinter import *
 
#Variables
game = True
turn = 1
 
num_fingers = [1,1,1,1]
hands = ["Left","Right"]
 
player1_selection = "No"
player2_selection = 'No'
 
#Functions
#This function was written by my collaborative partner
def update(num):
    global turn, turn_label, player_hands, game_over_frame, game_over_label
    turn_label.config(text = "Player " + str(turn) + "'s turn to attack! \n Click on a hand to select.")
    
    for n in range(len(num)):
        if num[n] >= 5:
            num[n] = 0
 
        if num[0] == 0 and num[1] == 0:
            game_over_label.config(text= "Player 2 Won!\nGame Over!")
            game_over_frame.tkraise()
        
        if num[2] == 0 and num[3] == 0:
            game_over_label.config(text= "Player 1 Won!\nGame Over!")
            game_over_frame.tkraise()
 
    for p in range(len(player_hands)):
        player_hands[p].config(image = pics[num[p]])
 
#This function was written by my collaborative partner
def select(hand,player):
    global player1_selection, player2_selection
    if player == 1:
        if hand == 'Left':
            player1_selection = 'Left'
        elif hand == "Right":
            player1_selection = 'Right'
    elif player == 2:
        if hand == "Left":
            player2_selection = 'Left'
        elif hand == "Right":
            player2_selection = 'Right'
    
    player1_select_label.config(text=player1_selection + " Hand")
    player2_select_label.config(text=player2_selection + ' Hand')
 
def attacking(t): 
    global num_fingers, turn, player1_selection, player2_selection
 
    if t == 1:
        if player1_selection == "Left":
            if player2_selection == "Left":
                num_fingers[2] = num_fingers[0] + num_fingers[2]
            elif player2_selection == "Right":
                num_fingers[3] = num_fingers[0] + num_fingers[3]
            turn=2
        elif player1_selection == "Right":
            if player2_selection == "Left":
                num_fingers[2] = num_fingers[1] + num_fingers[2]
            elif player2_selection == "Right":
                num_fingers[3] = num_fingers[1] + num_fingers[3]
            turn = 2
 
    elif t == 2:
        if player2_selection == "Left":
            if player1_selection == "Left":
                num_fingers[0] = num_fingers[0] + num_fingers[2]
            elif player1_selection == "Right":
                num_fingers[1] = num_fingers[1] + num_fingers[2]
            turn = 1
        
        else:
            if player1_selection == "Left":
                num_fingers[0] = num_fingers[0] + num_fingers[3]
            elif player1_selection == "Right":
                num_fingers[1] = num_fingers[1] + num_fingers[3]
            turn = 1
    
    update(num_fingers)
 
def switching(t):
    global num_fingers, turn
    sum=0
    avg=0
    if t == 1:
        start = 0
        length = 2
        turn = 2
    elif t == 2:
        start = 2
        length = 4
        turn = 1
 
    for i in range(start,length):
        sum = num_fingers[i] + sum
    avg = sum/2
    num_fingers[start] = sum - int(avg)
    num_fingers[length-1] = int(avg)
 
    update(num_fingers)
 
#Window Setup (This code was written by my collaborative partner)
root=Tk()
root.title('Sticks') 
root.geometry('600x750')
 
main_frame=Frame(root)
main_frame.grid(row=0,column=0, sticky='news')
 
game_over_frame=Frame(root)
game_over_frame.grid(row=0,column=0, sticky='news')
 
main_frame.tkraise()
 
game_over_label=Label(game_over_frame, text= "Someone Won!\nGame Over!", font='Arial, 24', anchor="center")
game_over_label.pack()
 
welcome_label=Label(main_frame, text="Sticks Simulator!", font='Arial, 24')
welcome_label.grid(row=0,column=1)
 
player1_label = Label(main_frame, text="Player 1's Side", font='Arial, 12')
player1_label.grid(row=2,column=0, padx=35)
 
player1_select_label = Label(main_frame, text= "No"  + " Hand", font='Arial, 14')
player1_select_label.grid(row=3,column=0)
 
player2_label = Label(main_frame, text="Player 2's Side", font='Arial, 12')
player2_label.grid(row=2,column=2)
 
player2_select_label = Label(main_frame, text= "No"  + " Hand", font='Arial, 14')
player2_select_label.grid(row=3,column=2)
  
turn_label=Label(main_frame, text="Player " + str(turn) + "'s turn \n Click on a hand to select.", font='Arial, 16')
turn_label.grid(row=1,column=1)
 
attack = Button(main_frame, text = "ATTACK",font = "Arial, 14",command= lambda : attacking(turn))
attack.grid(row=6, column = 1)
 
switch = Button(main_frame, text = "SWITCH",font = "Arial, 14",command= lambda : switching(turn))
switch.grid(row=7, column = 1)
 
#Photos
#Hand images courtesy of https://www.madebyteachers.com/seller/sticky-foot-studio/
hand0_image = PhotoImage(file="Hand 0 Front Brown.png")
hand0_image = hand0_image.subsample(7,7)
 
hand1_image = PhotoImage(file="Hand 1 Front Brown.png")
hand1_image = hand1_image.subsample(7,7)
 
hand2_image = PhotoImage(file="Hand 2 Front Brown.png")
hand2_image = hand2_image.subsample(7,7)
 
hand3_image = PhotoImage(file="Hand 3 Front Brown.png")
hand3_image = hand3_image.subsample(7,7)
 
hand4_image = PhotoImage(file="Hand 4 Front Brown.png")
hand4_image = hand4_image.subsample(7,7)
pics = [hand0_image, hand1_image, hand2_image, hand3_image, hand4_image]

#Logo to abide by terms of use of image author
logo = PhotoImage(file='1 logo.png')
logo = logo.subsample(1,1)

logo_label = Label(game_over_frame, text='Images courtesy of: ')
logo_label.pack()

logo_image = Label(game_over_frame, image=logo)
logo_image.pack()
 
#Hand Buttons (This code was written by my collaborative partner) 
player1_left = Button(main_frame, image = pics[1], command= lambda : select(hands[0],1),relief = "groove")
player1_left.grid(row=4,column=0, pady = 20)
 
player1_right = Button(main_frame, image = pics[1], command= lambda : select(hands[1],1),relief = "groove")
player1_right.grid(row=5,column=0)
 
player2_left = Button(main_frame, image = pics[1], command=lambda : select(hands[0],2),relief = "groove")
player2_left.grid(row=4,column=2, pady = 20)
 
player2_right = Button(main_frame, image = pics[1], command=lambda : select(hands[1],2),relief = "groove")
player2_right.grid(row=5,column=2)
 
player_hands = [player1_left, player1_right, player2_left, player2_right]
 
root.mainloop()