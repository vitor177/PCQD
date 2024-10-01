def encontrar_indices(lista_menor, lista_maior):
    """
    Retorna os índices de correspondência entre elementos da lista_menor
    que aparecem na lista_maior, ignorando maiúsculas e minúsculas.
    
    Parâmetros:
    - lista_menor: lista com os termos a serem buscados (ex: col_Temp)
    - lista_maior: lista onde a busca será realizada (ex: finais)
    
    Retorno:
    - Uma lista de índices da lista_maior onde ocorre a correspondência.
    """
    return [i for i, item in enumerate(lista_maior) if item.lower() in [term.lower() for term in lista_menor]]