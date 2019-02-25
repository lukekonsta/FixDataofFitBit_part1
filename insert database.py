import os
import json

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

#variable_previous = 0
counter = 1
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0

f = open("demofile.txt", "a")

connection = mysql.connector.connect(host='localhost',
                             database='users_data',
                             user='root',
                             password='')

mycursor = connection.cursor()

def pause():
    programPause = raw_input("Press the <ENTER> key to continue...")

'''
    For the given path, get the List of all files in the directory tree
'''
def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles


def main():

    dirName = 'C:\Users\user\Desktop\My Folder\PhD\Projects\Placebo\Database\Files';

    # Get the list of all files in directory tree at given path
    listOfFiles = getListOfFiles(dirName)

    # Print the files
    variable_previous = 0

    for elem in listOfFiles:
        print(elem)

        user = elem[elem.index("Files\\") + len("Files\\"):]
        userN = user[:6]
        print("userN")
        print(userN)

        dw = elem[elem.index("fitbit-") + len("fitbit-"):]
        date = dw.replace(".js", "")
        print(date)

        jsonfile=open(elem)
        data=json.load(jsonfile)
        for element in data:
            print(element)
            value = element['value']
            time = element['time']
            variable_previous+=value
            print(variable_previous)
            sql = "INSERT INTO data_info (USER, DATE, TIME, VALUE, FINALDAYSTEPS) VALUES (%s, %s, %s,%s,%s)"
            val = (userN, date, time, variable_previous, 0)
            mycursor.execute(sql, val)
            connection.commit()
            print(mycursor.rowcount, "record inserted.")

        print("total steps ",variable_previous)
        print("change of day")
    
        data = (variable_previous, userN, date)
        #print(data)


        sqlq = "UPDATE data_info SET `FINALDAYSTEPS`= %s  WHERE USER = %s AND DATE = %s"
        mycursor.execute(sqlq,data)
        connection.commit()
        global counter
        print("DID THE UPDATE")
        #time.sleep(10)

        #mycursor.execute("SELECT DISTINCT (TIME) FROM newtable")

        if(variable_previous>0 and variable_previous < 1000):

            if(one<counter):
                global one
                mycursor.execute(sqlq,data)
                connection.commit()
                variable_previous = 0
                one = one+1
                print("ONE:))))))")

            else:
                data = (userN,date)
                sql1 = "DELETE FROM `data_info` WHERE USER = %s AND DATE = %s"
                mycursor.execute(sql1,data)
                connection.commit()
                

        elif(variable_previous>1000 and variable_previous < 2000):
            global two
            if(two<counter):
                mycursor.execute(sqlq,data)
                connection.commit()
                variable_previous = 0
                two = two+ 1
                print("TWO:))))))")
                
            else:
                data = (userN,date)
                sql1 = "DELETE FROM `data_info` WHERE USER = %s AND DATE = %s"
                mycursor.execute(sql1,data)
                connection.commit()
                
        elif(variable_previous>2000 and variable_previous < 3000):
            global three
            if(three<counter):
                mycursor.execute(sqlq,data)
                connection.commit()
                variable_previous = 0
                three = three +1
                print("THREE:))))))")
                
            else:
                data = (userN,date)
                sql1 = "DELETE FROM `data_info` WHERE USER = %s AND DATE = %s"
                mycursor.execute(sql1,data)
                connection.commit()
                
        elif(variable_previous>3000 and variable_previous < 4000):
            global four
            if(four<counter):
                mycursor.execute(sqlq,data)
                connection.commit()
                variable_previous = 0
                four = four +1
                print("FOUR:))))))")
                
            else:
                data = (userN,date)
                print("deleting", data)
                sql1 = "DELETE FROM `data_info` WHERE USER = %s AND DATE = %s"
                mycursor.execute(sql1,data)
                connection.commit()
                
        elif(variable_previous>4000 and variable_previous < 5000):
            global five
            if(five<counter):
                mycursor.execute(sqlq,data)
                connection.commit()
                variable_previous = 0
                five = five +1
                print("FIVE:))))))")
                
            else:
                data = (userN,date)
                sql1 = "DELETE FROM `data_info` WHERE USER = %s AND DATE = %s"
                mycursor.execute(sql1,data)
                connection.commit()
                
        elif(variable_previous>5000 and variable_previous < 6000):
            global six
            if(six<counter):
                mycursor.execute(sqlq,data)
                connection.commit()
                variable_previous = 0
                six = six +1
                print("SIX:))))))")
                
            else:
                data = (userN,date)
                sql1 = "DELETE FROM `data_info` WHERE USER = %s AND DATE = %s"
                mycursor.execute(sql1,data)
                connection.commit()
                
        elif(variable_previous>6000 and variable_previous < 7000):
            global seven
            if(seven<counter):
                mycursor.execute(sqlq,data)
                connection.commit()
                variable_previous = 0
                seven = seven +1
                print("SEVEN:))))))")
                
            else:
                data = (userN,date)
                sql1 = "DELETE FROM `data_info` WHERE USER = %s AND DATE = %s"
                mycursor.execute(sql1,data)
                connection.commit()
                
        elif(variable_previous>7000 and variable_previous < 8000):
            global eight
            if(eight<counter):
                mycursor.execute(sqlq,data)
                connection.commit()
                variable_previous = 0
                eight = eight +1
                print("EIGHT:))))))")
                
            else:
                data = (userN,date)
                sql1 = "DELETE FROM `data_info` WHERE USER = %s AND DATE = %s"
                mycursor.execute(sql1,data)
                connection.commit()
                
        elif(variable_previous>8000 and variable_previous < 9000):
            global nine
            if(nine<counter):
                mycursor.execute(sqlq,data)
                connection.commit()
                variable_previous = 0
                nine = nine +1
                print("NINE:))))))")
                
            else:
                data = (userN,date)
                sql1 = "DELETE FROM `data_info` WHERE USER = %s AND DATE = %s"
                mycursor.execute(sql1,data)
                connection.commit()
                
        elif(variable_previous>9000 and variable_previous <10000):
            global ten
            if(ten<counter):
                mycursor.execute(sqlq,data)
                connection.commit()
                variable_previous = 0
                ten = ten +1
                print("TEN:))))))")
                
            else:
                data = (userN,date)
                sql1 = "DELETE FROM `data_info` WHERE USER = %s AND DATE = %s"
                mycursor.execute(sql1,data)
                connection.commit()
        else:
            print("bigger")
            data = (userN,date)
            sql1 = "DELETE FROM `data_info` WHERE USER = %s AND DATE = %s"
            mycursor.execute(sql1,data)
            connection.commit()
                

        
        print(one,two,three,four,five,six,seven,eight,nine,ten)
        #pause()
        variable_previous = 0

        if(one == counter & two == counter & three == counter & four == counter & five == counter & six == counter & seven == counter & eight == counter & nine == counter & ten == counter):
            print(one,two,three,four,five,six,seven,eight,nine,ten)
            sys.exit()

    print ("****************")
    variable_previous = 0



    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]


    # Print the files
    '''for elem in listOfFiles:
        print(elem)'''




if __name__ == '__main__':
    main()
