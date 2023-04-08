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
    nText = text.strip()

    for i in range(len(nText)):
        print(nText[i], end='')
        if nText[i] in (':', '.', '?'):
            print('\n')
        if (i == len(nText) - 1) and (nText[i] not in ('.:?')):
            print('\n')
