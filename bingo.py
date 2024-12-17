import random
import time

consumed = [0]

while True:
    call = random.randint(1,90)
    
    
    if call in consumed:
        pass
    else:
        print(" ")
        print(call)
    
        match call:
            case 1: print("Chart topper")
            case 2: print("One little duck / buckle my shoe")
            case 3: print("Cup of tea")
            case 4: print("Knock at the door")
            case 5: print("Man alive")
            case 6: print("Half a dozen")
            case 7: print("Lucky / Monkey gone to heaven")
            case 8: print("Garden gate")
            case 9: print("Revolution 9")
            case 10: print("Kier's den")
            case 11: print("Legs / Ocean's")
            case 12: print("One dozen")
            case 13: print("Unlucky for some")
            case 14: print("Valentine's day")
            
            case 16: print("Sweet sixteen")
            case 17: print("Dancing queen")
            case 18: print("Coming of age")
            case 19: print("Quarantine")
            case 20: print("One score")
            case 21: print("Forever")
            case 22: print("Ducks on the pond")
            case 23: print("Michael Jordan")
            case 24: print("Two dozen")
            case 25: print("Duck dive")
            case 26: print("Pick and mix")
            case 27: print("Stairway to heaven")
            
            
            
            case 31: print("Get up and run")
            case 32: print("Deja vu")
            case 33: print("Dirty knee")
            case 34: print("Who could ask for more")
            case 35: print("Jump and jive")
            case 36: print("Three dozen")
            
            case 38: print("Your girlfriend's late")
            
            case 40: print("Life begins at 40")
            case 41: print("Time for fun")
            case 42: print("Bus to the airport")
            case 43: print("Bus to Stockport")
            case 44: print("Mobile numbers")
            case 45: print("Halfway there")
            case 46: print("Up to tricks")
            case 47: print("The 47 Ronin")
            case 48: print("Four dozen")
            
            case 50: print("Bullseye")
            
            case 52: print("Weeks in a year / deck of cards")
            case 53: print("Stuck in a tree")
            case 54: print("Wipe the floor")
            case 55: print("All the fives")
            
            case 57: print("Heinz varieties")
            
            
            case 60: print("Five dozen")
            case 61: print("Baker's bun")
            case 62: print("Tickety-boo")
            case 63: print("You and me")
            case 64: print("Nintendo")
            case 65: print("Off work")
            
            case 67: print("Summer of love")
            case 68: print("In a state")
            case 69: print("Summer of 69")
            
            case 71: print("Bang a drum")
            case 72: print("Six dozen")
            case 73: print("Sail the seven seas")
            
            
            
            case 77: print("Lightning strikes twice")
            case 78: print("Give it to me straight")
            case 79: print("One more time")
            case 80: print("Ate nothing")
            
            case 82: print("Straight on through")
            case 83: print("Time for tea")
            case 84: print("Give me more")
            case 85: print("Staying alive")
            
            
            case 88: print("Two snowmen")
            case 89: print("Nearly there")
            case 90: print("Top of the shop")
        
        consumed.append(call)
    
        input("Press a key to continue...")  
        