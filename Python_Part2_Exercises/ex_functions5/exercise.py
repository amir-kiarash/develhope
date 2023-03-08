import random

def random_list_summer(n=15):
    # Generate a random list of n integers between -100 and 100
    lst = [random.randint(-100, 100) for i in range(n)]

    # Print the list
    print("Random List: ", lst)

    # Calculate the sum of all the elements in the list
    lst_sum = sum(lst)

    # Print the sum of the list
    print("Sum of the List: ", lst_sum)

# Call the random_list_summer function with default n value of 15
random_list_summer()