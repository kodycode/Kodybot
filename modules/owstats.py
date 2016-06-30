from bs4 import BeautifulSoup
import urllib.request

class OWStats:

    def __init__(self, battle_tag):
        self.battle_tag = battle_tag
        self.URL = 'https://playoverwatch.com/en-us/career/pc/us/' + battle_tag
        self.html_source = urllib.request.urlopen(self.URL)
        self.level = '0'

    async def get_level(self):
        soup = BeautifulSoup(self.html_source, 'html.parser')

        level = soup.find('div', {'class': 'u-vertical-center'})
        
        prestige1 = soup.find('div', {'style': 'background-image:url(https://' +
                                     'blzgdapipro-a.akamaihd.net/game/playerlevelrewards/0x025000000000092B_Rank.png)'})
        prestige2 = soup.find('div', {'style': 'background-image:url(https://' +
                                      'blzgdapipro-a.akamaihd.net/game/playerlevelrewards/0x0250000000000951_Rank.png)'})
        prestige3 = soup.find('div', {'style': 'background-image:url(https://' +
                                      'blzgdapipro-a.akamaihd.net/game/playerlevelrewards/0x0250000000000952_Rank.png)'})
        prestige4 = soup.find('div', {'style': 'background-image:url(https://' +
                                      'blzgdapipro-a.akamaihd.net/game/playerlevelrewards/0x0250000000000953_Rank.png)'})
        prestige5 = soup.find('div', {'style': 'background-image:url(https://' +
                                      'blzgdapipro-a.akamaihd.net/game/playerlevelrewards/0x0250000000000954_Rank.png)'})

        if (prestige1):
            self.level = str(int(level.text) + int(100))
        elif(prestige2):
            self.level = str(int(level.text) + int(200))
        elif(prestige3):
            self.level = str(int(level.text) + int(300))
        elif (prestige4):
            self.level = str(int(level.text) + int(400))
        elif (prestige5):
            self.level = str(int(level.text) + int(500))
        else:
            self.level = str(level.text)
        

    async def display_level(self, client, channel):
            await client.send_message(channel, self.battle_tag + ' is level ' + self.level)
