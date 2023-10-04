lives = 3
countries = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cameroon', 'Central African Republic', 'Chad', 'Comoros', 'Ivory Coast', 'Djibouti', 'Democratic Republic Of The Congo', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Republic Of The Congo', 'Rwanda', 'Sao Tome & Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe' ]
guessed = []

print('---Countries of Africa---')
score = 0
while len(countries) > 0:
    print(len(countries), 'countries left')
    print('Score:', score)
    print('Lives:', lives)
    country = input('Enter the name of a country in Africa: ')
    if country.title() in countries:
        print('Good guess!')
        score = score + 1
        countries.remove(country.title())
        guessed.append(country.title())
    elif country.title() in guessed:
        print('You already guessed that!')
    else:
        print('Invalid guess')
        lives = lives - 1
    if lives == 0 or countries == 0:
        print ('Game Over')
        break 
            