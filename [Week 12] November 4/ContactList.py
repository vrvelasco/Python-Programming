# Victor Velasco (ContactList) 11/4/19

def main():
    # Lists of information
    
    names = { 'Bruce Wayne' : 'BW', 'Clark Kent' : 'CK', 'Diana Prince' : 'DP' }
    emails = { 'BW' : 'bway@wayne-ent.com', 'CK' : 'clark.kent@dailyplanet.com', 'DP' : 'themyscira@yahoo.com' }
    addresses = { 'BW' : '1007 Mountain Dr.', 'CK' : '344 Clinton St.', 'DP' : '2890 W. 20th St.' }
    cities = { 'BW' : 'Gotham City', 'CK' : 'Metropolis', 'DP' : 'Washington' }
    states = { 'BW' : 'NJ', 'CK' : 'IL', 'DP' : 'D.C.' }
    zip_codes = { 'BW' : 12345, 'CK' : 62960, 'DP' : 20001 }
    phones = { 'BW' : '212-515-2505', 'CK' : '618-959-1906', 'DP' : '202-227-7362' }

    name = input('Enter a name: ') # Get name from user to search

    # Search and print if found
    if name not in names:
        print(name, 'is not a contact in your contact\'s list')
    else:
        initials = names[name]
        print(name, 'Contact Information:')
        print('Email:', emails[initials])
        print('Phone:', phones[initials])
        print('Address:', addresses[initials])
        print('City:', cities[initials])
        print('State:', states[initials])
        print('ZIP Code:', zip_codes[initials])

# Call main
main()
