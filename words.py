def remove_spaces(words: str):
    """Remove espaços da entrada dada

    Args:
        words (str): String dada como entrada

    Returns:
        str: String de entrada sem espaços
    """
        
    return words.replace(' ', '')

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
