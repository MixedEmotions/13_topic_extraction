# -*- coding: utf-8 -*-

import unicodedata

def remove_accents(s):
        """ Remove accents
        Notes:
            * s must be unicode!
        """
        if not isinstance(s, str):
            s = s.decode('utf-8')
        no_accents = ''
        normalized = unicodedata.normalize('NFD', s)
        for i,c in enumerate(normalized):
            if unicodedata.category(c) != 'Mn': 
                if i == (len(normalized) - 1) or normalized[i+1] != '\u0303':
                    no_accents += c
                elif c == 'n' and normalized[i+1] == '\u0303':
                    no_accents += 'ñ'
        return no_accents

def remove_diacritic(input):
    '''
    Accept a unicode string, and return a normal string (bytes in Python 3)
    without any diacritical marks.
    '''
    return unicodedata.normalize('NFKD', input).encode('ASCII', 'ignore')


if __name__ == '__main__':
    print(remove_accents('aaaa'))
    # input = '\xc0 quelle \xe9cole va-tu?'
    # output = remove_diacritic(input).decode()

    # normalized_unicode = unicodedata.normalize('NFC', 'áéí '.decode('utf-8'))
    # print(normalized_unicode)