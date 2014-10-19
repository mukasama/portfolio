import cards

def setup():
    '''
    paramaters: None
    returns a tuple of:    
    - a foundation (a single list to hold completed runs)
    - a tableau (a list of 10 lists, containing 54 cards (all are hidden except
        top cards)
    - a stock contains the remaining 50 cards. Cards from four total decks are used.
    '''
    pass

    
def print_game(fdation,tableau,stock):
    '''
    parameters: a foundation, a tableau and a stock
    returns: Nothing
    prints the game, i.e, print all the info user can see.
    Includes:
        a) print tableau  (Make sure only show those cards which are revealed. For hidden cards, just print "XX".
        b) print foundation (report how many runs have been completed)
        c) print stock  (only need to show how many cards left in stock)
    '''
    pass
    

def reveal_card(tableau, tRow):
    '''
    parameters: a tableau row and a tableau
    returns: Nothing
    reveal the top card of the indicated row
    '''
    pass
    

def check_completion(tableau, fdation, tRow):
    '''
    parameters: a tableau, a foundati
    on, and a tableau row
    returns: Nothing
    checks for a completed run in the given row, adds that completed run to the
    foundation, and prints a message
    '''
    pass

def can_be_connected(card1, card2):
    '''
    parameters: two cards
    return: Boolean
    if the second card has the same suit as the first one, and the rank of card2 is one less than that of card1, return True
    Otherwise, return False
    '''
    pass
    

def move_in_tableau(tableau,num_of_cards,t_row_source_index,t_row_dest_index):
    '''
    parameters: a tableau, number of cards, the source tableau row and the destination tableau row
    returns: Boolean
    moves a certain number of cards from one row to another
    hint: 1. first make sure the cards you are moving are built down by rank and are the same suit
          2. if the dest row is empty, move those cards
             else, make sure the card of tableau[t_row_source_index][-num_of_cards] is one rank lower than the top card of destination row (tableau[t_row_dest_index][-1]),
                     and the suit doesn't matter
             If a single card is moved, if it's rank is one less than the destination card, allow opposing colors
    '''
    pass
        
        
def deal_more_cards(stock,tableau):
    '''
    parameters: a stock and a tableau
    returns: Boolean
    Deal one card to each tableau row if there are no empty rows in the tableau. Otherwise, print an error message.
    For the last deal operation, deal the remaining cards to the first couple rows of tableau.
    returns False if the stock is empty or if there was an empty row. Otherwise, deal cards, and return True
    '''
    pass


def is_winner(fdation):
    '''
    parameters: a fdation
    return: Boolean
    If all of the cards have been successfully ordered and put in the fdation,
    return True
    '''
    pass


def print_rules():
    '''
    parameters: none
    returns: nothing
    prints the rules
    '''
    pass


def show_help():
    '''
    parameters: none
    returns: nothing
    prints the supported commands
    '''
    pass


def play():
    ''' 
    main program. Does error checking on the user input. 
    '''
    pass



play()


        
    

