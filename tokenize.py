import string
def word_tokenize(s):
    """
    ascii letters -- digits -- punctuations -- whitespace
    """
    tokens = []
    indices = []
    prev_idx = 0
    for i, (c1, c2) in enumerate(zip(s, s[1:])):

        #Ascii to others
        if c1 in string.ascii_letters and c2 in string.digits:
            tokens.append(s[prev_idx:i+1])
            indices.append((prev_idx, i+1))
            prev_idx = i+1
            
        if c1 in string.ascii_letters and c2 in string.punctuation:
            tokens.append(s[prev_idx:i+1])
            indices.append((prev_idx, i+1))
            prev_idx = i+1            

        if c1 in string.ascii_letters and c2 in string.whitespace:
            tokens.append(s[prev_idx:i+1])
            indices.append((prev_idx, i+1))
            prev_idx = i+1
        
        #digits to others
        if c1 in string.digits and c2 in string.ascii_letters:
            tokens.append(s[prev_idx:i+1])
            indices.append((prev_idx, i+1))
            prev_idx = i+1            

        if c1 in string.digits and c2 in string.punctuation:
            tokens.append(s[prev_idx:i+1])
            indices.append((prev_idx, i+1))
            prev_idx = i+1
            
        if c1 in string.digits and c2 in string.whitespace:
            tokens.append(s[prev_idx:i+1])
            indices.append((prev_idx, i+1))
            prev_idx = i+1

        #punctuation to others
        if c1 in string.punctuation and c2 in string.digits:
            tokens.append(s[prev_idx:i+1])
            indices.append((prev_idx, i+1))
            prev_idx = i+1

        if c1 in string.punctuation and c2 in string.ascii_letters:
            tokens.append(s[prev_idx:i+1])
            indices.append((prev_idx, i+1))
            prev_idx = i+1

        if c1 in string.punctuation and c2 in string.whitespace:
            tokens.append(s[prev_idx:i+1])
            indices.append((prev_idx, i+1))
            prev_idx = i+1
            
        #whitespace to others
        if c1 in string.whitespace and c2 in string.digits:
            tokens.append(s[prev_idx:i+1])
            indices.append((prev_idx, i+1))
            prev_idx = i+1
            
        if c1 in string.whitespace and c2 in string.punctuation:
            tokens.append(s[prev_idx:i+1])
            indices.append((prev_idx, i+1))
            prev_idx = i+1
            
        if c1 in string.whitespace and c2 in string.ascii_letters:
            tokens.append(s[prev_idx:i+1])
            indices.append((prev_idx, i+1))
            prev_idx = i+1
                    
            
    else:
        tokens.append(s[prev_idx:])
        indices.append((prev_idx, len(s)))
                
    return tokens, indices

import sys
if __name__ == '__main__':
    print(word_tokenize(sys.argv[1]))
