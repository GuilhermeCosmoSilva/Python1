import this
import ExerciciosModel
this.opcao = -1

def menu():
    print('Menu\n\n' +
          '\n1. Exercício 1' +
          '\n2. Exercício 2' +
          '\n3. Exercício 3' +
          '\n4. Exercício 4' +
          '\n5. Exercício 5' +
          '\n6. Exercício 6' +
          '\n7. Exercício 7' +
          '\n8. Exercício 8' +
          '\n9. Exercício 9' +
          '\n10. Exercício 10' +
          '\n11. Exercício 11' +
          '\n12. Exercício 12' +
          '\n13. Exercício 13' +
          '\n14. Exercício 14' +
          '\n15. Exercício 15' +
          '\n16. Exercício 16' +
          '\n17. Exercício 17' +
          '\n18. Exercício 18' +
          '\n19. Exercício 19' +
          '\n20. Exercício 20' +
          '\n0. Sair' +
          '\n\nEscolha uma das opções acima: ')
    this.opcao = int(input())

def executar():
    while this.opcao != 0:
        menu()
        if this.opcao == 0:
            print('Obrigado')
        elif this.opcao == 1:
            print(ExerciciosModel.exercicio1())
        elif this.opcao == 2:
            print(ExerciciosModel.exercicio2())
        elif this.opcao == 3:
            print(ExerciciosModel.exercicio3())
        elif this.opcao == 4:
            print(ExerciciosModel.exercicio4())
        elif this.opcao == 5:
            print(ExerciciosModel.exercicio5())
        elif this.opcao == 6:
            print(ExerciciosModel.exercicio6())
        elif this.opcao == 7:
            print(ExerciciosModel.exercicio7())
        elif this.opcao == 8:
            print(ExerciciosModel.exercicio8())
        elif this.opcao == 9:
            print(ExerciciosModel.exercicio9())
        elif this.opcao == 10:
            print(ExerciciosModel.exercicio10())
        elif this.opcao == 11:
            print(ExerciciosModel.exercicio11())
        elif this.opcao == 12:
            print(ExerciciosModel.exercicio12())
        elif this.opcao == 13:
            print(ExerciciosModel.exercicio13())
        elif this.opcao == 14:
            print(ExerciciosModel.exercicio14())
        elif this.opcao == 15:
            print(ExerciciosModel.exercicio15())
        elif this.opcao == 16:
            print(ExerciciosModel.exercicio16())
        elif this.opcao == 17:
            print(ExerciciosModel.exercicio17())
        elif this.opcao == 18:
            print(ExerciciosModel.exercicio18())
        elif this.opcao == 19:
            print(ExerciciosModel.exercicio19())
        elif this.opcao == 20:
            print(ExerciciosModel.exercicio20())
        else:
            print('Opção inserida não é válida!')