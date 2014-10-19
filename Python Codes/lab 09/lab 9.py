import cards


def cont_prompt():
    print("Enter:")
    print("'c' - to continue & press enter")
    print("'q' - to quit & press enter")
    user = input("")
    return user


def war(player1_card_nums, prompt1, player2_card_nums, prompt2):
    player1_card = player1_card_nums[0]
    player2_card = player2_card_nums[0]
    print()
    print(prompt1, "plays", player1_card)
    print()
    print(prompt2, "plays", player2_card)
    print()
    if player1_card > player2_card:
        print()
        print(prompt1, "wins this round")
        print()
        player1_card_nums.extend((player1_card, player2_card))
        player1_card_nums.remove(player1_card)
        player2_card_nums.remove(player2_card)
    if player2_card > player1_card:
        print(prompt2, "wins this round")
        print()
        player2_card_nums.extend((player1_card, player2_card))
        player2_card_nums.remove(player2_card)
        player1_card_nums.remove(player1_card)
    if player1_card == player2_card:
        print("It's a tie!")
        print()
        player1_card_nums.remove(player1_card)
        player1_card_nums.append(player1_card)
        player2_card_nums.remove(player2_card)
        player2_card_nums.append(player2_card)
    if len(player1_card_nums)==0:
        print(prompt2, "won the game!")
        print()
    if len(player2_card_nums)==0:
        print(prompt1, "won the game!")
        print()
    print(prompt1, player1_card_nums)
    print()
    print(prompt2, player2_card_nums)


def main():
    print()
    prompt1=input("Enter first player's name:")
    print()
    prompt2=input("Enter second player's name:")

    aDeck = cards.Deck()
    aDeck.shuffle()

    player1 = [aDeck.deal() for i in range (26)]
    player1_card_nums = []
    for card in player1:
        value = card.get_rank()
        player1_card_nums.append(value)
    print()
    print(prompt1, player1_card_nums)

    aDeck.shuffle()
    player2= [aDeck.deal() for i in range (26)]
    player2_card_nums = []
    for card in player2:
        value = card.get_rank()
        player2_card_nums.append(value)
    print()
    print(prompt2, player2_card_nums)
    print()

    while True:
        war(player1_card_nums, prompt1, player2_card_nums, prompt2)
        response = cont_prompt()
        if response == "q":
            break

main()
