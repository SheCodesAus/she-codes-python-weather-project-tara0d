import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    from datetime import datetime
    # iso_string = "2021-07-05T07:00:00+08:00"
    iso = datetime.fromisoformat(iso_string)
    iso_format = iso.strftime("%A %d %B %Y")

    return iso_format


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    degrees_celsius = (float(temp_in_farenheit) - 32) * 5/9
    rounded_celcius = round(degrees_celsius, 1)
    return rounded_celcius


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    weather_data = [float(item) for item in weather_data]
    mean_calculation = float(sum(weather_data) / len(weather_data))
    return mean_calculation


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    with open (csv_file) as load_data:
        data = csv.reader(load_data)
        next(data)
        data_list = []
        data_b_c = []
        for item in data:
            if not (item):
                continue
            elif (item):
                data_list.append(item)
        for bc in data_list:
            data_b_c.append([bc[0], int(bc[1]), int(bc[2])])
        for item in data_b_c:
            data_list.append(item)
        return data_b_c


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    weather_data = [float(i) for i in weather_data]

    if len(weather_data) == 0:
        return ()
    else:
        min_temp = weather_data[0]
        for n in range(len(weather_data)):
            if weather_data[n] <= min_temp:
                min_temp = weather_data[n]
                min_index = n

    return min_temp, min_index


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    weather_data = [float(i) for i in weather_data]

    if len(weather_data) == 0:
        return ()
    else:
        max_temp = weather_data[0]
        for n in range(len(weather_data)):
            if weather_data[n] >= max_temp:
                max_temp = weather_data[n]
                max_index = n

    return max_temp, max_index


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    min_list = []
    for item in weather_data:
        min_list.append(item[1])
    min_return = find_min(min_list)
    min_f = min_return[0]

    min_index = min_return[1]
    min_date = convert_date(weather_data[min_index][0])
    min_temp = convert_f_to_c(min_f)
    min_temp = format_temperature(convert_f_to_c(min_f))

    max_list = []
    for item in weather_data:
        max_list.append(item[2])
    max_return = find_max(max_list)
    max_f = max_return[0]

    max_index = max_return[1]
    max_date = convert_date(weather_data[max_index][0])
    max_temp = convert_f_to_c(max_f)
    max_temp = format_temperature(convert_f_to_c(max_f))

    min_average = format_temperature(convert_f_to_c(calculate_mean(min_list)))

    max_average = format_temperature(convert_f_to_c(calculate_mean(max_list)))

    overview_days = len(weather_data)
    summary = (f"{overview_days} Day Overview\n  The lowest temperature will be {min_temp}, and will occur on {min_date}.\n  The highest temperature will be {max_temp}, and will occur on {max_date}.\n  The average low this week is {min_average}.\n  The average high this week is {max_average}.\n")
    return summary


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    total_daily_summary = ''
    for row in weather_data:
        day = convert_date(row[0])
        min_temp = format_temperature(convert_f_to_c(row[1]))
        max_temp = format_temperature(convert_f_to_c(row[2]))
        daily_summary = (f"---- {day} ----\n  Minimum Temperature: {min_temp}\n  Maximum Temperature: {max_temp}\n\n")
        total_daily_summary += daily_summary
    return total_daily_summary
