
class Item():
    def __init__(self, name,pocket):
        self.name = name
        self.pocket = pocket

    def find_use(self, player):
        if self.name == 'Potion':
            self.potion(player)
        elif self.name == 'Poké Ball':
            self.ball()

    def ball(self):
        print('You can\'t use that item here')
        
    def potion(self, player):
        print(f'You used a {self.name}!')
        print('Which one would you like to heal')
        while True:
            for index, pokemon in enumerate(player.pokemonBag):
                print(f'{index+1}. {pokemon.data.name}')
            choice = int(input('> '))
            for index, pokemon in enumerate(player.pokemonBag):
                if index+1 == choice:
                    if pokemon.data.health != pokemon.data.maxHealth:
                        pokemon.heal(20)
                        player.remove_item(self)
                        return
                    else:
                        print('This pokemon doesn\'t need healed')