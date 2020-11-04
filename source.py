from tkinter import *
import tkinter as tk
import networkx as nx 
import matplotlib.pyplot as plt 
class GraphVisualization:
  def __init__(self): 
    self.visual = [] 
    
  def addEdge(self, a, b): 
    temp = [a, b] 
    self.visual.append(temp) 

  def visualize(self): 
    G = nx.Graph() 
    G.add_edges_from(self.visual) 
    nx.draw_networkx(G) 
    plt.show() 

root = Tk()
root.geometry("233x69")

Label(root, text='Number of vertices').grid(row=0, column = 0, sticky = 'NEWS') 
Label(root, text='Number of edges').grid(row=1 , column = 0, sticky = "NEWS") 
e1 = Entry(root, textvariable = IntVar()) 
e2 = Entry(root, textvariable = IntVar()) 
e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)


def new_Window():
	new_window = Toplevel(root)
	a1 = int(e2.get())
	x = a1 + 1
	lst = []
	arr = []
	G = GraphVisualization()
	def generate():
		for x in lst:
			i = int(x[0].get())
			j = int(x[1].get())
			G.addEdge(i, j)
		G.visualize()
	for i in range(1, a1 + 1):
		a = Entry(new_window, textvariable = IntVar())
		b = Entry(new_window, textvariable = IntVar())
		Label(new_window, text = 'edge{} = '.format(i)).grid(row = i, column = 0)
		arr.append(a)
		arr.append(b)
		lst = (arr)
		a.grid(row = i, column = 1)
		b.grid(row = i, column = 2)

	B1 = Button(new_window, text = 'Generate Graph', command = generate).grid(row = x, columnspan = 3, sticky = "NEWS")

B = Button(root, text = 'Insert Values!', command = new_Window).grid(row = 3, columnspan = 2, sticky = "NEWS")
mainloop()
