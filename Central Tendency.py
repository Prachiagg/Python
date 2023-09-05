def calculate_mean(data):
    if len(data) == 0:
        return None
    total = sum(data)
    mean = total / len(data)
    return mean
# mean---------------------

def calculate_median(data):
    if len(data) == 0:
        return None
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        median = sorted_data[n // 2]
    else:
        middle1 = sorted_data[(n - 1) // 2]
        middle2 = sorted_data[n // 2]
        median = (middle1 + middle2) / 2
    return median

# median--------------------------------

def calculate_mode(data):
    if len(data) == 0:
        return None
    frequency_dict = {}
    for value in data:
        if value in frequency_dict:
            frequency_dict[value] += 1
        else:
            frequency_dict[value] = 1
    max_frequency = max(frequency_dict.values())
    mode = [key for key, value in frequency_dict.items() if value == max_frequency]
    return mode

# mode----------------------------------