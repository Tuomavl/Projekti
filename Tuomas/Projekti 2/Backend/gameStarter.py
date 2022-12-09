from game import Game

game = Game()

print("\n")

value = game.player.flyTo()
if value == -1:
    print(f'Maassa {game.player.location} ei ole ketään.')
else:
    print(f'Maassa {game.player.location} on: {game.Suspects[value].name}')
    text = game.Suspects[value].accuse().format(playerName=game.player.username, addSuspect=game.person_dictionary[game.Suspects[value]])
    print(text)