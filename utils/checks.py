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
            login = input(f'{request_text} ').strip()
        except KeyboardInterrupt:
            print('\nYou are out of the game')
            exit()
        if ' ' in login:
            print(error_text)
        else:
            print(output_text, login)
            return login
