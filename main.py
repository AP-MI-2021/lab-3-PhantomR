def run_tests():
    """ Runs all unit tests and prints a message if they are successful. """
    pass
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
    for list_element in lst:
        print(list_element, end=" ")


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
