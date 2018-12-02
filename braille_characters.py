def toBraille(char):
    if not(char.lower() in braille):
        return braille[' ']
    return braille[char.lower()]

braille = {
    'a' : [
        1, 0,
        0, 0,
        0, 0
    ],
    'b' : [
        1, 0,
        1, 0,
        0, 0
    ],
    'c' : [
        1, 1,
        0, 0,
        0, 0
    ],
    'd' : [
        1, 1,
        0, 1,
        0, 0
    ],
    'e' : [
        1, 0,
        0, 1,
        0, 0
    ],
    'f' : [
        1, 1,
        1, 0,
        0, 0
    ],
    'g' : [
        1, 1,
        1, 1,
        0, 0
    ],
    'h' : [
        1, 0,
        1, 1,
        0, 0
    ],
    'i' : [
        0, 1,
        1, 0,
        0, 0
    ],
    'j' : [
        0, 1,
        1, 1,
        0, 0
    ],
    'k' : [
        1, 0,
        0, 0,
        1, 0
    ],
    'l' : [
        1, 0,
        1, 0,
        1, 0
    ],
    'm' : [
        1, 1,
        0, 0,
        1, 0
    ],
    'n' : [
        1, 1,
        0, 1,
        1, 0
    ],
    'o' : [
        1, 0,
        0, 1,
        1, 0
    ],
    'p' : [
        1, 1,
        1, 0,
        1, 0
    ],
    'q' : [
        1, 1,
        1, 1,
        1, 0
    ],
    'r' : [
        1, 0,
        1, 1,
        1, 0
    ],
    's' : [
        0, 1,
        1, 0,
        1, 0
    ],
    't' : [
        0, 1,
        1, 1,
        1, 0
    ],
    'u' : [
        1, 0,
        0, 0,
        1, 1
    ],
    'v' : [
        1, 0,
        1, 0,
        1, 1
    ],
    'w' : [
        0, 1,
        1, 1,
        0, 1
    ],
    'x' : [
        1, 1,
        0, 0,
        1, 1
    ],
    'y' : [
        1, 1,
        0, 1,
        1, 1
    ],
    'z' : [
        1, 0,
        0, 1,
        1, 1
    ],
    ' ' : [
        0, 0,
        0, 0,
        0, 0
    ],
    '1' : [
        1, 0,
        0, 0,
        0, 0
    ],
    '2' : [
        1, 0,
        1, 0,
        0, 0
    ],
    '3' : [
        1, 1,
        0, 0,
        0, 0
    ],
    '4' : [
        1, 1,
        0, 1,
        0, 0
    ],
    '5' : [
        1, 0,
        0, 1,
        0, 0
    ],
    '6' : [
        1, 1,
        1, 0,
        0, 0
    ],
    '7' : [
        1, 1,
        1, 1,
        0, 0
    ],
    '8' : [
        1, 0,
        1, 1,
        0, 0
    ],
    '9' : [
        0, 1,
        1, 0,
        0, 0
    ],
    '0' : [
        0, 1,
        1, 1,
        0, 0
    ],
    
}
