"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*number_of_wagon):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(number_of_wagon)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    a, b, c, *part_of_id = each_wagons_id
    print(a, b, c, part_of_id)
    fix_list = c, *missing_wagons, *part_of_id, a, b

    return list(fix_list)


def add_missing_stops(route: dict, **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    lst_stops = []
    for value in stops.values():
        lst_stops.append(value)
    route["stops"] = lst_stops

    return route
        

def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    extend_info = {**route, **more_route_information}
    return extend_info


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    pass
    # a, *rest = zip(*wagons_rows)
    # print(list(rest))


# task_1
# print(get_list_of_wagons(1, 7, 12, 3, 14, 8, 5)) 
# output: [1, 7, 12, 3, 14, 8, 5]

# task_2
# print(fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15]))  
# output: [1, 3, 17, 6, 15, 7, 4, 12, 6, 3, 13, 2, 5]

# taks_3
# print(add_missing_stops({"from": "New York", "to": "Miami"},
#                       stop_1="Washington, DC", stop_2="Charlotte", stop_3="Atlanta",
#                       stop_4="Jacksonville", stop_5="Orlando"))
# output: {"from": "New York", "to": "Miami", "stops": ["Washington, DC", "Charlotte", "Atlanta", "Jacksonville", "Orlando"]}

# task_4
# print(extend_route_information({"from": "Berlin", "to": "Hamburg"}, {"length": "100", "speed": "50"}))
# output: {"from": "Berlin", "to": "Hamburg", "length": "100", "speed": "50"}

# task_6
fix_wagon_depot([
                [(2, "red"), (4, "red"), (8, "red")],
                [(5, "blue"), (9, "blue"), (13,"blue")],
                [(3, "orange"), (7, "orange"), (11, "orange")],
                ])

# [
# [(2, "red"), (5, "blue"), (3, "orange")],
# [(4, "red"), (9, "blue"), (7, "orange")],
# [(8, "red"), (13,"blue"), (11, "orange")]
# ]