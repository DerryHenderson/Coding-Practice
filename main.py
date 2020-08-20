# Coding Practice

PupilNames = []
prices = []

#get group name
GroupName = input("Please enter group name:   ")

#get a valid number of pupils in the group
NoOfPupils = int(input("Please enter number of pupils:   "))

if NoOfPupils != int(NoOfPupils):
  NoOfPupils = int(input("Please enter a valid number of pupils:   "))


for Counter in range (NoOfPupils) :
    #Get pupil Name
    PupilName = input("Please enter pupil name:   ") 
    PupilNames.append(PupilName)

    Photo = input("would you like to pre order a photo?:   ").lower()

    price1 = 3.00
    price2 = 4.99
    if Photo == "yes":
      ticketprice = str(PupilName) + "    £" + str(round(price2,2))
    elif Photo == "no":
      ticketprice = str(PupilName) + "    £" + str(round(price1,2))
    prices.append(ticketprice)
    

print ("Group Name:   " + str(GroupName))
print ("Number in group:   " + str(NoOfPupils))
for y in range(NoOfPupils):
  print (prices[y])