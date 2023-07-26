# Program to enter and calculate new insurance policy
# information for the One Stop Insurance Company.
#Program Written on July 21, 2023
#Program Written by: Ashley Colbert

# Import Libraries

import datetime
CurrDate = datetime.datetime.now()
import FormatValues as FV

# Open Defaults and read the constants stored there:

f = open('OSICDef.dat', 'r')
NEXT_POL_NUM = int(f.readline())
BASIC_PREMIUM = float(f.readline())
DISC_ADD_CAR = float(f.readline())
EX_LIA_COST = float(f.readline())
COST_GLASS_COVER = float(f.readline())
COST_LOAN_CAR = float(f.readline())
HST_RATE = float(f.readline())
PROCESS_FEE = float(f.readline())
f.close()

# Functions

# Main Program

while True:
    custName = input("Enter the customer's first and last name(enter End to exit): ").title()
    if custName == "End":
        break

    custAdd = input("Enter the customer's address: ").title()
    custCity = input("Enter the customer's city: ").title()
    provList = ["AB", "BC", "MB", "NB", "NL", "NT", "NS", "NU", "ON", "PE", "QC", "SK", "YT"]
    while True:
        custProv = input("Enter the customer's province(XX): ").upper()
        if custProv not in provList:
            print("Error - must be valid province")
        else:
            break

    custPC = input("Enter the customer's postal code(X#X #X#): ").upper()
    custPhone = input("Enter the customer's phone number(###-###-####): ")
    numCars = int(input("Enter the number of cars being insured: "))
    exLiaLst = ["Y", "N"]
    while True:
        exLia = input("Was extra liability chosen?(Y/N): ").upper()
        if exLia not in exLiaLst:
            print("Error - please enter Y or N only")
        else:
            break
    glassCovLst = ["Y", "N"]
    while True:
        glassCov = input("Was glass coverage chosen?(Y/N): ").upper()
        if glassCov not in glassCovLst:
            print("Error - please enter Y or N only")
        else:
            break
    loanCarLst = ["Y", "N"]
    while True:
        loanCar = input("Was loaner car option chosen:(Y/N): ").upper()
        if loanCar not in loanCarLst:
            print("Error - please enter Y or N only")
        else:
            break
    payList = ["Full", "Monthly"]
    while True:
        payType = input("How will payment be made? (Full/Monthly): ").title()
        if payType not in payList:
            print("Error - enter Full or Monthly only")
        else:
            break
    print()

# Calculations

    payDate = CurrDate + datetime.timedelta(days=30)

    if numCars == 1:
        insPrem = BASIC_PREMIUM
    else:
        insPrem = BASIC_PREMIUM + (numCars - 1) * (BASIC_PREMIUM - (BASIC_PREMIUM * DISC_ADD_CAR))

    if exLia == "Y":
        exLiaCost = EX_LIA_COST
        exLia = "Yes"
    else:
        exLiaCost = 0
        exLia = "No"

    if glassCov == "Y":
        glassCovCost = COST_GLASS_COVER
        glassCov = "Yes"
    else:
        glassCovCost = 0
        glassCov = "No"

    if loanCar == "Y":
        loanCarCost = COST_LOAN_CAR
        loanCar = "Yes"
    else:
        loanCarCost = 0
        loanCar = "No"

    totExCost = exLiaCost + glassCovCost + loanCarCost

    totInsPrem = insPrem + totExCost

    HST = totInsPrem * HST_RATE

    totalCost = HST + totInsPrem

    if payType == "Full":
        monPayment = totalCost
        payDate = CurrDate
    else:
        monPayment = (PROCESS_FEE + totalCost)/8

# Receipt
    print()
    print()
    print("--------------------------------------------------------------")
    print("                  One Stop Insurance Company")
    print("                      Customer Receipt")
    print("--------------------------------------------------------------")
    print(f"Policy Number: {NEXT_POL_NUM:<5d}                      {FV.FDateN(CurrDate):>20s}")
    print()
    print(f"Customer: {custName:<15s}")
    print(f"          {custAdd:<15s}")
    print(f"          {custCity:<10s}, {custProv:<2s}")
    print(f"          {custPC:<7s}                   Phone Number: {custPhone:>12s}")
    print()
    print(f"Number of cars insured: {numCars}")
    print(f"Extra liability: {exLia}")
    print(f"Optional glass coverage: {glassCov}")
    print(f"Optional loaner car: {loanCar}")
    print()
    print(f"Insurance premium:                                   ${FV.FComma2(insPrem):>8s}")
    print(f"Extra liability cost:                                ${FV.FComma2(exLiaCost):>8s}")
    print(f"Optional glass cover cost:                           ${FV.FComma2(glassCovCost):>8s}")
    print(f"Optional loaner car cost:                            ${FV.FComma2(loanCarCost):>8s}")
    print(f"Total extra costs:                                   ${FV.FComma2(totExCost):>8s}")
    print(f"Total insurance premium:                             ${FV.FComma2(totInsPrem):>8s}")
    print(f"HST:                                                 ${FV.FComma2(HST):>8s}")
    print("--------------------------------------------------------------")
    print(f"Total Cost:                                          ${FV.FComma2(totalCost):>8s}")
    print(f"Payment option: {payType}")
    print(f"Payment date: {FV.FDateN(payDate):<16s}       Payment amount: ${FV.FComma2(monPayment):>8s}")
    print("--------------------------------------------------------------")
    print("      Thank you for choosing One Stop Insurance Company")
    print()
    print()



    import time
    from tqdm import tqdm

    print()
    print()
    print("Saving data...")
    print()

# Processing bar
    for _ in tqdm(range(20), desc="Processing", unit="ticks", ncols=100, bar_format="{desc}  {bar}"):
        time.sleep(.1)

    f = open("Policies.dat", "a")
    f.write(f"{NEXT_POL_NUM}, ")
    f.write(f"{CurrDate}, ")
    f.write(f"{custName}, ")
    f.write(f"{custAdd}, ")
    f.write(f"{custCity}, ")
    f.write(f"{custProv}, ")
    f.write(f"{custPC}, ")
    f.write(f"{custPhone}, ")
    f.write(f"{numCars}, ")
    f.write(f"{exLia}, ")
    f.write(f"{glassCov}, ")
    f.write(f"{loanCar}, ")
    f.write(f"{payType}, ")
    f.write(f"{monPayment}\n")
    f.close()
    print("Policy Information processed and saved.")
    print()
    print()

# HouseKeeping

    NEXT_POL_NUM += 1

    f = open('OSICDef.dat', 'w')
    f.write(f"{NEXT_POL_NUM}\n")
    f.write(f"{BASIC_PREMIUM}\n")
    f.write(f"{DISC_ADD_CAR}\n")
    f.write(f"{EX_LIA_COST}\n")
    f.write(f"{COST_GLASS_COVER}\n")
    f.write(f"{COST_LOAN_CAR}\n")
    f.write(f"{HST_RATE}\n")
    f.write(f"{PROCESS_FEE}\n")
    f.close()