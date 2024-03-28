
class Pesquisa():
    def pesquisa_binaria(lista, item):
        ''''
        Pesquisa um item em um array por meio de pesquisa binária.
        
        Args:
            lista (array): Lista ORDENADA e completa de itens que serão pesquisado.
            item (int): Valor que se deseja encontrar.

        Returns:
            int : Retorna posição em que item está na array ou none caso não esteja contido.
        '''

        menor_valor = 0
        maior_valor = len(lista) - 1

        while menor_valor <= maior_valor:
                meio = (menor_valor + maior_valor) // 2
                chute = lista[meio]

                if chute == item:
                     return meio
                if chute > item:
                     maior_valor = meio - 1
                else:
                     menor_valor = meio + 1

        return None
    


# Lista deve estar ordenada para pesquisas Binárias
minha_lista = [1, 3, 5, 7, 9]

print(Pesquisa.pesquisa_binaria(minha_lista, 5))
