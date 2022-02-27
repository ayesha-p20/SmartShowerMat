from tkinter import *

def displayActivatedSensor(alpha, num):
    col = (ord(alpha) - 65) * 100 
    row = (num - 1)* 100
    c.create_rectangle(col, row, col+100, row+100, outline="red", fill="red")

def indices():
    letter = 64
    for i in range(0,8):
        num = 1
        letter += 1
        for j in range(0,4):
            if j == 2 and i == 7:
                break
            
            index = str(chr(letter)) + str(num)
            c.create_text(i*100 + 50, j * 100 + 50, text= index, fill="white", font=('Helvetica 12 bold'))
            num += 1
            
    
def create_grid(event=None):
    w = c.winfo_width() # Get current width of canvas
    h = c.winfo_height() # Get current height of canvas
    c.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines at intevals of 100
    for i in range(0, w, 100):
        c.create_line([(i, 0), (i, h)], tag='grid_line',fill="white")

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, 100):
        c.create_line([(0, i), (w, i)], tag='grid_line', fill="white")

    #numbers()
    #adcIndices()
    indices()

viz = Tk()
viz.title("Sensor Visualization")
viz.resizable(0,0)

c = Canvas(viz, height=400, width=800, bg='black')
c.pack(fill=BOTH, expand=True)

c.bind('<Configure>', create_grid)

displayActivatedSensor('A',3)
viz.mainloop()
