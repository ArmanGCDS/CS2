#Author: Arman Ahmadzadeh
#Date: 09/30/2025
#Description: A set of methods that manipulate and interrogate an array of characters
#Bugs: Does not include all possible titles or distinctions
#Bonuses:    Calculates subtotals for each consonant
#            Returns full-name as a sorted array of characters 
#            Includes a function menu
#            Returns boolean if the name contains a title/distinction
#            Encrypts the string using a substitution cipher with a random keymap
#            Decrypts the string using a substitution cipher with the generated keymap
#Sources: Previous code
#Mr. Campbell's lessons
# How to bubble sort google search
# How ciphers work google search
# How does a substitution cipher work in python google search

import random
import string #For generating random keymap

def reverse_and_display(my_string):
    '''
    Reverses string using slicing
    Args:
        my_string (str): The string the user provided
    Returns:
        str: the reversed string

    '''
    reversed_string = my_string[::-1]               #Slicing the entire string backwards
    return reversed_string

def count_chars(my_string, my_char):
    '''
    Counts a given charcter in a given string
    Args:
        my_string (str): The string the user provided
        my_char (str): The character to be counted
    Returns:
        int: count of the char

    '''
    count = 0
    for this_char in my_string:                  
        if this_char.lower() == my_char:           #If a charcter in the string lower or uppercase = a specifci character
            count += 1                             #Add 1 to the count
    return count

def count_char_locations(my_string, my_char):
    '''
    Finds the locations of a given character without .split
    Args:
        my_string (str): The string the user provided
        my_char (str): The character to be located
    Returns:
        list: the locations of the char

    '''
    count = 0
    locations = []
    for this_char in my_string:
        if this_char.lower() == my_char:        #if a character in lower or uppercase in the string  = a specific character
            locations.append(count)             #Add the count to a list
        count += 1                              #Add 1 to the count
    return locations

def determine_vowels(my_string):
    '''
    Takes a string and returns a dict with the amount of vowels in it
    Args:
        string (str): The string the user provided.
    Returns:
        dict: All the vowels and their counts
    '''
    vowels = 'aeiou'
    counts = dict()
    for vowel in vowels:                                           #For each vowel
        counts[f'vowel {vowel}'] = count_chars(my_string, vowel)   #In a dictrionary, have the vowel equal to the amount of times it is in the string
    counts['total count of vowels'] = sum(counts.values())         #In a dictionary have the total vowels equal to the sum of all values in the dict
    return counts

def consonant_frequency(my_string):
    '''
    Returns a dict with the number of each consonant in a string  
    Args:
        my_string (str): The string the user provided
        my_char (str): The character to be counted
    Returns:
        dict: the consonants and their counts        

    '''
    consonants = 'bcdfghjklmnpqrstvwxyz'
    counts = dict()                                                          #For each consonant
    for consonant in consonants:                                             #In a dictrionary, have the consonant equal to the amount of times it is in the string
        counts[f'consonant {consonant}'] = count_chars(my_string, consonant)
    counts['total count of consonants'] = sum(counts.values())               #In a dictionary have the total consonants equal to the sum of all values in the dict
    return counts

def remove_title(my_string, titles, distinctions):
    '''
    Determines if the string has a title or distinction and returns it without using space locations
    Args:
        my_string (str): The string the user provided
        titles (list): List of titles
        distinctions (list): List of distinctions
    Returns:
        str: The string without a title or distinction

    '''

    if any(title in my_string for title in titles) and any(distinction in my_string for distinction in distinctions):#If string has a title and distinction
        space_locs = count_char_locations(my_string, ' ')                                                            #Locates spaces
        return my_string[space_locs[0]+1:space_locs[-1]]                                                             #Return the string from the first to last space without the title and distinction
    elif any(title in my_string for title in titles):                                                                #If the string only has a title
        space_locs = count_char_locations(my_string, ' ')                                                            #Locates spaces
        return my_string[space_locs[0]+1:]                                                                           #Return string after the first space without a title
    elif any(distinction in my_string for distinction in distinctions):                                              #If the string only has a distinction
        space_locs = count_char_locations(my_string, ' ')                                                            #Locates spaces
        return my_string[:space_locs[-1]]                                                                            #Return string up to the last space without distinction
    else:
        return my_string                                                                                             #If there is no title or distinction return

def return_first_middle_last_name(my_string):
    '''
    Locates the spaces in a string and then determines the first, middle, and last names which are put into a dict
    Args:
        my_string (str): The string the user provided
    Returns:
        dict: The names and if they are first, middle or last
    '''

    titles = ['Mr.', 'Ms.', 'Mrs.', 'Dr.', 'Sir.', 'Prof.','Gen.','Capt.','Col.','Lt.','Mr. President','Gov.','Sen.','Rep.','Duke','Dutches','Lord','Lady','His Majesty','Sir']   #List of titles
    distinctions = ['Esq.','Phd.','B.A.','M.D', 'B.Sc.','B.F.A.','B.Eng.','M.A.','Ms.c.','M.B.A.','M.F.A','M.Eng.','M.Phill','D.O.','Ed.D', 'Jr.', 'Sr.', 'II', 'III']            #List of distinctions
    if any(title in my_string for title in titles) or any(distinction in my_string for distinction in distinctions): #If there is a title or a distinction in the string
        my_string = remove_title(my_string, titles=titles, distinctions=distinctions)                                           #Call remove title function
    l = len(my_string)                                                                #Variable for string lengh                
    name_split = dict()
    space_locs = count_char_locations(my_string, ' ')                                 #Counts the amount of spaces in the string

    if l > 0 and len(space_locs) == 0:                                                #If the string's lengh is more than 0 and there are no spaces
        name_split['first name'] = my_string                                          #In the dict first name is = to string
        name_split['middle names'] = ''                                               #In the dict there is no middle name
        name_split['last name'] = ''                                                  #In the dict there is no last name

    elif l > 0 and len(space_locs) == 1:                                              #If the string's lengh is more than 0 and there is 1 space
        name_split['first name'] = my_string[0:space_locs[0]]                         #In the dict first name = first word of string
        name_split['middle names'] = ''                                               #In the dict there is no middle name
        name_split['last name'] = my_string[space_locs[0]+1:]                         #In the dict last name =  last word of string

    elif l > 0 and len(space_locs) >= 2:                                              #If the string's lengh is more than 0 and there are 2 spaces or more
        name_split['first name'] = my_string[0:space_locs[0]]                         #In the dict first name = first word of string
        name_split['middle names'] = my_string[space_locs[0]+1:space_locs[-1]]        #In the dict middle names = names in between first and last space
        name_split['last name'] = my_string[space_locs[-1]+1:]                        #In the dict last name = last word of the string

    else:                                                                             #If anything else
        name_split['first name'] = ''                                                 #In the dict there is no name
        name_split['middle names'] = ''                                               #In the dict there is no name
        name_split['last name'] = ''                                                  #In the dict there is no name
    return name_split

def last_name_hyphen(my_string):    
    '''
    Determines if there is a hyphen in the last name
    Args:
        my_string (str): The string the user provided
    Returns:
        bool: If there is a hyphen
    '''
    if "-" in return_first_middle_last_name(my_string)['last name']:     #If there is a hypen in the last name value of the dict
        return True
    else:
        return False

def to_lowercase(my_string):
    '''
    Convert a string to lowercase without .lower
    Args:
        my_string (str): The string the user provided
    Returns:
        str: converted string
    '''
    name_out = ""                                                       #Variable created
    for letter in my_string:                                            #For each letter in the string
          if ord(letter)>=65 and ord(letter)<= 90:                      #If the letter is uppercase
            num = ord(letter)                                           #number equals the numerical representation of the letter
            num = num + 32                                              #Add 32 to make lowwercase
            letter = chr(num)                                           #Turns numerical representation into character
            name_out = name_out + letter                                #Variable = itself + the converted letter
          else:                                                         #If not uppercase
            name_out = name_out + letter                                #Return letter
    return name_out

def to_uppercase(my_string):
    '''
    Convert a string to uppercase without .upper
    Args:
        my_string (str): The string the user provided
    Returns:
        str: converted string
    '''
    name_out = ""                                            #Variable created
    for letter in my_string:                                 #For each letter in the string
          if ord(letter)>=97 and ord(letter)<= 122:          #If the letter is lowercase
            num = ord(letter)                                #number equals the numerical representation of the letter
            num = num - 32                                   #Subtract 32 to make lowercase
            letter = chr(num)                                #Turns numerical representation into character
            name_out = name_out + letter                     #Variable = itself + the converted letter
          else:                                              #If not lowercase
            name_out = name_out + letter                     #Return letter
    return name_out                                          

def shuffle_name(my_string):
    '''
    Shuffles a string without .shuffle
    Args:
        integer (int): The user provided string
    Returns:
        str: The shuffled string
    '''
    my_list = list(my_string)                     #Converts the string into a list
    my_list2 = my_list[:]                         #Creates copy of the list
    new_list = []                                 #New list
    for i in my_list2:                            #For each item in the copy list
        random_letter = random.choice(my_list)    #Random choice from original list
        new_list.append(random_letter)            #Add choice to the new list
        my_list.remove(random_letter)             #Remove choice from original list
    random_name = ''.join(new_list)               #Joins the list back into a string  
    return random_name

def is_palindrome(my_string):        #specify first name
    '''
    Takes a string and checks whether the first word is a palindrome
    Args:
        string (str): The string the user provided
    Returns:
        bool: If the string is a palindrome or not
    '''
    first_name = return_first_middle_last_name(my_string)['first name'] #Call function to create dict of the names, get first name value
    first_name_lower = to_lowercase(first_name)                         #Convert first name to lowercase
    if first_name_lower[::-1] == first_name_lower:                      #If the lowercase first name reversed = lowercase first name
        return True
    else:
        return False

def sorted_array(my_string):
    '''
    Takes a string and bubble sorts it without .sort and .join
    Args:
        string (str): The string the user provided
    Returns:
        list: sorted array
    '''
    my_list = list(my_string)                                          #converts string into a list                
    n = len(my_list)                                                   #Number = the lengh of the list
    for i in range(n - 1):                                             #For each element in the lengh of the list - 1 (outer loop passes)
        for j in range(0, n - i - 1):                                  #Inner loop for swaps and comparisons
            if my_list[j] > my_list[j + 1]:                            #If an element in the list is greater than the next one
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]#Swap the elements 
    return my_list

def get_initials(my_string):
    '''
    Takes a name and returns the initials
    Args:
        string1 (str): The first name the user provided, it's initial will be returned
        string2 (str): The last name the user provided, it's initial will be returned
    Returns:
        str: The initials of the first and last name

    '''
    first_last_names = return_first_middle_last_name(my_string)                      #Call function to create dict of the names
    try:                                                                            #Try for error
        return first_last_names['first name'][0] + first_last_names['last name'][0] #return the frist name value and the last name value
    except IndexError:                                                              #If there is an index error, last name dose not exist
        return first_last_names['first name'][0]                                    #return the first name value only

def contains_title(my_string):
    '''
    Takes a string and checks if it contains a title
    Args:
        string (str): The string the user provided
    Returns:
        bool: If the string has a title
    '''
    titles = ['Mr.', 'Ms.', 'Mrs.', 'Dr.', 'Sir.','Esq.','Phd.','Prof.','B.A.','M.D','Gen.', 'Capt.','Col.','Lt.', 'Mr. President', 'Gov.','Sen.','Rep', 'Duke', 'Dutches', 'Lord', 'Lady', 'His Majesty','Sir','B.Sc.','B.F.A.','B.Eng.','M.A.','Ms.c.','M.B.A.','M.F.A','M.Eng.','M.Phill','D.O.','Ed.D', 'Jr.', 'Sr.', 'II', 'III']  #List of titles and distinctions
    if any(title in my_string for title in titles):                #If there is any title in the string
        return True                                                
    else:
        return False    

def encryption(original_string, keymap):
    '''
    Encrypts a string using a substituion cipher
    Args:
        original_string (str): The string the user provided
        keymap (dict): The keymap for the cipher
    Returns:
        str: The encrypted string
    '''
    return ''.join([keymap[s] for s in original_string]) #Joins each character in the original string with its corresponding value in the keymap

def decryption(coded_string, keymap):
    '''
    Decrypts a string using a substitution cipher
    Args:
        coded_string (str): The string the user provided
        keymap (dict): The keymap for the cipher  
    Returns:
        str: The decrypted string
    '''
    reverse_keymap = dict(zip(keymap.values(), keymap.keys())) #Creates a reverse keymap by swapping keys and values from the original dict, .zip first turns the data into a tuple
    return ''.join([reverse_keymap[s] for s in coded_string]) #Join each character in the ciphered string with its corresponding value in the reverse keymap dict

def random_keymap():
    '''
    Generates a random keymap for the cipher
    Args:
        None
    Returns:
        dict: The random keymap
    '''
    letters = list(string.printable) #Makes a list of all printable characters
    shuffled_letters = letters.copy() #Creates a copy of the list
    random.shuffle(shuffled_letters) #Shuffles the copy (My shuffle function will not work for this)
    return dict(zip(letters, shuffled_letters)) #Uses .zip to create a tuple that is turned into a dict with the original list as keys and the shuffled list as values 

def main():

    string = input(" Enter your name or a word: ")
    print("")

    while True:        
        function_list = ['1: Reverse and display',                                              #List of function names
                     '2: Determine the number of vowels',    
                     '3: Consonant frequency',
                     '4: Return first name',
                     '5: Return last name',
                     '6: Return middle name(s)',
                     '7: Return boolean if last name contains a hyphen',
                     '8: Convert to lowercase',
                     '9: Convert to uppercase',
                     '10: Modify array to create a random name',
                     '11: Return boolean if first name is a palindrome',
                     '12: Return full-name as a sorted array of characters',
                     '13: Make initials from name',
                     '14: Return boolean if name contains a title/distinction',
                     '15: encypt string',
                     '16: decrypt string \n',]
        for i in function_list:                                                               #For loop that prints the function names in the list
            print(i)
     
        function_menu = input('-Enter a function from the menu above-   \n')                  #Asks the user for a function name from the list  

        if function_menu == '1':                                     #If the user input matches a function name, the function is called with the user provided string as an argument
            reversed_string = reverse_and_display(string)
            print(f"Reversed string is {reversed_string}")

        elif function_menu == '2':
            vowel_count = determine_vowels(string)
            for key, value in vowel_count.items():                  #Loop through dict    
                print(f"{key}: {value}")                            #Display key value pair

        elif function_menu == "3":
             consonant_count = consonant_frequency(string)
             for key, value in consonant_count.items():            #Loop through dict
                 print(f"{key}: {value}")                          #Display key value pair

        elif function_menu == '4':
            print(f"First name is {return_first_middle_last_name(string)['first name']}") #Print value for first name key

        elif function_menu == '5':
            print(f"Last name is {return_first_middle_last_name(string)['last name']}") #Print value for last name key

        elif function_menu == '6':
            print(f"Middle name(s) is/are {return_first_middle_last_name(string)['middle names']}")  #Print value for middle names key

        elif function_menu == '7':
            if last_name_hyphen(string) == True:                            #If function returns true bool
                print(f"True, {return_first_middle_last_name(string)['last name']} contains a hyphen")
            else:
                print(f"False, {return_first_middle_last_name(string)['last name']} does not contain a hyphen")
                 
        elif function_menu == '8':
            print(f'Lower case of {string} is: {to_lowercase(string)}')

        elif function_menu == '9':
            print(f'Upper case of {string} is: {to_uppercase(string)}')

        elif function_menu == '10':
            print(f'Randomly shuffled name of {string} is: {shuffle_name(string)}')

        elif function_menu == '11':
            bool = is_palindrome(string)
            if bool == True:                                #If the function returns the bool true
                print(f"{bool}, the first name of {string} is a palindrome" )
            else:                                           #If not
                print(f"{bool}, the first name of {string} is not a palindrome" )

        elif function_menu == '12':
            print(f'Sorted array of {string} is: {sorted_array(string)}')

        elif function_menu == '13':
            print(f'Initials of {string} are: {get_initials(string)}')

        elif function_menu == '14':
            if contains_title(string) == True:            #If function returns bool true
                print(f"True, {string} contains a title/distinction")
            else:
                print(f"False, {string} does not contain a title/distinction")

        elif function_menu == '15':
             random_map = random_keymap()                      #Uses function to create a random keymap for the cipher
             encrypted_string = encryption(string, random_map) #Encrypts the string using it and the generated key map
             print(f'Encrypted string of {string} is: {encrypted_string} with keymap: {random_map}')

        elif function_menu == '16':
             decrypted_string = decryption(encrypted_string, random_map)  #Decrypts the encrypted string using the encrypted string and the same key map
             print(f'Decrypted string of {encrypted_string} is: {decrypted_string}')
           
        else:
            print("Invalid input, please try again.")                                    
       
        print("")

main()

















