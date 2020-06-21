"# TrafficManagement"   
	Import map.csv and frame a 2D array. This csv file has the adjacency matrix.  
	Read lane.json and form a list of dictionaries  
	Read traffic.json and form a list of dictionaries  
	Initialiase indepJunc to hold the information of juctions and their lanes  
	Use selection sort the list of tuples where the last index in every tuple is the density of vehicles.  
	Use edf func to schedule based on the densities at each lane    
	Print the periods during which respective lanes will remain open (signal-green).  
