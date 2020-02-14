#File: nguyenSpeedLimit.py

#Project: CSIS2101 - Assignment 3 (Final Draft)

#Author: Jenny P. Nguyen

#History: September 24, 2019



def nguyenSpeedLimit():


#The fine starts off at 0 because it hasn't been determined by the user's input
    fine = 0
    

#A greeting from the computer then it askes the 3 questions to determine the speeding fine
    print("Welcome, User!")

    print("\n")

    speedLimit = float(input("Please enter the Speed Limit: "))

    print("\n")

    speedVh = float(input("Please enter the Speed of the Vehicle: "))

    print("\n")

    cOrSZone = input("Construction or School Zone?: ")

    

#With the boolean, this is used to define the fine cost based on (speedVh - speedLimit)
    if (speedVh-speedLimit) < 10 and  (speedVh-speedLimit) >0:
        fine = 120.00
    
    elif (speedVh-speedLimit) < 15 and  (speedVh-speedLimit) >= 10:
        fine = 199.00        
        
    elif (speedVh-speedLimit) < 20 and  (speedVh-speedLimit) >= 15:
        fine = 248.00     
        
    elif (speedVh-speedLimit) < 30 and  (speedVh-speedLimit) >= 20:
        fine = 286.00
        
    elif (speedVh-speedLimit) >=30:
        print("\n")
        print("Court Mandatory. See ya in court!")
        
    else:
        print("\n")
        print("You are driving within the speed limit. Thank you for driving safely!")



#With the boolean, this is part of the fine whether or not it doubles based on the Construction or School zone
    if cOrSZone == "yes" or cOrSZone == "Yes" or cOrSZone == "Y":
        cOrSZone2 = fine * 2
        print("\n")
        print("Your total fine is: ${0:0.2f}".format(cOrSZone2))
        print("\n")
        
    elif cOrSZone == "no" or cOrSZone == "No" or cOrSZone == "N":
        cOrSZone2 = fine
        print("\n")
        print("Your total fine is: ${0:0.2f}".format(cOrSZone2))
        print("\n")
        
    else:
        print("Your input is invalid.")



#With the boolean, this prints out a message after their total fine

    if (speedVh-speedLimit) < 10 and  (speedVh-speedLimit) >0:
        print("Slow Down!")
    
    elif (speedVh-speedLimit) < 15 and  (speedVh-speedLimit) >= 10:
        print("Drive with caution!")
    
    elif (speedVh-speedLimit) < 20 and  (speedVh-speedLimit) >= 15:
        print("You are over speeding!")
        
    else:
        if (speedVh-speedLimit) < 30 and  (speedVh-speedLimit) >= 20:
            print("You are in Danger zone!")
            


        


        

nguyenSpeedLimit()





