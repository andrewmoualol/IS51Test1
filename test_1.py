

"""
The program is trying to determin which payment of the two option is better (more money).
Frist option is 100 dollars pre day for 10 days. The second option is 1 dollars 
a day with it being doubled each day for 10 days. 
There will be two functions to calculate the pay rate.
Function1 will calculate the amount for the first option, function2 will calculate 
the amount for the second options.

Function1 will output 100 + 30 days.
Function2 will loop 10 times, with each time, doubling the amount and add the amount to the total.

If the amount is equal, we output to the user "Option 1 and Option 2 pays the same"
If the Option1 is better, we output to the user "Option 1 is better"
If the Option2 is better, we output to the user "Option 2 is better"
"""





"""
#option1
return 100 * 10

#option2
amount= 1
list1 = []
loop 10 times
    add amount to list
    amount *= 2
sum = sum of all items in loop
return sum
# main
    var1 = option1
    var2 = option2

    If var1 = var 2
        "Option 1 and Option 2 pays the same"
    If var1 < var2
        "Option 2 is better."
    else
        "Option 1 is better."

main
"""


def option1():
    return 100 * 10

def option2():
    amount= 1
    list1 = []
    for i in range (0, 10):
        list1.append(amount)
        amount *= 2
    print("list1", list1)
    total = sum(list1)
    return total

def main():
    answer = ""
    var1 = option() # 1000
    var2 = option() # 1023
    if var1 == var2:
        answer = "Option 1 and Option 2 pays the same"
    if var1 < var2:
         answer = "Option 2 is better."
    else:
        answer = "Option 1 is better."
    print(answer)
main()
