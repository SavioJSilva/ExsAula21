def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos:
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com váris informações sobre a situação da turma.
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÀVEL'
        else:
            r['Situação'] = 'RUIM'
    return r


# Programa Principal
resp = notas(10, 5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)