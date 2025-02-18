
palavraSecreta = 'python'  #palavra que foi definida
letrasCorretas = [] #armazenar as letras que o jogador acertar
continuar = 's'


while continuar == 's':
    #pede p colocar uma letra
    jogador = input('Digite uma letra: ').lower()

    #vê se essa letra está na palavra secreta
    if jogador in palavraSecreta:
        
        #ve se o jogador ja acertou essa letra antes
        if jogador not in letrasCorretas:
            letrasCorretas.append(jogador)  #adiciona a letra correta a lista
            print(f"Você acertou a letra '{jogador}'!")
        else:
            print(f"Você já adivinhou a letra '{jogador}'. Tente outra!")
    else:
       
        print(f"A letra '{jogador}' não está na palavra secreta!")

    #verifia se todas as letras foram advinhadas 
    acertouTodas = True
    for letra in palavraSecreta:
        if letra not in letrasCorretas:
            acertouTodas = False  
            break

    
    if acertouTodas:
        print(f"Parabéns! Você adivinhou todas as letras da palavra secreta: '{palavraSecreta}'")
        break

    
    continuar = input("Deseja continuar? [s]im - [n]ão: ").lower()

    if continuar != 's':
        print("Encerrando...")
