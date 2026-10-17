# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv

# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format

with open("sales.csv","r") as infile:

    data = infile.readlines()
    data = [ line.strip().split(",") for line in data[1:]]

ProductToSaleMapping = {}

LargestSaleDay = 0
HighestSale =0
TotalSales = 0
for i in range(len(data)):
    if (int(data[i][2]) > HighestSale):
        HighestSale = int(data[i][2])
        LargestSaleDay = data[i][0]

    TotalSales += int(data[i][2])

    if data[i][1] in ProductToSaleMapping:
        ProductToSaleMapping[data[i][1]] += 1
    else:
        ProductToSaleMapping[data[i][1]] =1

AvgSale = TotalSales / len(data)

HighestQuantity = 0
MostSold = ""

HighestQuantity = max(ProductToSaleMapping.values())

for i in ProductToSaleMapping.keys():
    if ProductToSaleMapping[i] == HighestQuantity:
        MostSold = i



print(LargestSaleDay)
print(f"£{AvgSale}")
print(MostSold)


# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows