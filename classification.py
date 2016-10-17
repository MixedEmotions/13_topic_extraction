# -*- coding: utf-8 -*-

from commons import *

class Classificator:

    def __init__(self, taxonomy):
        self.taxonomy = taxonomy

    def classify(self, text):
        """ 
        Return those concepts that appear in text.

        Example:

        >>> taxonomy = {'adsl' : ['telco'], 'tarifa plana': ['telco', 'otro concepto'],
                        'tarifa' : ['telco']}
        >>> classify(taxonomy, 'la tarifa plana de movistar es mejor que el adsl')
        {'adsl': ['telco'], 'tarifa': ['telco'], 'tarifa plana': ['telco', 'otro concepto']}
        """
        if not text:
            return {}
        taxonomy = self.taxonomy
        text = remove_accents(text.lower())
        concepts ={}
        
        window_text = 1
        for item in taxonomy:
            aux = len(item.split(' '))
            if aux >= window_text:
                window_text=aux
        
        # Split text in parts
        text_parts = text.split(' ')
        # Length of this parts
        n = len(text_parts)
        # Max recursive segments
        max_segment = window_text
        # Auxiliar structure for save tuples (match , index_start, index_end)
        chunks = []
        chunks_len = {}
        # Start loop
        i = 0
        while i < n :
            # Start the window from i position
            j = i + max_segment
            # Check if window is not overload the text length
            if j > n:
                j = n
            # Check all posibilities
            while (j > i):
                match = ' '.join(text_parts[i : j])
                # If found the chance in the index, save chunktext and position into string
                try:
                    if taxonomy[match] != None:
                        chunks.append((match , i , j))
                except:
                    pass
                j -= 1
            i += 1
     
        # Calculate acumulative character len of each split
        character_len_acum = []
        ant = 0
        # I need count to sumarize blanks
        cont = 0
        for part in text_parts:
            aux = len(part)
            # Add acumulative value
            character_len_acum.append(ant + cont)
            ant += aux
            cont += 1
        # Calculate overloads between chunks
        group_count = 0
        # Start previus chunk
        max_ant_scope = -1
        for chunk in chunks:
            # If there is a gap between two chunks, create new cluster
            if (chunk[1] >= max_ant_scope):
                group_count += 1
            i = chunk[1] - window_text
            if i < 0:
                i = 0
            j = chunk[2] + window_text
            last_word_tail = 0
            if j > len(character_len_acum) - 1:
                j = len(character_len_acum) - 1
                last_word_tail = len(text_parts[n - 1])
            # Save text scope of the word
            concepts[chunk[0]]= taxonomy[chunk[0]]
            if chunk[2] > max_ant_scope:
                max_ant_scope = chunk[2]

        return concepts

if __name__ == '__main__':
    taxonomy = {'adsl' : ['telco'], 'tarifa plana': ['telco', 'otro concepto'],
                        'tarifa' : ['telco']}
    classif = Classificator(taxonomy)
    print(classif.classify('la tarifa plana de movistar es mejor que el adsl'))
