notas = []

# notas.append(float(input("Insira a primeira nota: ")))
# notas.append(float(input("Insira a segunda nota: ")))
# notas.append(float(input("Insira a terceira nota: ")))
# notas.append(float(input("Insira a quarta nota: ")))

for _ in range(4):
    notas.append(float(input(f"Insira a {_+1}º nota: ")))

print("-"*50)

print(f"""
Sua maior nota: {max(notas)}
Sua menor nota: {min(notas)}
Soma das suas notas: {sum(notas)}
Média das suas notas: {sum(notas)/len(notas)}
situação: {"Aprovado" if (sum(notas)/len(notas)) >= 6 else "Reprovado"}
      """)

