# 99300 Pedro Rodrigues
"""
Esta funcao recebe um argumento e devolve True se tiver um tabuleiro valido
"""
def eh_tabuleiro(tab):
   if not (isinstance(tab, tuple) and len(tab) == 3):
      return False
   for l in tab:
      if not eh_linha(l):
         return False
   return True

"""
Esta funcao verifica se cada linha (sub-tuplo) tem exatamente tres elementos
"""
def eh_linha(l):
    if not (isinstance(l, tuple) and len(l) == 3):
        return False
    for n in l:
        if not eh_elemento(n):
            return False            
    return True

"""
Esta funcao verifica se cada posicao do tabuleiro tem valor -1, 0 ou 1
"""
def eh_elemento(n):
    if (isinstance(n, int) and (n>= -1) and (n<= 1)):
        return True
    else:
        return False
 
"""   
Esta funcao recebe um argumento de qualquer tipo e devolve True se o seu argumento
corresponde a uma posicao
"""
def eh_posicao(nr):
    if (isinstance(nr, int)) and (nr>=1) and (nr<=9):
        return True
    else:
        return False

"""    
Esta funcao verifica se o numero da coluna esta entre 1 e 3
"""
def eh_coluna(c):
    if c>=1 and c<=3:
        return True
    return False

"""
Esta funcao recebe um tabuleiro e um inteiro com valor de 1 a 3 que representa
o nr da coluna e devolve um vetor com os valores dessa coluna
"""
def obter_coluna(tab,c):
    if not (isinstance(tab, tuple) or c>3 or c<1):
      raise ValueError('obter_coluna: algum dos argumentos e invalido')
    else:
      col = ()
      for i in range (0,3):
         m = tab[i]
         n = m[c-1]
         n = (n, )
         col = col + n
      return col

"""
Esta funcao recebe um tabuleiro e um inteiro com valor de 1 a 3 que representa
o numero da linha e devolve um vector com os valores dessa linha
"""
def obter_linha(tab,l):
    if not (isinstance(tab, tuple)) or l<1 or l>3:
        raise ValueError('obter_linha: algum dos argumentos e invalido')
    else:
        linha = tab[l-1]
        linha = (linha)
    return linha
 
"""  
Esta funcao recebe um tabuleiro e um inteiro que representa a direcao da diagonal
1 para descendente da esquerda para a direita e 2 para ascendente da esquerda 
para a direita e devolve um vector com os valores dessa diagonal    
"""
def obter_diagonal(tab,d):
    if not (isinstance(tab, tuple)) or d>2 or d<1:
        raise ValueError('obter_diagonal: algum dos argumentos e invalido')
    else:
        if d==1:
            diagonal=()
            a = tab[0][0]
            a = (a, )
            b = tab[1][1]
            b = (b, )
            c = tab[2][2]
            c = (c, )
        else:
            diagonal=()
            a = tab[2][0]
            a = (a, )
            b = tab[1][1]
            b = (b, )
            c = tab[0][2]
            c = (c, )
        diagonal = diagonal + a + b + c
    return diagonal

"""
Esta funcao recebe um tabuleiro e devolve a cadeia de caracteres que o representa
atraves da soma da cadeia de caracteres de cada linha que o completa
"""
def tabuleiro_str(tab):
    if not (eh_tabuleiro(tab)):
        raise ValueError('tabuleiro_str: o argumento e invalido')
    else:
        space_t = '' 
        for linha in tab:
            space_t = space_t + nova_linha(linha)
        return space_t[:-len('\n-----------\n')]
 
""" 
Esta funcao devolve a cadeira de caracteres que representa uma so linha 
"""
def nova_linha(l):
    linha = ''
    for s in l:
        if s == -1:
            (s) = (' O ')
        if s == 0:
            (s) = ('   ')
        if s == 1:
            (s) = (' X ')
        linha = linha + str(s) + '|'  
    linha = linha[:-1]
    return (linha) + '\n-----------\n'

"""
Esta funcao recebe um tabuleiro e uma posicao e devolve True se a posicao 
corresponde a uma posicao livre do tabuleiro
"""
def eh_posicao_livre(tab, p):
    if not (eh_tabuleiro(tab) and isinstance(p,int) and (p>=1) and (p<=9)):
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
    else:
        con = ()
        for l in tab:
            for c in l:
                con = con + (c, )        
        if con[p-1] == 0:
            return True
        else:
            return False

"""    
Esta funcao recebe um tabuleiro e devolve o vetor ordenado com todas as posicoes
livres do tabuleiro
"""
def obter_posicoes_livres(tab):
    if not eh_tabuleiro(tab):
       raise ValueError('obter_posicoes_livres: o argumento e invalido')
    else: 
      livres = ()
      posicoes = ()
      for i in range(0,3):
         a = tab[i]
         for i in range(0,3):
            b = a[i]
            posicoes = posicoes + (b, )
      for b in range(0,9):
         c = posicoes[b]
         if c == 0:
            livres = livres + (b + 1, )
      return livres

"""
Esta funcao recebe um tabuleiro e devolve um valor inteiro a indicar o jogador
que ganhou a partida no tabuleiro passado por argumento, sendo 1 se X ganhou
ou -1 se O ganhou ou 0 se nao ganhou nenhum jogador
"""
def jogador_ganhador(tab):
    if not (eh_tabuleiro(tab)):
       raise ValueError('jogador_ganhador: o argumento e invalido')
    else:
       for l in range(1,4):
         linha = obter_linha(tab,l)
         if linha[0] == linha[1] == linha[2]:
            ganhador = linha[0]     
            return ganhador
       for c in range(1,4):
         col = obter_coluna(tab,c)
         if col[0] == col[1] == col[2]:
            ganhador = col[0]
            return ganhador
       for d in range(1,3):
         diagonal = obter_diagonal(tab,d)
         if diagonal[0] == diagonal[1] == diagonal[2]:
            ganhador = diagonal[0]
            return ganhador
       return 0

"""
Esta funcao recebe um tabuleiro e um inteiro identificando o jogador 
(1 para o jogador X ou -1 para o jogador O) e uma posicao livre e devolve
um novo tabuleiro modificado com uma nova marca do jogador nessa posicao
"""
def marcar_posicao(tab, n, nr):
   if not (eh_tabuleiro(tab) or eh_elemento(n) or eh_posicao_livre(tab,nr)): 
      raise ValueError('marcar_posicao: algum dos argumentos e invalido')
   else:
      posicao = 0
      novo = ()
      tuplof = ()
      for i in range(3):
         for j in range(3):
            posicao = posicao + 1
            if posicao == nr and (n==1 or n==-1) and tab[i][j]==0:
               novo += (n, )                
            else: 
               novo += (tab[i][j], )
      for i in range(0,9,3):
         tuplof += ((novo[i], novo[i+1], novo[i+2]), ) 
      return tuplof

"""   
Esta funcao realiza a leitura de uma posicao introduzida manualmente por um 
jogador e devolve esta posicao escolhida
"""
def escolher_posicao_manual(tab):
   if not eh_tabuleiro(tab):
      raise ValueError('escolher_posicao_manual: o argumento e invalido.')
   else:
      a = int(input('Turno do jogador. Escolha uma posicao livre: '))
      if a<1 or a>9:
         raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida.')
      if not (eh_posicao_livre(tab,a)):
         raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida.')
      else:
         return a

"""
Esta funcao verifica se uma posicao esta ocupada ou nao pelo jogador
Tem as mesmas funcionalidades que a posicao livre mas em vez de verificar se 
esta livre verifica sim se esta ocupada pelo jogador
"""
def eh_posicao_jog(tab, p, player):
   con = ()
   for l in tab:
      for c in l:
         con = con + (c, )        
   if con[p-1] == player:
      return True
   else:
      return False

"""   
Esta funcao recebe um tabuleiro, um inteiro identificando um jogador (1 para o 
jogador X ou -1 para o jogador O) e uma cadeia de carateres correspondente 
a estrategia, e devolve a posicao escolhida automaticamente de acordo com a 
estrategia seleccionada (basico, normal ou perfeito)
"""
def escolher_posicao_auto(tab, player, cad):
   if not (eh_tabuleiro(tab) or (player == 1 or player == -1) or isinstance(cad, str)):
      raise ValueError('escolher_posicao_auto: algum dos argumentos e invalido.')
   if not (cad == 'basico' or cad == 'normal' or cad == 'perfeito'):
      raise ValueError('escolher_posicao_auto: algum dos argumentos e invalido.')
   else:
      if cad == 'basico':
         if eh_posicao_livre(tab,5):  #verificar se a posicao central esta livre
            return 5
         i = 1
         while i < 10:     #verificar se tem um canto vazio
            if eh_posicao_livre(tab, i):
               return i
            i += 2
         i = 2
         while i < 9:     #verificar se tem uma lateral vazia
            if eh_posicao_livre(tab, i):
               return i
            i += 2
      if cad == 'normal':
         for i in range(1,10):             #verificar se tem duas pecas em linha
            if eh_posicao_livre(tab,i):    #e uma posicao livre para marcar
               if jogador_ganhador(marcar_posicao(tab, player, i)):
                  return i
         for i in range(1,10):             #verificar se o adversario tem duas
            if eh_posicao_livre(tab,i):    #em linha e marcar la para bloquear
               if jogador_ganhador(marcar_posicao(tab, player*(-1), i)):
                  return i            
         if eh_posicao_livre(tab,5):  #verificar se a posicao central esta livre
            return 5
         i = 1           #Se o adversario estiver num canto e se o canto 
         l = 9           #diagonalmente oposto for uma posicao livre
         while i < 10:   #entao jogar nesse canto oposto
            if eh_posicao_jog(tab ,i, player*(-1)) and eh_posicao_livre(tab, l):
               return l
            i += 2
            l -= 2
         i = 1
         while i < 10:      #verificar se tem um canto vazio
            if eh_posicao_livre(tab, i):
               return i
            i += 2
         i = 2
         while i < 9:       #verificar se tem uma lateral vazia
            if eh_posicao_livre(tab, i):
               return i
            i += 2        
      if cad == 'perfeito':
         for i in range(1,10):            #verificar se tem duas pecas em linha
            if eh_posicao_livre(tab,i):   #e uma posicao livre para marcar
               if jogador_ganhador(marcar_posicao(tab, player, i)):
                  return i
         for i in range(1,10):            #verificar se o adversario tem duas
            if eh_posicao_livre(tab,i):   #em linha e marcar la para bloquear
               if jogador_ganhador(marcar_posicao(tab, player*(-1), i)):
                  return i            
         if eh_posicao_livre(tab,5):  #verificar se a posicao central esta livre
            return 5
         i = 1              #Se o adversario estiver num canto e se o canto 
         l = 9              #diagonalmente oposto for uma posicao livre
         while i < 10:      #entao jogar nesse canto oposto
            if eh_posicao_jog(tab ,i, player*(-1)) and eh_posicao_livre(tab, l):
               return l
            i += 2
            l -= 2
         i = 1
         while i < 10:       #verificar se tem um canto vazio
            if eh_posicao_livre(tab, i):
               return i
            i += 2
         i = 2
         while i < 9:        #verificar se tem uma lateral vazia
            if eh_posicao_livre(tab, i):
               return i
            i += 2
 
""" 
Esta funcao principal corresponde a funcao que permite jogar um jogo completo 
do Jogo do Galo de um jogador contra o computador. O jogo comeca sempre com o jogador
X a marcar uma posicao livre e termina quando um dos jogadores vence ou, se nao
existem posicoes livres no tabuleiro. 
O primeiro argumento corresponde a escolher entre (X ou O) dependendo do que 
o jogador humano pretende utilizar
O segundo argumento indica a estrategia de jogo utilizada pela maquina
"""
def jogo_do_galo(jog, estrategia):
   if not (jog != 'O' or jog != 'X'):
      raise ValueError('jogo_do_galo: algum dos argumentos e invalido.')
   else:
      tab = ((0,0,0),(0,0,0),(0,0,0))
      print('Bem-vindo ao JOGO DO GALO.')
      print("O jogador joga com '%s'." % jog) 
      jogadas = 0
      while jogadas<10:
         if str(jog) == 'O':
            print('Turno do computador (%s):' % estrategia)
            a = escolher_posicao_auto(tab,-1,estrategia)
            tab = marcar_posicao(tab, -1, a)
            print(tabuleiro_str(tab))
            if jogador_ganhador(tab):
               return 'O'
            jogadas +=1
            if jogadas==9:
               break
            a = escolher_posicao_manual(tab)
            tab = marcar_posicao(tab, 1, a)
            print(tabuleiro_str(tab))
            if jogador_ganhador(tab):
               return 'X'
            jogadas +=1
         else:
            a = escolher_posicao_manual(tab)
            tab = marcar_posicao(tab, 1, a)
            print(tabuleiro_str(tab))
            if jogador_ganhador(tab):
               return 'X'
            jogadas +=1            
            print('Turno do computador (%s):' % estrategia)
            a = escolher_posicao_auto(tab,-1,estrategia)
            tab = marcar_posicao(tab, -1, a)
            print(tabuleiro_str(tab))
            if jogador_ganhador(tab):
               return 'O'
            jogadas +=1 
      return 'EMPATE'