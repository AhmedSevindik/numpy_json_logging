import numpy as  np
import json
import logging

logging.basicConfig(
    filename='logger.log',   
    level=logging.DEBUG,    
    format='%(asctime)s - %(levelname)s - %(message)s'
)
class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
def add_user():
    
    try:
        
        name=input("enter name : ") 
        
        age = int(input("enter age : "))
        
        new_user = User(name,age)
        
        user_data={
            "name":new_user.name,
            "age":new_user.age 
        }   
        
        try:
            with open ("users.json","r") as file:
                
                users=json.load(file)
                
        except:
            
            users=[]
            
        users.append(user_data)
        
        with open ("users.json","w") as file:
            
            json.dump(users ,file, indent= 4)
            
        print("User added")
        
        logging.info(f"User added: {name}")
        
    except ValueError as e:
        logging.error(e)
        print("Age must be number")
        
def analiz_users():
    try:
        with open ("users.json","r") as file:
            
            users=json.load(file)
            
        if len(users)==0:
            
            print("there is no user")
            
            return
        
        
        ages = np.array([user["age"] for user in users])
        names = np.array([user["name"] for user in users])
        
        print("\n--- Age Analyze ---")    
        
        print("Ages : ",ages)

        print("Name : ", names)
        
        print("Avarage : " ,ages.mean())
        
        print("Oldest age : " ,ages.max())
        
        print("Youngest age : " ,ages.min())
        
        print("total user : ", ages.size)
        
        
        logging.info("Analyzed")
        
    except Exception as e:
        
        logging.error(e)
        
        print("Something wrong")
        
def remove_all():
    try:
        with open ("users.json","w") as file:
            json.dump([],file,indent=4)

        print("REMOVED ALL USERS")

        logging.info("REMOVED ALL USERS.")

    except Exception as e:

        logging.exception(e)
        
        print("something wrong about remove function")

def menu ():
    
    while True:
        
        print("\n1 -Add user")
        print("2 - Analyze")
        print("3 - REMOVE ALL")
        print("4 - Exit")
        
        
        choice = input("choice : ")
        
        if(choice=="1"):
            
            add_user()
            
        elif(choice=="2"):
            
            analiz_users()
        
        elif(choice=="3"):
            
            remove_all()
            
        elif(choice=="4"):
            
            print("program ended")
            
            logging.info("program ended")
            
            break
        
        else:
            
            print("Please enter 1,2 or 3")
            
menu()