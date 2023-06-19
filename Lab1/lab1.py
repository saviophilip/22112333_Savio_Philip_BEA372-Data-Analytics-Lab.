

#counting marital status 
def count_marital_status(data):
    married_count = 0
    single_count = 0
    divorced_count = 0
    
    for i in data:
        col = i.split(';')
        marital = col[2].strip('"')
        if marital == 'married':
            married_count += 1
        elif marital == 'single':
            single_count += 1
        elif marital == 'divorced':
            divorced_count += 1
            
    print("Marital Categories:")
    print("Married:", married_count)
    print("Single:", single_count)
    print("Divorced:", divorced_count)

#Creating Histogram 
def create_age_histogram(data):
    age_count = {}
    
    for i in data:
        col = i.split(';')
        age = int(col[0])  # Assuming age column is at index 0, adjust if necessary
        if age in age_count:
            age_count[age] += 1
        else:
            age_count[age] = 1
    
    print("Age Histogram:")
    for age, count in age_count.items():
        print(f"{age}: {'=' * count}")


file = open("/Users/saviophilip/Documents/GitHub/22112333_Savio_Philip_BEA372-Data-Analytics-Lab/Lab1/bank.csv", 'r')
header = file.readline()
data = file.readlines()

def menu():
    while True:
        print("Choose any:")
        print("1. Count Marital Status")
        print("2. Create Age Histogram")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            count_marital_status(data)
        elif choice == '2':
            create_age_histogram(data)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

menu()