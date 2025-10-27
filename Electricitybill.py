# Electricity bill
import sys
PastReading = int(sys.argv[1])
PresentReading = int(sys.argv[2])
Total_units = PresentReading - PastReading
print("Total Units:", Total_units)

eBill = 0

if Total_units > 500 :
    eBill = Total_units * 10
    print(f"Your electricity Bill is: Rs.{eBill}")
elif Total_units > 400 and Total_units <= 500:
    eBill = Total_units * 8
    print(f"Your electricity Bill is: Rs.{eBill}")
elif Total_units > 300 and Total_units <= 400:
    eBill = Total_units * 6
    print(f"Your electricity Bill is: Rs.{eBill}")
elif Total_units > 200 and Total_units <= 300:
    eBill = Total_units * 4
    print(f"Your electricity Bill is: Rs.{eBill}")
elif Total_units > 75 and Total_units <= 200:
    eBill = Total_units * 2
    print(f"Your electricity Bill is: Rs.{eBill}")
elif Total_units >= 0 and Total_units <= 75:
    eBill = Total_units * 0
    print(f"Your electricity Bill is: Rs.{eBill}")

    