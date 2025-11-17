#Author: Arman Ahmadzadeh
#Date: 10/31/2025
#Description: algorithm to
#determine the postage cost for entered mail. Postage class is determined by the size of a piece of
#mail. The cost to mail the piece is determined by its class and the number of postal zones the
#piece must travel through.
#Bugs: Assumes user enters data sperated by a comma and space
#Sample data 1:
#4, 5, 0.01, 1234, 5678 Expected: 0.20
#5, 7, 0.01, 7245, 45216 Expected: 0.43 
#5, 7, 0.2, 45216, 7245 Expected: 0.45 
#15, 12, 0.4, 15000, 80000 Expected: 0.75
#2, 2, 0.001, 1000, 2000 Expected: UNMAILABLE 
#Sample data 2:
#10, 10, 1, 20000, 25000 Expected: 2.95
#12, 8, 1, 1000, 40000 Expected: 3.70 
#10, 12, 30, 21505, 72400 Expected: 4.65 
#20, 15, 2, 5000, 95000 Expected: 4.20
#50, 50, 10, 1000, 2000 Expected: UNMAILABLE 
#Sources: Previous code
#https://www.w3schools.com/python/ref_func_round.asp
#https://www.w3schools.com/python/ref_func_abs.asp
#https://www.w3schools.com/python/ref_func_enumerate.asp
#https://www.geeksforgeeks.org/python/how-to-add-leading-zeros-to-a-number-in-python/
#https://www.geeksforgeeks.org/python/check-if-value-is-int-or-float-in-python/


def get_type(data, post_type):
    '''
    Gets the class of post using inequalities
    Args:
        data (dict): data of the mail
        post_type (str): the type of post
    Returns:
        str: the type of post
    '''  
    length = data['length']         #Turns dict values into variables
    height = data['height']
    thickness = data['thickness']

    size_measure = length + 2*height + 2*thickness #Has size = length + 2 times height + 2 times thickness

    if 3.5 <= length <= 4.25 and 3.5 <= height <= 6 and 0.007 <= thickness <= 0.016: #if it matches regular post using inequalities 
        post_type = "regular_post"

    elif 4.25 <= length <= 6 and 6 <= height <= 11.5 and 0.007 <= thickness <= 0.015: #if it matches large post using inequalities 
        post_type = "large_post"

    elif 3.5 <= length <= 6.125 and 5 <= height <= 11.5 and 0.016 <= thickness <= 0.25: #if it matches envelope post using inequalities 
        post_type = "envelope"

    elif 6.125 <= length <= 24 and 11 <= height <= 18 and 0.25 <= thickness <= 0.5: #if it matches large envelope using inequalities 
        post_type = "large_envelope"
                    
    elif 84 < size_measure <= 130: #If the size is between 84 not inclusive and 130
        post_type = "large_package"

    elif (length > 24 or height > 18 or thickness > 0.5) and size_measure <= 84: #If it is a package using inequalities and size measure 
        post_type = "package"

    else:                         
        post_type = "UNMAILABLE"    #Unmailable if none matches

    return post_type


def check_zone_distance(data, zone):
     '''
   Calculates how many zone the post passes by looping through list of tuples
    Args:
        data (dict): data of the mail
    Returns:
        int: the number of zones the mail passes
    '''    
     zones = [                   #List of tuples, each tuple represents a zone 
                (1, 6999),
                (7000, 19999),
                (20000, 35999),
                (36000, 62999),
                (63000, 84999),
                (84999, 99999),
                ]

     start_zone = None
     end_zone = None

     for i, (start, end) in enumerate(zones):  #Loops through the zones, i gets the index of the ranges and the tuple gets the values of each zone 
         if start <= data['starting zip code'] <= end:  #if the first item in the tuple is less than or equal to the starting zip and the zip is less than or equal to the end item
             start_zone = i                             #i is saved start zone
         if start <= data['ending zip code'] <= end:    #if the second item in the tuple is less than or equal to the ending zip and the zip is less than or equal to the end item
             end_zone = i                               #i is saved as end zone

     return abs(end_zone - start_zone)        #Returns the absolute values of the start zone - the end zone (the zones the mail will pass through)


def check_cost(type, zone_count):
    '''
    Calculates the cost of the mail based on its type and zone distance
    Args:
        type (str): the type of post
        zone_count (int): the number of zones the mail passes
    Returns:
        float: the cost of the mail
        str: unmailable
    '''
    cost = 0   #Cost set to 0 
    if type == "regular_post":  #If it is some type add the cost of the type + the zone distance * the added price per zone for the type
        cost += .20
        cost += zone_count * .03
    elif type == "large_post":
        cost += .37
        cost += zone_count * .03
    elif type == "envelope":
        cost += .37
        cost += zone_count * .04
    elif type == "large_envelope":
        cost += .60
        cost += zone_count * .05
    elif type == "package":
        cost += 2.95
        cost += zone_count * .25
    elif type == "large_package":
        cost += 3.95
        cost += zone_count * .35
    else:            #If it is unmailable return "umailable"
        return type 
    return round(cost, 2) #Return the cost rounded by 2 decimal points
     
def main():

    while True:
        list_1 = ['1: length',                                              
                  '2: height',    
                  '3: thickness',
                  '4: starting zip code',
                  '5: ending zip code \n']
                                   
        for i in list_1:                                                            
                print(i)

        final_cost = [] #empty list

        for i in range(5): #5 times

            i += 1 #Add 1 to i for f string

            variables_input = input(f"Enter data line {i}: \n")

            print("")

            values = variables_input.split(", ")  #The users input is split into a list seperated by a , and space

            values =  [float(item) for item in values] #The list is equal itself with all its values looped through to turn into floats

            data = {} #Empty dictionary 
        
            data['length'] = values[0]   #Dictionary key values pairs assigned                         
            data['height'] = values[1]
            data['thickness'] = values[2]
            data['starting zip code'] = values[3]
            data['ending zip code'] = values[4]
        
            post = 0  
            zone_count = 0 
            post_type = get_type(data, post) #Get post type using the data
            zone_distance = check_zone_distance(data, zone_count) #Get zone distance using the data
            final_cost.append(check_cost(post_type, zone_distance)) #Get the cost using both the type and distance and add it to list
        for i in final_cost: #for each item of final costs list
            if isinstance(i, float): #If i is a float
                print(f"{i:.2f}")  #print costs using f string to show 2 decimal points by adding placeholder 0
            else:        #If i is Unmailable
                print(i)
        break #Program ends (can be removed for testing)

main()   






    
