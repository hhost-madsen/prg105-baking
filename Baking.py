# 1 ml = .2 tsp

def convert(ml):
    tsp = round (float(ml) * .20)
    return tsp


print("This program will convert milliters to teaspoons")
milliliters = raw_input("How many milliliters? ")

# this is where we call the function
teaspoons = convert(milliliters)
print (milliliters + " milliliters is equal to " + str(teaspoons) + " teaspoons")
