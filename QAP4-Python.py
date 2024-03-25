# Purpose:  One Stop Insurance New Policy Calculator
# Author:   Ardent Pardy
# Date(s):  24-03-24

import random
import math
import datetime
import sys
import QAP4Values as QV
import os.path  

defaults_file = 'Defaults.dat'
prev_claims_file = 'PrevClaims.dat'

if not os.path.isfile(defaults_file):
    with open(defaults_file, 'w') as file:
        file.write('1\n') 

with open(defaults_file, 'r') as file:
    PolicyNum = int(file.readline().strip())
    PolicyNum += 1

prev_claims_file = 'PrevClaims.dat'  # Already defined, no change needed

PrevClaims = []  # Initialize an empty list to store previous claims

# Open the file and read previous claims
with open(prev_claims_file, 'r') as file:
    for line in file:
        claim_data = line.strip().split(',')
        PrevClaims.append({
            "claim_num": claim_data[0],
            "claim_date": claim_data[1],
            "claim_amount": float(claim_data[2])
        })

PREMIUM_COST = 869.00
ADD_CAR_DISC = 0.75
XTR_LBLTY_COST = 130.00
GLSS_CVG_COST = 86.00
LOANER_COST = 58.00
HST_RATE = 0.15
MNTHLY_PYMNT_PROC_FEE = 39.99

with open('Defaults.dat', 'r') as file:
    ClaimNum = int(file.readline().strip())

ClaimTotal=0

while True:
    CustFName = input("\nFirst Name?(END = Quit)").title()
    if CustFName.upper() == "End":
        print("\nThank You. Goodbye.")
        exit()
    elif CustFName == "":
        print("Error - Blank Field")
    else:
        break

while True:
    CustLName = input("\nLast Name?(END = Quit)  ").title()
    if CustLName.upper() == "End":
        print("\nThank You. Goodbye.")
        exit()
    elif CustLName == "":
        print("Error - Blank Field")
    else: 
        break

CustAddr = input("\nAddress?  ").title()

CustCity = input("\nCity?  ").title()

while True:
    CustProv = input("\nProvince?  ").upper()
    if CustProv == "":
        print("Error - Blank Field")
    elif CustProv not in ["AB", "BC", "MB", "NB", "NL", "NS", "ON", "PE", "QC", "SK", "NT", "NU", "YT"]:
            print("\nError - Input Incorrect - Enter Province Abbreviation")
    else: 
        break

while True:
    CustPstCde = input("\nPostal Code?  ").upper()
    if len(CustPstCde) != 6 or not CustPstCde[0].isalpha() or not CustPstCde[1].isdigit() or not CustPstCde[2].isalpha() or not CustPstCde[3].isdigit() or not CustPstCde[4].isalpha() or not CustPstCde[5].isdigit():
        print("\nError - Input Incorrect - Enter Postal Code in X#X#X# format only.")
    else:
        CustPstCode = QV.CustPstCde(CustPstCde)
        break

while True:
    CustPhn=input("\nPhone Number?  ")
    if len(CustPhn) != 10:
        print("\nError - Incorrect Input - 10 Digits only.")
    elif not CustPhn.isdigit():
        print("\nError - Incorrect Input - 10 Digits only.")
    else:
        CustPhn = f"({CustPhn[:3]}) {CustPhn[3:6]}-{CustPhn[6:]}"
        break

while True:
    NumCrsInsd=int(input("\nHow many cars to insure?  "))
    if NumCrsInsd == 1:
        ClaimTotal = PREMIUM_COST
        break
    elif NumCrsInsd > 1:
        ClaimTotal = (NumCrsInsd*PREMIUM_COST*ADD_CAR_DISC)+PREMIUM_COST
        break
    elif NumCrsInsd == 0:
        print("\nMust insure at least one.")
    elif NumCrsInsd.isdigit() != True:
        print("\nResponse should be Numeric.")
    else:
        break

while True:
    XtrLblty=input("\nDo you want extra liability? (Y/N)  ").upper()
    if XtrLblty == "Y":
            ClaimTotal += XTR_LBLTY_COST
            break
    else:
        break

while True:
    GlssCvg=input("\nDo you want glass coverage? (Y/N)  ").upper()
    if GlssCvg == "Y":
            ClaimTotal += GLSS_CVG_COST
            break
    else:
        break

while True:
    Loaner=input("\nDo you want a loaner car? (Y/N)  ").upper()
    if Loaner == "Y":
        LoanDays = int(input("\nFor how many days?  "))
        ClaimTotal += (LOANER_COST*LoanDays)
        break
    else:
        break

while True:
    PymntMthd = input("\nWhat payment structure suits you? (Pay in Full = F; Monthly Payments = M)  ").upper()
    if PymntMthd != "M" and PymntMthd != "F":
        print("\nInvalid Input - Enter F or M only.")
    elif PymntMthd == "M":
        ClaimTotal += MNTHLY_PYMNT_PROC_FEE
        while True:
            DownChoice = input("\nWould you like to make a Down Payment? (Y/N)  ").upper()
            if DownChoice == "Y":
                DownPay = int(input("\nEnter Down Payment Amount:  "))
                ClaimTotal += DownPay
                break
            elif DownChoice == "N":
                break
            else:
                print("\nInvalid Input - Enter Y or N only.")
        break
    elif PymntMthd == "F":
        break
   
ClaimNum += 1

with open(defaults_file, 'w') as file:
    file.write(str(PolicyNum) + '\n')
    file.write(str(ClaimNum))

ClaimTotal += ClaimTotal*HST_RATE

ClaimDate = datetime.datetime.now().strftime('%Y-%m-%d')

ClaimTotalDsp = '${:,.2f}'.format(ClaimTotal)

print("\n=== One Stop Insurance Policy Receipt ===")
print("Policy Number:", PolicyNum)
print("Customer:", CustLName," ", CustFName)
print("Province:", CustProv," ","Postal Code:", CustPstCode)
print("Phone Number:", CustPhn)
print("Number of Cars Insured:", NumCrsInsd)
print("Extra Liability:", "Yes" if XtrLblty == "Y" else "No")
print("Glass Coverage:", "Yes" if GlssCvg == "Y" else "No")
print("Loaner Car:", "Yes" if Loaner == "Y" else "No")
print("Payment Method:", "Monthly" if PymntMthd == "M" else "Full")

print("\nPrevious Claims:")
print("---------------------------------")
print("Claim #  Claim Date        Amount")
print("---------------------------------")
for claim in PrevClaims:
    print("{:<8} {:<16} {:>10}".format(claim["claim_num"], claim["claim_date"], '${:,.2f}'.format(claim["claim_amount"])))

print("\nTotal Insurance Premium:", '${:,.2f}'.format(ClaimTotal))
print("\nPolicy data has been saved. Next policy number:", PolicyNum + 1)
