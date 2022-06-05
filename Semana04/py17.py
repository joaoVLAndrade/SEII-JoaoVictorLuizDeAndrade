try:
    f = open('Copia_Teste.txt', 'r')
except ZeroDivisionError as ze:
    print('Não é possível dividir por 0!',ze)
except FileNotFoundError as fe:
    print('Arquivo não encontrado!', fe)
except Exception:
    print('Algo de errado aconteceu!')
else:#É executado se a tentativa for bem sucedida 
    print(f.read())
    f.close
finally:#É executado independete de houver uma exceção ou não
    print('Teste')