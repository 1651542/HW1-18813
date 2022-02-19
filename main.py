import mysql.connector
from random import choice

# Initialize database credentials (free online mysql database)
SQL_HOST = "sql11.freemysqlhosting.net"
SQL_USER = "sql11474078"
SQL_PASS = "4lSQadVU5J"
SQL_DB = "sql11474078"

# Function that returns a connection to the database
def connect():
    return mysql.connector.connect(
        host=SQL_HOST,
        user=SQL_USER,
        passwd=SQL_PASS,
        database=SQL_DB
    )


# Function to execute a query and return its result if its a select
def query(query, *args):
    # If the query starts with select, return its output
    if query.upper().startswith("SELECT"):
        return query_return(query, *args)
    
    # Otherwise, connect to the database
    con = connect()
    # Get the cursor
    cursor = con.cursor()
    # Execute the query
    cursor.execute(query, *args)
    # Commit to save the results
    con.commit()
    # Close cursor and connection
    cursor.close()
    con.close()

# Function to execute a query and return its result
def query_return(query, *args):
    # Connect to the database
    con = connect()
    # Get the cursor
    cursor = con.cursor()
    # Execute the query
    cursor.execute(query, *args)
    # Get all the results
    ret = cursor.fetchall()
    # Close cursor and connection
    cursor.close()
    con.close()
    # Return results
    return ret
    

# Function to initialize and create a table with 15 random cars
def init_table():
    # Create table
    query("CREATE TABLE IF NOT EXISTS garage(id INT AUTO_INCREMENT PRIMARY KEY, make TEXT, model TEXT, year TEXT, color TEXT)")
    # Initialize list of colors, makes, models, years
    colors = ["red", "yellow", "green", "blue", "purple"]
    makes = ["toyota", "audi", "ferrari", "bugatti"]
    models = ["A8", "tesla", "mini", "B14"]
    years = ["2022", "2021", "2009", "2001"]
    # Loop 15 times
    for _ in range(15):
        # Pick random color, make, model, year from the lists
        color = choice(colors)
        make = choice(makes)
        model = choice(models)
        year = choice(years)
        # Insert the data in the database
        query("INSERT INTO garage(make, model, year, color) VALUES (%s, %s, %s, %s)", (make, model, year, color))


# Main function to display the menu
def main():
    # Start infinite loop
    while True:
        # Print menu
        print("MENU")
        print("a - Add car")
        print("d - Remove car")
        print("u - Update car details")
        print("r1 - Output all cars sorted by year (ascending)")
        print("r2 - Output all cars of a certain color")
        print("q - Quit")
        # Get user input
        answer = input("> ")
        print()
        # If the answer is 'a'
        if answer == "a":
            # Initialize list of fields to ask
            fields = ["make", "model", "year", "color"]
            # Initialize empty list to store user's answers
            answers = []
            # Loop over all fields
            for field in fields:
                # Ask the user to enter a value and store its answer in the list
                answers.append(input(f"Enter {field}: "))
            # Insert the requested data
            query("INSERT INTO garage(make, model, year, color) VALUES (%s, %s, %s, %s)", answers)
            
        # If the answer is 'd'
        elif answer == "d":
            # Get car id from the user as input
            id = int(input("Enter car id: "))
            # Delete the corresponding car
            query("DELETE FROM garage WHERE id=%s", (id,))
        
        # If the answer is 'u'
        elif answer == "u":
            # Get the car id from the user as input
            id = int(input("Enter car id: "))
            # Initialize list of fields to ask
            fields = ["make", "model", "year", "color"]
            # Initialize empty list to store user's answers
            answers = []
            # Loop over all fields
            for field in fields:
                # Ask the user to enter a value and store its answer in the list
                answers.append(input(f"Enter {field}: "))
            # Update the requested car with the entered data                
            query("UPDATE garage SET make=%s, model=%s, year=%s, color=%s WHERE id=%s", (*answers, id))
        
        # If the answer is 'r1'
        elif answer == "r1":
            # Get the cars sorted by year
            cars = query("SELECT * FROM garage ORDER BY year")
            # Display headers with fixed size
            print(f"{'ID':<5}{'Make':<15}{'Model':<20}{'Year':<10}{'Color':<20}")
            # Loop over all cars
            for id, make, model, year, color in cars:
                # Print the values with the same fixed size
                print(f"{id:<5}{make:<15}{model:<20}{year:<10}{color:<20}")
                
        # If the answer is 'r2'
        elif answer == "r2":
            # Get color from user input
            color = input("Enter color: ")
            # Get the cars
            cars = query("SELECT * FROM garage WHERE color=%s", (color,))
            # Display headers with fixed size
            print(f"{'ID':<5}{'Make':<15}{'Model':<20}{'Year':<10}{'Color':<20}")
            # Loop over all cars
            for id, make, model, year, color in cars:
                # Print the values with the same fixed size
                print(f"{id:<5}{make:<15}{model:<20}{year:<10}{color:<20}")
        
        # If the answer is 'q'
        elif answer == "q":
            # Exit the loop
            break
        
        # Otherwise, print error message
        else:
            print("Invalid option")
            
        print()
            
                
main()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
