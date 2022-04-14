import os 

def showservers():
    os.system("clear")
    print("Your Servers :\n")
    with open(os.path.dirname(os.path.realpath(__file__)) + '/serverlist.txt') as readlist:
        
        serverlist = readlist.readlines()
        li = [x.strip() for x in serverlist]
        amount = len(li)
        readlist.close()

    for i in range(amount):
        print("[",i+1,"]",li[i],"\n")

    print("Choose the Server you wanna connect to:")
    Selection = input()
    connection = li[int(Selection)-1].split("#")[1]
    os.system("clear")
    os.system('ssh ' + connection)    
   


showservers()