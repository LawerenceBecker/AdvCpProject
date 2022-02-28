def effective(attPokeType, defPokeType):

  attPokeType = attPokeType.title()
  defPokeType = defPokeType.title()
  
  try:
    efficacy = effectivity[types[attPokeType]][types[defPokeType]]
  
    if efficacy == 1.6:
      return "Super effective!"
    elif efficacy == .625:
      return "Not very effective..."
    elif efficacy == .39:
      return "Defending pokémon is immune!"
    else:
      return "No effectivity"
  except:
    return "Invalid types"

# types and their places in the table
types = {'Bug': 0, 'Dark': 1, 'Dragon': 2, 'Electric': 3, 'Fairy': 4, 'Fighting': 5, 'Fire': 6, 'Flying': 7, 'Ghost': 8, 'Grass': 9, 'Ground': 10, 'Ice': 11, 'Normal': 12, 'Poison': 13, 'Psychic': 14, 'Rock': 15, 'Steel': 16, 'Water' : 17}

# effectivity table 
## found here: https://gamepress.gg/pokemongo/damage-mechanics
effectivity = [
[1, 1.6, 1, 1, .625, .625, .625, .625, .625, 1.6, 1, 1, 1, .625, .625],
[1, .625, 1, 1, .625, .625, 1, 1, 1.6, 1, 1, 1, 1, 1, 1.6, 1, 1, 1], 
[1, 1, 1.6, 1, .39, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, .625, 1], 
[1, 1, .625, .625, 1, 1, 1, 1.6, 1, .625, .39, 1, 1, 1, 1, 1, 1, 1.6],
[1, 1.6, 1.6, 1, 1, 1.6, .625, 1, 1, 1, 1, 1, 1, .625, 1, 1, .625, 1],
[.625, 1.6, 1, 1, .625, 1, 1, .625, .39, 1, 1, 1.6, 1.6, .625, .625, 1.6, 1.6, 1],
[1.6, 1, .625, 1, 1, 1, .625, 1, 1, 1.6, 1, 1.6, 1, 1, 1, .625, 1.6, .625],
[1.6, 1, 1, .625, 1, 1.6, 1, 1, 1, 1.6, 1, 1, 1, 1, 1, .625, .625, 1],
[1, .625, 1, 1, 1, 1, 1, 1, 1.6, 1, 1, 1, .39, 1, 1.6, 1, 1, 1],
[.625, 1, .625, 1, 1, 1, .625, .625, 1, .625, 1.6, 1, 1, .625, 1, 1.6, .625, 1.6],
[.625, 1, 1, 1.6, 1, 1, 1.6, .39, 1, .625, 1, 1, 1, 1.6, 1, 1.6, 1.6, 1],
[1, 1, 1.6, 1, 1, 1, .625, 1.6, 1, 1.6, 1.6, .625, 1, 1, 1, 1, .625, .625],
[1, 1, 1, 1, 1, 1, 1, 1, .39, 1, 1, 1, 1, 1, 1, .625, .625, 1],
[1, 1, 1, 1, 1.6, 1, 1, 1, .625, 1.6, .625, 1, 1, .625, 1, .625, .39, 1],
[1, .39, 1, 1, 1, 1.6, 1, 1, 1, 1, 1, 1, 1, 1.6, .625, 1, .625, 1],
[1.6, 1, 1, 1, 1, .625, 1.6, 1.6, 1, 1, .625, 1.6, 1, 1, 1, 1, .625, 1],
[1, 1, 1, .625, 1.6, 1, .625, 1, 1, 1, 1, 1.6, 1, 1, 1, 1.6, .625, .625],
[1, 1, .625, 1, 1, 1, 1.6, 1, 1, .625, 1.6, 1, 1, 1, 1, 1.6, 1, .625]]

