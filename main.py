# main.py

import dockingBays as db

# Function to print docking bays information
def print_docking_bays():
    print("Docking Bays:")
    for bay in db.docking_bays:
        print(f"Bay {bay['bay_id']} - Size: {bay['size']}, Schedule: {bay['schedule']}")

# Function to print incoming ships information
def print_incoming_ships():
    print("\nIncoming Ships:")
    for ship in db.incoming_ships:
        print(f"Ship {ship['ship_name']} - Size: {ship['size']}, Arrival: {ship['arrival_time']}, Departure: {ship['departure_time']}")
print()
# Main function
def main():
    print_docking_bays()
    print_incoming_ships()
    
    # Level 1
    print("\nShip bays by size: ")
    # Using the For Loop function to print out each list from the docking bay function and from incoming ship function
    for bay in db.docking_bays: 
        for ship in db.incoming_ships:
            # Using the if statement to check which bay id size correspond with which ship sizes
            if bay['size'] == ship['size']:
                # Printing out the list of bay number according to thier sizes
                print(f"Bay {bay['bay_id']}: {ship['ship_name']} - Size: {bay['size']}")
 


    # Level 2
    print("\nShip Time: ")
    # Using the For Loop function to print out each list from the docking bay function and from incoming ship function
    for bay in db.docking_bays:
        for ship in db.incoming_ships:
            # Using the if statement to check which time from ship and from bay corresponds with each other
            if bay['size'] == ship['size']:
                if ship['arrival_time'] or ship['departure_time'] == bay['schedule']:
                # Using the print statement to print out a list of ships 
                    print(f"Bay {bay['bay_id']}, {ship['ship_name']}: Arrives at {ship['arrival_time']}, and Departes at {ship['departure_time']}")

    # Level 3
    print("\nFull bay schedule according to size and time: ")
    for bay in db.docking_bays:
        for ship in db.incoming_ships:
            if bay['size'] == ship['size']:
                if bay['schedule'] == ship['arrival_time'] or ship['departure_time']:
                    print(f"Bay {bay['bay_id']}: {ship['ship_name']}, Arrival: {ship['arrival_time']} - Departure: {ship['departure_time']}")
    
    # Level 4 
    print("\nFull Schedule: ")
    for bay in db.docking_bays:
        for ship in db.incoming_ships:
            if bay['size'] == ship['size']:
                if bay['schedule'] == ship['arrival_time'] or ship['departure_time']:
                    if ship['arrival_time'] == ship['departure_time']:
                        print(f"Bay {bay['bay_id']}: {ship['ship_name']},  Arrives: {ship['arrival_time']} and Departs: {ship['departure_time']}")

    # Bonus 
    print('\nBay Schedule: ')
    for bay in db.docking_bays:
        for ship in db.incoming_ships:
            if bay['size'] == ship['size']:
                print(f"Bay {bay['bay_id']}: {ship['ship_name']} - {ship['arrival_time']} to {ship['departure_time']}")


    # TODO: Implement the docking scheduler logic here
    # Levels 1 to 4 and the bonus can be implemented below

if __name__ == "__main__":
    main()
