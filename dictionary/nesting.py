alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 15}
alien_2 = {'color': 'blue', 'points': 25}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# make 30 aliens
aliens2 = []

for alien_number in range(30):
    new_alien = {'alien-id': alien_number, 'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens2.append(new_alien)

for alien in aliens2[:5]:
    print(alien)

print(f"Total number of aliens: {len(aliens2)}")
