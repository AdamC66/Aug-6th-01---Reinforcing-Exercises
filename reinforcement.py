# Write a function that accepts a number as an argument and returns a string containing that number along with its "ordinal indicator". 
# E.g. passing in 1 would return "1st", 2 would return "2nd", 3 would return "3rd", 4 would return "4th", etc.

# Make sure your function works for every number between 1 and 20. If you're feeling ambitious, see if you can get it working for numbers beyond that.
# Write a function that accepts a number as an argument and returns a string containing that number along with its "ordinal indicator". 
# E.g. passing in 1 would return "1st", 2 would return "2nd", 3 would return "3rd", 4 would return "4th", etc.

# Make sure your function works for every number between 1 and 20. If you're feeling ambitious, see if you can get it working for numbers beyond that.


def ordinal(num):
    last = num%10
    ordinalstr = str(num)
    if num in [11,12,13]:
        ordinalstr += "th"
    elif last == 1:
        ordinalstr += "st"
    elif last == 2:
        ordinalstr += "nd"
    elif last == 3:
        ordinalstr += "rd"
    else:
        ordinalstr+= "th"
    return ordinalstr

for num in range (1,21):
    print(ordinal(num))
    