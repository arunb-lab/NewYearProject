alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
print(alien_0['color'])
print(aliens)
for alien in aliens:
    print(alien)
for alien in aliens:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
print("\nUpdated aliens:")
for alien in aliens:
    print(alien)
    