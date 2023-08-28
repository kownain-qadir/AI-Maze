from tkinter import *
from tkinter.font import BOLD
from pyamaze import maze,agent,COLOR,textLabel
from SearchingAlgorithms import *
from timeit import *

rows = 0
cols = 0

#window
tkWindow = Tk()  
tkWindow.configure(bg='beige')
tkWindow.geometry('750x300')  
tkWindow.title('Maze Game')
v = IntVar()
def startGame():
  tkWindow.destroy()
  m = maze(rows.get(),cols.get())
  m.CreateMaze(loopPercent=v.get(), theme=COLOR.light)

  #Running Depth First Search
  dfsSearchPath, dfsSearch, dfsPath=DFS(m)
  b=agent (m, footprints=True, color=COLOR.red, shape='arrow') 
  m.tracePath({b:dfsPath}, showMarked=True,delay=150, kill=True)

  #Running Breath First search
  bfsSearchPath, bfsSearch, bfsPath=BFS(m)
  a=agent(m,footprints=True,color=COLOR.cyan, shape='arrow')
  m.tracePath({a:bfsPath}, showMarked=True,delay=150, kill=True)

  #Dijkstra searching Algo  
  djkSearch,djkPath,tCost=dijkstra(m)
  textLabel(m,'Djk COST',tCost+1)
  c=agent(m,color=COLOR.green,footprints=True , shape='arrow')
  m.tracePath({c:djkPath}, showMarked=True,delay=150)

  textLabel(m, 'DFS Search ', len(dfsSearchPath)+1)
  textLabel(m, 'BFS Search ', len(bfsSearchPath)+1)
  textLabel(m, 'Djk Search ', len(djkSearch)+1)
  textLabel(m, 'DFS Path ', len(dfsPath)+1)
  textLabel(m, 'BFS Path ', len(bfsPath)+1)
  textLabel(m, 'Djk Path ', len(djkPath)+1)

  t1=timeit('DFS' , globals=globals())
  t2=timeit('BFS' , globals=globals())
  t3=timeit('dijkstra' , globals=globals())

  textLabel(m, 'DFS ' ,t1)
  textLabel(m, 'BFS ' ,t2)
  textLabel(m, 'Dijkstra ' ,t3)
 
  m.run()

colLabel = Label(tkWindow, 
        text="MAZE GAME",
        background = "beige",
        font=('Times New Roman',30,BOLD)).grid(row=0, column=2)
#rows entry
rowLadel = Label(tkWindow, text="No. of rows          ",background = "beige").grid(row=1, column=0)
try:
  rows = IntVar()
  rowEntry = Entry(tkWindow, textvariable=rows,background = "light blue").grid(row=1, column=1)  
except:
  rowEntry = Entry(tkWindow, textvariable="Invalid Input ").grid(row=1, column=1)  

#Columns Entry 
colLabel = Label(tkWindow,text="No. of columns",background = "beige").grid(row=1, column=3)  
try:
  cols = IntVar()
  colEntry = Entry(tkWindow, textvariable=cols,background = "light blue").grid(row=1, column=4)  
except:
  colEntry = Entry(tkWindow, textvariable="Invalid Input ").grid(row=1, column=4)  


colLabel = Label(tkWindow, 
        text="Choose a Maze Type:",
         background = "beige",
        font=('Times New Roman', )).grid(row=4, column=2)

radio1 = Radiobutton(tkWindow, 
               text="Perfect Maze",
               padx = 2, 
               variable=v, 
               value=0,
               background = "light blue").grid(row=8, column=1)

radio2 = Radiobutton(tkWindow, 
               text="Multiple Path Maze",
               background = "light blue",
               variable=v, 
               value=80).grid(row=8, column=3)

#login button
loginButton = Button(tkWindow, text="Start Comparing", command=startGame ,background = "light blue",).grid(row=9, column=2)  

tkWindow.mainloop()