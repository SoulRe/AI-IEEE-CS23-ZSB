import itertools as tools


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
            
            #limiting the flips to 24 as it will take a long time and could crash your pc (i tried :P!)
            if num_of_flips > 24:
                print("Please enter a number less than 24!")
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



def make_truth_table(num_of_flips, event, event_appearances):
    #solving using truth table was much easier, as i couldn't figure out a different way to get the count accurately
    """Function to create a truth table of soltions to check the count of specific 
       appearances the user entered

    Args:
        num_of_flips (int): size of truth table 2**num_of_flips
        event (str): event flag to check for and count 
        event_appearances (_type_): how many times the event appeared in the amount of flips

    Returns:
        count(int): number of times the appearance pattern happened in the truth table
    """
    count = 0
    
    #creating the truthtable using the product function from the itertools library
    try :
        table = list(tools.product(["head", "tail"], repeat= num_of_flips))
        # for k in table: print(k)
        
        #looping over the truth table and checking the freq of appearance pattern
        for i in range(len(table)):
            if table[i].count(event.lower()) == event_appearances:
                count += 1
    except KeyboardInterrupt:
        print("\nExited!")
        exit()
    
    return count
        
    
    
def main():
    #getting the number of flips from user
    num_of_flips = get_flips()
    #getting the event from the user (tail or head)
    event = get_event()
    #getting the appearances of event from user 
    event_appearances  = get_appearances(event, num_of_flips)
    #getting the event probability from the user
    event_probabilty = get_probabilty(event)   
    count = make_truth_table(num_of_flips, event, event_appearances)
    
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