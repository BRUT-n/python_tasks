# def abbreviate(words):
#     spliting = words.replace("-"," ").replace("_", " ").split()
#     acronym = ""
#     for ch in spliting:
#         item_to_add = ch[0]
#         if ch.isalpha:
#             acronym += item_to_add.title()
#     return acronym


# def abbreviate(words):
#     collect_chars = ""
#     acronym = ""
#     for ch in words:
#         if ch.isalpha() or ch.isspace() or ch == "'":
#             collect_chars += ch
#         else:
#             collect_chars += " "
#     spliting = collect_chars.split()
#     for ch in spliting:
#         acronym += ch[0].upper()
#     return acronym

def abbreviate(words):
    spliting = words.replace("-"," ").replace("_", " ").split()
    return "".join(ch[0].upper() for ch in spliting)

