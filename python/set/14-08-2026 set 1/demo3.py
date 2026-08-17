'''
3.
=========================================
WEBSITE VISITOR TRACKING SYSTEM
=========================================

A website stores unique visitor IDs.

Menu:
1. Add Visitor
2. Remove Visitor
3. Check Visitor
4. Display All Visitors
5. Count Unique Visitors
6. Clear Visitor Data
7. Exit

Requirements:
- Use a set to store visitor IDs.
- Duplicate visitor IDs should not be stored.
- Use add(), remove(), and membership operations.
'''

visitor = set()
while True:
    print()
    print("=========================================")
    print("     WEBSITE VISITOR TRACKING SYSTEM")
    print("=========================================")
    print("1. Add Visitor")
    print("2. Remove Visitor")
    print("3. Check Visitor")
    print("4. Display All Visitors")
    print("5. Count Unique Visitors")
    print("6. Clear Visitor Data")
    print("7. Exit")

    choice = int(input("Enter your choice: "))
    match choice:

        case 1:
            vis = int(input("Enter no. of visitors to add: "))
            for i in range(vis):
                visit_id = input("Enter Visitor ID: ")
                visitor.add(visit_id)
            print("Visitor added")

        case 2:
            rem = int(input("Enter no. of visitors to remove: "))
            for i in range(rem):
                visit_id = input("Enter Visitor ID: ")
                if visit_id in visitor:
                    visitor.remove(visit_id)
            print("Visitor removed")

        case 3:
            visit_id= input("Enter Visitor ID to check: ")
            if visit_id in visitor:
                print("Visitor found")
            else:
                print("Visitor not found")

        case 4:
            print("All Visitors are:",visitor)

        case 5:
            print("Total Unique Visitors:",len(visitor))

        case 6:
            visitor.clear()
            print("Visitor data cleared.")

        case 7:
            print("End of Program")
            break

        case _:
            print("Invalid choice")