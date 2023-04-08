#!/usr/bin/python3
''' A module define an indentation function '''


def text_indentation(text):
    '''
    A function to add indentation to the text
    agrs:
    text (string): Th string to be edited
    '''

    if type(text) is not str:
        raise TypeError('text must be a string')

    for i in range(len(text)):
        print(text[i], end='')
        if text[i] in (':', '.', '?'):
            print('\n')
        if (i == len(text) - 1) and (text[i] not in ('.:?')):
            print('\n')
