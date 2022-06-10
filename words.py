import random

def remove_spaces(words: str):
    """Remove espaços da entrada dada

    Args:
        words (str): String dada como entrada

    Returns:
        str: String de entrada sem espaços
    """
        
    return words.replace(' ', '')

def remove_spaces_and_small_words(words: list):
    """Remove espaços da entrada dada e palavras com menos de 4 caracteres

    Args:
        words (list): Palavras dadas como entrada

    Returns:
        str: String de entrada sem espaços e sem palavras com menos de 4 caracteres
    """
        
    return ''.join([word for word in words if len(word) > 3])

def get_large_words(words: list):
    """
    Remove palavras pequenas das palavras dadas como entrada

    Args:
        words (list): Palavras dadas como entrada

    Returns:
        list: Lista de palavras dadas como entrada com mais de 3 caracteres
    """
        
    return [word for word in words if len(word) > 3]

def get_acronym(words: list):
    """
    Gera acrônimos a partir das palavras dadas como entrada

    Args:
        words (list): Lista de strings contendo as palavras dadas como entrada

    Returns:
        str: Acrônimo das palavras dadas como entrada
    """
    return ''.join([word[0] for word in words])

def get_large_words_acronym(words: list):
    """
    Função que gera acrônimos a partir das palavras dadas como entrada, considerando apenas palavras com 4 caracteres ou mais

    Args:
        words (list): Lista de strings contendo as palavras dadas como entrada

    Returns:
        str: Acrônimo das palavras com 4 caracteres ou mais dadas como entrada
    """
    return ''.join([word[0] for word in words if len(word) > 3])

def generate_number_sequences():
    """
    Gera sequências numéricas aleatórias e não aleatórias.
    """
    
    # Sequencias aleatórias        
    for i in range(3000):
        print(random.randint(1000,10000))
        
    for i in range(3000):
        print(random.randint(10000,100000))
        
    for i in range(3000):
        print(random.randint(100000,1000000))
        
    # Sequencias não aleatórias
    for i in range(7):
        print(''.join([str(number) for number in (list(range(i, i + 4)))]))
        
    for i in range(6):
        print(''.join([str(number) for number in (list(range(i, i + 5)))]))
    
    for i in range(5):
        print(''.join([str(number) for number in (list(range(i, i + 6)))]))
