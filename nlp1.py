# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 22:54:02 2018

@author: ahanmr
"""

import re
my_string="Let's write RegEx!  Won't that be fun?  I sure think so.  Can you find 4 sentences?  Or perhaps, all 19 words?"
pattern= r"\w+"
#prints all the words in the string 
print(re.findall(pattern, my_string))
#finds  all the words starting with a capital letter
pattern1= r"[A-Z]\w+"
print(re.findall(pattern1, my_string))
#splits the sentence exactly when we find a stopping symbols
pattern2= r"[.,?,!]"
print(re.split(pattern2, my_string))

#splits at spaces
pattern3= r"\s"
print(re.split(pattern3, my_string))

#splits at digits
pattern4= r"\d"
print(re.split(pattern4, my_string))
