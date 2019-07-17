#First Way
m = "cadburymilk"
w = "cadburywhite"
d = "cadburydark"

print("I have 5",m, "3",d, "8",w,)
#My Way
d = "dark chocolate"
m = "milk chocolate"
w = "white chocolate"

print("There are 3",d,"8",w,"and 5",m,)

#My Way
d = "3 dark chocolate"
m = "5 milk chocolate"
w = "8 white chocolate"

print("There are",d,",",m,",",w,".")

#dict data structure
chocolate1 = {"cadburymilk":5}
chocolate2 = {"cadburydark":3}
chocolate3 = {"cadburywhite":8}

#single line dict
chocolatebox = {"milk":5,"dark":3,"white":8}
print(chocolatebox)
print("The chocolates in the box are",chocolatebox,)

#students name/age
age = {"Steve":32, "Lia":28, "Vin":45, "Katie":38}
gender = {"Steve":"M", "Lia":"F", "Vin":"M", "Katie":"F"}


chocolatebox = {"milk":5, "dark":3, "white":8}
print("The number of white chocolates in chocolate box is",chocolatebox,{"white"})
#Lia's Age/Gender
age = {"Lia":28}
gender = {"Lia":"F"}
print("Lia's age is",age,"and gender is",gender)

age = 28
gender = "girl"
print("Lia's age is",age,"and gender is",gender)
#Pandas!
import pandas
dir(pandas)
#My Pandas Example
people = {"Sara":15, "Mary":17, "Jane":16}
teens = pandas.Series(people)
print(teens)

#data frame
newPeople = pandas.DataFrame(people, index=["quantity"])
print(newPeople)

people = {32,"Male","Steve"},{"Lia",28,"Female"},{"Male","Vin",45},{"Katie","Female",38}
df = pandas.DataFrame(people)
print(df)

df2 = pandas.DataFrame(people,columns=["Name","Age","Gender"])
print(df2)

