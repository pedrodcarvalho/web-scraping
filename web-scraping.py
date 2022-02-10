import urllib.request

import re

from bs4 import BeautifulSoup


def initialize():
    url, user_input = get_input()

    data_parsed = validate_socket(url)

    user_input = user_input.lower()
    user_input = user_input.capitalize()
    user_input = user_input.replace('_', ' ')

    print(f'\nInformations about {user_input}:')

    try:
        words = data_parsed[0].split()
    except:
        print("\nToo little information")
        repeat()

    show_info(words)


def get_input():
    template = 'https://en.wikipedia.org/wiki/'
    user_input = input('\nEnter any word to get information about it: ')
    user_input = user_input.replace(' ', '_')
    url = template + user_input

    return url, user_input


def sock(url):
    html = urllib.request.urlopen(url).read()

    soup = BeautifulSoup(html, 'html.parser')

    data = soup.get_text()

    data_array = data.split('\n')
    data_parsed = []

    for i in data_array:
        if i and len(i) > 750:
            data_parsed.append(i)

    return data_parsed


def repeat():
    try_again = input('\nDo you want to try another word? [Y/n]: ')

    if try_again.upper() == 'Y':
        initialize()
    elif try_again.upper() == 'N':
        quit()
    else:
        print('\nPlease choose between \'Y\' or \'n\'')
        repeat()


def validate_socket(url):
    try:
        data_parsed = sock(url)
        return data_parsed
    except:
        print('\nSorry, the word that you have entered didn\'t work...')
        repeat()


def show_info(words):
    data_transformed = []
    pattern = r'\[.+\]'

    for word in words:
        if re.search(pattern, word):
            word = re.sub(pattern, '', word)

        data_transformed.append(f'{word} ')

    index = 0
    final_data = ''

    for word in data_transformed:
        final_data += data_transformed[index]
        index += 1

    print(f'\n{final_data}')

    quit()


initialize()
