def slices(series, length):
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if len(series) == 0:
        raise ValueError("series cannot be empty")
    if len(series) < length:
        raise ValueError("slice length cannot be greater than series length")
    # else:
    #     lst_of_values = []
    #     first_i = 0
    #     length_of_series = len(series)
    #     while length <= length_of_series:
    #         lst_of_values.append(series[first_i:length])
    #         first_i += 1
    #         length += 1
    # return lst_of_values
    return [series[i:i+length] for i in range(len(series) - length + 1)]

    '''
    len(series) - length + 1
    длина номера минус длина среза + 1 - дает последний возможный индекс среза:
    9184939_0_4243 - проследний возможный индекс 7, а длина среза 5
    '''