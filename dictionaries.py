def test1():
    PhoneBook = {"John":"123-456-789", "Susan":"987-654-321"}   
    
    print(f"There are {len(PhoneBook)} entries in the dictionary.")
    print(f"The phone number of John is {PhoneBook['John']}") #if we use "John" then python is confused with the f string - ends at {PhoneBook["
    #let's change things up for a little
    PhoneBook["Susan"] = PhoneBook["John"]
    PhoneBook["John"] = "111-222-333"
    PhoneBook["Mary"] = "555-666-777"
    
    for key in PhoneBook:
        print(f"{key}'s number is {PhoneBook[key]}.")
    
    
def test2(text):
    """Calculates the number of all 
    characters in the given text
    """
    LetterCounter = {}
    FORBIDDEN_CHARACTERS = {" ", "!"} 
    # [" ", "!"], if = [], everything is counted. Why finally choose {} - set()? 
    #Set usage is more natural than list - all elements appear only once.
    #Set works faster than a list - looking for something is way faster. 
    #Better implementation, nothing can be repeated, unlike in a list
    for character in text:
       if character not in FORBIDDEN_CHARACTERS:
            if character in LetterCounter:  
                LetterCounter[character] += 1
            else: #having encountered a character for the first time
                LetterCounter[character] = 1     
    #display counters
    for character in LetterCounter:
        print(f"{character}'s number of occurences is {LetterCounter[character]}.")
         
           
def main():
    print("Start dictionaries")
    test1()
    test2("Happy New Year!")
    print("Finished!")   
    
main()