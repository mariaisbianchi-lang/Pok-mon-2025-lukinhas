pokemons = []

while True:
    print("\n===== POKEDEX =====")
    print("1. Cadastrar Pokémon")
    print("2. Listar Pokémons")
    print("3. Batalhar")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do Pokémon: ")
        tipo = input("Tipo (água, fogo, planta, etc.): ")
        try:
            ataque = int(input("Valor de ataque: "))
            vida = int(input("Pontos de vida: "))
            pokemons.append({"nome": nome, "tipo": tipo, "ataque": ataque, "vida": vida})
            print(f"Pokémon {nome} cadastrado com sucesso!")
        except ValueError:
            print("Ataque e vida devem ser números inteiros.")

    elif opcao == "2":
        if not pokemons:
            print("Nenhum Pokémon cadastrado.")
        else:
            print("\n--- Lista de Pokémons ---")
            for i, p in enumerate(pokemons, start=1):
                print(f"{i}. {p['nome']} | Tipo: {p['tipo']} | Ataque: {p['ataque']} | Vida: {p['vida']}")

    elif opcao == "3":
        if len(pokemons) < 2:
            print("É necessário ter pelo menos 2 Pokémons cadastrados para batalhar.")
        else:
            for i, p in enumerate(pokemons, start=1):
                print(f"{i}. {p['nome']} | Tipo: {p['tipo']} | Ataque: {p['ataque']} | Vida: {p['vida']}")
            try:
                escolha1 = int(input("Escolha o número do primeiro Pokémon: ")) - 1
                escolha2 = int(input("Escolha o número do segundo Pokémon: ")) - 1
                if escolha1 == escolha2:
                    print("Escolha dois Pokémons diferentes.")
                    continue
                if 0 <= escolha1 < len(pokemons) and 0 <= escolha2 < len(pokemons):
                    p1 = pokemons[escolha1].copy()
                    p2 = pokemons[escolha2].copy()
                    print(f"\nIniciando batalha: {p1['nome']} vs {p2['nome']}")
                    while p1['vida'] > 0 and p2['vida'] > 0:
                        p2['vida'] -= p1['ataque']
                        print(f"{p1['nome']} atacou {p2['nome']}. Vida de {p2['nome']}: {max(p2['vida'],0)}")
                        if p2['vida'] <= 0:
                            print(f"{p2['nome']} foi derrotado! {p1['nome']} venceu a batalha!")
                            break
                        p1['vida'] -= p2['ataque']
                        print(f"{p2['nome']} atacou {p1['nome']}. Vida de {p1['nome']}: {max(p1['vida'],0)}")
                        if p1['vida'] <= 0:
                            print(f"{p1['nome']} foi derrotado! {p2['nome']} venceu a batalha!")
                            break
                else:
                    print("Número inválido.")
            except ValueError:
                print("Digite apenas números válidos.")

    elif opcao == "4":
        print("Saindo da Pokedex. Até logo!")
        break

    else:
        print("Opção inválida, tente novamente.")

