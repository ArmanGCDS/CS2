#Author: Arman Ahmadzadeh
#Date: 12/22/2025
#Description: Titanic Dataset Analysis all goals and bonuses completed without importing CSV or pandas 
#Bugs: User must have the titanic.csv file in the same folder
#Sources: Previous code
#https://www.w3schools.com/python/python_file_handling.asp
#https://www.w3schools.com/python/python_dictionaries.asp
#https://www.w3schools.com/python/ref_func_max.asp
#https://www.w3schools.com/python/ref_func_min.asp
#https://www.geeksforgeeks.org/python/how-to-create-list-of-dictionary-in-python/
#https://www.w3schools.com/python/matplotlib_histograms.asp
#https://www.w3schools.com/python/matplotlib_bars.asp
#https://www.w3schools.com/python/ref_dictionary_items.asp
#https://www.w3schools.com/python/ref_string_strip.asp
#https://www.w3schools.com/python/ref_func_zip.asp


import matplotlib.pyplot as plt

def goal_1(data):
    '''
    Load the titanic.csv file and display the first 10 rows.
    Print the column names and the total number of passengers.
    Args:
        data (list): list of dictionaries to access data by column names
    Returns: 
        rows_list (list): first 10 rows 
        column_list (list): column names
        passenger_count (int): total number of passengers
    '''    
    rows_list = data[:10] #slicing 

    column_list = [key for key in data[0]] 

    passenger_count = len(data) 

    return rows_list, column_list, passenger_count  


def goal_2(data):
    '''
    Calculate and print the overall survival rate (percentage of passengers who survived).
    Args:
        data (list): list of dictionaries to access data by column names
    Returns:
        survival_rate (float): overall survival rate
    '''    
    data_length = len(data) 
    survived_count = sum(1 for passenger in data if passenger['Survived'] == '1') #sum of survivors 
    survival_rate = (survived_count / data_length) * 100 #mean 

    return survival_rate


def goal_3(data):
    '''
    Calculate the survival rate for males and females separately.
    Display which gender had a higher survival rate.
    Args:
        data (list): list of dictionaries to access data by column names
    Returns:
        male_survival_rate (float): survival rate for males
        female_survival_rate (float): survival rate for females
        higher_survival_gender (str): higher survival rate gender
    '''    
    male_data = [passenger for passenger in data if passenger['Sex'] == 'male']
    female_data = [passenger for passenger in data if passenger['Sex'] == 'female']
    male_survived_count = sum(1 for passenger in male_data if passenger['Survived'] == '1')
    female_survived_count = sum(1 for passenger in female_data if passenger['Survived'] == '1')
    male_survival_rate = (male_survived_count / len(male_data)) * 100 #mean (count/total)
    female_survival_rate = (female_survived_count / len(female_data)) * 100
    higher_survival_gender = "male" if male_survival_rate > female_survival_rate else "female"
   
    return male_survival_rate, female_survival_rate, higher_survival_gender


def goal_4(data):
    '''
    Find and print:
    - The average age of all passengers
    - The average age of survivors vs non-survivors
    - The youngest and oldest passengers  
    Args:
        data (list): list of dictionaries to access data by column names
    Returns:
        average_age (float): average age of all 
        average_survivor_age (float): average survival age 
        average_non_survivor_age (float): average age of non-survivors
        min_age (float): youngest passenger age
        max_age (float): oldest passenger age
    '''    
    age_list_old = [d["Age"] for d in data]              
    age_list = [i for i in age_list_old if i != ''] #Removes empty strings from the list
    age_data = [] 
    for i in age_list: 
        i = float(i)
        age_data.append(i) #appends floats into new list
    age_sum = sum(age_data)
    elements = len(age_data)
    average_age = age_sum / elements #mean (sum/total)

    sum_non_survivor = 0
    count = 0
    for d in data:
        if d['Survived'] == "0" and d['Age'] != '': #If not survived and not empty
            sum_non_survivor += float(d["Age"]) #Adding age to sum
            count += 1 #count increases by 1
    average_non_survivor_age = sum_non_survivor / count #mean (sum/total)

    sum_survivor = 0
    count = 0
    for d in data:
        if d['Survived'] == "1" and d['Age'] != '': #If survived and not empty
            sum_survivor += float(d["Age"])
            count += 1
    average_survivor_age = sum_survivor / count  

    max_age = max(age_data) #highest value in list
    min_age = min(age_data) #lowest
   
    return average_age, average_survivor_age, average_non_survivor_age, min_age, max_age


def goal_5(data):
    '''
    For each passenger class (1st, 2nd, 3rd):
    - Calculate the survival rate
    - Calculate the average fare paid
    Create a summary showing which class had the best survival chances.  
    Args:
        data (list): list of dictionaries to access data by column names
    Returns:
        survival_rate1 (float): survival rate for 1st class
        Average_Fare_1 (float): average fare for 1st class
        survival_rate2 (float): survival rate for 2nd class
        Average_Fare_2 (float): average fare for 2nd class
        survival_rate3 (float): survival rate for 3rd class
        Average_Fare_3 (float): average fare for 3rd class
    '''    
    
    #For 1st class
    sum_1st = 0
    count_1st = 0
    survived_count1 = 0
    class1_data = [passenger for passenger in data if passenger['Pclass'] == '1'] #gets first class data filtered
    for d in data: 
        if d['Pclass'] == "1":    
            sum_1st += float(d["Fare"]) #Adding fare to sum
            count_1st += 1 #count increases by 1
        if d['Pclass'] == "1" and d["Survived"] == '1': #If survived in 1st class
            survived_count1 += 1 #count increases by 1

    survival_rate1 = (survived_count1 / len(class1_data)) * 100 #mean (count/total)
    Average_Fare_1 = sum_1st/ count_1st #mean (sum/total)
   
    #same for 2nd
    sum_2nd = 0
    count_2nd = 0
    survived_count2 = 0
    class2_data = [passenger for passenger in data if passenger['Pclass'] == '2']
    for d in data:
        if d['Pclass'] == "2":
            sum_2nd += float(d["Fare"])
            count_2nd += 1
        if d['Pclass'] == "2" and d["Survived"] == '1':
            survived_count2 += 1

    survival_rate2 = (survived_count2 / len(class2_data)) * 100
    Average_Fare_2 = sum_2nd/ count_2nd
   
    #same for 3rd
    sum_3rd = 0
    count_3rd = 0
    survived_count3 = 0
    class3_data = [passenger for passenger in data if passenger['Pclass'] == '3']
    for d in data:
        if d['Pclass'] == "3":
            sum_3rd += float(d["Fare"])
            count_3rd += 1
        if d['Pclass'] == "3" and d["Survived"] == '1':
            survived_count3 += 1
   
    survival_rate3 = (survived_count3 / len(class3_data)) * 100
    Average_Fare_3 = sum_3rd/ count_3rd
   
    return survival_rate1, Average_Fare_1, survival_rate2, Average_Fare_2, survival_rate3, Average_Fare_3


def goal_6(data):
    '''
    Create a new column called 'FamilySize' (SibSp + Parch + 1).
    Analyze survival rates based on family size.
    Determine if traveling alone or with family improved survival chances.  
    Args:
        data (list): list of dictionaries to access data by column names
    Returns:
        alone_survival_rate (float): survival rate for passengers traveling alone
        family_survival_rate (float): survival rate for passengers traveling with family
        higher_survival_group (str): group with higher survival rate
    '''    
    for d in data:
        d['FamilySize'] = int(d['SibSp']) + int(d['Parch']) + 1 #New column created
   
    alone_data = [passenger for passenger in data if passenger['FamilySize'] == 1] #alone filtered
    family_data = [passenger for passenger in data if passenger['FamilySize'] > 1] #family filtered (more than 1 family size)
    
    alone_survived_count = sum(1 for passenger in alone_data if passenger['Survived'] == '1')
    family_survived_count = sum(1 for passenger in family_data if passenger['Survived'] == '1')
    
    alone_survival_rate = (alone_survived_count / len(alone_data)) * 100 
    family_survival_rate = (family_survived_count / len(family_data)) * 100
    
    higher_survival_group = "alone" if alone_survival_rate > family_survival_rate else "with family"
   
    return alone_survival_rate, family_survival_rate, higher_survival_group


def goal_7(data):
    '''
    Create at least 3 different charts:
    1. Bar chart comparing survival rates by gender
    2. Histogram showing age distribution
    3. Bar chart showing survival rates by passenger class
    (You'll need matplotlib: pip install matplotlib)    
    Args:
        data (list): list of dictionaries to access data by column names
    Returns:
        none 
    '''    
    # 1: Bar chart comparing survival rates by gender
    male_survival_rate, female_survival_rate, _ = goal_3(data)
    plt.figure(figsize=(8, 6)) #8 by 6 inches chart size
    plt.bar(['Male', 'Female'], [male_survival_rate, female_survival_rate], color=['blue', 'pink']) #bar chart
    plt.title('Survival Rate by Gender') #title
    plt.ylabel('Survival Rate (%)') #y axis label
    plt.show()

    # 2: Histogram showing age distribution
    ages = [float(d['Age']) for d in data if d['Age'] != ''] #filter ages without empty strings
    plt.figure(figsize=(8, 6)) #8 by 6 inches chart size
    plt.hist(ages, bins=20, color='green', edgecolor='black') #histogram with 20 bins (number of bars)
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()

    # 3: Bar chart showing survival rates by passenger class
    survival_rate1, _, survival_rate2, _, survival_rate3, _ = goal_5(data)
    classes = ['1st Class', '2nd Class', '3rd Class'] #Class names
    plt.figure(figsize=(8, 6)) #8 by 6 inches chart size
    plt.bar(classes, [survival_rate1, survival_rate2, survival_rate3], color=['gold', 'silver', 'brown']) 
    plt.title('Survival Rate by Passenger Class')
    plt.ylabel('Survival Rate (%)')
    plt.show()
   
    return #nothing needs to be returned, the charts are displayed already 


def goal_8(data):
    '''
    Write a function that generates a complete survival analysis report including:
    - Overall statistics (total passengers, survivors, survival rate)
    - Breakdown by gender, class, and age group (child <18, adult 18-60, senior >60)
    - Identify the profile of passengers most likely to survive (combination of features)
    - Handle missing data appropriately
    - Save the report to a text file    
    Args:
        data (list): list of dictionaries to access data by column names
    Returns:
        None
    '''    

    #data from other functions 
    rows_list, column_list, passenger_count  = goal_1(data)
    survival_rate = goal_2(data)
    male_survival_rate, female_survival_rate, higher_survival_gender = goal_3(data)
    average_age, average_non_survivor_age, average_survivor_age, max_age, min_age = goal_4(data)
    survival_rate1, Average_Fare_1, survival_rate2, Average_Fare_2, survival_rate3, Average_Fare_3 = goal_5(data)
    alone_survival_rate, family_survival_rate, higher_survival_group = goal_6(data) 

    # Age group data
    child_data = [d for d in data if d['Age'] != '' and float(d['Age']) < 18] #filters child without empty strings
    adult_data = [d for d in data if d['Age'] != '' and 18 <= float(d['Age']) <= 60] #filters adult without empty strings
    senior_data = [d for d in data if d['Age'] != '' and float(d['Age']) > 60] #filters senior without empty strings

    child_survived = sum(1 for d in child_data if d['Survived'] == '1')
    adult_survived = sum(1 for d in adult_data if d['Survived'] == '1')
    senior_survived = sum(1 for d in senior_data if d['Survived'] == '1')

    child_survival_rate = (child_survived / len(child_data)) * 100 
    adult_survival_rate = (adult_survived / len(adult_data)) * 100 
    senior_survival_rate = (senior_survived / len(senior_data)) * 100 

    report = f"""
    Titanic Survival Analysis Report
    ---------------------------------
    Overall Statistics:
    Total Passengers: {passenger_count}
    Overall Survival Rate: {survival_rate:.2f}%

    Breakdown by Gender:
    Male Survival Rate: {male_survival_rate:.2f}%
    Female Survival Rate: {female_survival_rate:.2f}%
    Higher Survival Gender: {higher_survival_gender}

    Breakdown by Class:
    1st Class Survival Rate: {survival_rate1:.2f}% (Avg Fare: ${Average_Fare_1:.2f})
    2nd Class Survival Rate: {survival_rate2:.2f}% (Avg Fare: ${Average_Fare_2:.2f})
    3rd Class Survival Rate: {survival_rate3:.2f}% (Avg Fare: ${Average_Fare_3:.2f})

    Ages Analysis:
    Average Age: {average_age:.2f}
    Average Age of Non-Survivors: {average_non_survivor_age:.2f}
    Average Age of Survivors: {average_survivor_age:.2f}
    Youngest Passenger: {min_age}, Oldest Passenger: {max_age}

    Survival by Age Group:
    Child (<18): {child_survival_rate:.2f}%
    Adult (18-60): {adult_survival_rate:.2f}%
    Senior (>60): {senior_survival_rate:.2f}%

    Family Analysis:
    Alone Survival Rate: {alone_survival_rate:.2f}%
    With Family Survival Rate: {family_survival_rate:.2f}%
    Higher Survival Group: {higher_survival_group}

    Profile of Passengers Most Likely to Survive:
    Based on all of the survival rates: female passengers in 1st class under 18 years old were the most likey to survive.
    """

    #Write reprot to file
    with open('survival_report.txt', 'w') as f:
        f.write(report)
    
    return 

def goal_9(data):
    '''
    Find the most common first names among survivors  
    Args:
        data (list): list of dictionaries to access data by column names
    Returns:
        common_names (dict): dictionary of common first names among survivors (apear more than once)

    '''    

    survived_names_list = []
    counts = {}
    
    for passenger in data:
        if passenger['Name'] and (passenger['Survived'] == '1'): #If name is not empty and survived
            names = passenger['Name'].split(" ") #Split the name into words
            survived_names_list.append(names[2]) #Third word in the name is first name so 3rd appended into list

    for name in survived_names_list: #for every name in the list
        if name in counts: #If the name is in the dictionary already
            counts[name] += 1 #Add 1 to its value
        else: #If name not counted yet
            counts[name] = 1  #Add name to dictionary with value 1

    common_names = {name: count for name, count in counts.items() if count > 1}
    #common_names dict only has names that have value above 1 

            
    return common_names

def goal_10(data):
    '''
    Analyze survival rates by port of embarkation  
    Args:
        data (list): list of dictionaries to access data by column names
    Returns:
        s_survival_rate (float): survival rate for Southampton
        c_survival_rate (float): survival rate for Cherbourg
        q_survival_rate (float): survival rate for Queenstown
        higher_survival_port (str): port with higher survival rate
    '''    
    #gets data for each port
    s_data = [passenger for passenger in data if passenger['Embarked'] == "S"]
    c_data = [passenger for passenger in data if passenger['Embarked'] == "C"]
    q_data = [passenger for passenger in data if passenger['Embarked'] == "Q"]
    
    #gets the sums of survivors in each port
    s_survived_count = sum(1 for passenger in s_data if passenger['Survived'] == '1')
    c_survived_count = sum(1 for passenger in c_data if passenger['Survived'] == '1')
    q_survived_count = sum(1 for passenger in q_data if passenger['Survived'] == '1')

    #gets the survival rates for each port using mean caluclation (count/total)
    s_survival_rate = (s_survived_count / len(s_data)) * 100 
    c_survival_rate = (c_survived_count / len(c_data)) * 100 
    q_survival_rate = (q_survived_count / len(q_data)) * 100 

    #gets the port with the highest survival rate
    if s_survival_rate > c_survival_rate and q_survival_rate:
        higher_survival_port = "S"
    elif c_survival_rate > s_survival_rate and q_survival_rate:
        higher_survival_port = "C"
    else: 
        higher_survival_port = "Q"

    return s_survival_rate, c_survival_rate, q_survival_rate, higher_survival_port


def goal_11(data):
    '''
    Investigate if cabin location affected survival
    Args:
        data (list): list of dictionaries to access data by column names
    Returns:
        a_survival_rate (float): survival rate for cabin A
        b_survival_rate (float): survival rate for cabin B
        c_survival_rate (float): survival rate for cabin C
        d_survival_rate (float): survival rate for cabin D
        e_survival_rate (float): survival rate for cabin E
        f_survival_rate (float): survival rate for cabin F
        g_survival_rate (float): survival rate for cabin G
    '''    
    #gets data for each passenger's cabin location (first letter of cabin number)
    a_data = [passenger for passenger in data if passenger['Cabin'] and passenger['Cabin'][0] == "A"]
    b_data = [passenger for passenger in data if passenger['Cabin'] and passenger['Cabin'][0] == "B"]
    c_data = [passenger for passenger in data if passenger['Cabin'] and passenger['Cabin'][0] == "C"]
    d_data = [passenger for passenger in data if passenger['Cabin'] and passenger['Cabin'][0] == "D"]
    e_data = [passenger for passenger in data if passenger['Cabin'] and passenger['Cabin'][0] == "E"]
    f_data = [passenger for passenger in data if passenger['Cabin'] and passenger['Cabin'][0] == "F"]    
    g_data = [passenger for passenger in data if passenger['Cabin'] and passenger['Cabin'][0] == "G"]    
    
    #gets the sums of survivors in each cabin letter
    a_survived_count = sum(1 for passenger in a_data if passenger['Survived'] == '1')
    b_survived_count = sum(1 for passenger in b_data if passenger['Survived'] == '1')
    c_survived_count = sum(1 for passenger in c_data if passenger['Survived'] == '1')
    d_survived_count = sum(1 for passenger in d_data if passenger['Survived'] == '1')
    e_survived_count = sum(1 for passenger in e_data if passenger['Survived'] == '1')
    f_survived_count = sum(1 for passenger in f_data if passenger['Survived'] == '1')
    g_survived_count = sum(1 for passenger in g_data if passenger['Survived'] == '1')

    #Calculates survival rates 
    a_survival_rate = (a_survived_count / len(a_data)) * 100 
    b_survival_rate = (b_survived_count / len(b_data)) * 100 
    c_survival_rate = (c_survived_count / len(c_data)) * 100 
    d_survival_rate = (d_survived_count / len(d_data)) * 100 
    e_survival_rate = (e_survived_count / len(e_data)) * 100 
    f_survival_rate = (f_survived_count / len(f_data)) * 100 
    g_survival_rate = (g_survived_count / len(g_data)) * 100 


    return a_survival_rate, b_survival_rate, c_survival_rate, d_survival_rate, e_survival_rate, f_survival_rate, g_survival_rate


def goal_12(data):
    '''
    Predict survival for a hypothetical passenger based on their attributes
    Args:
        data (list): list of dictionaries to access data by column names
    Returns:
        survival_rate (float): predicted survival rate for the hypothetical passenger
    '''    
    
    #inputs for atributes
    Class = input("Enter Class (1,2,3)")
    Gender = input("Enter Gender (male/female)")
    Age = float(input("Enter Age"))
    Family_size = int(input("Enter family size"))
    Port = input("Enter embarked port S/C/Q)")

    if Age < 18:
        age_category = 'child'
    elif Age <= 60:
        age_category = 'adult'
    else:
        age_category = 'senior'

    #Filtering data based on inputs
    hypothetical_data = [d for d in data if d['Pclass'] == Class and d['Age'] != '' and (('child' if float(d['Age']) < 18 else 'adult' if float(d['Age']) <= 60 else 'senior') == age_category) and d['Sex'] == Gender and int(d['SibSp']) + int(d['Parch']) + 1 == Family_size and d['Embarked'] == Port] 

    #Gets the sum of survivors in the hypothetical data
    survived_count = sum(1 for passenger in hypothetical_data if passenger['Survived'] == '1')
    
    #Calculates survival rate
    survival_rate = (survived_count / len(hypothetical_data)) * 100 if hypothetical_data else 0

    return survival_rate


def parse_line(line):
    """
    Splits a CSV line into a list of separate values avoiding column shifting from the names column.
    Uses for loop and if statements to navigate in and out of quoted name column
    Args:
        line (str): a line from the csv file
    Returns:
        values (list): list of seperated (parsed) values from the csv line
    """
    values = []      
    current_val = ""
    in_quotes = False #in qoutes starts as false
   
    for char in line: #For each character in the given csv line
        if char == '"': #If the character is a quote
            #flip in_quotes from True to False and vice versa
            in_quotes = not in_quotes
        elif char == ',' and not in_quotes:
            #If a separator is found (comma outside of quotes), Save a space to the list
            values.append(current_val)
            current_val = "" #Reset the current value
        else:
            #Normal character added to the value
            current_val += char
   
    #Append the last value after the loop finishes
    values.append(current_val)
    return values

def read_csv_manual(filename):
    """
    Reads the csv file into a list of dictionaries
    """
    list_of_dicts = []
    try: #Try and except to handlge potential errors 
        with open(filename, 'r') as file:
            header_line = file.readline().strip() #Read the header line and strip any extra spaces
           
            #split the header in to each correct category in different function
            headers = parse_line(header_line)

            for line in file: #For each line in the CSV file
                line = line.strip() #Read without extra spaces

                #Parse each line correctly
                values = parse_line(line)

                # Create dictionary for the current line, headers are keys
                row_dict = dict(zip(headers, values))
                list_of_dicts.append(row_dict)
               
        return list_of_dicts

    except FileNotFoundError:
        print(f"Error: '{filename}' file not found.")
        return

def main():
    my_data = read_csv_manual('titanic.csv')

    while True:        
        function_list = ['1: Load and Display Data',                                              #List of function names
                     '2: Calculate Survival Rate',    
                     '3: Survival by Gender',
                     '4: Age Analysis',
                     '5: Class-Based Analysis',
                     '6: Family Survival Patterns',
                     '7: Data Visualization',
                     '8: Comprehensive Report',
                     '9: Most Common First Names Among Survivors',              
                     '10: Analyze Survival Rates by Port of Embarkation',
                     '11: Investigate if Cabin Location Affects Survival',
                     '12: Predict Survival for Hypothetical Passenger \n',]
   
        for i in function_list:                                                               #For loop that prints the function names in the list
            print(i)
        function_menu = input('-Enter a goal from 1 to 12   \n')
        if function_menu == '1':
            print("\n First 10 Rows: \n")
            for i  in (goal_1(my_data)[0]):
                print (i)
            print("\n")
            print("Column Names:")
            for i  in (goal_1(my_data)[1]):
                print (i)  
            print('\n')
            print(f"passenger count: {(goal_1(my_data)[2])} \n")        

        elif function_menu == '2':
            print(f"\nSurvival Rate: {goal_2(my_data):.2f}%\n")    

        elif function_menu == '3':
            print(f"\nMale Survival Rate: {(goal_3(my_data)[0]):.2f}%\n")
            print(f"Female Survival Rate: {(goal_3(my_data)[1]):.2f}%\n")
            print(f"Higher Survival Rate: {(goal_3(my_data)[2])} \n")

        elif function_menu == '4':
            print(f"\nAverage Age: {(goal_4(my_data)[0]):.2f}\n")
            print(f"Average Survival Age: {(goal_4(my_data)[1]):.2f}\n")
            print(f"Average Non Survival Age: {(goal_4(my_data)[2]):.2f}\n")
            print(f"Youngest Passenger: {(goal_4(my_data)[3])} \n")
            print(f"Oldest Passenger: {(goal_4(my_data)[4])} \n")
       
        elif function_menu == '5':
            print(f"\n1st Class Survival Rate: {(goal_5(my_data)[0]):.2f}%\n")
            print(f"1st Class Average Fare: {(goal_5(my_data)[1]):.2f}\n")
            print(f"2nd Class Survival Rate: {(goal_5(my_data)[2]):.2f}%\n")
            print(f"2nd Class Average Fare: {(goal_5(my_data)[3]):.2f}\n")
            print(f"3rd Class Survival Rate: {(goal_5(my_data)[4]):.2f}%\n")
            print(f"3rd Class Average Fare: {(goal_5(my_data)[5]):.2f}\n")

        elif function_menu == '6':
            print(f"\nAlone Survival Rate: {(goal_6(my_data)[0]):.2f}%\n")
            print(f"With Family Survival Rate: {(goal_6(my_data)[1]):.2f}%\n")
            print(f"Higher Survival Rate: {(goal_6(my_data)[2])} \n")  

        elif function_menu == '7':
            print('\n')
            goal_7(my_data)


        elif function_menu == '8':
            goal_8(my_data)
            print("\nComprehensive report saved to survival_report.txt\n")

        elif function_menu == '9':
            print('\n')
            name_dict = (goal_9(my_data)) 
            for key, value in name_dict.items(): #Print each key and value together with for loop
                print(f"{key}: {value} \n")

        elif function_menu == '10':
           print(f"\nSouthhapton Survival Rate: {(goal_10(my_data)[0]):.2f}%\n")
           print(f"Cherbourg Survival Rate: {(goal_10(my_data)[1]):.2f}%\n")
           print(f"Queenstown Survival Rate: {(goal_10(my_data)[2]):.2f}%\n")
           print(f"Higher Survival Port: {(goal_10(my_data)[3])} \n")  

        elif function_menu == '11':
           print(f"\nA Survival Rate: {(goal_11(my_data)[0]):.2f}%\n")
           print(f"B Survival Rate: {(goal_11(my_data)[1]):.2f}%\n")
           print(f"C Survival Rate: {(goal_11(my_data)[2]):.2f}%\n")
           print(f"D Survival Rate: {(goal_11(my_data)[3]):.2f}%\n")
           print(f"E Survival Rate: {(goal_11(my_data)[4]):.2f}%\n")
           print(f"F Survival Rate: {(goal_11(my_data)[5]):.2f}%\n")
           print(f"G Survival Rate: {(goal_11(my_data)[6]):.2f}%\n")

        elif function_menu == '12':
            print(f"\nHypothetical Survival Rate: {goal_12(my_data):.2f}%\n")

        else:
            print("\nInvalid input, please try again.\n")

main()
























