
import pyautogui, time
time.sleep(10)	#  10 Seconds to open target location
f = open("junk.txt", 'r')

for word in f:
	pyautogui.typewrite(word)
	pyautogui.press("enter")
	

f.close()
#dijsktra
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
 
    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])
