inventory = []
point = 0
directions = [["e", "east"], ["w", "west"]]


def game():
    start()
    scene1()
    scene2()
    print("game complete")


def start():
    print("Hello, welcome to my game... muhhahaha")
    print("My name is Danielle, Danielle from MLH and I prepared a beginner text based adventure for you all!")
    print("Use this to learn how text based adventures work and to inspire yours!")

    start = "false"
    start = input("Are you ready to begin? ").lower()
    while start != "yes":
        if start in ["y", "true", "yeah"]:
            start = "yes"
        else:
            print("Um... okay...")
            start = input("Are you ready to begin now? ").lower()

    print("Excellent!")


def commonAsks(action):
    global inventory, point
    if action in ["inventory", "i"]:
        print("You have this in your inventory: ")
        for item in inventory:
            print(item)
    if "point" in action:
        print("You now have", point, "points")


def scene1():
    print("You wake up in your room.")
    print(
        "In text based adventures you can use commands like: Type l to look around and type x [item name] to examine an item.")
    print("Other common key works include (but are not limited to) push, pull, open, read, and take")
    sceneDone = "false"
    while sceneDone == "false":
        action = input("What do you want to do? ").lower()
        commonAsks(action)
        if action == "l":
            print("You look around the room. You see a door and a mirror.")
        if action == "x door":
            print("It is just your bedroom door")
        if action == "x mirror":
            print("You look in the mirror, you see your long neck, and brown spots on your yellow fur. You look at the sparkly colors fluctuate around your body. You are... Gene the Glitchy Giraffe")
        if action == "open door":
            sceneDone = "true"


def scene2():
    global directions
    print("You are now in the woods outside your house.")
    sceneDone = "false"
    while sceneDone == "false":
        action = input("What do you want to do? ").lower()
        if action == "l":
            print(
                "There is a path to your east and west. The door to your home is behind you.")
        if action in directions[0]:
            frankieScene()
            sceneDone = "true"
        if action in directions[1]:
            adaScene()
            sceneDone = "true"
        commonAsks(action)


def frankieScene():
    global point, directions
    print("You head down the east path and come to a river.")
    sceneDone = "false"
    while sceneDone == "false":
        action = input("What do you want to do? ").lower()
        if action == "l":
            print(
                "You see frankie standing on the edge of the river looking frustrated and nervous.")
            print("There are several trees on your right.")
            print("Your house is to the West.")
            print("There is a rock like lump in the water downstream")
        if action == "x frankie":
            print(
                "Frankie is standing on the edge of the river looking frustrated and nervous.")
        if action == "talk frankie":
            print("You walk up to Frankie and ask what he is doing")
            print("Frankie: Hey y y Gene... I'm trying to get across the river to get to the store, but I just dont know how to swim!")
            print("Poor Frankie... I wonder if we can help him!")
        if action in ["x tree", "x trees"]:
            print("There is a cup on the on of the trees")
        if action == "take cup":
            inventory.append("LeFlurry")
            print("You put a LeFlurry ice cream cup from LeDonald in your pocket.")
        if action in ["x rock", "x lump"]:
            print("The lump start moving!")
            print("IT IS ACTUALLY BLAHAJ!!")
        if action == "talk to blahaj":
            print("Blajah: Hey what's up, I'm just chilling the stream taking a bath B)")
        if action == "talk to blahaj about frankie":
            print("Blahaj: oh, frankie needs help crossing the stream? I am on it!")
            print("Blahaj carries frankie across stream and frankie thanks you all!")
            print("You suddently feel like you earned a point.")
            point += 1
            print("You now have", point, "points")
        if action in directions[1]:
            scene2()
        commonAsks(action)


def adaScene():
    global directions
    print("You see Ada sitting under a tree")
    sceneDone = "false"
    while sceneDone == "false":
        global point
        action = input("What do you want to do? ").lower()
        if action == "l":
            print("You see Ada sitting under a tree")
        if action == "x ada":
            print("Ada looks tired.")
        if action == "talk to ada":
            print(
                "Ada: Geez I skipped breakfast to code this hackathon project. I am so hungry!")
        if action == "give ada leflurry":
            print("Ada: OMG Thank you so much! I was STARVING!")
            print("You suddently feel like you earned a point.")
            point += 1
            print("You now have", point, "points")
        if action in directions[0]:
            scene2()
        commonAsks(action)


game()
