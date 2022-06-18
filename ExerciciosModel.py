import datetime
import this

def exercicio1():
    a = 10
    b = 20
    msg = 'Antes da troca: A {}, B = {}'.format(a,b)
    aux = a
    a = b
    b = aux
    msg = msg + '\nDepois da troca: A = {}, B = {}'.format(a,b)
    return msg

def exercicio2():
    num = int(input('Informe um número: '))
    ant = num - 1
    msg = 'O número anterior a {} é {}'.format(num, ant)
    return msg

def exercicio3():
    base = int(input('Informe o valor da base: '))
    alt = int(input('Informe o valor da altura: '))
    area = base * alt
    msg = 'A área do retângulo é {}'.format(area)
    return msg

def exercicio4():
    dia = int(input('Informe o dia do nascimento '))
    mes = int(input('Informe o mês de nascimento: '))
    ano = int(input('Informe o ano de nascimento: '))

    data = datetime.datetime.now()

    anoNow = (data.year)
    mesNow = (data.month)
    diaNow = (data.day)

    ano = (anoNow - ano) * 365
    mes = abs(mesNow - mes) * 30
    dia = abs(diaNow - dia)

    value = ano + mes + dia

    msg = 'Você tem um total de {} dias de vida'.format(value)
    return msg

def exercicio5():
    eleit = float(input('Informe o Nº total de eleitores: '))
    brancos = float(input('Informe o Nº total de votos em branco: '))
    nulos = float(input('Informe o Nº total de votos em branco: '))
    validos = float(input('Informe o Nº total de votos em branco: '))

    soma = brancos + nulos + validos

    if soma == eleit:
        bran = (brancos / eleit) * 100
        nul = (nulos / eleit) * 100
        val = (validos / eleit) * 100

        msg = ('\nO percentual de votos brancos é de {}% '
               '\nO percentual de votos nulos é de {}% '
               '\nO percentual de votos válidos é de {}%'.format(bran, nul, val))
        return msg
    elif soma != eleit:
        msg = 'As quantidades de todos os votos não é similar a quantidade de eleitores!'
        return msg

def exercicio6():
    sal = float(input('Informe o salário: '))
    ajuste = float(input('Informe o valor do reajuste em percentual: '))

    total = sal * (1 + ajuste/100)

    msg = 'O valor do salário de {} após o reajuste de {}% é de {}'.format(sal, ajuste, total)
    return msg

def exercicio7():
    custo = float(input('Informe o custo de fábrica do carro: '))
    value = custo + (custo * 0.28) + (custo * 0.45)

    msg = 'O custo final do carro para o consumidor é de: {}'.format(value)

    return msg

def exercicio8():
    not1 = float(input('Informe a 1° nota: '))
    not2 = float(input('Informe a 2° nota: '))
    not3 = float(input('Informe a 3° nota: '))

    media = (not1 + not2 + not3) / 3

    msg = 'A média do aluno é de: {}'.format(media)
    return msg

def exercicio9():
    aplle = int(input('Informe a quantidade de maçãs compradas: '))

    if aplle < 12:
        value = aplle * 1.3
        msg = 'O valor total das maçãs é de: {}'.format(value)
        return msg
    elif aplle >= 12:
        total = aplle * 1
        msg = 'O valor total das maçãs é: {}'.format(total)
        return msg

def exercicio10():
    num = []
    for i in range(0,10):
        valor = int(input('Informe o {}º valor: '.format(i+1)))
        num.append(valor)
    num.sort()
    print('Os números em ordem são:')
    return num

def exercicio11():
    sal = float(input('Informe o valor do seu salário: '))
    vend = float(input('Informe o valor das vendas: '))

    if vend < 1500:
        salario = sal + (0.03 * vend)
        msg = 'O seu salário este mês é R$ {}'.format(salario)
        return msg
    elif vend > 1500:
        vendasParcial = (vend - 1500) * 0.05
        salario = sal + vendasParcial + (1500 * 0.03)
        msg = 'O seu salário este mês é de R$ {}'.format(salario)
        return msg

def exercicio12():
    nConta = int(input('Informe o número da conta: '))
    saldo = float(input('Informe o saldo atual da conta: '))
    debito = float(input('Informe o debito atual da conta: '))
    credito = float(input('Informe o valor atual do crédito: '))

    saldoAtual = saldo - debito + credito

    if saldoAtual < 0:
        msg = 'A conta {}, está com saldo negativo'.format(nConta)
        return msg
    elif saldoAtual > 0:
        msg = 'A conta {}, está com saldo positivo'.format(nConta)
        return msg

def exercicio13():
    n = int(input('Informe um número: '))

    while (n > 10) and (n < 1):
        print('Selecione um valor válido entre 1 e 10')

    for i in range(1, 11):
        print('{} x {} = {}'.format(n, i, (n*i)))

def exercicio14():
    n = int(input('Informe um valor: '))
    numeros = []
    i = 0
    while n < 0:
        n = int(input('Escreva um valor válido, que no caso seria, maior do que 1: '))

    for i in range(1, n+1):
        numeros.append(i)

    msg = 'Os números entre 1 e {} é: {}'.format(n, numeros)
    return msg

def exercicio15():
    lista = []
    neg = 0

    for i in range(1, 11):
        num = int(input('Informe o {}° número: '.format(i)))
        lista.append(num)
        if num < 0:
            neg += 1

    msg = 'Entre os números listados há {} valores negativos'.format(neg)
    return msg

def exercicio16():
    lista = []
    soma = 0

    for i in range(1, 11):
        num = int(input('Informe o {}° número: '.format(i)))
        lista.append(num)
        if num < 40:
            soma += num

    msg = 'Entre os números informados, a soma dos valores abaixo de 40 é de: {}'.format(soma)
    return msg

def exercicio17():
    soma = 0
    for i in range(15, 101):
        soma += i
    media = soma / 85

    msg = 'A média aritmética dos Nº entre 15 e 100 é {}'.format(media)
    return msg

def exercicio18():
    n = int(input('Informe o valor de números a serem lidos: '))
    lista = []
    soma = 0

    for i in range(1, n+1):
        num = int(input('Informe o {}° número'.format(i)))
        lista.append(num)
        soma += num

    media = soma / n
    lista.sort()
    print('O maior número entre os digitados é: {}'.format(lista[n-1]))
    print('A média é: {}'.format(media))

def exercicio19():
    lista = []
    somaNota = 0
    qtdAlunos = 0
    for i in range(1, 21):
        nota = float(input('Informe a {}ª nota:'.format(i)))
        lista.append(nota)
        somaNota += nota
    media = somaNota / 20
    for i in range(1, len(lista)):
        if lista[i] > media:
            qtdAlunos += 1

    msg = 'A média de notas da turma foi de {} e a quantidade de alunos acima da média foi de {}'.format(media, qtdAlunos)
    return msg

def exercicio20():
    maiorSalario = []
    continuar = 1
    populacao = 0
    smallSalary = 0
    valorSalario = 0
    numeroFilhos = 0

    while continuar == 1:
        salario = float(input('Informe o seu salário: '))
        nFilhos = int(input('Informe o número de filhos: '))

        maiorSalario.append(salario)
        numeroFilhos += nFilhos
        valorSalario += salario
        populacao += 1

        continuar = int(input('Deseja coletar mais dados? (1 = Sim, é claro) (Qualquer tecla = Não, obrigado): '))

    mediaDeSalario = valorSalario / populacao
    mediaDeFilhos = numeroFilhos / populacao
    maiorSalario.sort()
    maior = maiorSalario[populacao-1]

    for i in range(1, len(maiorSalario)):
        if maiorSalario[i] < 150:
            smallSalary += 1

    percentual = (smallSalary / populacao) * 100

    msg = 'A média salarial é de R$ {} ' \
          '\nA média de filhos é de: {} ' \
          '\nO maior salário foi de RS {} ' \
          '\nO percentual da população com salário menor do que 150 foi de {}%'.format(mediaDeSalario, mediaDeFilhos, maior, percentual)
    return msg