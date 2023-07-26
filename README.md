# QAP-4-Files-AC

main.py 

This is a Python program designed to track new insuraces policies for the fictional company, "One Stop Insurance Company". It allowers the user to input all relevant data and then generates a customer invoice displaying all data in an easy to read format.  The data to be input includes: customer name, phone number, and full address; options for extra liability, glass coverage, or loaner car; and what payment options, either monthly or in full.  If payment is to be made in full, payment will be due on the invoice date, but if monthly payments are choosen, payments will be divided into 8 equal payments, with the first payment being due a month from the invoice date.  Users can input the data for as many customers as necessary, and will be then be required to enter "End" in the customer's name field to break the loop and end the program. All data that is entered into the program is then saved into a data file called, Policies.dat. A data file containing all default values, called OSICDef.dat, is also included in this repository.  This file contains the starting invoice number, and default values for tax rate, discount rate for multiple cars, cost of optional extras, and monthly porcessing fee. Note that after each policy that is entered the policy number in the defualt file will increase by one. An additional file, called, FormatValues.py is also included. This is imported to allow for easy formatting of things suce as dollar amount or dates. 

graph.py 

This is a Python program that allows the user to enters monthly sales revenue for each month.  This data is then used to create a bar graph displaying all the sales numbers for the month.  The python library Matplotlib is imported to aid in the creation of the graph.  
