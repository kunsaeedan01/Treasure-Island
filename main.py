
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("left or right?")

if direction == "left":
  action = input("swim or wait ")
  if action == "wait":
    door = input("which door? ")
    if door =="red":
      print("burned by fire. game over ")
    elif door == "blue":
      print("eaten by beast. game over ")
    elif door == "yellow":
      print("You win")
    else:
      print("game over")
  else:
    print("attacked by shark. game over")
else:
   print("fall into hole, game over")
