# Name: M. Sabbir Rahman
#email: m.rahman@tuni.fi



#Define function to recieve customer input and return list
def customer_response():
    customer_list=[]            #Declear empty list to store customer responses
    # "number_of_cups" variable to store each response
    number_of_cups=input("Enter one response per line. End by entering an empty row.\n")
    while number_of_cups!='':   #Check the ' ' mark to stop storing responses in empty list
        customer_list.append(int(number_of_cups))  #storing user input in empty list
        number_of_cups = input()
    return customer_list        #Return the 'customer_list' for future use in other function




#Define function to count non-coffee drinkers and return int data
def non_coffee_drinkers(customer_response_list):
    #'count_non_coffee_drinker' variable for counting total number of non coffee drinker
    count_non_coffee_drinker=0
    for i in range(len(customer_response_list)):
        if customer_response_list[i]==0:
            count_non_coffee_drinker+=1
    return count_non_coffee_drinker #return the int typ date (sum of all no-coffee drinkes)




#Define function to sort the coffee drinkers customer list and return sorted list
def sort_customer_list(customer_response_list):
    coffee_drinkers=[] # coffee_drinkers is decleared empty list to store only coffee drinkers response
    for j in range(len(customer_response_list)):
        if customer_response_list[j]>0:
            coffee_drinkers.append(customer_response_list[j])
    return sorted(coffee_drinkers) #Returning sorted coffee drinkers list




#Define function to show the maximum and common responses among coffee drinkers
def info_coffee_drinkers(sorted_coffee_drinker_list):
    print("Information related to coffee drinkers:")
    number_of_cups=[]
    for k in range( min(sorted_coffee_drinker_list[:]),max(sorted_coffee_drinker_list[:])+1):
        print(f"{k:2d}",sorted_coffee_drinker_list.count(k)*'#')
        number_of_cups.append(sorted_coffee_drinker_list.count(k))
    print()
    common_response=number_of_cups.index(max(number_of_cups[:]))+min(sorted_coffee_drinker_list[:])
    print("The greatest response:",max(sorted_coffee_drinker_list[:]),"cups of coffee per day")
    print("The most common response:",common_response,"cups of coffee per day" )




# Define function to show the coffee drinker response in percentage with 4 cups of coffee as reference
def percentage_calculation(customer_response_list):
    total_responder=len(sort_customer_list(customer_response_list)) #total_responder denote tho\
    # total number of coffee drinkers
    coffee_drinker_less4_cups = []    # coffee_drinker_less4_cups is empty list to\
    # store drinkers consume less than 4cups
    Reference_value=4 #Reference_value is the constant value which refer 4cups of coffee
    for h in range(min(sort_customer_list(customer_response_list)[:]),\
                   max(sort_customer_list(customer_response_list)[:]) + 1):
        if h <= Reference_value:
            coffee_drinker_less4_cups.append(sort_customer_list(customer_response_list).count(h))
        else:
            coffee_drinker_less4_cups.append(0)
    response_rate = ((total_responder - sum(coffee_drinker_less4_cups[:])) * 100) / total_responder

    if response_rate ==100: #Check the condition while all responder drink more than 4 cups of coffee
        print(f"{response_rate:.1f}%","of the respondents drink more than 4 cups of coffee per day")

    elif response_rate ==0: #Check the condition while all responder drink less than 4 cups of coffee
        print("None of the respondents drink too much coffee")

    else: #Check the condition while responder have mix response
        print(f"{response_rate:.1f}%", "of the respondents drink more than 4 cups of coffee per day")




def main():
    customer_response_list=customer_response() #call customer_response function to get customer_response_list
    total_non_coffee_drinkers =non_coffee_drinkers(customer_response_list) #call non_coffee_drinkers\
    # to get total_non_coffee_drinkers
    sorted_coffee_drinker_list = sort_customer_list(customer_response_list) #s call ort_customer_list\
    #function to get sorted coffee drinker list

    if total_non_coffee_drinkers!=0: #check the condition while there is non-coffee drinker response
        print("Removed", total_non_coffee_drinkers, "non-coffee-drinkers responses \n")
    if total_non_coffee_drinkers!=len(customer_response_list): #check the condition while there is at\
        #  least one coffee drinkers
        info_coffee_drinkers(sorted_coffee_drinker_list) #call the info_coffee_drinkers function
        percentage_calculation(customer_response_list) #call the percentage_calculation function

main()