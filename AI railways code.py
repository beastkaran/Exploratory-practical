# Initialize an empty list to store train records
train_records = []

# Function to add a new train record
def add_train():
    train_number = int(input("Enter Train Number: "))
    train_name = input("Enter Train Name: ")
    fare = float(input("Enter Fare: "))
    starting_point = input("Enter Starting Point: ")
    destination = input("Enter Destination: ")
    
    train = {
        "Train Number": train_number,
        "Train Name": train_name,
        "Fare": fare,
        "Starting Point": starting_point,
        "Destination": destination
    }
    
    train_records.append(train)
    print("Train details added successfully!")

# Function to display all train records
def display_trains():
    if not train_records:
        print("No train records available.")
    else:
        print("\nTrain Records:\n")
        for index, train in enumerate(train_records, start=1):
            print(f"Train {index}:")
            for key, value in train.items():
                print(f"{key}: {value}")
            print("\n")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add Train")
    print("2. Display Trains")
    print("3. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_train()
    elif choice == "2":
        display_trains()
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
