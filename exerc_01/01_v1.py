def prencher_lista():
      lista = [1, 2, 3, 4, 5]

      try:
            posicao = int(input("Informe uma posição de 0 e 4: "))
            valor = int(input(f"Informe o valor para a posição {posicao}: "))
            lista[posicao] = valor

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