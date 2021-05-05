def get_txt(s):
    if s == 'shakespeare':
        with open('./texts/shakespeare.txt') as f:
            return f.read().splitlines()
    
    if s == 'potter':
        with open('./texts/potterspells.txt') as f:
            return f.read().splitlines()

    if s == 'uzumaki':
        with open('./texts/uzumakibayu.txt') as f:
            return f.read().splitlines()

def get_copypasta(s):
    if s == 'amogus':
        with open('./texts/amogus.txt') as f:
            return f.read()

    if s == 'amogus1':
        with open('./texts/amogus1.txt') as f:
            return f.read()

    if s == 'amogus2':
        with open('./texts/amogus2.txt') as f:
            return f.read()
    
    if s == 'amogus3':
        with open('./texts/amogus3.txt') as f:
            return f.read()
