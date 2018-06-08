# our 4 rooms
def kitchen():
    print("you are in the kitchen.")

def tv
tvRoom():
    print("you are in the TV room.")

def bedroom():
    print("you are in the bedroom.")

def bathroom():
    print("you are in the bathroom")
# Our Main Function
def main():
    currentRoom = "TV_ROOM"
    direction = ""
     
    tvRoom()
    direction = raw_input("What direction would you like to go? (north, south, east, west)").lower()
 
    # How to leave the Kitchen
    if currentRoom == "KITCHEN":
        if direction == "south":
            currentRoom = "TV_ROOM"
        elif direction == "east":
            currentRoom = "BEDROOM"
        else:
            print("Ouch! You hit a wall!")
 
    # How to get leave the TV Room
    if currentRoom == "TV_ROOM":
        if direction == "north":
            currentRoom = "KITCHEN"
        elif direction == "east":
            currentRoom = "BATHROOM"
        else:
            print("Ouch! You hit the wall!")
     
    # Display the information about which room is occupied
    if(currentRoom == "KITCHEN"):
        kitchen()
    elif(currentRoom == "TV_ROOM"):
        tvRoom()
    elif(currentRoom == "BEDROOM"):
        bedroom()
    elif(currentRoom == "BATHROOM"):
        bathroom()
 
# Call the Main Function
main()
