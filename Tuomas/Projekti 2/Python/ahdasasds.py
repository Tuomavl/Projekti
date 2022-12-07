
#print('\n'+player.location)

value = player.flyTo()
if value == -1:
    print(f'Maassa {player.location} ei ole ketään.')
else:
    print(f'Maassa {player.location} on: {Suspects[value].name}')
    text = Suspects[value].accuse().format(playerName=player.username, addSuspect=person_dictionary[Suspects[value]])
    print(text)