import sys
from heapq import heappush, heappop, heapify


def file_character_frequencies(file_name):
    freqs = {}
    contents = ""
    with open(file_name) as f:
        contents = f.read()
    for symbol in contents:
        freqs[symbol] = freqs.get(symbol, 0) + 1
    return freqs


class PriorityTuple(tuple):
    """A specialization of tuple that compares only its first item when sorting.
    Create one using double parens e.g. PriorityTuple((x, (y, z))) """
    def __lt__(self, other):
        return self[0] < other[0]

    def __le__(self, other):
        return self[0] <= other[0]

    def __gt__(self, other):
        return self[0] > other[0]

    def __ge__(self, other):
        return self[0] >= other[0]

    def __eq__(self, other):
        return self[0] == other[0]

    def __ne__(self, other):
        x = self.__eq__(other)
        return not x

def huffman_codes_from_frequencies(frequencies):
    huffmanCodes = {}
    heap = [PriorityTuple((freq, (sym,))) for sym, freq in frequencies.items()]
    heapify(heap)
    
    
    while len(heap) > 1:
        leftFreq, leftSymbols = heappop(heap)
        for symbol in  leftSymbols:
            huffmanCodes[symbol] = "0" + huffmanCodes.get(symbol, "")
        rightFreq, rightSymbols = heappop(heap)
        for symbol in rightSymbols:
            huffmanCodes[symbol] = "1" + huffmanCodes.get(symbol, "")
            
        newNode = PriorityTuple((leftFreq + rightFreq, leftSymbols + rightSymbols))
        heappush(heap, newNode)
    
    return huffmanCodes


def huffman_letter_codes_from_file_contents(file_name):
    """WE WILL GRADE BASED ON THIS FUNCTION."""
    frequencies = file_character_frequencies(file_name)
    return huffman_codes_from_frequencies(frequencies)


def encode_file_using_codes(file_name, letter_codes):
    """Provided to help you play with your code."""
    contents = ""
    with open(file_name) as f:
        contents = f.read()
    file_name_encoded = file_name + "_encoded"
    with open(file_name_encoded, 'w') as fout:
        for c in contents:
            fout.write(letter_codes[c])
    print("Wrote encoded text to {}".format(file_name_encoded))
    return file_name_encoded


def decode_file_using_codes(file_name_encoded, letter_codes):
    """Provided to help you play with your code."""
    contents = ""
    with open(file_name_encoded) as f:
        contents = f.read()
    file_name_encoded_decoded = file_name_encoded + "_decoded"
    codes_to_letters = {v: k for k, v in letter_codes.items()}
    with open(file_name_encoded_decoded, 'w') as fout:
        num_decoded_chars = 0
        partial_code = ""
        while num_decoded_chars < len(contents):
            partial_code += contents[num_decoded_chars]
            num_decoded_chars += 1
            letter = codes_to_letters.get(partial_code)
            if letter:
                fout.write(letter)
                partial_code = ""
    print("Wrote decoded text to {}".format(file_name_encoded_decoded))
    return file_name_encoded_decoded


def main():
    """Provided to help you play with your code."""
    import pprint
    fileName = sys.argv[1]
    frequencies = file_character_frequencies(fileName)
    #pprint.pprint(frequencies)
    codes = huffman_codes_from_frequencies(frequencies)
    #pprint.pprint(codes)
    encodedFile = encode_file_using_codes(fileName, codes)
    encodedText = ""
    with open(encodedFile) as f:
        encodedText = f.read()
    print("Encoded Text: {}".format(encodedText))
    decodedFile = decode_file_using_codes(encodedFile, codes)
    decodedText = ""
    with open(decodedFile) as f:
        decodedText = f.read()
    print("Decoded Text: {}".format(decodedText))
    


if __name__ == '__main__':
    """We are NOT grading you based on main, this is for you to play with."""
    main()