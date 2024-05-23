def prencher_lista():
      lista = [1, 2, 3, 4, 5]
      permanecer = True
      
      while(permanecer):
            try:
                  posicao = int(input("Informe uma posição de 0 e 4: "))
                  if (posicao < 0) or (posicao > 4):
                        print("Posição inexistente na lista")
                        print("Informe outra posição")

                  else:
                        valor = int(input(f"Informe o valor para a posição {posicao}: "))
                        lista[posicao] = valor
                        permanecer = False

            except IndexError as e:
                  print(f"Erro: {e}")

            except ValueError as e:
                  print("Valor informado não é um número.")
                  print(f"Erro: {e}")
      
            except Exception as e:
                  print("Entrada invalida")
      
      
      return lista

if __name__ == "__main__":
    valores = prencher_lista()
    print(valores)