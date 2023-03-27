from typing import List

freezing_point = 0
boiling_point = 100
FILENAME = "todos.txt"

if __name__ == "__main__":
    print("Executing the functions directly!")


def water_state(temperature):
    """Use an integer as a parameter and return a string designating
    the state that woter would be in at that temperature."""
    if temperature <= freezing_point:
        w_state = "solid"
    elif freezing_point < temperature < boiling_point:
        w_state = "liquid"
    else:
        w_state = "gas"
    return w_state


def getint(prompt):
    """Use string parameter to ask the user to enter an integer. If the
    user enters a valid string, convert it to an integer and return it.
    If the user does not enter a string that represents an integer, return -1.
    """
    answer_string = input(prompt)
    if str.isdigit(answer_string):
        return_code = True
        answer_int = int(answer_string)
    else:
        print(f"Sorry, {answer_string} is not valid.")
        return_code = False
        answer_int = -1

    return([return_code, answer_int])


def get_list(filename=FILENAME):
    """Read the contents of a text file and return each
    line as an item in a list."""
    file = open(filename, 'r')
    listvar: list[str] = file.readlines()
    file.close()
    return listvar

def put_list(listvar, filename=FILENAME):
    """Write a list of strings to a file. Each item in
    the list must end with and End-of-Line character."""
    file = open(filename, 'w')
    file.writelines(listvar)
    file.close()


def get_age(creation_year, current_year = 2023):
    """Calculate the age of something given the year it was created.
    Note: The current year is defaulted to 2023, the year this module was written."""
    age = current_year - creation_year
    return age


