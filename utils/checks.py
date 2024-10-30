from typing import Tuple


def spaces_in_words(request_text: str, error_text: str, output_text: str) -> str:
    """
        Checks for whitespace characters in the input string
        :param request_text: Text of the invitation to enter data
        :param error_text: Text to display the error
        :param output_text: Final result text
        :return: Verified inscription without spaces
    """
    while True:
        try:
            user_text = input(f'{request_text} ').strip()
        except KeyboardInterrupt:
            print('\nYou are out of the game')
            exit()
        if ' ' in user_text:
            print(error_text)
        else:
            print(output_text, user_text)
            return user_text


def checking_numbers(welcome_text: str, error_text: str, *args: str) -> tuple[int, ...]:
    while True:
        print(f'{welcome_text} ')
        try:
            nums_tuple = tuple([int(input(f'{num_text} ')) for num_text in args])
            break
        except KeyboardInterrupt:
            print('\nВы вышли из игры')
            exit()
        except ValueError:
            print(f'{error_text} ')

    return nums_tuple
