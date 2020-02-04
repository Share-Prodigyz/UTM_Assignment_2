##############################################
# Author: Justin Sousa
# Class: CCT 111, Winter 2019
# Programming Assignment # 2
# 10/22/19
#
# Description: This project will prompt a user for four different things ( a character, an integer, an integer, an integer ) which will be used to calculate a float. The purpose of this project is to simulate a the billing process of a car rental agency. It will focus on using control structures to allow the user to provide information for a fictional car rental agency and provide a report related to the amount each customer owes. 
# No sources to cite. 
##############################################

import math
 
def calculating_cost_of_rental(classification_code, days_vehicle_rented, odometer_start, odometer_end):
    ''' Calculates the total cost of the rental and displays it. Done by using the four parameters ( classification_code, days_vehicle_rented, odometer_start, odometer_end ), then based on the classification code the mathamatical equations will vary for the base_charge and millage_charge. The rental_cost is caculate by adding the base_charge and millage_charge. At the end of the function the customers information as well as the price will be printed, in the case of a invalid classification code the program will stop and print the customers information. The overage charge for the daily limit was done by mulitplying the excess that the user went over by the fee. The way the overage charge was calculate for weekly was the done by using the additional kilometers per week ( which was rounded up the next whole weeks) mulitplied by the respective fee for going over on the weekly limit. '''
    
    rental_cost = 0.00
    base_charge = 0.00
    millage_charge = 0.00
    millage_difference = odometer_end - odometer_start
    
    if classification_code.upper() == "B":
        base_charge = 20.00 * days_vehicle_rented
        millage_charge = (millage_difference) * 0.15
        rental_cost = round(base_charge + millage_charge, 2)
    elif classification_code.upper() == "D":
        base_charge = 30.00 * days_vehicle_rented
        if millage_difference/ days_vehicle_rented <= 150:
            rental_cost = round(base_charge, 2)
        else:
            millage_charge = ((millage_difference / days_vehicle_rented) - 150 ) * 0.15 
            rental_cost = round(base_charge + millage_charge, 2)
    elif classification_code.upper() == "W":
        base_charge = 190 * math.ceil(days_vehicle_rented / 7)
        if  millage_difference / math.ceil(days_vehicle_rented / 7) <= 900:
            rental_cost = round(base_charge, 2)
        elif millage_difference / math.ceil(days_vehicle_rented / 7) > 900 and millage_difference / math.ceil(days_vehicle_rented / 7) <= 1500:
            millage_charge = 100 * math.ceil((days_vehicle_rented / 7))
            rental_cost = round(base_charge + millage_charge, 2)
        elif millage_difference /  math.ceil(days_vehicle_rented / 7) > 1500: 
            millage_charge = (200 * math.ceil((days_vehicle_rented / 7))) + (((millage_difference / math.ceil(days_vehicle_rented / 7) - 1500 ) * 0.15) * math.ceil((days_vehicle_rented / 7)))
            rental_cost = round(base_charge + millage_charge, 2)
            
    elif classification_code.upper() == "Q" or ( classification_code.upper() != "B" and classification_code.upper() != "D" and classification_code.upper() != "W"):
        print("\nError invalid classification code entered")        
        print("Summary: \n\tThe customers classification code is: " , classification_code.upper())
        print("\tThe number of days the vehicle was rented is: " , days_vehicle_rented)
        print("\tThe vehicle's odometer reading at the start of the rental period is: " , odometer_start)
        print("\tThe vehicle's odometer reading at the end of the rental period is: " , odometer_end)
        print("\tThe number of kilometers driven during the rental period is: " , round(millage_difference,1) , "km")
        print("\tThe amount of money billed to the customer for the rental period is:  $" , '{:0.2f}'.format(rental_cost))     
        print("\tInformation previously provided: \nThe classification code is: ", classification_code.upper())
        print("\tThe number of days the car was rented for is:" , days_vehicle_rented)
        print("\tThe vehicle's odometer reading at the start of the rental period is: " , odometer_start)
        print("\tThe vehicle's odometer reading at the end of the rental period is: " , odometer_end)
        return
    
    print("\nThe customers classification code is: " , classification_code.upper())
    print("The number of days the vehicle was rented is: " , days_vehicle_rented)
    print("The vehicle's odometer reading at the start of the rental period is: " , odometer_start)
    print("The vehicle's odometer reading at the end of the rental period is: " , odometer_end)
    print("The number of kilometers driven during the rental period is: " , round(millage_difference,1) , "km")
    print("The amount of money billed to the customer for the rental period is:  $" , '{:0.2f}'.format(rental_cost)) 
    customer_input()
    return

def customer_input():
    ''' The function will run a loop that will repeatedly ask the user to input certain things. After the user is promptted the four statements ( classification code, days rented, odometer start, odometer end ) an if statment will check if each requirement is fulfilled, if not it will reiterate those same statements, if it is fulfilled it will then call the function calculating_cost_of_rental using the set of data the user inputted for the parameters of the function calculating_cost_of_rental and break the loop. '''
    
    while True:
        classification_code = str(input("\nPlease enter the classification code "))
        days_vehicle_rented = int(input("Please enter the number of days the car was rented for "))
        odometer_start = int(input("Please enter the reading on the odometer at the start of the rental period "))
        odometer_end = int(input("Please enter the reading on the odometer at the end of the rental period "))
        if classification_code == "" or days_vehicle_rented == 0 or odometer_start == 0 or odometer_end == 0:
            print("You forgot to enter something")  
        else:   
            calculating_cost_of_rental(classification_code, days_vehicle_rented, odometer_start, odometer_end)
            break            

customer_input()