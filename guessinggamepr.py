import random
def gamewin(comp,you):
 if comp==you:
  return None

 elif comp=="s":
  if you=="g":
   return True
  elif you=="w":
   return False

 elif comp=="w":
  if you=="s":
   return True
  elif you=="g":
   return False

 elif comp=="g":
  if you=="s":
   return False
  elif you=="w":
   return True
randomno=random.randint(1,3)
if randomno==1:
 comp=("s")
elif randomno==2:
 comp=("w")
elif randomno==3:
 comp=("g")

you=input("""your turn:snak(s),water(w),
gun(g)?")""")
a=gamewin(comp,you)
print("computer choose",(comp))
print("you choose",(you))

if a==None:
 print("it is tie")
elif a:
 print("you are win")
else:
 print("you are lose")




