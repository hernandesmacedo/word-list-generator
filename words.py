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
        
    return ''.join([word if len(word) > 3 else '' for word in words])

def acronym(words: list):
    """
    Gera acrônimos a partir das palavras dadas como entrada

    Args:
        words (list): Lista de strings contendo as palavras dadas como entrada

    Returns:
        str: Acrônimo das palavras dadas como entrada
    """
    return ''.join([word[0] for word in words])

def large_words_acronym(words: list):
    """
    Função que gera acrônimos a partir das palavras dadas como entrada, considerando apenas palavras com 4 caracteres ou mais

    Args:
        words (list): Lista de strings contendo as palavras dadas como entrada

    Returns:
        str: Acrônimo das palavras com 4 caracteres ou mais dadas como entrada
    """
    return ''.join([word[0] if len(word) > 3 else '' for word in words])
