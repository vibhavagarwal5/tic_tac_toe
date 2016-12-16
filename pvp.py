from Tkinter import *
import tkMessageBox

class pvp_app(Frame):
    def __init__(self):
        Frame.__init__(self)

    #Takes user to the main gaming area
    def PlayerGame(self):    
        #clears the screen when player vs player is selected
        self.pvp_button.grid_forget()
        self.back_s_button.grid_forget()
        self.comp_button.grid_forget()
        self.startgame_label.grid_forget()

        #Adding buttons and label
        self.start_label=Label(self,text="Who will start the game?")                                    #lable
        self.start_label.grid(row=0,columnspan=4)
        self.p1_button=Button(self,text="player 1",fg="blue",command=lambda: self.startGame(TRUE,FALSE))#player 1 button
        self.p1_button.grid(row=1,column=0)
        self.p2_button=Button(self,text="player 2",fg="blue",command=lambda: self.startGame(FALSE,TRUE))#player 2 button
        self.p2_button.grid(row=1,column=2) 
        self.back_p_button=Button(self,text="Back",fg="blue",bg="green",command=self.back_r_button)     #back button
        self.back_p_button.grid(row=5,column=1)

        #initializing a list to use to create grid buttons                  
        self.button_lst=[0,1,2,3,4,5,6,7,8,9]

        #loop to create grid buttons 
        for i in range(1,10):
           self.button_lst[i]=Button(self,text=" ",fg="yellow",bg="red",state=DISABLED,command=lambda j=i: self.handle_button(j), height=3,width=7, font=("Purisa", 24))

        #loop to arrange grid buttons 
        L = [[1,4,0], [2,4,1], [3,4,2],             #[button number,row,column] 
             [4,3,0], [5,3,1], [6,3,2],
             [7,2,0], [8,2,1], [9,2,2]]
        for i in L:
            self.button_lst[i[0]].grid(row=i[1], column=i[2])
    
    #starting the game when player is selected.
    def startGame(self,p1,p2):
        #Disabling buttons        
        self.p1_button.config(state=DISABLED)
        self.p2_button.config(state=DISABLED)
        self.back_p_button.config(state=DISABLED)

        #turning on the grid buttons
        for i in range(1,10):
            self.button_lst[i].config(state=NORMAL)
            
        #if player1 is true, player1 starts the game otherwise the player2 starts     
        if(p1==TRUE):
            self.start_label.config(text="Player 1 starts the game with a X")                   #label if player 1 is selected
            self.turn=TRUE
        else:
            self.start_label.config(text="Player 2 starts the game with a O")                   #label if player 2 is selected
            self.turn=FALSE

        self.bState=[10,0,0,0,0,0,0,0,0,0]                                                      #state of button +1=player1,-1=player2.
        self.GameDone=FALSE

    #if a grid button is clicked
    def handle_button(self,i):
        #i is the number of the button that was pushed
        if(self.turn==TRUE):
            self.button_lst[i].config(text="X",state=DISABLED)
            self.turn=FALSE
            self.bState[i]=1

        else:
            self.button_lst[i].config(text="O",state=DISABLED)
            self.turn=TRUE
            self.bState[i]=-1

        self.check()                                

    #checking whether the game is finished or not
    def check(self):
        #list of possible win combinations in the form of button numbers
        WinCombo=[[1,2,3], [4,5,6], [7,8,9],    #rows   
                  [1,4,7], [2,5,8], [3,6,9],    #columns
                  [1,5,9], [3,5,7]]             #diagonals

        #after doing sums look for 3 or -3 to find if there was a winner
        for i in WinCombo:                                                                      
            if((self.bState[i[0]]+self.bState[i[1]]+self.bState[i[2]])==3):                     #3 means player1 has won
                self.start_label.config(text="Player 1 won!!")                                  #label if player 1 is won
                self.GameDone=TRUE
                for k in range(1,10):
                    self.button_lst[k].configure(state=DISABLED)
                break
            elif((self.bState[i[0]]+self.bState[i[1]]+self.bState[i[2]])==-3):                  #-3 means player2 has won
                self.start_label.config(text="Player 2 won!!")                                  #label if player 2 is won
                self.GameDone=TRUE
                for k in range(1,10):
                    self.button_lst[k].configure(state=DISABLED)
                break
            else:
                                                                                                
                if not (0 in self.bState):                                                      #if there is no 0 in button state , the game is done
                    self.start_label.config(text="Match drawn!!")                               #label if match is drawn
                    self.GameDone=TRUE
                    for k in range(1,10):
                        self.button_lst[k].configure(state=DISABLED)
                    break

        #if game is done,asking the player if he want to play again through tkmessagebox
        if(self.GameDone==TRUE):
            self.message=tkMessageBox.askquestion(" ","Do you want to play the game again?")    #message in the tkmessage box
            if(self.message=="no"):                                         #if player want to exit
                self.QuitGame()
            else:                                                           #if player want to play again
                self.p1_button.config(state=NORMAL)
                self.p2_button.config(state=NORMAL)
                self.back_p_button.config(state=NORMAL)
                self.start_label.config(text="Who will start the game?")
                for i in range(1,10):
                    self.button_lst[i].config(text=" ", state=DISABLED)

    #back button to startpage
    def back_r_button(self):
        #takes player to startpage
        self.p1_button.grid_forget()
        self.p2_button.grid_forget()
        self.back_p_button.grid_forget()
        self.start_label.grid_forget()
        for i in range(1,10):
            self.button_lst[i].grid_forget()
        self.StartGame()                 
