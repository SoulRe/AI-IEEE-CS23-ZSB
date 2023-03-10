import math


def get_event():
    """function to get the event whether it's head or tail

    Returns:
        the event
    """
    event = str(input("Head or Tail?: "))
        
    while event.lower() not in ["head", "tail"]:
        print("Please enter a valid event!")
        event = str(input("Head or Tail?: "))
        
    return event.lower()
        
  
        
def get_flips():
    """function to get the number of flips done 

    Returns:
        number of flips as int
    """
    while True:
        try:
            num_of_flips = int(input("Enter the number of flips: "))
            
            if num_of_flips < 1:
                print("Please enter a number bigger than 0!")
                continue
            break
        
        except ValueError:
            print("Please enter a valid int")
            
    return num_of_flips



def get_appearances(event, num_of_flips):
    while True:
        try:
            event_appearance = int(input("Number of {} appearances: ".format(event)))
            
            if event_appearance > num_of_flips:
                print("event appearance cannot be greater than flips done!")
                continue
            break
        
        except ValueError:
            print("Please enter a valid int")
            
    return event_appearance



def get_probabilty(event):
    """function to get the a valid probability from the user

    Returns:
       event_probabilty (Float): the probabilty the user entereed
    """
    while True:
        try:
            event_probaility = float(input("Enter the probabilty of {} ( < 1): ".format(event)))
            
            if event_probaility < 0:
                print("Please enter a valid probabilty ( > 0)!")
                continue
            break
        
        except ValueError:
            print("Please enter a valid int")
            
    return event_probaility


    
    
def main():
    #getting the number of flips from user
    num_of_flips = get_flips()
    #getting the event from the user (tail or head)
    event = get_event()
    #getting the appearances of event from user 
    event_appearances  = get_appearances(event, num_of_flips)
    #getting the event probability from the user
    event_probabilty = get_probabilty(event)   
    
    #using comb library from math function to get freq of appearance pattern
    count = math.comb(num_of_flips, event_appearances)
    
    #probabilty answer: it's the probabilty of current event * how many times is appeared * the probability of the other event * how many times it appeared * the freq of the pattern in the truth table
    answer = ((event_probabilty ** event_appearances) * ((1 - event_probabilty) ** (num_of_flips - event_appearances))) * count
    
    #returning the answer rounded to 3 points 
    print("Output:\n%.03f " %answer)
 
 
 
# the forbidden try except 
#this bit is to exit the code without errors whenever the user wants
try:
    main()
    
except KeyboardInterrupt:
    print("\nExited!")
    exit()