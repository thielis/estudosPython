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
        return f"Olá! Meu nome é {self.nome}. Meu poder de ataque é {self.ataque} e tenho {self.vida} de vida!"

    def esta_vivo(self):
        return self.vida > 0

    def recebe_dano(self, ataque):
        self.vida -= ataque
        if self.vida < 0:
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
        return super().__str__() + f" Sou um defensor com {self.escudo} de escudo!"
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
        return super().__str__() + f" Sou um atacante com {self.taxa_critico} de taxa de crítico!"

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
        return not self.atacante.esta_vivo() and not self.defensor.esta_vivo()

    def realiza_ataque(self, personagem_atacado):
        personagem_atacado.recebe_dano(self.atacante.calcula_ataque())
        return personagem_atacado.esta_vivo()

class Round:
    """
    Propriedades:
        equipe_a : objeto Equipe A (tipo Equipe)
        equipe_b : objeto Equipe B (tipo Equipe)
    """
    def __init__(self, equipe_a, equipe_b):
        self.equipe_a = equipe_a
        self.equipe_b = equipe_b

    def houve_vencedor(self):
        if self.equipe_a.foi_derrotada() and not self.equipe_b.foi_derrotada():
            return f"{self.equipe_b.nome} venceu!"
        if not self.equipe_a.foi_derrotada() and self.equipe_b.foi_derrotada():
            return f"{self.equipe_a.nome} venceu!"
        return None

    def realiza_ataques(self):
        if self.equipe_b.defensor.esta_vivo():
            self.equipe_a.realiza_ataque(self.equipe_b.defensor)
        elif self.equipe_b.atacante.esta_vivo():
            self.equipe_a.realiza_ataque(self.equipe_b.atacante)
        else:
            print(f"Equipe {self.equipe_b.nome} está derrotada!")

        if self.equipe_a.defensor.esta_vivo():
            self.equipe_b.realiza_ataque(self.equipe_a.defensor)
        elif self.equipe_a.atacante.esta_vivo():
            self.equipe_b.realiza_ataque(self.equipe_a.atacante)
        else:
            print(f"Equipe {self.equipe_a.nome} está derrotada!")

class Partida:
    def __init__(self, equipe_a, equipe_b, qtd_rounds):
        self.equipe_a = equipe_a
        self.equipe_b = equipe_b
        self.qtd_rounds = qtd_rounds

    def realiza_partida(self):
        for round_num in range(1, self.qtd_rounds + 1):
            print(f"\n--- Round {round_num} ---")
            round_atual = Round(self.equipe_a, self.equipe_b)
            round_atual.realiza_ataques()
            vencedor = round_atual.houve_vencedor()
            if vencedor:
                print(f"O vencedor do round {round_num} é: {vencedor}")
                break
            else:
                print("A luta ainda não acabou!")
            print("Estado das equipes após o round:")
            print(self.equipe_a)
            print(self.equipe_b)

#executando
# Criando personagens para a equipe A
atacante_a = Atacante("Archer", 450, 80, 0.25)
defensor_a = Defensor("Brutus", 80, 150, 50)
equipe_a = Equipe("Valiant", atacante_a, defensor_a)

# Criando personagens para a equipe B
atacante_b = Atacante("Warrior", 300, 97, 0.3)
defensor_b = Defensor("Guardian", 90, 130, 65)
equipe_b = Equipe("Brave", atacante_b, defensor_b)

# Iniciando uma partida de combate com 3 rounds
partida = Partida(equipe_a, equipe_b, 3)
partida.realiza_partida()

# Exibindo o estado final das equipes
print("Estado final das equipes:")
print(equipe_a)
print(equipe_b)
