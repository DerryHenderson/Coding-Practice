# Coding Practice

PupilNames = []
prices = []
NoOfPupils = 0

#get group name
GroupName = input("Please enter group name:   ")

#get a valid number of pupils in the group
NoOfPupils = float(input("Please enter number of pupils:   "))

while not NoOfPupils.is_integer():
  NoOfPupils = float(input("Please enter number of pupils:   "))

NoOfPupils = int(NoOfPupils)


#Loop for each pupil in the group
for Counter in range (NoOfPupils) :
    #Get pupil Name
    PupilName = input("Please enter pupil name:   ") 
    PupilNames.append(PupilName)

    #Ask if pupil wants to pre-order a photo
    Photo = input("would you like to pre order a photo?:   ").lower()

    while Photo != "yes" and Photo != "no":
      Photo = input("Please enter yes or no:   ")

    #Decide and store ticket cost for each pupil
    price1 = 3.00
    price2 = 4.99
    if Photo == "yes":
      ticketprice = price2
    elif Photo == "no":
      ticketprice = price1
    prices.append(ticketprice)
    
#Display results
print ("Group Name:   " + str(GroupName))
print ("Number in group:   " + str(NoOfPupils))
for y in range(NoOfPupils):
  print (f'{PupilNames[y]:20}{ticketprice:.2f}')