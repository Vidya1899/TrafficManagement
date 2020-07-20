"# TrafficManagement"   
	Import map.csv and frame a 2D array. This csv file has the adjacency matrix.  
	Read lane.json and form a list of dictionaries  
	Read traffic.json and form a list of dictionaries  
	Initialiase indepJunc to hold the information of juctions and their lanes  
	Use selection sort the list of tuples where the last index in every tuple is the density of vehicles.  
	Use edf func to schedule based on the densities at each lane    
	Print the periods during which respective lanes will remain open (signal-green).  
  
Output(elaborated) :  
At junction 1 :a1(end 1 of lane ‘a’) opens at 12:00.  
At junction 2: b1(end 1 of lane ‘b’) opens at 12:00.  
At junction 2: d2(end 2 of lane ‘d’) opens at 12:00.  
At junction 3: c1(end 1 of lane ‘c’) opens at 12:00.  
At junction 4: c2(end 2 of lane ‘c’) opens at 12:00.  
At junction 2: e2(end 2 of lane ‘e’) opens at 12:02.  
At junction 2: a2(end 2 of lane ‘a’) opens at 12:02.  
At junction 3: b2(end 2 of lane ‘b’) opens at 12:04.  
At junction 4: d1(end 1 of lane ‘d’) opens at 12:06.  





