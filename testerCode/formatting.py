global_range = 1

def format_ranges(values):
    if not values:
        return []

    result = []
    current_range = [values[0]]

    for i in range(1, len(values)):
        if float(values[i]) - float(current_range[-1]) <= global_range:
            current_range.append(values[i])
        else:
            if len(current_range) > 1:
                result.append(current_range[0] + '-' + current_range[-1])
            else:
                result.append(current_range[0])
            current_range = [values[i]]

    if len(current_range) > 1:
        result.append(current_range[0] + '-' + current_range[-1])
    else:
        result.append(current_range[0])

    return result

# Example usage
values = ["1.2", "1.3", "1.4", "1.5", "4.3"]
formatted_ranges = format_ranges(values)
print(formatted_ranges)  # Output: ['1.2-1.5', '4.3']

# Now let's add 4.5 and format the ranges again
values.append("4.5")
formatted_ranges = format_ranges(values)
print(formatted_ranges)  # Output: ['1.2-1.5', '4.3-4.5']
