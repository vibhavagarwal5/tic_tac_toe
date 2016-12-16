from Tkinter import *
import tkMessageBox
import pvp
import comp

class MainGUI(Frame,pvp.pvp_app,comp.comp_app):
        #initializing the frame
	def __init__(self,master):
		Frame.__init__(self,master)
		self.grid()
		self.configure(background="green")
		self.ShowHomepage()

        #creating the buttons and label for the home page.
	def ShowHomepage(self):
		self.homepage_label = Label(self,text="WELCOME TO THE WORLD OF TIC-TAC-TOE",font=("courier",15),fg="red",bg="yellow") #label
		self.homepage_label.grid(row=0 , column=1 , padx=20 , pady=25 )
		
		self.start_button = Button(self,text="Start Game",command=self.StartGame,fg="blue")                                   #start button
		self.start_button.grid(row=1,column=1,padx=100,pady=50)

		self.rules_button = Button(self,text="Rules",command=self.ShowRule,fg="red")                                          #rules button
		self.rules_button.grid(row=2,column=1,padx=100,pady=50)

		self.quit_button = Button(self,text="Quit",command=self.QuitGame,fg="purple")                                         #exit button
		self.quit_button.grid(row=3,column=1,padx=100,pady=50)
       
        #creating the start page
	def StartGame(self):
        #Clears the screen when start button is pressed
		self.rules_button.grid_forget()
		self.quit_button.grid_forget()
		self.homepage_label.grid_forget()
		self.start_button.grid_forget()
		#Player is given two options as to whom he wants to play against.
		self.startgame_label = Label(self,text="Whom do you want to play against?",font=("courier",15),fg="red",bg="yellow")#label
		self.startgame_label.grid(row=0 , column=1 , padx=20 , pady=25 )
		self.pvp_button = Button(self,text="2 Player Mode",command=lambda: pvp.pvp_app.PlayerGame(self))                    #player VS player button
		self.pvp_button.grid(row=2 , column=1 ,padx=100 , pady=50)
		self.comp_button = Button(self,text="VS Computer Mode",command=lambda: comp.comp_app.computerGame(self))            #against computer button
		self.comp_button.grid(row=3 , column=1 ,padx=100 , pady=50)	
		self.back_s_button = Button(self,text="Back",command=self.back_startGame)                                           #back button
		self.back_s_button.grid(row=4,column=1,padx=100,pady=50)

        #creating the rules page
	def ShowRule(self):
        #clears the screen when rules button is pressed
		self.homepage_label.grid_forget()
		self.start_button.grid_forget()
		self.rules_button.grid_forget()
		self.quit_button.grid_forget()
		#displays rules to the player
		self.rules_label = Label(self,text="Game for two players,X and O,\nwho take turns marking the spaces\nin a 3x3 grid.The player who\nsucceeds in placing three of their marks\nin a horizontal,vertical\nor diagonal row wins the game.",font=("pursia",15),fg="red",bg="green")
		self.rules_label.grid(row=0 , column=1 , padx=45, pady=35 )                                                         
		self.back_r_button = Button(self,text="Back",command=self.back_rules)                                            
		self.back_r_button.grid(row=2,column=1,padx=100,pady=50)                                                            #back button

        #Enables the player to exit the game
	def QuitGame(self):
		self.message=tkMessageBox.askquestion("Exit","Do you want to exit ?")
		if (self.message =='yes'):
			root.destroy()

        #takes player back to home page from rules page
	def back_rules(self):
		self.rules_label.grid_forget()
		self.back_r_button.grid_forget()
		self.ShowHomepage()

        #takes player back to homepage from start page
	def back_startGame(self):
        #clearing all the buttons
		self.pvp_button.grid_forget()
		self.back_s_button.grid_forget()
		self.comp_button.grid_forget()
		self.startgame_label.grid_forget() 
        #calling showHomepage function
		self.ShowHomepage()		

# "root" is the Tkinter window
root=Tk()
root.title("Tic Tac Toe")
root.geometry("460x600")
root.config(bg="green")
#"appl" is the object of the super-class "MainGUI" whose sub-classes are pvp and comp.         
appl=MainGUI(root)
root.mainloop()
