
def median(array):
    array.sort()
    n = len(array)
    if n % 2 == 0:
        return (array[n // 2 - 1] + array[n // 2]) / 2
    else:
        return array[n // 2]
def mean(array):
    return sum(array) / len(array)


def mode(array):
    frequency_dict = {}
    for value in array:
        frequency_dict[value] = frequency_dict.get(value, 0) + 1

    max_frequency = 0
    modes = []
    for key, value in frequency_dict.items():
        if value > max_frequency:
            max_frequency = value
            modes = [key]
        elif value == max_frequency:
            modes.append(key)

    if len(modes) == len(array):
        return "No mode"
    else:
        return modes
def standardDivation(array):
    m = sum(array) / len(array)
    return (sum((xi - m) ** 2 for xi in array) / len(array))**(1/2)
def data(array,boolean):
    temporary = []
    if boolean == True:
        temporary.append("Median")
    temporary.append(median(array))
    if boolean == True:
        temporary.append("Mean")
    temporary.append(mean(array))
    if boolean == True:
        temporary.append("Mode")
    temporary.append(mode(array))
    if boolean == True:
        temporary.append("Standard Divation")
    temporary.append(standardDivation(array))
    return temporary












