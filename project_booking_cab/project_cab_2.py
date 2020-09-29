
#==============================================================================
#       C A B       B O O K I N G       P R O J E C T
# 
#                  - BY DEWANSH DEV
#
#==============================================================================

from pandas import DataFrame
import pandas as pd 
import sys

import xlrd
import os

#==============================================================================
#           M A I N     F U N C T I O N
#==============================================================================


def main():
    print("==================================================")
    print('\n\t \t \t Cab Booking System \n \t \t')
    print("==================================================")
    print("By Dewansh Dev\n")
    
       
    print("\t \t * M E N U *\n \n 1. Passenger \n\n 2. Cab Driver \n\n 3. Exit\n")
    Type_user = input("Option:")
    if(Type_user == '3'):
        sys.exit()
    
    print("1. Log in \n\n2. Sign up \n\n3. Exit")
    Usertype = input("Option: ")

    if(Type_user == '1'):
        passengerSignIn(Usertype)
    if(Type_user == '2'):
        driverSignIn(Usertype)
    if(Usertype == '3'):
        sys.exit()


#==============================================================================
#           U S E R     S I G N     I N
#==============================================================================

def passengerSignIn(Usertype):
    ''' passenger Login
    '''
    if(Usertype == '1'):
        print("\t \t L O G   I N")
        print('')
        print('PLEASE ENTER FOLLOWING DETAILS:')
        username = input('Username:')
        password = input('Password:')
        testPrint = [username,password]
        print(testPrint)
        Pass_Authentication(username,password)
    elif(Usertype == '2'):
        print("\t \t S I G N    U P")
        print('REGISTER YOURSELF AS NEW USER')
        name = input('Full Name:')
        phone = input('Contact Number:')
        address = input('Address:')
        username = input('Username:')
        password = input('Password:')
        regPassenger = [name, phone, address, username, password]
        print('information submitted' )
        print(regPassenger)
        registerPassenger(name,phone,address,username,password)
        book_cab = input ('Want to booka ride ?\n yes or no :')
        if(book_cab == 'yes'):
            Bookingcab(username)
        else :
            sys.exit()
    elif(Usertype == '3'):
        sys.exit()
    else:
        print('You have entered a wrong value.')

#________DriverSignIn________#

def driverSignIn(Usertype):
    ''' Driver Login
    '''
    if(Usertype == '1'):
        print("\t \t L O G   I N")
        print('')
        print('PLEASE ENTER FOLLOWING DETAILS')
        username = input('Username:')
        password = input('Password:')
        Driv_Authentication(username,password)
    elif(Usertype == '2'):
        print("\t \t S I G N    U P")
        print('REGISTER YOURSELF AS NEW DRIVER')
        name = input('Full Name:')
        phone = input('Contact Number:')
        address = input('Address:')
        carType = input('Car Type:')
        vehicleNumber = input('vehicle Number:')
        username = input('Username:')
        password = input('Password:')
        regdriver = [name,phone,address,carType,vehicleNumber,username,password]
        print('information submitted')
        print(regdriver)
        registerDriver(name,phone,address,carType,vehicleNumber,username,password)
    elif(Usertype == '3'):
        sys.exit()
    else:
        print('wrong information entered')
    #print("Inside driver sign in")

#==============================================================================
#           R E G I S T E R
#==============================================================================

def registerPassenger(name,phone,address,username,password):
    regPassenger = [name, phone, address, username, password]
    
    df = DataFrame([regPassenger], columns = ['Name', 'Phone', 'Address', 'Username', 'Password'])
   
    if(os.path.isfile(r'E:\#1 attain u\github\python-project-devansh-dev-au9\project_booking_cab\Registered Passenger.xlsx')):
        existingData = pd.read_excel(r'E:\#1 attain u\github\python-project-devansh-dev-au9\project_booking_cab\Registered Passenger.xlsx')
        allData = [existingData,df]
        appnd_df = pd.concat(allData)
        appnd_df.to_excel(r'E:\#1 attain u\github\python-project-devansh-dev-au9\project_booking_cab\Registered Passenger.xlsx',index = False, header=True)
    else:
        df.to_excel(r'E:\#1 attain u\github\python-project-devansh-dev-au9\project_booking_cab\Registered Passenger.xlsx',index = False, header=True)
    


def registerDriver(name,phone,address,carType,vehicleNumber, username,password):
    regDriver = [name, phone, address, carType, vehicleNumber, username, password]
    
    df = DataFrame([regDriver], columns = ['Name', 'Phone', 'Address', 'Car Type', 'Vehicle Number', 'Username', 'Password' ])
    if(os.path.isfile(r'E:\#1 attain u\github\python-project-devansh-dev-au9\project_booking_cab\Registered Driver.xlsx')):
        existingData = pd.read_excel(r'E:\#1 attain u\github\python-project-devansh-dev-au9\project_booking_cab\Registered Driver.xlsx')
        allData = [existingData,df]
        appnd_df = pd.concat(allData)
        appnd_df.to_excel(r'E:\#1 attain u\github\python-project-devansh-dev-au9\project_booking_cab\Registered Driver.xlsx',index = False, header=True)
    else:
        df.to_excel(r'E:\#1 attain u\github\python-project-devansh-dev-au9\project_booking_cab\Registered Driver.xlsx',index = False, header=True)
    

  
#==============================================================================
#               A U T H E N T I C A T I O N
#==============================================================================

def Pass_Authentication(username,password):
    print(username, password)
    wb = xlrd.open_workbook(r'E:\#1 attain u\github\python-project-devansh-dev-au9\project_booking_cab\Registered Passenger.xlsx')
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0,0)
    for i in range(sheet.nrows):
        if(sheet.cell_value(i,3) == username and sheet.cell_value(i,4) == password):
            print('Successful Login. \n')
            book_cab = input ('\n Want to booka ride ?\n yes or no :') #____booking___
            if(book_cab == 'yes'):
                Bookingcab(username)
            else :
                sys.exit()


#________Driver_Authentication______#

def Driv_Authentication(username,password):
    
    wb = xlrd.open_workbook(r'E:\#1 attain u\github\python-project-devansh-dev-au9\project_booking_cab\Registered Driver.xlsx')
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0,0)
    for i in range(sheet.nrows):
        if(sheet.cell_value(i,5) == username and sheet.cell_value(i,6) == password):
            print('Successful Login')
            Driver_profile(username)


#==============================================================================
#           D R I V E       P R O F I L E
#==============================================================================

def Driver_profile(username):
    df = pd.read_excel (r'E:\#1 attain u\github\python-project-devansh-dev-au9\project_booking_cab\Registered Driver.xlsx')
    print (df)
    """wb = xlrd.open_workbook("E:\#1 attain u\github\python-project-devansh-dev-au9\project_booking_cab\Cab_Availability.xlsx")
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0,0)
    for i in range(sheet.nrows):
        if(sheet.cell_value(i,5) == username):
            print(i,sheet.row_value(0,i))"""

#==============================================================================
#           U S E R          P R O F I L E
#==============================================================================

#_________BOOKING______#

def Bookingcab(username):

    print('\n Sir/Ma"am , \n', username )
    pickpoint = ''
    print ('____BOOK YOUR RIDE !!____ ')
    print(' \n SELECT DESTINATION :\n')
    #print('No.   cost  drop\n')
    wb = xlrd.open_workbook(r"E:\#1 attain u\github\python-project-devansh-dev-au9\project_booking_cab\Destination_&_cost.xlsx")
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0,0)
    for i in range(sheet.nrows):
        print(i,sheet.cell_value(i,0), sheet.cell_value(i,1))
    locNumber = int(input("\n Select Destination:"))
    for i in range(sheet.nrows):
        if(i == locNumber):
            pickpoint = sheet.cell_value(i,0)

    print('Select cab:')
    df = pd.read_excel (r'E:\#1 attain u\github\python-project-devansh-dev-au9\project_booking_cab\Cab_Availability.xlsx')
    print (df)
    wb = xlrd.open_workbook(r"E:\#1 attain u\github\python-project-devansh-dev-au9\project_booking_cab\Cab_Availability.xlsx")
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0,0)
    for i in range(sheet.nrows):
    
        if(sheet.cell_value(i,5) == pickpoint and sheet.cell_value(i,6) == 'Yes'):
            print(i,sheet.cell_value(i,1),sheet.cell_value(i,2),sheet.cell_value(i,3),sheet.cell_value(i,4))
    choosedCab = int(input('Choose Cab Number:'))
    print('Your Cab is booked succesfully, ENJOY THE RIDE !!')
    End_trip = input ('Want to End ride ? \n yes or no :')
    if(End_trip == 'yes'):
           print('Your Cab ride is Ended succesfully, please pay the amount mention previously on time of your booking !!')
    else :
            sys.exit()





if __name__ == "__main__":
    main()
    
