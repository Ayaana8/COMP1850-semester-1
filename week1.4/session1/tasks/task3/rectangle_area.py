
# function implementation

def rectangle_area( width, height):  # define suitable input data
    """Return the area of a rectange with the inputs of width and height """
    area = width * height               # implement the function
    return area             # return an appropriate value

# testing the function

print(f"Area is {rectangle_area(3,2)}")   # provide suitable data matching your inputs

def even_integers(maxVal):
    """ Return a string of the even integers between 0 and a specified value"""
    evenInt = []
    for i in range(maxVal+1):
        if i % 2 ==0:
            evenInt.append(i)
    return evenInt

maximum = int(input("Enter the maximum value "))
print(f"List of the even integers up to {maximum} is {even_integers(maximum)}")

def calc_mean(intList):
    """Returns the mean of a list"""
    total = 0
    for i in intList:
        total += i
    mean = total / len(intList)
    return mean

ListOfInts = [1,2,3,4]
print(f"Mean is: {calc_mean(ListOfInts)}")