import random

#global variables
MAX_LINES = 3  
MAX_BET = 100
MIN_BET = 10

ROWS = 3
COlS = 3

symbol_count = {  #a dictionary for symbols in each reel 
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {  #a dictionary for values of each symbol 
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_wins(columns,lines,bet,values):
    wins = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            wins += values[symbol]*bet
            winning_lines.append(line + 1)
    return wins,winning_lines 



def get_slot_spin (rows,cols,symbols):
    all_symbols = []
    for symbols, symbol_count in symbols.items():
        for _ in range (symbol_count):  #here "_" is an anonyomus variable 
            all_symbols.append(symbols)

    columns =[]
    for _ in range(cols):
        column =[]
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)   
    return columns

def print_slot_symbols(columns):
    for row in range (len(columns[0])): 
        for i , column in enumerate(columns) :
            if i != len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")
        print()

#getting user input like deposit from function
def deposit():
    
    while True: #for checking the amount is sufficient to play 
        amount = input("How much do you want to deposit? $")
        if amount.isdigit(): #isdigit checks if the input is an int 
            amount = int(amount) #if not int then turn into int 
            if amount > 0: #if the amount is greater than 0 then break the loop 
                break
            else:
                print("Amount must be greater than 0.") #if amount less than 0
        else:
            print("Please enter a number.") #if input is not a number 
    return amount

#function for getting lines
def get_number_of_lines():
    while True: 
        lines = input("Enter the number of lines to bet on (1-"+str(MAX_LINES)+ ")? ") 
        if lines.isdigit():  
            lines = int(lines) 
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.") 
        else:
            print("Please enter a number.") 
    return lines

def get_bet():
    while True:
        amount = input("How much do you want to bet on each line ? $")
        if amount.isdigit(): #isdigit checks if the input is an int 
            amount = int(amount) #if not int then turn into int 
            if MIN_BET <= amount <= MAX_BET: 
                break
            else:
                print(f"Amount must be greater than ${MIN_BET}-${MAX_BET}.") #f string is used for embedding string literals
        else:
            print("Please enter a number.") #if input is not a number 
    return amount
 
        
def spin(bal):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        tot_bet = bet*lines

        if tot_bet > bal:
            print("Not Sufficient amount,your current balance is:${bal}")
        else:
            break

    print(f"You are betting ${bet} on {lines}. Total bet is : ${tot_bet}")

    slots = get_slot_spin(ROWS, COlS, symbol_count)
    print_slot_symbols(slots)
    wins,winning_lines = check_wins(slots,lines,bet,symbol_value)
    print(f"YOU WON ${wins}")
    print(f"YOU WON ON LINES: ", *winning_lines)
    return wins - tot_bet
    

def main():
    bal = deposit()
    while True:
        print(f"CURRENT BALANCE IS ${bal}")
        answer = input("PRESS ENTER TO SPIN(q to QUIT).")
        if answer == "q":
            break
        bal += spin(bal)


    print(f"YOU ARE LEFT WITH ${bal}")
    


main()


