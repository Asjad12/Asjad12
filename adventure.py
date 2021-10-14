actions = ["forward", "backward", "left" ,"right"]

def menu():
 for action in actions:
   print(f" {action}")


def action_1():
  print("""
  Level 1
  """)
  print(" Choose an action: ")
  menu()
  action_input = input("action: ")
  if action_input in actions[0]:
    print("Ran into the garbage")
    action_1()
  if action_input in actions[1]:
    print("You hit the cop")
    action_1()
  if action_input in actions[2]:
    print("There's a wall")
    action_1()
  if action_input in actions[3]:
    print("Drive on the right side")
    action_2()
  elif action_input not in actions:
    print("invalid action")
  
def action_2():
  print("""
  Level 2
  """)
  print(" Choose an action: ")
  menu()
  action_input = input("action: ")
  if action_input in actions[0]:
    print("hit a pedestrian")
    action_2()
  if action_input in actions[1]:
    print("the cop cought up")
    action_2()
  if action_input in actions[2]:
    print("700m from safe house")
    action_2()
  if action_input in actions[3]:
    print("Drive on the left side")
    action_2()
  elif action_input not in actions:
    print("invalid action")

action_1()

menu()

def action_2():
  print("""
  Level 3
  """)
  print(" Choose an action: ")
  menu()
  action_input = input("action: ")
  if action_input in actions[0]:
    print("drove of a bridge")
    action_2()
  if action_input in actions[1]:
    print("made it to safehouse")
    action_2()
  if action_input in actions[2]:
    print("cop arrested You")
    action_2()
  if action_input in actions[3]:
    print("Drive straight")
    action_2()
  elif action_input not in actions:
    print("invalid action")

action_1()

menu() 
def action_2():
  print("""
  Level 3
  """)
  print(" Choose an action: ")
  menu()
  action_input = input("action: ")
  if action_input in actions[0]:
    print("drove of a bridge")
    action_2()
  if action_input in actions[1]:
    print("made it to safehouse")
    action_2()
  if action_input in actions[2]:
    print("cop arrested You")
    action_2()
  if action_input in actions[3]:
    print("Drive straight")
    action_2()
  elif action_input not in actions:
    print("invalid action")