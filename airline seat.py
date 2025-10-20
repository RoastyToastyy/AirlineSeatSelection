#Aeroplane seating system :D

import random
def class_seat_Selector(clsno):

    if clsno==1:
            while True:
                rowf=int(input("Enter the row from 1-5:"))
                if 1<=rowf<=5:
                    return rowf
                else:
                    print("Invalid value.")
                    continue
    if clsno==2:
        while True:
            rowb=int(input("Enter the row from 6-20:"))
            if 6<=rowb<=20:
                return rowb
            else:
                print("Invalid value.")
                continue
    if clsno==3:
        while True:
            rowe=int(input("Enter the row from 21-50:"))
            if 21<=rowe<=50:
                return rowe
            else:
                print("Invalid value.")
                continue

def class_seat_letter(seat_no):
    while True:
    
        print("W.Window")
        print("M.Middle")
        print("I.Isle")
        letter=input("Choose window,middle or isle seat W/M/I: ")
        if letter.lower()=="w":
            letr=random.choice(["A","F"])
            return letr
        elif letter.lower()=="m":
            letr=random.choice(["B","E"])
            return letr
        elif letter.lower()=="i":
            letr=random.choice(["C","D"])
            return letr
        else:
            print("Invalid choice.")
            continue

def class_select():
    while True:
        print("Let's pick a seat!")
        print("Choose a class: ")
        print("F:First")
        print("B:Buisness")
        print("E:Economy")
        cls=input("Enter the class F/B/E: ")
        clno=0
        if cls.lower()=="f":
            clno=1
            return clno
        elif cls.lower()=="b":
            clno=2
            return clno
        elif cls.lower()=="e":
            clno=3
            return clno
        else:
            print("Invalid class.")
            continue


# Seat matrix initialization: 50 rows, 7 columns (A-G) -> 1 means available, 0 means booked
seat_matrix = [[1 for _ in range(6)] for _ in range(50)]  # 1 is available, 0 is booked

def matrix_seat_plan():
    j = ['A', 'B', 'C', 'D', 'E', 'F']  # Full 7-seat layout (A-G)

    for i in range(50):  # Loop over 50 rows

        row = i + 1  # Row number (1-indexed)
        if row < 10:
            print(f"Row 0{row} : ", end=" ")  # Align row numbers for 1-9
        else:
            print(f"Row {row} : ", end=" ")  # For rows 10-50
        
        for col in range(6):  # Loop over 7 columns (A-G)
            if col==3:
                print("  ", end="D ")
            if seat_matrix[i][col] == 0:  # If the seat is booked
                print("█", end=" ")  # Mark booked seat as a filled block
            else:
                if col == 3:  # Skip the middle seat (D) entirely when printing
                    continue
                print(j[col], end=" ")  # Available seat with its letter (A-C, E-G)
        print()  # Move to the next line for the next row

        
print("Welcome to SwagAirlines! Where only the sigmas are welcome!")
while True:
    
    print("1: Book a seat")
    print("2.Seating plan")
    print("3.Exit")
    opt=int(input("Select an option: "))
    if opt not in [1,2,3]:
        print("Invalid option chosen")
        break
    else:
        #Seat booking
        ##FIX THIS MATRIX FOR SEAT PLAN
        mat=[[],[]]
        if opt==1:
            clsno=class_select() 
            seat_no=class_seat_Selector(clsno)
            seat_letter=class_seat_letter(seat_no)
            print(f"Your seat is {seat_no} {seat_letter}")
            mat=[seat_no,seat_letter]
            # Mark the seat as booked in the seat matrix (0 for booked)
            row_idx = seat_no - 1  # Convert to 0-based index
            seat_idx = ord(seat_letter) - ord('A')  # Convert letter to index (A=0, B=1, etc.)
            seat_matrix[row_idx][seat_idx] = 0  # Mark the seat as booked (X)
            print("Would you like to exit or continue?")
            
            ans=input("Exit:E or Continue:C? ")
            if ans.lower()=="e":
                break
            elif ans.lower()=="c":
                continue      
        #seat plan
        if opt==2:
            matrix_seat_plan()
        if opt==3:
            break