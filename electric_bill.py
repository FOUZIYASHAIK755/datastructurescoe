def ebill():
    try:
        
        units = float(input("Enter the number of units consumed: "))
        if units < 0:
            print("Units consumed cannot be negative!")
            return
        
    
        if units <= 100:
            bill = units * 1.5
        elif units <= 200:
            bill = 100 * 1.5 + (units - 100) * 2.0
        elif units <= 300:
            bill = 100 * 1.5 + 100 * 2.0 + (units - 200) * 3.0
        else:
            bill = 100 * 1.5 + 100 * 2.0 + 100 * 3.0 + (units - 300) * 5.0
        
        print(f"Total Electricity Bill: Rs {bill:.2f}")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

ebill()
