class Personagem:
    """
    Propriedades:
        nome : nome do personagem (string)
        forca : poder de ataque (int ou float)
        vida : quantidade de dano suportado, o hp (int ou float)
    """
    def __init__(self, nome, ataque, vida):
        self.nome = nome
        self.ataque = ataque
        self.vida = vida

    def __str__(self):
        string_apresentacao = f"Olá! Meu nome é {self.nome}. Meu poder de ataque é {self.ataque} e tenho {self.vida} de vida!"
        return string_apresentacao

    def esta_vivo(self):
        return self.vida > 0

    def recebe_dano(self, ataque):
        self.vida -= ataque
        if(self.vida < 0):
          self.vida = 0

class Defensor(Personagem):
    """
    Propriedades:
        nome : nome do personagem (string)
        forca : poder de ataque (int ou float)
        vida : quantidade de dano suportado, o hp (int ou float)
        escudo: quantidade extra de vida(int ou float)
    """
    def __init__(self, nome, ataque, vida, escudo):
        super().__init__(nome, ataque, vida)
        self.escudo = escudo

    def __str__(self):
        return super().__str__() + f"Sou um defensor com {self.escudo} de escudo!"

    '''
    Essa funcao processa um ataque recebido de outro personagem levando
    em conta o escudo do defensor; para isso, sobrescrevemos a função
    recebe_dano
    '''
    def recebe_dano(self, ataque):
        if self.escudo > 0:
          if (self.escudo - ataque) >= 0: #verifica se o escudo vai aguentar todo o dano recebido
              self.escudo -= ataque
          else: #caso em que o escudo aguentou apenas uma parte do dano
              self.vida -= (ataque - self.escudo)
              self.escudo = 0

              if(self.vida < 0):
                self.vida = 0
        else:
            self.vida -= ataque

            if(self.vida < 0):
                self.vida = 0

class Atacante(Personagem):
  """
    Propriedades:
        nome : nome do personagem (string)
        forca : poder de ataque (int ou float)
        vida : quantidade de dano suportado, o hp (int ou float)
        taxa_critico : taxa de dano crítico (float)
  """
  def __init__(self, nome, ataque, vida, taxa_critico):
    super().__init__(nome, ataque, vida)
    self.taxa_critico = taxa_critico

  def __str__(self):
    return super().__str__() + f"Sou um atacante com {self.taxa_critico} de taxa de critico!"

  def calcula_ataque(self):
    return self.ataque + (self.ataque * self.taxa_critico)

class Equipe:
    """
    Propriedades:
        nome : nome da equipe (string)
        atacante : personagem do tipo Atacante
        defensor : personagem do tipo Defensor
    """
    def __init__(self, nome, atacante, defensor):
        self.nome = nome
        self.atacante = atacante
        self.defensor = defensor

    def __str__(self):
        apresentacao = f"Equipe {self.nome}"
        if self.atacante.esta_vivo():
            apresentacao += f"\nAtacante: {self.atacante}"
        if self.defensor.esta_vivo():
            apresentacao += f"\nDefensor: {self.defensor}"
        return apresentacao

    def foi_derrotada(self):
        #defina esta função aqui!
        if self.atacante.esta_vivo() == False and self.defensor.esta_vivo() == False:
          return "Equipe derrotada!"
        else:
          return "Equipe ainda no jogo!"

    def realiza_ataque(self, persoangem_atacado):
        #lembre-se de usar bem os métodos que já foram definidos!
        #Em caso de dúvida, não hesite em falar com a gente :p
        persoangem_atacado.recebe_dano(self.atacante.calcula_ataque())
        return persoangem_atacado.esta_vivo()
    
class Round:
    """
    Propriedades:
        equipe_a : objeto Equipe A (tipo Equipe)
        equipe_b : objeto Equipe B (tipo Equipe)
    """
    def __init__(self, equipe_a, equipe_b, data):
        self.equipe_a = equipe_a
        self.equipe_b = equipe_b

    def houve_vencedor(self):
        if self.equipe_a.foi_derrotada() and not(self.equipe_b.foi_derrotada()):
            return f"{self.equipe_b.nome} venceu!"
        if not(self.equipe_a.foi_derrotada()) and self.equipe_b.foi_derrotada():
            return f"{self.equipe_a.nome} venceu!"
        else:
            return 0

    def realiza_ataques(self):
      #Escreva a solução aqui!
      if self.equipe_b.defensor.esta_vivo():
        self.equipe_a.realiza_ataque(self.equipe_b.defensor)
      elif self.equipe_b.atacante.esta_vivo():
        self.equipe_a.realiza_ataque(self.equipe_b.atacante)
      else:
        print(f"Equipe {equipe_b.nome} está derrotada!")

#Utilize as técnicas aprendidas e sua criatividade para concluir nosso sistema
#de batalha com chave de ouro!
class Partida(Round):
  """
    Propriedades:
        equipe_a : objeto Equipe A (tipo Equipe)
        equipe_b : objeto Equipe B (tipo Equipe)
        data : quantidade de rounds (int)
    """
  def __init__(self, equipe_a, equipe_b, data):
    super().__init__(equipe_a, equipe_b)
    self.data = data

  def realiza_partida(self):
    qtd_partidas = self.data
    round_atual = Round(equipe_a, equipe_b)
    for rounds in range(qtd_partidas):
      if rounds % 2 != 0:
        round_atual.realiza_ataques()
        round_atual = Round(equipe_b, equipe_a)
        if self.houve_vencedor() == 0:
          print("Mais um Round!")
      if rounds % 2 == 0:
        round_atual.realiza_ataques()
        round_atual = Round(equipe_a, equipe_b)
        if self.houve_vencedor() == 0:
          print("Mais um Round!")

# Criando personagens para a equipe A
atacante_a = Atacante("Archer", 450, 80, 0.25)
defensor_a = Defensor("Brutus", 80, 150, 50)
equipe_a = Equipe("Valiant", atacante_a, defensor_a)

# Criando personagens para a equipe B
atacante_b = Atacante("Warrior", 300, 97, 0.3)
defensor_b = Defensor("Guardian", 90, 130, 65)
equipe_b = Equipe("Brave", atacante_b, defensor_b)

# Iniciando um round de combate
round_1 = Round(equipe_a, equipe_b)

#Realizando os ataques do round
round_1.realiza_ataques()

# Verificando se houve vencedor nesse round
resultado = round_1.houve_vencedor()
if resultado == 0:
    print("A luta ainda não acabou!")
else:
    print(f"O vencedor do round é: {resultado}")

# Exibindo o estado final das equipes
print("Estado das equipes após o round 1:")
print(equipe_a)
print(equipe_b)