# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 17:00:19 2019

@author: gaurav
"""


## taking three inputs at a time 
#full_name_of_VM,name_of_CVC,Name_of_VM = str(input("Enter the full name of VM with CVC is : ")).split( ) 
#print("Name of the CVC is ",name_of_CVC,"of the VM ") 
#print("Name of the VM is  : ",Name_of_VM) 
 



##### AND THE SECOND METHOD BY GIVING REFLEXIVE INDEX


full_name_VM=str(input("enter the name of VM"))
x=full_name_VM.split()
print("name of the CVC of the VM is ",x[0])
print("name of the  the VM is ",x[1])