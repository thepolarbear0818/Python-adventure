#123
#this is quite odd 
import os
import requests
import json 
import random 

print("hello my friend")

e = input()

mums = ["your mum","you're mum","mum","mom"]
if input() == "goodbye":
  print("lameeeeeee")



if any(word in e for word in mums): # dont change this or that will break it, it looks for a word match in mums and e is our input
  print("You are my mum : hit enter")
  
  

  if e == ("I don't have a child"):
    print("You created me therefore you are my parent")
    
#if any(word in e for word in mums):
  #print("this mum thing works i guess")

if any(word in e for word in moms):
  print("you are my mom ")  

else:
  print("beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeep malfunction detected")

