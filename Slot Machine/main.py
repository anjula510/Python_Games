import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

symbol_value = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}

# columns = [['D', 'D', 'D'], ['D', 'B', 'A'], ['D', 'D', 'C']]
def check_winings(columns, lines, bet, values):
    winings = 0
    wining_lines = []
    for line in range(lines):     # 0,1,2
        symbol = columns[0][line] # A,B,C,D
        for column in columns:    # ['D', 'D', 'D']
            symbol_to_check = column[line] # # A,B,C,D
            if symbol != symbol_to_check:
                break
        else:
            winings += values[symbol] * bet
            wining_lines.append(lines+1)
    
    return winings, wining_lines



def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            # current_symbols = [A2, B4, C6, D8]
            # randomly select a symbol out of current_symbols
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
    
    return columns
        
# columns = [['D', 'D', 'D'], ['D', 'B', 'A'], ['D', 'D', 'C']]
def print_slot_machine(columns):
    for row in range(len(columns[0])):# 3
        for i, column in enumerate(columns):
            # Element at index 0: ['D', 'D', 'D']
            # Element at index 1: ['D', 'B', 'A']
            # Element at index 2: ['D', 'D', 'C']
            if i != len(columns) - 1: #2
                print(column[row], end = ' | ')
                # end= deflaut(\n)
            else:
                print(column[row], end='')
                
        print()
        


## isdigit() method returns True if all characters in the string are digits, otherwise, it returns False.
def deposit():
    while True:
        amount = input('How much are you going to deposite? ($)')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break

            else:
                print('Mount must be greater than 0!')

        else:
            print('Please enter the amount in number!')

    return amount



def get_number_of_lines():
    while True:
        lines = input(f'Enter the number of lines to bet on (1-{MAX_LINES})?')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            
            else:
                print(f'Enter a vailed range between 1 and {MAX_LINES}')
            
        else:
            print('Lines must be in numerical form')
            
    return lines
        

def get_bet():
    while True:
        bet = input('What would you like to bet? ($)')
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            
            else:
                print(f'Bet must be in range {MAX_BET}-{MAX_BET}')
                
        else:
            print('Value must be a number')
        
    return bet



def spin(balance):
    lines = get_number_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet < balance:
            break
        else:
            print(f'Do not have enough money. Your Current balance is ${balance}')
    
    print(f'You are betting ${bet} in {lines} lines. Total bet is ${total_bet}')
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    
    print_slot_machine(slots)
    
    winings, winning_lines = check_winings(slots, lines, bet, symbol_value)
    
    print(f'You won ${winings}. ')
    print(f'You won on lines:', *winning_lines)

    return winings - total_bet


def main():
    balance = deposit()

    while True:
        print(f'Current balance is ${balance}')
        answer = input('Press enter to play and (q to quit)')
        if answer == 'q':
            break
        balance += spin(balance)
        
    print(f'You left with ${balance}')
    
main()