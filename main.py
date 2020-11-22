import matplotlib.pyplot as plt
import numpy as np


def RightTurn(p1, p2, p3):
	if (p3[1]-p1[1])*(p2[0]-p1[0]) >= (p2[1]-p1[1])*(p3[0]-p1[0]):
		return False
	return True
	
def GrahamScan(P):
	P.sort()			
	L_upper = [P[0], P[1]]		
	for i in range(2,len(P)):
		L_upper.append(P[i])
		while len(L_upper) > 2 and not RightTurn(L_upper[-1],L_upper[-2],L_upper[-3]):
			del L_upper[-2]
	L_lower = [P[-1], P[-2]]	
	for i in range(len(P)-3,-1,-1):
		L_lower.append(P[i])
		while len(L_lower) > 2 and not RightTurn(L_lower[-1],L_lower[-2],L_lower[-3]):
			del L_lower[-2]
	del L_lower[0]
	del L_lower[-1]
	L = L_upper + L_lower	
	return np.array(L)

def main():
	
	fileWithDots = open("DS9.txt", "r")
	listOfDots = fileWithDots.readlines()
	fileWithDots.close()

	P = []

	for i in range(len(listOfDots)):
	    listOfDots[i] =  listOfDots[i].split()
	    temp_lst = (int(listOfDots[i][1]), int(listOfDots[i][0]))
	    P.append(temp_lst)

	L = GrahamScan(P)
	P = np.array(P)
	
	plt.figure()
	plt.plot(L[:,0],L[:,1], 'b-', picker=5)
	plt.plot([L[-1,0],L[0,0]],[L[-1,1],L[0,1]], 'b-', picker=5)
	plt.savefig('plot.png', dpi=70, bbox_inches='tight')
	plt.show()

if __name__ == '__main__':
	main()

