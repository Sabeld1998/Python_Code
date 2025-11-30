
import tkinter
#create class for gui tool kit 
class PlanetSize:
    #initialize attributes(planets)
    def __init__(self):
        self.main_window=tkinter.Tk()
        
        self.main_window.title('Solar System')
        
        self.canvas=tkinter.Canvas(self.main_window, width=1250, height=600, background='black')
        
        self.canvas.pack()
        
        self.sun()
        
        self.mercury()
        
        self.venus()
        
        self.earth()
        
        self.mars()
        
        self.jupiter()
        
        self.saturn()
        
        self.uranus()
        
        self.neptune()
        
        self.pluto()
        

    #create loop for program persistence
        tkinter.mainloop()

       #draw solar system and create labels
    def drawSolarSystem(self, name, size, color, x, y):
        self.canvas.create_oval(x - size, y - size, x + size, y + size, fill=color, outline=color)
        self.canvas.create_text(x, y + size + 12, text=name, fill='white')
    #set parameters for planet name, size and color. 
    def sun(self):
        self.drawSolarSystem('Sun', 100, 'yellow', 200, 250)
    
    def mercury(self):
        self.drawSolarSystem('Mercury', 20, 'brown', 340, 250)
    
    def venus(self):
        self.drawSolarSystem('Venus', 40, 'saddle brown', 410, 250)
    
    def earth(self):
        self.drawSolarSystem('Earth', 50, 'teal', 510, 250)
    
    def mars(self):
        self.drawSolarSystem('Mars', 35, 'red', 610, 250 )
    
    def jupiter(self):
        self.drawSolarSystem('Jupiter', 70, 'tan', 725, 250)
    
    def saturn(self):
        self.drawSolarSystem('Saturn', 55, 'orange', 860, 250)  
    
    def uranus(self):
        self.drawSolarSystem('Uranus', 40, 'blue', 965, 250)
    
    def neptune(self):
        self.drawSolarSystem('Neptune', 45, 'dark blue', 1060, 250)
    
    def pluto(self):
        self.drawSolarSystem('Pluto', 10, 'grey', 1135, 250)
        #use main statement 

def main():
    PlanetSize()
main()