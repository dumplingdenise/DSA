# Denise Teo 214329G Gp07
# This is the latest updated codes
records = [{'Package Name': 'Package 1', 'Customer Name': 'Denise', 'pax': 2, 'cost': 495},
               {'Package Name': 'Package 2', 'Customer Name': 'Zaren', 'pax': 2, 'cost': 325},
               {'Package Name': 'Package 3', 'Customer Name': 'Nat', 'pax': 4, 'cost': 275},
               {'Package Name': 'Package 2', 'Customer Name': 'Lylia', 'pax': 4, 'cost': 379},
               {'Package Name': 'Package 1', 'Customer Name': 'Dino', 'pax': 3, 'cost': 189},
               {'Package Name': 'Package 4', 'Customer Name': 'Johnson', 'pax': 3, 'cost': 275},
               {'Package Name': 'Package 5', 'Customer Name': 'Kagura', 'pax': 5, 'cost': 435},
               {'Package Name': 'Package 3', 'Customer Name': 'Stitch', 'pax': 2, 'cost': 379},
               {'Package Name': 'Package 1', 'Customer Name': 'Alice', 'pax': 4, 'cost': 534},
               {'Package Name': 'Package 2', 'Customer Name': 'Nathan', 'pax': 4, 'cost': 189}]
def displaymenu():
    print("****** Aloha Staycation Package Deals Inventory ******")
    menu = ["1. Display all records", "2. Sort record by Customer Name using Bubble sort",
            "3. Sort record by Package Name using Selection sort", "4. Sort record by Package Cost using Insertion sort",
            "5. Search record by Customer Name using Linear Search and update record", "6. Search record by Package name using Binary Search and update record",
            "7. List records range from $X to $Y. eg $100-$200", "8. Sort records using Shell sort", "9. Sort records by Package Cost using Pancake sort"]
    print(*menu, sep='\n')

def AllRecords():
    for x in records:
        print("\nPackage Name:", x['Package Name'])
        print("Customer Name:", x['Customer Name'])
        print("Number of pax:", x['pax'])
        print("Package cost Per Person: ${}".format(x['cost']) , '\n')

def BubbleSort():
    length = len(records)

    for i in range(length - 1, 0, -1):
        for j in range(i):
            if records[j]['Customer Name'] > records[j + 1]['Customer Name']:
                tmp = records[j]
                records[j] = records[j + 1]
                records[j + 1]= tmp
    print("\nRecords have been sorted by Customer Name. Press 1 to view.")

def SelectionSort():
    length = len(records)

    for i in range(length - 1):
        smallNdx = i
        for j in range(i+1, length):
            if records[j]['Package Name'] < records[smallNdx]['Package Name']:
                smallNdx = j
        if smallNdx != i:
            tmp = records[i]
            records[i] = records[smallNdx]
            records[smallNdx] = tmp
    print("\nRecords have been sorted by Package Name. Press 1 to view.")

def InsertionSort():
    length = len(records)

    for i in range(1, length):
        value = records[i]
        pos = i
        while pos > 0 and value['cost'] < records[pos - 1]['cost']:
            records[pos] = records[pos-1]
            pos -= 1
        records[pos] = value
    print("\nRecords have been sorted by Package Cost Per Person. Press 1 to view.")

def sortedLinearSearch():
    searching = True
    updating = True
    while searching:
        target = input("Search customer name or press x to go back: ")
        target = target.capitalize()
        namelist = []
        for x in records:
            namelist.append(x['Customer Name'])
        length = len(namelist)
        if target == 'X':
            searching = False
            break
        else:
            recordsfound = False
            for i in range(length):
                # If the target is in the ith element, return True
                if namelist[i] == target:
                    print("\nRecord found, here is the details for customer name '{0}'".format(target))
                    print("\nCustomer Name:", records[i]['Customer Name'])
                    print("Package Name:", records[i]['Package Name'])
                    print("Number of pax:", records[i]['pax'])
                    print("Package cost Per Person: ${}".format(records[i]['cost']))
                    recordsfound = True
                    updateChoice = input("Would you like to update your details (y/n)? ")
                    while updating:
                        if updateChoice.upper() == 'Y':
                            update = input("\n1. Customer Name \n2. Package Name \n3. Number of Pax \n4. Cost per Person \nWhat would you like to update? ")
                            if update == '1':
                                CN = input('Please enter the Customer Name you would like to update to: ')
                                CN = CN.capitalize()
                                records[i]['Customer Name'] = CN
                                yN = input('Customer Name has been updated, would you like to continue (y/n)? ')
                                if yN.upper() == 'Y':
                                    updateChoice = 'y'
                                    continue
                                elif yN.upper() == 'N':
                                    print("Your details has been updated. Thank you")
                                    updating = False
                                    searching = False
                                    break
                            if update == '2':
                                PN = input('Please enter the Package Name you would like to update to: ')
                                PN = PN.capitalize()
                                records[i]['Package Name'] = PN
                                yN = input('Package Name has been updated, would you like to continue (y/n)? ')
                                if yN.upper() == 'Y':
                                    updateChoice = 'y'
                                    continue
                                elif yN.upper() == 'N':
                                    print("Your details has been updated. Thank you")
                                    updating = False
                                    searching = False
                                    break
                            if update == '3':
                                P = input('Please enter the Number of Pax you would like to update to (max 5): ')
                                if P.isnumeric() and P < '6':
                                    records[i]['pax'] = P
                                    yN = input('Number of Pax has been updated, would you like to continue (y/n)? ')
                                    if yN.upper() == 'Y':
                                        updateChoice = 'y'
                                        continue
                                    elif yN.upper() == 'N':
                                        print("Your details has been updated. Thank you")
                                        updating = False
                                        searching = False
                                        break
                                else:
                                    print("Error please try again")
                                    continue
                            if update == '4':
                                C = input('Please enter the Cost per Person you would like to update to: ')
                                if C.isnumeric():
                                    records[i]['cost'] = C
                                    yN = input('Cost has been updated, would you like to continue (y/n)? ')
                                    if yN.upper() == 'Y':
                                        updateChoice = 'y'
                                        continue
                                    elif yN.upper() == 'N':
                                        print("Your details has been updated. Thank you")
                                        updating = False
                                        searching = False
                                        break
                                else:
                                    print("Error please try again")
                                    continue
                            else:
                                print("Please enter a valid value")
                        elif updateChoice.upper() == 'N':
                            print("Thank you!")
                            searching = False
                            break
                        else:
                            print("Please enter a valid choice.")
                            updateChoice = input("Would you like to update your details (y/n)? ")

            if recordsfound == False:
                print("Record for customer name: '{0}' not found. Please try again or press x to go back.".format(target))

def binarySearch():
    searching = True
    updating = True
    pNewList = []
    while searching:
        target = input("Search Package name or press x to go back: ")
        target = target.capitalize()
        pNamelist = []
        SearchedResult = False
        for x in range(len(records)):
            if records[x]['Package Name'] == target:
                pNamelist.append(records[x]['Package Name'])
        length = len(pNamelist)
        if target == 'X':
            searching = False
            updating = False
        else:
            #recordsFound = True
            low = 0
            high = len(pNamelist) - 1
            while low <= high:
                # Find the midpoint of the sequence
                mid = (high + low) // 2
                # Does the midpoint contain the target?
                # If yes, return midpoint (i.e. index of the list)
                if pNamelist[mid] == target:
                    SearchedResult = True
                    print("Here are the records found for {0}:".format(target))
                    for i in range(length):
                        for x in range(len(records)):
                            if pNamelist[mid] == records[x]["Package Name"]:
                                pNewList.append(records[x])
                                print("\nPackage Name:", records[x]['Package Name'])
                                print("Customer Name:", records[x]['Customer Name'])
                                print("Number of pax:", records[x]['pax'])
                                print("Package cost Per Person: ${}".format(records[x]['cost']))
                        searching = False
                        break
                    break
                # Or is the target before the midpoint?
                elif target < pNamelist[mid]:
                    high = mid - 1
                # Or is the target after the midpoint?
                elif target > pNamelist[mid]:
                    low = mid + 1
                    searching = False
            # If the sequence cannot be subdivided further,
            # target is not in the list of values
            if SearchedResult == False:
                print("Package Name '{0}' not found, please try again!".format(target))
                continue
            updateChoice = input("Would you like to update your details (y/n)? ")
    while updating:
        if updateChoice.upper() == 'Y':
            check1 = False
            check2 = False
            whichChoice = input("Which record would you like to update (Enter the customer name of the record)? ")
            whichChoice = whichChoice.capitalize()
            for x in range(len(pNewList)):
                if whichChoice == pNewList[x]['Customer Name']:
                    check1 = True
                    check2 = True
            while (check1 == True):
                for i in range(len(records)):
                    if whichChoice == records[i]['Customer Name']:
                        update = input("\n1. Customer Name \n2. Package Name \n3. Number of Pax \n4. Cost per Person \nWhat would you like to update? ")
                        if update == '1':
                            CN = input('Please enter the Customer Name you would like to update to: ')
                            CN = CN.capitalize()
                            records[i]['Customer Name'] = CN
                            yN = input('Customer Name has been updated, would you like to continue (y/n)? ')
                            if yN.upper() == 'Y':
                                whichChoice = CN
                                continue
                            elif yN.upper() == 'N':
                                print("Your details has been updated. Thank you")
                                updating = False
                                searching = False
                                check1 = False
                                break
                        if update == '2':
                            PN = input('Please enter the Package Name you would like to update to: ')
                            PN = PN.capitalize()
                            records[i]['Package Name'] = PN
                            yN = input('Package Name has been updated, would you like to continue (y/n)? ')
                            if yN.upper() == 'Y':
                                whichChoice = records[i]['Customer Name']
                                continue
                            elif yN.upper() == 'N':
                                print("Your details has been updated. Thank you")
                                updating = False
                                searching = False
                                check1 = False
                                break
                        if update == '3':
                            P = input('Please enter the Number of Pax you would like to update to (max 5): ')
                            if P.isnumeric() and P < '6':
                                records[i]['pax'] = P
                                yN = input('Number of Pax has been updated, would you like to continue (y/n)? ')
                                if yN.upper() == 'Y':
                                    whichChoice = records[i]['Customer Name']
                                    continue
                                elif yN.upper() == 'N':
                                    print("Your details has been updated. Thank you")
                                    updating = False
                                    searching = False
                                    check1 = False
                                    break
                            else:
                                print("Error please try again.")
                                continue
                        if update == '4':
                            C = input('Please enter the Cost per Person you would like to update to: ')
                            if C.isnumeric():
                                records[i]['cost'] = C
                                yN = input('Cost has been updated, would you like to continue (y/n)? ')
                                if yN.upper() == 'Y':
                                    whichChoice = records[i]['Customer Name']
                                    continue
                                elif yN.upper() == 'N':
                                    print("Your details has been updated. Thank you")
                                    updating = False
                                    searching = False
                                    check1 = False
                                    break
                            else:
                                print("Error please try again.")
                        else:
                            print("Please enter a valid value")
                            continue
            if(check1 == False and check2 == False):
                print("The customer name does not exist in the package you searched for. Try again!")
                continue
        elif updateChoice.upper() == 'N':
            print("Thank you")
            updating = False
            break
        else:
            print("Please enter a valid value. Try again")
            updateChoice = input("Would you like to update your details (y/n)? ")

def listingrecords():
    cost = []
    checkforrecords = False
    for x in records:
        cost.append(x['cost'])
    cost = list(dict.fromkeys(cost))
    length = len(cost)
    listing = True
    while listing:
        min = input("Please key in the minimum cost: ")
        if min.isdigit():
            min = int(min)
            if min < 0:
                print("Please enter a valid value.")
                continue
            else:
                max = int(input("Please key in the maximum cost: "))
                if max <= 0 or max < min:
                    print("Please enter a valid value")
                    continue
                if max == min:
                    print("Please enter a value more than the minimum value")
                    continue
                else:
                    for c in range(length):
                        for l in range(len(records)):
                            if cost[c] > min and cost[c] < max:
                                checkforrecords = True
                                if cost[c] == records[l]['cost']:
                                    print("\nPackage Name: ", records[l]['Package Name'])
                                    print("Customer Name: ", records[l]['Customer Name'])
                                    print("Pax: ", records[l]['pax'])
                                    print("Cost: ", records[l]['cost'])
                    if(checkforrecords == False):
                        print("There are no records in cost range ${0} to ${1}. Try Again".format(min, max))
                        continue
                    break
        else:
            print("Please key a valid value.")

def shellSort():
    while True:
        option = input("\n1. Customer Name \n2. Package Name \n3. Cost per Pax \n4. Number of Pax \nWhich would you like to sort? ")
        if option == '1':
            interval = len(records) // 2
            while interval > 0:
                for i in range(interval, len(records)):
                    temp = records[i]
                    j = i
                    while j >= interval and records[j - interval]['Customer Name'] > temp['Customer Name']:
                        records[j] = records[j - interval]
                        j -= interval
                    records[j] = temp
                interval //= 2
            print("\nRecords have been sorted by Customer Name. Press 1 to view.")
            break
        if option == '2':
            interval = len(records) // 2
            while interval > 0:
                for i in range(interval, len(records)):
                    temp = records[i]
                    j = i
                    while j >= interval and records[j - interval]['Package Name'] > temp['Package Name']:
                        records[j] = records[j - interval]
                        j -= interval
                    records[j] = temp
                interval //= 2
            print("\nRecords have been sorted by Package Name. Press 1 to view.")
            break
        if option == '3':
            interval = len(records) // 2
            while interval > 0:
                for i in range(interval, len(records)):
                    temp = records[i]
                    j = i
                    while j >= interval and records[j - interval]['cost'] > temp['cost']:
                        records[j] = records[j - interval]
                        j -= interval
                    records[j] = temp
                interval //= 2
            print("\nRecords have been sorted by Cost per Pax. Press 1 to view.")
            break
        if option == '4':
            interval = len(records) // 2
            while interval > 0:
                for i in range(interval, len(records)):
                    temp = records[i]
                    j = i
                    while j >= interval and records[j - interval]['pax'] > temp['pax']:
                        records[j] = records[j - interval]
                        j -= interval
                    records[j] = temp
                interval //= 2
            print("\nRecords have been sorted by Number of Pax. Press 1 to view.")
            break
        else:
            print("Please enter a valid value")
            continue

# pancake sort
# Reverses arr[0..i] */
def flip(records, i):
    start = 0
    while start < i:
        temp = records[start]
        records[start] = records[i]
        records[i] = temp
        start += 1
        i -= 1

# Returns index of the maximum
# element in arr[0..n-1] */
def findMax(records, n):
    mi = 0
    for i in range(0,n):
        if records[i]['cost'] > records[mi]['cost']:
            mi = i
    return mi

# The main function that
# sorts given array
# using flip operations
def pancakeSort(records, n):

    # Start from the complete
    # array and one by one
    # reduce current size
    # by one
    curr_size = n
    while curr_size > 1:
        # Find index of the maximum
        # element in
        # arr[0..curr_size-1]
        mi = findMax(records, curr_size)

        # Move the maximum element
        # to end of current array
        # if it's not already at
        # the end
        if mi != curr_size-1:
            # To move at the end,
            # first move maximum
            # number to beginning
            flip(records, mi)

            # Now move the maximum
            # number to end by
            # reversing current array
            flip(records, curr_size-1)
        curr_size -= 1

    print("\nRecords have been sorted by Package Cost Per Person. Press 1 to view.")
while True:
    displaymenu()
    choice = input("Please choose from the above selection (Q to quit): ")
    choice.upper()
    if choice == '1':
        AllRecords()
        continue
    elif choice == '2':
        BubbleSort()
    elif choice == '3':
        SelectionSort()
    elif choice == '4':
        InsertionSort()
    elif choice == '5':
        sortedLinearSearch()
    elif choice == '6':
        binarySearch()
    elif choice == '7':
        listingrecords()
    elif choice == '8':
        shellSort()
    elif choice == '9':
        n = len(records)
        pancakeSort(records, n)
    elif choice == 'Q' or choice == 'q':
        print("\nExiting application. Goodbye!")
        break
    else:
        print("Please enter a valid value")


