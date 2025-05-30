"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    face_cards = 'JQK'
    ace_card = 'A'
    numerical_card = {'2', '3', '4', '5', '6', '7', '8', '9', '10'}
    
    #Переменная numerical_value должна содержать строки, а не числа, чтобы соответствовать типу данных card (который является строкой).
    #Сейчас у вас список чисел, и проверка card in numerical_value всегда будет False, если card - строка (например, "2").

    if card in face_cards:
        return 10
        
    if card in ace_card:
        return 1
        
    if card in numerical_card:
        return int(card)

    return 0
   


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    value_1 = value_of_card(card_one)
    value_2 = value_of_card(card_two)

    if value_1 > value_2:
        return card_one
        
    if value_1 < value_2:
        return card_two
    
    return card_one, card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand) УСЛОВИЕ НЕ ПОНЯЛ!!!
    3.  '2' - '10' = numerical value.
    """
    sum_value = value_of_card(card_one) + value_of_card(card_two)

    if 'A' in (card_one, card_two): # если туз уже в руках, то сразу возвращает 1 (такое условие согласно тестам кода)
        return 1
        
    if sum_value <= 10: # сравнение суммы карт и возврат 11
        return 11
        
    if sum_value > 10: # сравнение суммы карт и возврат 1
        return 1

    return 0


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    card_values = (value_of_card(card_one), value_of_card(card_two))

    return 'A' in (card_one, card_two) and 10 in card_values


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    return value_of_card(card_one) == value_of_card(card_two)



def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    value_double_down = [9, 10, 11]
    sum_of_cards = value_of_card(card_one) + value_of_card(card_two)
    return sum_of_cards in value_double_down
