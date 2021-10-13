from copy import copy
from typing import Callable


def is_divisible_by(number: int, divisor: int) -> bool:
    """
    Tests if a number is divisible by another.
    :param number: int
        The number we want tested.
    :param divisor: int
        The potential divisor.
    :return: bool
        True, if the number is divisible by the divisor. False, otherwise.
    """
    return number % divisor == 0


def has_all_digits_prime(number: int) -> bool:
    """
    Tests whether the given integer's digits are all primes.
    :param number: int
        The given number.
    :return: bool
        True, if all the number's digits are primes. False, otherwise.
    """

    # instead of writing a primality checker, we'll just use a list of the only existing prime digits
    prime_digits = [2, 3, 5, 7]

    if number == 0:
        return False

    # transform the number into its absolute value, if negative
    if number < 0:
        number = -number

    # At each step, check the primality of the number's last digit.
    while number > 0:
        last_digit = number % 10
        if last_digit in prime_digits:
            # last digit is prime, so strip it from the number and continue
            number = number // 10
        else:
            # last digit is not prime, so we can stop
            return False

    return True


def find_longest_subsequence_satisfying_condition(
        lst: list[int], condition_function: Callable[[int], bool]) -> list[int]:
    """
    Finds the longest subsequence in a given list of integers such that each of its elements yield True when
    passed through a given condition function.

    :param lst: list
        The list in which we want to find the longest subsequence.
    :param condition_function: function(int) -> bool
        An int to bool function, representing a test that each member of the subsequence must pass.
    :return: list
        A list containing the longest subsequence satisfying the given condition.
    """

    lst_length = len(lst)
    previous_maximal_subsequence_length = 0
    previous_maximal_subsequence = []
    current_subsequence = []

    for i in range(lst_length):
        if condition_function(lst[i]):
            # current list element satisfies the condition, so add it to temporary subsequence
            current_subsequence.append(lst[i])
        else:
            # current element fails the condition, so we have to end our temporary subsequence
            # and compare its length to the previous maximum length
            current_subsequence_length = len(current_subsequence)
            if current_subsequence_length > previous_maximal_subsequence_length:
                previous_maximal_subsequence_length = current_subsequence_length
                previous_maximal_subsequence = copy(current_subsequence)

            current_subsequence = []

    # we have to compare the current subsequence to the previous maximal one in case
    # the last element tested in the loop above satisfied the condition function
    if len(current_subsequence) > previous_maximal_subsequence_length:
        previous_maximal_subsequence = current_subsequence

    return previous_maximal_subsequence


def test_find_longest_subsequence_satisfying_condition():
    """
    Tests the find_longest_subsequence_satisfying_condition(list[int], Callable[[int], bool]) function.
    """
    assert find_longest_subsequence_satisfying_condition(
        [10, 20, 5, 6, 7, 10, 20, 30, 1, 2, 3, 30], lambda x: is_divisible_by(x, 10)) == \
        [10, 20, 30]

    assert find_longest_subsequence_satisfying_condition(
        [10, 20, 5, 6, 7, 10, 20, 30, 1, 2, 3, 30], lambda x: not is_divisible_by(x, 2)) == \
        [5]

    assert find_longest_subsequence_satisfying_condition(
        [10, 20, 5, 75, 10, 20, 333, 5, 77, 30, 1, 2, 3, 30, 3, 5, 7, 3, 573], has_all_digits_prime) == \
        [3, 5, 7, 3, 573]


def test_is_divisible_by():
    """
    Tests the is_divisible_by(int, int) function.
    """
    assert not is_divisible_by(101, 17)
    assert not is_divisible_by(5, 2)
    assert is_divisible_by(4, 2)
    assert is_divisible_by(1992, 3)
    assert is_divisible_by(0, 1000)


def test_has_all_digits_prime():
    """
    Tests the has_all_digits_prime(int) function.
    """
    assert not has_all_digits_prime(576)
    assert not has_all_digits_prime(100)
    assert has_all_digits_prime(777)
    assert has_all_digits_prime(235)


def run_tests():
    """ Runs all unit tests and prints a message if they are successful. """
    test_is_divisible_by()
    test_has_all_digits_prime()
    test_find_longest_subsequence_satisfying_condition()
    print("\n[TEST] All tests passed, yay!\n")


def ui_process_read_list() -> list[int]:
    """
    Reads a sequence of integers separated by spaces from Standard Input, and converts it
    to a list of integers.

    Returns
    -------
    list[int]:
        The list of integers obtained from converting the user's input.
    """
    user_input = input("Input the elements of the list (integers) separated by spaces: ")
    list_of_strings = user_input.split(' ')
    list_of_ints = [int(element) for element in list_of_strings]
    return list_of_ints


def ui_read_command() -> int:
    """
    Reads an integer, representing a command number, from Standard Input.

    Returns
    -------
    int:
        The command number read.
    """
    return int(input("Please enter a command: "))


def ui_process_display_list(lst: list[int]):
    """
    Displays a list to Standard Output.

    Parameters
    ----------
    lst : list[int]
        The list to display.
    """
    print(lst)


def ui_process_find_longest_subsequence_with_elements_divisible_by(lst: list[int]):
    """
    Reads an integer from Standard Input, then finds the longest subsequence with elements divisible by this integer,
    and finally prints it to Standard Output.

    Parameters
    ----------
    lst : list[int]
        The list in which to find the longest subsequence.
    """
    divisor = int(input("Input the common divisor: "))
    longest_subsequence = find_longest_subsequence_satisfying_condition(lst, lambda x: is_divisible_by(x, divisor))
    ui_process_display_list(longest_subsequence)


def ui_process_find_longest_subsequence_with_elements_having_all_prime_digits(lst: list[int]):
    """
    Reads an integer from Standard Input, then finds the longest subsequence with elements having all prime digits,
    and finally prints it to Standard Output.

    Parameters
    ----------
    lst : list[int]
        The list in which to find the longest subsequence.
    """
    longest_subsequence = find_longest_subsequence_satisfying_condition(lst, has_all_digits_prime)
    ui_process_display_list(longest_subsequence)


def ui_process_find_longest_subsequence_with_even_elements(lst):
    """
    Reads an integer from Standard Input, then finds the longest subsequence with even elements,
    and finally prints it to Standard Output.

    Parameters
    ----------
    lst : list[int]
        The list in which to find the longest subsequence.
    """
    longest_subsequence = find_longest_subsequence_satisfying_condition(lst, lambda x: is_divisible_by(x, 2))
    ui_process_display_list(longest_subsequence)


def ui_process_command(command: int, lst: list[int]) -> (list[int], bool):
    """
    Receives a command number and processes it, eventually using the list lst.
    Returns the (possible modified) list and a bool telling whether an exit command was
    issued or not.

    Parameters
    ----------
    command : int
        The command to process, specified by a number.
    lst : list[int]
        The list used by some of the commands.

    Returns
    -------
    list[int]:
        The (possible modified) list.
    bool:
        True, if the command is an EXIT command; False, otherwise.
    """

    exit_command = False

    if command == 0:
        exit_command = True
    elif command == 1:
        lst = ui_process_read_list()
    elif command == 2:
        ui_process_display_list(lst)
    elif command == 3:
        ui_process_find_longest_subsequence_with_elements_divisible_by(lst)
    elif command == 4:
        ui_process_find_longest_subsequence_with_elements_having_all_prime_digits(lst)
    elif command == 5:
        ui_process_find_longest_subsequence_with_even_elements(lst)
    else:
        print("Invalid command. Please try again.")

    return lst, exit_command


def ui_loop():
    """ Reads and processes commands repeatedly until an EXIT command is received. """
    exit_command_was_received = False
    lst = []
    while not exit_command_was_received:
        ui_show_menu()
        command = ui_read_command()
        lst, exit_command_was_received = ui_process_command(command, lst)


def ui_show_menu():
    """ Displays a menu showing available commands. """
    print()
    print("Available commands:")
    print("--------------------")
    print("1. Read list")
    print("2. Display list")
    print("3. Find the longest subsequence whose elements are all divisible by a given integer")
    print("4. Find the longest subsequence whose elements have all prime digits")
    print("--------------------")
    print("0. EXIT")


def main():
    """ Entry point for the program. """
    run_tests()
    ui_loop()


if __name__ == "__main__":
    main()
