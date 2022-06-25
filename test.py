# import your modules here
import random as rnd
# deifne function here 
def getRandomNumber() :
    '''@getRandomNumber() function generates the random intgers for 
    specific range and returns the integer for these case we have setted
    the range as 0 -> 2'''
    int_rand = rnd.randint(0,2)
    choice = ""
#    while True :
#        choice = input("[+] Enter Y/N to see the documentation of the @getRandomNumber() : ")
#        if choice == "N" :
#            break;
#        else :
#            print(getRandomNumber.__doc__)
#            break;
#
#    return int_rand
    while choice != "N" : 
        print(int_rand)
        choice = input("[+] Enter your choice Y/N : ")
print(getRandomNumber())


