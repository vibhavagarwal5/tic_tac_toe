from Tkinter import *
import tkMessageBox
import random

class comp_app(Frame):
    def __init__(self):
        Frame.__init__(self)

    def computerGame(self):
        #clears the screen when vs computer button is selected
        self.pvp_button.grid_forget()
        self.back_s_button.grid_forget()
        self.comp_button.grid_forget()
        self.startgame_label.grid_forget()

        #Adding of new buttons and labels
        self.start_label=Label(self,text="Who will start the game?")                                            #lable
        self.start_label.grid(row=0,columnspan=4)
        self.player_button=Button(self,text="Me",fg="blue",command=lambda: self.startGame_c(TRUE))              #me button
        self.player_button.grid(row=1,column=0)
        self.computer_button=Button(self,text="Computer",fg="blue",command=lambda: self.startGame_c(FALSE))     #computer button
        self.computer_button.grid(row=1,column=2) 
        self.back_c_button=Button(self,text="Back",fg="blue",bg="green",command=self.back_c_button)             #back button    
        self.back_c_button.grid(row=5,column=1)  

        #initialize a list to use grid buttons (0 to 9 are taken so that buttons can be  assigned from 1 to 9)    
        self.button_lst=[0,1,2,3,4,5,6,7,8,9]

        #loop to create grid buttons
        for i in range(1,10):
           self.button_lst[i]=Button(self,text=" ",fg="yellow",bg="red",state=DISABLED, height=3,width=7, font=("Purisa", 24),command=lambda j=i: self.handle_button_c(j))

        #loop to arrange grid buttons
        L = [[1,4,0], [2,4,1], [3,4,2],         #[button number, row, column] 
             [4,3,0], [5,3,1], [6,3,2],
             [7,2,0], [8,2,1], [9,2,2]]
        for i in L:
            self.button_lst[i[0]].grid(row=i[1], column=i[2])

    #starting the game
    def startGame_c(self,pl):
        #turning me,computer and again buttons off"
        self.player_button.config(state=DISABLED)
        self.computer_button.config(state=DISABLED)
        self.back_c_button.config(state=DISABLED)

        #turning the grid buttons on
        for i in range(1,10):
            self.button_lst[i].config(state=NORMAL)

        # to reset the bState and Sums lists and instance variables
        self.bState=[8,0,0,0,0,0,0,0,0,0]                              #bStates of button  player-(1) ,computer-(-1) ,available-0
        self.bSum=[0,0,0,0,0,0,0,0]                                     #storing the values of the values according to the WinCombos

        self.GameDone=FALSE
        self.specialDefense = FALSE

        #if 'player' is True, the player starts the game otherwise the computer starts 
        if(pl==TRUE):
            self.start_label.config(text="You start the game with a X, make a move")    #label if player is selected
            self.turn=TRUE
        else:
            self.start_label.config(text="The computer starts the game with a O")       #label if computer is selected
            self.turn=FALSE
            self.move()

    #function to be performed when a button is pressed 
    def handle_button_c(self,i):
        #i is the number of the button that was pushed 
        # if turn is true the player makes a move otherwise computer makes a move        
        if(self.turn==TRUE):
            self.button_lst[i].config(text="X",state=DISABLED)
            self.turn=FALSE
            self.bState[i]=1

        else:
            self.button_lst[i].config(text="O",state=DISABLED)
            self.turn=TRUE
            self.bState[i]=-1

        #testing whether game is finished or not
        self.check_c()                                
        if (self.turn==FALSE and self.GameDone==FALSE):
            self.move()

    #defines how the computer makes the move according to the players move
    def move(self):
        #mix it up a little by starting with the center for first move sometimes
        #to make the first move if the first turn is computer's
        if 1 not in self.bState and -1 not in self.bState: 
            if random.random() < 0.50:                                                  #50% of the time start in center
                self.handle_button_c(5)
                return

        #to handle the case where player has made first move to a corner
        if 1 in self.bState and -1 not in self.bState:
            if(self.bState[1]==1 or self.bState[3]==1 or self.bState[9]==1 or self.bState[7]==1):
            
                self.handle_button_c(5)
                self.specialDefense = TRUE
                return

        #test if computer can win, if so do the move
        for i in range(1,10):
            if self.bState[i] == 0:
                self.bState[i] = -1                                                     # to make a trial move
                self.sum()
                if -3 in self.bSum:                                                     #if -3 means computer has won
                    self.handle_button_c(i)                                             #to make that move if its a win
                    return
                else:
                    self.bState[i] = 0                                                  #to switch back to the bstate=0

        #to test if player can win, if so to block it
        for i in range(1,10):
            if self.bState[i] == 0:
                self.bState[i] = 1                                                      #make a trial move
                self.sum()
                if 3 in self.bSum:                                                      #if 3 means player has won
                    self.handle_button_c(i)                                             #block if player could win
                    self.specialDefense = FALSE 
                    return
                else:
                    self.bState[i] = 0                                                  #switch back if not a win

        #for the second special defense move, to pick a side
        if self.specialDefense:
            self.specialDefense = FALSE
            sides = [2,4,6,8]
            random.shuffle(sides)                                                       #to shuffle them 
            for i in sides:
                if self.bState[i] == 0:
                    self.handle_button_c(i)
                    return

        #to pick a corner if open
        corners = [1,3,7,9]
        random.shuffle(corners)                                                         #to shuffle them 
        for i in corners:
            if self.bState[i] == 0:
                self.handle_button_c(i)
                return

        #to take center if open after the player's moves are done
        if self.bState[5] == 0:
            self.handle_button_c(5)
            return

        #to pick a side if open after the player's moves are done
        sides = [2,4,6,8]
        random.shuffle(sides)                                                           #to shuffle them 
        for i in sides:
            if self.bState[i] == 0:
                self.handle_button_c(i)
                return

    #checks whether game is done or not
    def check_c(self):
        self.sum()
        #after doing sums look for 3 or -3 to find if there was a winner
        for i in self.bSum:
            if(i==3):                                                                            # 3 in Sums means player has won
                self.start_label.config(text="Player 1 won!!")                                   # label if player is won
                self.GameDone=TRUE
                for k in range(1,10):
                    self.button_lst[k].configure(state=DISABLED)
                break
            elif(i==-3):                                                                         # -3 in Sums means computer has won
                self.start_label.config(text="Computer won!!")                                   #label if computer is won
                self.GameDone=TRUE
                for k in range(1,10):
                    self.button_lst[k].configure(state=DISABLED)
                break
            else:
                if not (0 in self.bState):                                                       #if there is no 0 in bState, the game is done
                    self.start_label.config(text="Match drawn!!")                                #label if game draws
                    self.GameDone=TRUE
                    for k in range(1,10):
                        self.button_lst[k].configure(state=DISABLED)
                    break

        #if game is done,asking the player if he want to play again, through Tkmessagebox
        if(self.GameDone==TRUE):
            self.message=tkMessageBox.askquestion(" ","Do you want to play the game again?")     
            if(self.message=="no"):                                                         #if player want to exit
                self.QuitGame()
            else:                                                                           #if player want to play again
                self.player_button.config(state=NORMAL)
                self.computer_button.config(state=NORMAL)
                self.back_c_button.config(state=NORMAL)
                self.start_label.config(text="Who will start the game?")
                for i in range(1,10):
                    self.button_lst[i].config(text=" ", state=DISABLED) 

    #to do sums of button states of rows, columns and diagonals      
    def sum(self):
        #list of possible win combinations in the form of button numbers
        WinCombo=[[1,2,3], [4,5,6], [7,8,9],    #rows
                  [1,4,7], [2,5,8], [3,6,9],    #diagnols
                  [1,5,9], [3,5,7]]             #columns
        count=0
        for i in WinCombo:
            self.bSum[count]=0
            for j in i:
                self.bSum[count]+=self.bState[j]
            count+=1    

    #takes player to start page
    def back_c_button(self):
        #clears the screen
        self.start_label.grid_forget()
        self.player_button.grid_forget()
        self.computer_button.grid_forget()
        self.back_c_button.grid_forget()
        for i in range(1,10):
            self.button_lst[i].grid_forget()
        #calling startgame function
        self.StartGame()               
