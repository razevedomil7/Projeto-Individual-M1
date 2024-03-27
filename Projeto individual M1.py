"""COMO FAZER?
⇨ Você deve criar com Python uma lista para armazenar esses resultados
(e outros resultados que quiser no mesmo formato, o código precisa
funcionar para qualquer lista que seja inserida nesse formato) e depois
uma função que busca o candidato de acordo com os critérios
digitados pelo usuário. O usuário vai informar qual a nota mínima de e,
t, p e s que ele deseja buscar, nossa aplicação deve listar quem são os
candidatos disponíveis com nota maior ou igual a essas informadas
pelo usuário.
⇨ Ao buscar por alguém com resultados 4,4,8,8 por exemplo vamos
receber que os candidatos 1 e 5 atendem esse critério, foram bem no
teste prático e apresentaram um ótimo nível de soft skills!"""

"""C = Candidato E= entrevista T = Teste P = Prática S = SoftSkills
Print("Olá, deseja inserir uma nota? Digite 1 para sim, 2 para não.")"""

id = ["C1", "C2", "C3", "C4", "C5" ]
vlr_notas = [
                [5, 6, 7, 8],
                [4, 5, 6, 7],
                [6, 7, 8, 9],
                [7, 8, 9, 10],
                [4, 4, 8, 8]
            ]

candidatos = []
for candidato, valor_notas in zip(id, vlr_notas):
    candidato = {"candidato": candidato, "valor das notas": valor_notas }
    candidatos.append(candidato)

pesquisa = int(input("Olá, digite um número para iniciar a pesquisa de candidatos:"))

def buscar_candidatos(notas_minimas, candidatos):
    candidatos_compativeis = []

    for candidato in candidatos:
        notas_candidato = candidato["valor das notas"]
        if all(nota_candidato >= nota_minima for nota_candidato, nota_minima in zip(notas_candidato, notas_minimas)):
            candidatos_compativeis.append(candidato["candidato"])

    return candidatos_compativeis

nota_e = int(input("Digite a nota mínima para entrevista (E): "))
nota_t = int(input("Digite a nota mínima para teste (T): "))
nota_p = int(input("Digite a nota mínima para prática (P): "))
nota_s = int(input("Digite a nota mínima para soft skills (S): "))

notas_minimas = [nota_e, nota_t, nota_p, nota_s]


candidatos_encontrados = buscar_candidatos(notas_minimas, candidatos)


if candidatos_encontrados:
    print("Candidatos encontrados:")
    for candidato in candidatos_encontrados:
        print(candidato)
else:
    print("Nenhum candidato encontrado com as notas mínimas especificadas.")