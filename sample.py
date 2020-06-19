# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 23:25:40 2020

@author: VIDYA
"""
def sortlist(samplelist):
    #samplelist=[('a', 2, 2), ('b', 1, 1), ('e', 1, 6)]
    sortedlist= sorted(samplelist, key=lambda tup: tup[2])
    return(sortedlist)

samplelist={1: [('a', 1, 4)], 2: [('a', 2, 2), ('b', 1, 1), ('e', 1, 6)], 3: [('b', 2, 6), ('c', 1, 2)], 4: [('c', 2, 3), ('d', 1, 4)], 5: [('d', 2, 1), ('e', 2, 2)]}
#ans=sortlist(samplelist)
for lists in samplelist:
    print(samplelist[lists])
    print(lists)
#print(ans)
#def bubble(ls):


  
    
    
    
    
    
    
    
    
    
    
    
    
    
    