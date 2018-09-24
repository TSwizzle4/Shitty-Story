

print("~~~~~~~~~~~~~~~~~~~")
print("Welcome to the Game")
print("~~~~~~~~~~~~~~~~~~~")

print("Hello traveler, Where would you like to go?")
ch1 = str(input("Do you go left or right? [l/r]: "))


if ch1 in ['l', 'L', 'left', 'Left', 'LEFT']:
    print("Ah left you said, I dont know if I would've gone with that one, but to each its own. To the left you see a man slumped up at a tree and nursing what looks like a gunshot wound.")
    ch2 = str(input("Do you help him? [y/n]: "))
    if ch2 in ['y', 'Y', 'Yes', 'YES', 'yes']:
        print("You walk over to the man and ask if he is ok, he smirks, and starts to laugh")
        ch3 = str(input("Do you stay help him? [y/n]: "))
        if ch3 in ['y', 'Y', 'Yes', 'YES', 'yes']:
            print("When you ask him what's wrong he pull a gun on you and shoots you right through the chest. I told you the left was a dangerous path: ")
        else:
            print("Good choice, run away, don't help the dying man. That's very nice of you. Then again I didn't help him when I saw him. Just restart and go to the right like you should've from the start.")
    else:
        print("Oh so you don't want to help him? That's alright, I wouldn't of either. Just restart and go to the right.")

else:
    print('Ah right you said, good choice, head down that way and see what your choice will lead you too.To the right you see a chest and a crown.')
    ch4 = str(input("Which do you chose: crown or chest? [Crown/Chest]"))
    if ch4 in ['chest', 'Chest', 'CHEST']:
        print("Inside the chest there is nothing and the crown disappears, sucks to be you. Better luck next time: ")
    else:
        print("You put on the crown and nothing changes. You do have a nice Party City crown though. Better luck next time.")
