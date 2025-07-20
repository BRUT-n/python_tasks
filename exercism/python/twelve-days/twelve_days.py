DAYS = ("first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth")
GIFTS = (
        "a Partridge in a Pear Tree.",
        "two Turtle Doves, ",
        "three French Hens, ",
        "four Calling Birds, ",
        "five Gold Rings, ",
        "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ", 
        "eight Maids-a-Milking, ",
        "nine Ladies Dancing, ", 
        "ten Lords-a-Leaping, ",
        "eleven Pipers Piping, ", 
        "twelve Drummers Drumming, "
      )


def recite(start_verse, end_verse):
    lyrics = []
    gifts_from_first_day = []
    index = 0
    while index <= start_verse and index < end_verse:
        gifts_from_first_day.append(GIFTS[index])
        lyrics.append(f"On the {DAYS[index]} day of Christmas my true love gave to me: {"".join(gifts_from_first_day[::-1])}")
        index += 1

    return lyrics


print(recite(3, 3))
'''
            "On the third day of Christmas my true love gave to me: "
            "three French Hens, "
            "two Turtle Doves, "
            "and a Partridge in a Pear Tree."
'''

# def recite(start_verse, end_verse):
#     lyrics = []
#     gifts_from_first_day = []
#     index = 0
#     while start_verse <= end_verse:
#         gifts_from_first_day.append(GIFTS[index])
#         lyrics.append(f"On the {DAYS[index]} day of Christmas my true love gave to me: {"".join(gifts_from_first_day[::-1])}")
#         start_verse += 1
        
#     return lyrics