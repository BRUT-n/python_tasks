"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    number = int(number)
    seat_letters = ["A", "B", "C", "D"]
    while number >= 1:
        for seat in seat_letters:
            yield seat
            number -= 1
            if number == 0:
                break


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    number = int(number) # кол-во мест
    row_numbers = 0 # нулевой ряд
    seats_letters = ["A", "B", "C", "D"]
    while number >= 1:
        row_numbers += 1
        if row_numbers == 13:
            row_numbers += 1
        for seat in seats_letters:
            yield f"{row_numbers}{seat}"
            number -= 1
            if number == 0:
                break


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    generated_seats = generate_seats(len(passengers))
    names_and_seats = {}
    for name in passengers:
        names_and_seats[name] = next(generated_seats)
    return names_and_seats

    
def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        result = seat + flight_id
        if len(result) < 12:
            result = result + "0" * (12 - len(result))
            yield result


#output tests
#task_1
# letters = generate_seat_letters(4)
# print(next(letters))
# "A"
# print(next(letters))
# "B"

#task_2
# seats = generate_seats(10)
# print(next(seats))
# "1A"
# print(next(seats))
# "1B"

#task_3
# passengers = ['Jerimiah', 'Eric', 'Bethany', 'Byte', 'SqueekyBoots', 'Bob']

# print(assign_seats(passengers))
# {'Jerimiah': '1A', 'Eric': '1B', 'Bethany': '1C', 'Byte': '1D', 'SqueekyBoots': '2A', 'Bob': '2B'}

#task_4
# seat_numbers = ['1A', '17D']
# flight_id = 'CO1234'
# ticket_ids = generate_codes(seat_numbers, flight_id)

# # print(next(ticket_ids))
# '1ACO12340000'
# print(next(ticket_ids))
# '17DCO1234000'