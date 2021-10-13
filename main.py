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
    lst : list
        The list to display.
    """
    print(lst)


def ui_process_command(command: int, lst: list[int]) -> (list[int], bool):
    """
    Receives a command number and processes it, eventually using the list lst.
    Returns the (possible modified) list and a bool telling whether an exit command was
    issued or not.

    Parameters
    ----------
    command : int
        The command to process, specified by a number.
    lst : list
        The list used by some of the commands.

    Returns
    -------
    list:
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
    print("--------------------")
    print("0. EXIT")


def main():
    """ Entry point for the program. """
    run_tests()
    ui_loop()


if __name__ == "__main__":
    main()
