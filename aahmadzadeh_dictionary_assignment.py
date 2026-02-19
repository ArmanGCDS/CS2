#Author: Arman Ahmadzadeh
#Date: 2/20/2025
#Description: Create Data Dictionary from 2 Shakespeare plays and display using plotly. Check if each word exists in english dictionary 
#Bugs: User must have the 3 .txt files in the same folder (including the english dictionary)
#      Not all non-descriptive words are removed but code can easily be edited to include more
#      The plotly graphs may take a while to load, if only one tab appears refresh and the next should appear then refresh the tab again for the last one to appear
#Sources: Previous code
#https://www.geeksforgeeks.org/python/python-sort-python-dictionaries-by-key-or-value/
#https://www.w3schools.com/python/python_dictionaries.asp
#https://www.geeksforgeeks.org/python/python-plotly-tutorial/
#https://plotly.com/python/creating-and-updating-figures/#:~:text=With%20A%20Dictionary-,Converting%20Graph%20Objects%20To%20Dictionaries%20and%20JSON,to_json()%20method.
#English dictionary file https://github.com/dwyl/english-words/blob/master/words_alpha.txt 
#https://www.w3schools.com/python/python_sets.asp

import plotly.graph_objects as go

def read_txt(file1, file2): 
    '''
    Read the text files into two individual dictionaries and one dictionary with both. 
    Sorts all the dictionaries and removes unnecessary words
    Args:
        file1 (txt file): Script of Macbeth
        file2 (txt file): Script of Romeo and Juliet 
    Returns: 
        sorted_dict (dict): 
        sorted_macbeth (dict):
        sorted_romeo (dict):
    '''    

    word_dict = {}
    macbeth_dict = {}
    romeo_dict = {}

    try: #Try and except to handle potential errors in file opening
        with open(file1, 'r') as file:
            words = file.read()  #Read file into variable
            words = words.lower() #Make lowercase 
            for char in '.,;:"!?-()[]{}*': #Get rid of punctuation by looping and .replace 
                words = words.replace(char, '')

            words = words.split() #split into list 

            for word in words: #loop through list
                word_dict[word] = word_dict.get(word, 0) + 1 #assign word as key and count of the word already in dict as key for main dict
                macbeth_dict[word] = macbeth_dict.get(word, 0) + 1 #Same for macbeth 


    except FileNotFoundError:                        #If error display message 
        print(f"Error: '{file1}' file not found.") 
        
    try: 
        with open(file2, 'r') as file:
            words = file.read()
            words = words.lower()
            for char in '.,;:"!?-()[]{}*':
                words = words.replace(char, '')

            words = words.split()

            for word in words:
                word_dict[word] = word_dict.get(word, 0) + 1
                romeo_dict[word] = romeo_dict.get(word, 0) + 1        


    except FileNotFoundError:
        print(f"Error: '{file2}' file not found.")
      
    sorted_dict = dict(sorted(word_dict.items(), key=lambda item: item[1]))       #Sort dictionary keys by increasing values
    sorted_macbeth = dict(sorted(macbeth_dict.items(), key=lambda item: item[1])) #Got this method from source 
    sorted_romeo = dict(sorted(romeo_dict.items(), key=lambda item: item[1]))

    remove_word= ['the', 'or', 'i', 'and'] #List of words I want to remove

    for word in remove_word: #loop through the words
        sorted_romeo.pop(word, None) #If found in any of the dicts remove it, none to avoid error 
        sorted_dict.pop(word, None)
        sorted_macbeth.pop(word, None)
        
    return sorted_dict, sorted_macbeth, sorted_romeo #Return sorted dicts 

def write_and_graph1(dict_file, data):
    '''
    Writes the dict into a text file and graphs the text file using plotly 
    Args:
        dict_file (txt file): file that the dict will be written to 
        data (dict): Dictionary from macbeth & romeo and juliet
    Returns: 
        fig1 (plotly fig): graph 
    '''     

    with open(dict_file, 'w') as file: #Opens file for the data to write into it
        for key, value in data.items(): #For each key and value in the dict
            file.write(f"{key}:{value}\n") #Write to the file in good format

    keys = []
    values = []

    with open(dict_file, 'r') as file: #Opens the file that we just wrote to
        for line in file:              #For each line in the file
            key, value = line.split(':') #Split keys and values and then append into respective lists
            keys.append(key)
            values.append(value)

        fig1 = go.Figure(data=go.Scatter(x=keys, y=values, mode='lines+markers')) #Create fig 1 in plotly 
        fig1.update_layout(title='Data from Macbeth & Romeo and Juliet', xaxis_title='Keys', yaxis_title='Values') #Assign title and x y titles 
        return fig1 #Return, the next two functions are the same but 1 just for macbeth and 1 just for romeo 

def write_and_graph2(dict_file, macbeth_data):
    '''
    Writes the dict into a text file and graphs the text file using plotly 
    Args:
        dict_file (txt file): file that the dict will be written to 
        macbeth_data (dict): Dictionary from macbeth 
    Returns: 
        fig2 (plotly fig): graph 
    '''     

    with open(dict_file, 'w') as file:
        for key, value in macbeth_data.items():
            file.write(f"{key}:{value}\n")

    keys = []
    values = []

    with open(dict_file, 'r') as file:
        for line in file:
            key, value = line.split(':')
            keys.append(key)
            values.append(value)

        fig2 = go.Figure(data=[go.Scatter(x=keys, y=values, mode='lines+markers')])
        fig2.update_layout(title='Data from Macbeth', xaxis_title='Keys', yaxis_title='Values')
        return fig2

def write_and_graph3(dict_file, romeo_data):
    '''
    Writes the dict into a text file and graphs the text file using plotly 
    Args:
        dict_file (txt file): file that the dict will be written to 
        romeo_data (dict): Dictionary from romeo and juliet
    Returns: 
        fig3 (plotly fig): graph 
    '''     

    with open(dict_file, 'w') as file:
        for key, value in romeo_data.items():
            file.write(f"{key}:{value}\n")

    keys = []
    values = []

    with open(dict_file, 'r') as file:
        for line in file:
            key, value = line.split(':')
            keys.append(key)
            values.append(value)

        fig3 = go.Figure(data=[go.Scatter(x=keys, y=values, mode='lines+markers')])
        fig3.update_layout(title='Data from Romeo and Juliet', xaxis_title='Keys', yaxis_title='Values')
        return fig3
    
def show_all_figures(fig_list):
    '''
    Loops through the figures and displays them 
    Made to avoid error of multiple figures not being able to be displayed at once
    Args:
        fig_list (list): list of plotly figures 
    Returns: 
        none
    '''     
    for fig in fig_list:
        fig.show()

def Dictionary(data, word_file, valid_file):
    '''
    Checks if each word from the plays exists in modern english and writes the result to a text file
    Args:
        data (dict): data from the plays
        word_file (txt file): English words text file 
        valid_file (txt file): Wether words are valid will be written to this file 
    Returns: 
        none 
    '''     
    english_words = set() #For this many words, a set is much more efficient than a list to quickly locate a given word

    try: #Try and except to handle potential errors 
        with open(word_file, 'r') as file: #Open the english words file
            english_words = {line.strip().lower() for line in file} #Add the words from each line of the file into the set
 
    except FileNotFoundError:
        print(f"Error: 'words_alpha' file not found.")

    with open(valid_file, 'w') as f: #Open file to write
        for word in data:            #For each word in the Shaskphere dictionary 
            if word in english_words: #If it is in the set (exists in english)
                status = 'valid'
            else:
                status = 'invalid'
            
            f.write(f"{word}: {status}\n") #Write the formatted status of each word to the file
    return
        
def main():
    File1 = "Macbeth.txt"
    File2 = "Romeo and Juliet.txt"
    my_data = (read_txt(File1, File2)[0]) 
    macbeth_data = (read_txt(File1, File2)[1])
    romeo_data = (read_txt(File1, File2)[2])
    all_dict_file = "shakespeare_dictionary.txt"
    macbeth_file = "macbeth_dictionary.txt"
    romeo_file = "Romeo_and_Juliet_dictionary.txt"
    fig1 = write_and_graph1(all_dict_file, my_data)   
    fig2 = write_and_graph2(macbeth_file, macbeth_data)      
    fig3 = write_and_graph3(romeo_file, romeo_data)
    fig_list = [fig1, fig2, fig3]
    show_all_figures(fig_list)
    word_file = "words_alpha.txt"
    valid_file = "Shaskphere Language Existence in Modern English.txt"
    Dictionary(my_data, word_file, valid_file)
    
          
main()