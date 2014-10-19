                                                    # Section 09 
                                                    # 11/ 12/ 2012 
                                                    # Project 08

# This game plays 2-suit spider solitaire. The aim of this game is to  sort all the cards into “runs” of
# cards. A completed run has cards from the same suit and are in descending order from King down to Ace.
# Once a run has been completed, it should automatically be placed in the foundation. Once the foundation
# contains all the cards, the game has been won.

# I would like to also acknowledge Dr. Dillon and Prof. Enbody for providing us with the functions (proj08Skel)
# used in this program that helped me create this game.

import cards


def setup():
# The setup function returns returns a tuple of a foundation (a single list to hold completed runs)
# a tableau (a list of 10 lists, containing 54 cards (all are hidden except top cards and a stock that
#contains the remaining 50 cards. Cards from four total decks are used.
    
    empty_deck=[]
    aDeck=[]

    for a in range(4):
        aDeck=cards.Deck()
        aDeck.shuffle()
        for b in range(52):
            card=aDeck.deal()
            card.set_hidden()
            if card.get_suit()== "H" or card.get_suit()=="S":
                empty_deck.append(card)
        
    tableau = []
    # A tableau is list of 10 lists, containing 54 cards (all are hidden except top cards).
    docks_list = []    
    # Docks_list creats all the 10 rows for the game play with the assigned cards when shurfled.
    
    for c in range(4):
        docks_list = []
        for d in range(6):
            card=empty_deck.pop()
            docks_list.append(card)
        tableau.append(docks_list)

    for e in range(6):
        docks_list=[]
        for f in range(5):
            card=empty_deck.pop()
            docks_list.append(card)
        tableau.append(docks_list)

    fdation=[]
    # A fdation is a single list to hold completed runs.
    stock=empty_deck
    # Stock contains the remaining 50 cards. Cards from four total decks are used.
    for row in tableau:
        row[-1].show_card()
    return fdation,tableau,stock


def move_to_stock(tableau,stock,tRow):
    if len(stock[tRow]) != 0:
        print ('invalid move')
        return False
    else:
        stock[tRow].append(tableau[tRow].pop())
        return True


def print_game(fdation,tableau,stock):
# The print_game function return nothing, it just prints all the information a user can see. This
# Information includes print tableau(Make sure only show those cards which are revealed and for the
# hidden cards, just print "XX". It prints foundation (report how many runs have been completed) and
# also prints the stock (only need to show how many cards left in stock)

    print('Foundation:0/8 runs completed')
    print()
    print('Stock: 50 cards remaining')
    print()

    for g in range(10):
        
        Row='Row'+str(g+1)
        print(Row,tableau[g])
        
    pass
    

def reveal_card(tableau, tRow):
# This function has no return it just reveals the top card of the indicated row.

    tableau[tRow][-1].set_hidden(False)
    
    pass
    

def check_completion(tableau, fdation, tRow):
# This function has no return it just ches for a completed run in the given row, adds that completed
# run to the foundation and prints a message.

    highest_rank=1
    for card in tableau[tRow]:
        if card.get_rank()==highest_rank:
            if highest_rank==13:
                fdation.extend(tableau[tRow][-13:])
                tableau[tRow]=tableau[tRow][:-13]
            highest_rank+=1
        else:
            break              

        pass


def can_be_connected(card1, card2):
# The can_be_connected function returns a Boolean, this means if the second card has the same suit as
# the first one, and the rank of card2 is one less than that of card1, return True Otherwise, return False.

    if card1.get_rank() + 1 == card2.get_rank():
        return True

    else:
        return False

    pass


def move_to_fdation(tableau,fdation, tRow):
    if len(fdation[tRow]) == 0 :  #foundation is empty
        if tableau[tRow][-1].get_rank() == 1: #card is ace
            fdation[tRow].append(tableau[tRow].pop())
        else:
            print ('invalid move') 
            return False
    

def move_in_tableau(tableau,num_of_cards, t_row_source_index, t_row_dest_index):
# The move_in_tableau function also returns a boolean only that this time it moves a certain number of cards
# from one row to another.
      
    card=tableau[t_row_source_index][-num_of_cards:]
    if can_be_connected(card[0], tableau[t_row_dest_index][-1]):
        tableau[t_row_dest_index].extend(card)
        for item in card:
          tableau[t_row_source_index].remove(item)
    else:
        print()
        print ('''*** Cannot Perform Move, The score card must be one lower
than the destination card.****''')
        print()
    reveal_card(tableau,t_row_source_index)
        
    pass
        
        
def deal_more_cards(stock,tableau):
# This is yet another function that returns a boolean too, it deals one card to each tableau row if there are
# no empty rows in the tableau otherwise, it prints an error message. For the last deal operation, it deals the
# remaining cards to the first couple rows of tableau. Either returs False if the stock is empty or if there was
# an empty row. If not then it will deal the cards and return True.

    for h in range(10):
        card=stock.pop()
        card.set_hidden(False)
        tableau[h].append(card)

    pass


def is_winner(fdation):
# Is_winner displays a win message once all the cards (104) have been successfully ordered and put in the fdation.

    # Total number of cards is 104 (start off with 52 cars so 52*2=104). 
    if len(fdation) == 104:
        return True
    
    pass


def print_rules():
# Print's out the rules of the game along with which commands the player can choose from.

    print('Rules of Spider Solitaire:')
    print()
    print('''The goal is to move all cards to the foundation. Cards can only be moved
to the foundation if in a completed run of cards (King, Queen, ..., Ace).
A single card in the tableau can be moved to another row if the destination
card is one rank higher than the moving card. Multiple cards can be moved at
once, but all cards within the stack being moved must be in descending order,
and they must all be the same suit. The destination card must also be one
rank higher than the top card of the stack being moved.
    ''')

    print(''' Acceptable commands:
    
    q = quit
    d = deal
    h = help
    m (# of cards) (source row #) (dest row #) =
    move the # of cards from source row to destination row
    ''')
    
    pass


def show_help():
    '''
    parameters: none
    returns: nothing
    prints the supported commands
    '''
    print("You're choices are: ")
    print()
    print("\t t2f #T #F - move from Tableau to Foundation")
    print("\t t2t #T1 #T2 - move card from one Tableau Stock to another")
    print("\t t2s #T #S - move from Tableau to Stock")
    print("\t s2t #S #T - move from Stock to Tableau")
    print("\t s2f #S #F - move from Stock to Foundation")
    print("\t 'h' for help")
    print("\t 'q' to quit")

    print('''
    Acceptable commands:
    
        q = quit
        d = deal
        h = help
        m (# of cards) (source row #) (dest row #) =
        move the # of cards from source row to destination row
    ''')
    
    pass


def play():
# This is the main function for the game that asks the user where to move next and also does error checking
# on the user inpuput.

    print_rules()
    fdation,tableau,stock = setup()
    
    while True:
        print_game(fdation,tableau,stock)
        print()
        choice = input('What is your move? --> ')
        print()
        
        if 'm' in choice:
            choice=choice.split()
            print(choice)
            move_in_tableau(tableau,int(choice[1]),int(choice[2])-1,int(choice[3])-1)
            check_completion(tableau,fdation,int(choice[3]))
            if is_winner(fdation):
                print('Player Wins!')
                break

        elif choice == 'q':
            print('Thanks for playing')
            break

        elif choice == 'd':
            deal_more_cards(stock,tableau)
    
        elif choice == 'h':
            print()
            show_help()
            print()
            continue    

        pass
    

def play2():
    ''' 
    main program. Does error checking on the user input. 
    '''
    print_rules()
    fdation,tableau,stock = setup()

    while True:
        print_game(fdation,tableau,stock)
        choice = raw_input("Make a choice (type 'h' for help): ")
        choice = choice.strip()
        choice_ans = choice.split()
        if len(choice_ans) > 0:
            x = choice_ans[0]
            if x == 't2f':
                can_be_connected(tableau,fdation,int(choice_ans[1])-1,int(choice_ans[2])-1)
            elif x == 't2t':
                pass
            elif x == 't2s':
                deal_more_cards(tableau,stock,int(choice_ans[1])-1,int(choice_ans[2])-1)
            elif x == 's2t':
                move_in_tableau((tableau,int(choice[1]),int(choice[2])-1),int(choice[3])-1)
            elif x == 's2t':
                pass
            elif x == 'q':
                break
            elif x =='h':
                show_help()
            else:
                print("Unknown Choice:",r)
        else:
            print("Unknown Choice:",choice)
    print("Thanks for playing")
play()
