import random
from datetime import datetime
import itertools

def replace_special_characters(words: str):
    """
    Substitui caracteres especiais de uma string por caracteres comuns

    Args:
        words (str): Entrada a ser analisada

    Returns:
        str: Entrada com caracteres especiais substituidos
    """
    words = words.replace('ç', 'c')
    words = words.replace('á', 'a').replace('à', 'a').replace('ã', 'a').replace('â', 'a')
    words = words.replace('é', 'e').replace('ê', 'e')
    words = words.replace('í', 'i').replace('î', 'i')
    words = words.replace('ó', 'o').replace('õ', 'o').replace('ô', 'o')
    words = words.replace('ú', 'u').replace('û', 'u')
    
    return words

def get_permutations(words: list):
    """
    Obtém todas as permutações possíveis das palavras em uma lista e seus acrônimos

    Args:
        words (list): Lista de palavras

    Returns:
        list, list: Lista de acrônimo das permutações e lista das permutações das palavras em `words`
    """
    
    permutations_acronym_list = []
    permutations_list = []
    
    for k in range(1, len(words) + 1):
        new_list = list(itertools.permutations(words, k))
        permutations_acronym_list.append(new_list[0])
        permutations_list += new_list
    
    return [permutations_acronym for permutations_acronym in permutations_acronym_list if len(permutations_acronym) > 1], [''.join(words_permutation) for words_permutation in permutations_list]

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

def generate_number_sequences(word: str):
    """
    Gera sequências numéricas aleatórias e não aleatórias.
    """
    
    # Geração de 7 sequências numéricas ordenadas de tamanho 4
    for i in range(7):
        output_file.write(word + ''.join([str(number) for number in (list(range(i, i + 4)))]) + '\n')
        
    # Geração de 6 sequências numéricas ordenadas de tamanho 5
    for i in range(6):
        output_file.write(word + ''.join([str(number) for number in (list(range(i, i + 5)))]) + '\n')
    
    # Geração de 5 sequências numéricas ordenadas de tamanho 6
    for i in range(5):
        output_file.write(word + ''.join([str(number) for number in (list(range(i, i + 6)))]) + '\n')
    
    # Geração de 1000 números aleatórios de 100 a 99999999
    for i in range(1000):
        output_file.write(word + str(random.randint(100,99999999)) + '\n')

def main():
    print("Digite a(s) palavra(s) de entrada:")
    input_string = input()
    input_string = replace_special_characters(input_string)
    input_words = input_string.split()
    
    output_file_name = 'wordlist_' + datetime.now().strftime("%Y%m%d_%H%M%S") + '.txt'
    global output_file
    output_file = open(output_file_name, mode='w')
    
    # Obtenção de palavras grandes
    large_words = get_large_words(input_words)
    
    # Geração de acrônimo
    acronym = get_acronym(input_words)
    output_file.write(acronym + '\n')
    
    # Geração de acrônimo e permutações das palavras grandes da entrada
    permutations_acronym_list, words_permutations = get_permutations(large_words)
    
    for permutations_acronym in permutations_acronym_list:
        large_words_acronym = get_acronym(permutations_acronym)
        output_file.write(large_words_acronym + '\n')
    
    for words_permutation in words_permutations:
        output_file.write(words_permutation + '\n')
        
    # Geração de palavras da entrada sem espaços
    no_whitespace_entry = input_string.replace(' ', '')
    output_file.write(no_whitespace_entry + '\n')
    
    
    # Associação das palavras individuais à sequências numéricas
    for word in large_words:
        generate_number_sequences(word)
        
    # Associação das permutações de palavras à sequências numéricas
    for words_permutation in words_permutations:
        generate_number_sequences(words_permutation)
    
    # Associação do acrônimo à sequências numéricas
    generate_number_sequences(acronym)
    
    # Associação do acrônimo das palavras grandes à sequências numéricas
    generate_number_sequences(large_words_acronym)
    
    # Associação das palavras da entrada sem espaços à sequências numéricas
    generate_number_sequences(no_whitespace_entry)
    
    output_file.close()

main()
