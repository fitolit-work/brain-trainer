def spaces_in_word(text: str) -> tuple[str, bool]:
    """
        Checks for whitespace characters in the input string
        :param text: Text to check
        :return: Verified inscription without spaces
    """
    text = text.strip()
    if ' ' in text:
        return 'Name without spaces!', False
    else:
        return text, True


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
