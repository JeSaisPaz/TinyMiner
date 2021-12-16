from termcolor import colored
import requests
import os
import time
import json

def bitcoin_value():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    return float(data["bpi"]["USD"]["rate"].replace(",",""))

class BTCminer:
    def __init__(self):
        self.money = 150 # Modify this to cheat
        self.crypto = 0
        self.hashrate = 0

    def save_game(self):
        save_data = {
            "money": str(self.money),
            "crypto": str(self.crypto),
            "hashrate": str(self.hashrate)
        }
        jsondata = open("save_game.json", "w")
        jsondata.write(json.dumps(save_data))
        jsondata.close()

    def load_game(self):
        open_save = open("save_game.json", "r")
        content = json.loads(open_save.read())
        self.money = float(content["money"])
        self.crypto = float(content["crypto"])
        self.hashrate = float(content["hashrate"])

    def mine(self):
        if self.hashrate == 0:
            print("Buy a graphic card first")
            time.sleep(3)
            os.system("cls")
        else:
            for x in range(1, 10):
                    os.system('cls')
                    print("[]"*x + ((9 - x) * "--" ))
                    if x == 9:
                        print("Done !")
                    else:
                        print("Mining...")
                    self.crypto += (0.000021*self.hashrate)
                    time.sleep(0.3)

    def shop(self):
            os.system("cls")
            round(self.money, 2)
            print("money: " + str(self.money))
            print(colored("""
Welcome to the Shop
- GTX 1030 | $150
- GTX 1060 | $200
- GTX 1060 Ti | $250
- Radeon 5700x | $300
- RTX 2060 | $350
- RTX 2070s | $400
- RTX 3060 | $450
- RTX 3070 | $500
- RTX 3080 | $550
- RTX 3080 Ti | 1000
- RTX 3090 Ti | $1500
""", "cyan"))
            choice = input("Choose graphic card > ")
            if choice == "GTX 1030":
                if self.money >= 150:   
                    self.money -= 150
                    self.hashrate += 2
                else:
                    print("NOT ENOUGH MONEY")
            elif choice == "GTX 1060":
                if self.money >= 200:
                    self.money -= 200
                    self.hashrate += 4
                else:
                    print("NOT ENOUGH MONEY")
            elif choice == "GTX 1060 Ti":
                if self.money >= 250:
                    self.money -= 250
                    self.hashrate += 6
                else:
                    print("NOT ENOUGH MONEY")
            elif choice == "Radeon 5700x":
                if self.money >= 300:
                   self.money -= 300
                   self.hashrate += 8
                else:
                    print("NOT ENOUGH MONEY")
            elif choice == "RTX 2060":
                if self.money >= 350:
                    self.money -= 350
                    self.hashrate += 10
                else:
                    print("NOT ENOUGH MONEY")
            elif choice == "RTX 2070s":
                if self.money >= 400:
                    self.money -= 400
                    self.hashrate += 12
                else:
                    print("NOT ENOUGH MONEY")
            elif choice == "RTX 3060":
                if self.money >= 450:
                    self.money -= 450
                    self.hashrate += 14
            elif choice == "RTX 3070":
                if self.money >= 500:
                    self.money -= 500
                    self.hashrate += 16
                else:
                    print("NOT ENOUGH MONEY")
            elif choice == "RTX 3080":
                if self.money >= 550:
                    self.money -= 550
                    self.hashrate += 18
                else:
                    print("NOT ENOUGH MONEY")
            elif choice == "RTX 3080 Ti":
                if self.money >= 1000:
                    self.money -= 1000
                    self.hashrate += 20
                else:
                    print("NOT ENOUGH MONEY")
            elif choice == "RTX 3090 Ti":
                if self.money >= 1000:
                    self.money -= 1000
                    self.hashrate += 25
                else:
                    print("NOT ENOUGH MONEY")

    def sellcrypto(self):
        cryptotosell = input("" + str(self.crypto) + " Type *sell_all* do you want to sell everything (type *cancel* to cancel) > ")
        if cryptotosell == "sell_all":
            tosell = self.crypto
            self.money += tosell*bitcoin_value()
            self.crypto -= tosell
        elif cryptotosell == "cancel":
            main()
        else:
            print("ERROR, NOT ENOUGH CRYPTO")
    
def main():
    
    running = True

    btcminer = BTCminer()
    print(colored("""
MMMMMMMMMMMMMMMMMMMMNmmmmmmmmmmmmmmmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmmmmmmmmmNMMMMMMMMMMm
MMMMMMMMMMMMMMMMMMMMh++++++++++++++oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo++++++++dMMMMMMMMMMm
MMMMMMMMMMMMMMdhhhhhhhdhdhdhhhhhhhhhyyhMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNhyyhhdhhhdhhhhhmMMMMMMMm
MMMMMMMMMMMNNNs++ooohMMMNNNNNNNNNNNmoosNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmoooNMMMMMMMMy++hMMMMMMMm
MMMMMMMMMMMyoo+++hNNNMMdooooooooooosNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNoosmNNMMMMMMMMMy++hMMMMMMMm
MMMMMMMMMMMs++syymMMmddhyyyyyyyyyyyyMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdddyyyMMMdddNMMMMMy++hMMMMMMMm
MMMMMMMMMMMs++dMMMMMy++yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm++oNMMMMNo++mMMMMMy++hMMMMMMMm
MMMMMMMNyssdmmNMMhsso++osshMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmmdssssssdmmNMMysshmmNMMMMMMMm
MMMMMMMNo++mMMNmNysoo+++++smmNMMMMMMMMMNNNNNNNNNNNNNNNNNNNNmNMMMMMMMMNmmm++++++NMMNmmyssmMMMMMMMMMMm
MMMMMMMNo++mMMs++dMMy++++++++sMMMMMMMMN+++++++++++++++++++++yMMMMMMMMm+++++++++NMMs++mMMMMMMMMMMMMMm
MMMMMMMNo++mMMs++dMMmhhs++shhdMMNyyyyyyhhhhhhhhhhhhhhhhhhhhhyyyyyyhMMNhhh+++hhhyyyhhhNMMMMMMMMMMMMMm
MMMMMMMNo++mMMs++dMMMMMdooyMMMNNmooooooNMMNNNNNNNNNNNNNNNMMMdooooosNNNMMNoooNMNooomMMMMMMMMMMMMMMMMm
MMMMMMMNo++mMMs++dMMMMMNNNNMMmoosmNNNNNMMMsoooooooooooooodMMNNNNNNdooyMMMNNNMMMNNNMMMMMMMMMMMMMMMMMm
MMMMMMMNo++mMMs++dMMMMMMMMNddhyyhMMMdddddd+++syyo++syyo++ydddddmMMmyyydddMMMMMMMMMMMMMMMMMMMMMMMMMMm
MMMMMMMNo++mMMs++dMMMMMMMMd++sMMMMMN+++++++++mMMs++dMMy++++++++yMMMMMm++oMMMMMMMMMMMMMMMMMMMMMMMMMMm
MMMMMMMMmmmysshmmNMMMMMMMMd++sMMmsss+++++++++NMMs++dMMy++++++++osshMMm++oMMMMMMMMMMMMMMMMMMMMMMMMMMm
MMMMMMMMMMMyoomMMMMMMMMNmmhooyMMm++++++ooooooNMMyoomMMhooo++++++++sMMmoosmmNMMMMMMMMMMMMMMMMMMMMMMMm
MMMMMMMMMMMMMMMMMMMMMMMd++yMMMMMm+++++oNNMMMMMMMMMMMMMMMNh++++++++sMMMMMN++oNMMMMMMMMMMMMMMMMMMMMMMm
MMMMMMMMMMMMMMMMMMMMMMMd++yMMNhhy++++++yhhNMMMMMdhhhhhmMMmhhs+++++ohhdMMN++oNMMMMMMMMMMMMMMMMMMMMMMm
MMMMMMMMMMMMMMMMMMMMMMMd++yMMm++++++++++++NMMMMMs+++++dMMMMMh++++++++sMMN++oNMMMMMMMMMMMMMMMMMMMMMMm
MMMMMMMMMMMMMMMMMMMMMMMd++yMMm++++++++++++NMMMMMs+++++dMMMMMh++++++++sMMN++oNMMMMMMMMMMMMMMMMMMMMMMm
MMMMMMMMMMMMMMMMMMMMMMMd++yMMm++++++++++++NMMMMMhsyyyymMMmddy++++++++sMMN++oNMMMMMMMMMMMMMMMMMMMMMMm
MMMMMMMMMMMMMMMMMMMMMMMd++yMMm++++++++++++NMMMMMMMMMMMMMMh+++++++++++sMMN++oNMMMMMMMMMMMMMMMMMMMMMMm
MMMMMMMMMMMMMMMMMMMMMMMd++yMMm++++++++++++NMMMMMysssssdMMNmmy++++++++sMMN++oNMMMMMMMMMMMMMMMMMMMMMMm
MMMMMMMMMMMMMMMMMMMMMMMd++yMMm++++++++++++NMMMMMs+++++dMMMMMh++++++++sMMN++oNMMMMMMMMMMMMMMMMMMMMMMm
MMMMMMMMMMMMMMMMMMMMMMMd++yMMm++++++++++++NMMMMMs+++++hMMMMMh++++++++sMMN++oNMMMMMMMMMMMMMMMMMMMMMMm
MMMMMMMM7MMMMMMMMMMMMMMMd++yMMNhhy++++++hhhNMMMMMdhhhhhmMMmhhs+++++ohhdMMN++oNMMMMMMMMMMMMMMMMMMMMMm
MMMMMMMMMMMMMMMMMMMMMMMdooyNNNMMm+++++oNNNNNNMMMNNNMMMNNNy++++++++sMMMNNmoooNMMMMMMMMMMMMMMMMMMMMMMm
MMMMMMMMMMMMMMMMMMMMMMMNmmhooyMMm++++++ooooosNMMyoomMMhooo++++++++sMMmoosmmNMMMMMMMMMMMMMMMMMMMMMMMm
MMMMMMMMMMMMMMMMMMMMMMMMMMd++sMMmyys+++++++++NMMs++dMMy++++++++oyyhMMm++oMMMMMMMMMMMMMMMMMMMMMMMMMMm
MMMMMMMMMMMMMMMMMMMMMMMMMMd++sMMMMMN+++++++++mMMs++dMMy++++++++yMMMMMm++oMMMMMMMMMMMMMMMMMMMMMMMMMMm
MMMMMMMMMMMMMMMMMMMMMMMMMMNddhssyMMMdddddd+++sss+++ssso++ydddddmMMmssydddMMMMMMMMMMMMMMMMMMMMMMMMMMm
MMMMMMMMMMMMMMMMMMMMMMMMNNNMMmoosNNNNNNMMMsoooooooooooooodMMNNNNNNdooyMMMNNNMMMMMMMMMMMMMMMMMMMMMMMm
MMMMMMMMMMMMMMMMMMMMMMMd++yMMMMMm+++++oNMMMMMMMMMMMMMMMMMMMMh+++++sMMMMMN++oNMMMMMMMMMMMMMMMMMMMMMMm
MMMMMMMMMMMMMMMMMMMMmhhs++ohhdMMNhhhhhhhhhhhhhhhhhhhhhhhhhhhyhhhhhdMMNhhy+++yhhNMMMMMMMMMMMMMMMMMMMm
MMMMMMMMMMMMMMMMMMMMy++++++++sMMMMMMMMNo++++++++++++++++++++yMMMMMMMMm+++++++++NMMMMMMMMMMMMMMMMMMMm
MMMMMMMMMMMMMMMMMyoo++++++yNNNMMMMMMMMMNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMMNNm++++++oooNMMMMMMMMMMMMMMMMm
MMMMMMMMMMMMMMmdds+++++osshMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNyss++++++hddNMMMMMMMMMMMMMm
MMMMMMMMMMMMMMs++++++++yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo++++++++mMMMMMMMMMMMMMm
MMMMMMMMMMMMMMs+++++yddmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmddo+++++mMMMMMMMMMMMMMm
MMMMMMMMMMMMMMyooooodMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMsooooomMMMMMMMMMMMMMm
        """, "green"))
    while running:
        print("money: $" + str(round(btcminer.money, 2)) + ", crypto: " + str(btcminer.crypto) + ", hashrate: " + str(btcminer.hashrate))
        mainaction = input("Welcome to TinyMiner CMD or help > ")
        if mainaction == "help":
            print("""
mine - Start mining on node
clear - Clear the screen
buy - Browse the net
sell - Sell the crypto
save - Save the game
load_game - Load previous game
exit - Quit the game and save
                   """)
            main()
        elif mainaction == "buy":
            btcminer.shop()
        elif mainaction == "sell":
            btcminer.sellcrypto()
        elif mainaction == "mine":
            btcminer.mine()
        elif mainaction == "cls" or mainaction == "clear":
            os.system("cls")
        elif mainaction == "save":
            btcminer.save_game()
        elif mainaction == "load_game":
            btcminer.load_game()
        elif mainaction == "exit":
            time.sleep(1)
            running = False
main()
