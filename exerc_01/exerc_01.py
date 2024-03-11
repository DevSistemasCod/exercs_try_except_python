def preencher_lista():
    lista = [1, 2, 3, 4, 5] 

    print("Lista atual:", lista)
    for i in range(5):
        
        try:
            posicao = int(input("Informe uma posição entre (0 a 4): "))    
            if ( (posicao < 0) or (posicao >= 5)):
                print("Posição inexistente na lista.")
                print("Você deve informar outra posição")

            else:
                valor = int(input(f"Informe o valor para a posição {posicao}: "))
                lista[posicao] = valor
                break
        except IndexError as e:
            print(f"Erro: {e}")

        except ValueError as e:
            print("Valor informado não é um número.")
            print(f"Erro: {e}")

        except Exception:
            print("Entrada invalida.")


    return lista


if __name__ == "__main__":
    valores = preencher_lista()
    print("Lista atual:", valores)
