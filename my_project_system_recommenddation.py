# -*- coding: utf-8 -*-
#"""
#Created on Thu Jun 20 12:45:39 2019
#
#@author: gaurav
#
#"""

from collections import OrderedDict

def search(nirbhay,harshit):
    ans = False
    for i in nirbhay :
        for j in harshit :
            if i==j:
                ans = True  
                break
    return ans

def not_common_movies(nirbhay,harshit):
    recommended_list = {}
    for key1,value1 in nirbhay.items():
        ans = False
        for key2,value2 in harshit.items():    
            if key1==key2:
                ans = True
                break
        if ans == False:
           recommended_list.update({key1:value1})
    return recommended_list







nirbhay={'spiderman': 4,'Jhonny_English': 3,'ironman': 3}
harshit={'spiderman': 5,'ironman': 3 }
find=search(nirbhay,harshit)
if find:
    if len(nirbhay)>len(harshit):
        recommended_movies=not_common_movies(nirbhay,harshit)
        for key,value in recommended_movies.items():
            if value >=3 :
                print("harshit should watch ",key)
        else:
            recommended_movies = not_common_movies(harshit,nirbhay)
            for key,value in recommended_movies.items():
                if value >=3 :
                  print("nirbhay should watch ",key)
        
else:   
     print("not common interest")  
   
