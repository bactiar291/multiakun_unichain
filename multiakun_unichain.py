from web3 import Web3
import time
from datetime import datetime
from colorama import Fore, Style, init
import json
import random

init(autoreset=True)

CHECK_MARK = Fore.GREEN + "✔️" + Style.RESET_ALL
CROSS_MARK = Fore.RED + "❌" + Style.RESET_ALL
MONEY_BAG = Fore.YELLOW + "💰" + Style.RESET_ALL
GAS_PUMP = Fore.MAGENTA + "⛽" + Style.RESET_ALL
SUCCESS_MARK = Fore.BLUE + "🚀" + Style.RESET_ALL

print(Fore.YELLOW + "========================================")
print(Fore.CYAN + "AUTHOR : ANAM BACTIAR")
print(Fore.MAGENTA + "THANKS TO : ANAM BACTIAR!")
print(Fore.BLUE + "GITHUB: https://github.com/bactiar291")
print(Fore.GREEN + "BUY COFFE FOR ME : 0x648dce97a403468dfc02c793c2b441193fccf77b ")
print(Fore.YELLOW + "========================================\n")


web3 = Web3(Web3.HTTPProvider("https://autumn-cosmological-scion.unichain-sepolia.quiknode.pro/c568806873f2a9edb9fcdea8aef0569ff729eb25"))

if web3.is_connected():
    print(Fore.GREEN + "Terkoneksi dengan jaringan Ethereum " + CHECK_MARK)
else:
    print(Fore.RED + "Gagal terhubung ke jaringan Ethereum " + CROSS_MARK)
    raise Exception("Gagal terhubung ke jaringan Ethereum")


with open('accounts.json', 'r') as f:
    accounts = json.load(f)


receivers = [
    '0xb6D8c5f48B5B2467dfd8046C712A591EBCA1Cbdc',
   
]


min_amount = 0.00000001
max_amount = 0.00000005

gas_price = web3.eth.gas_price
gas_price_gwei = web3.from_wei(gas_price, 'gwei')


def send_transaction(sender_address, private_key, receiver_address, gas_price, max_retries=3):
    nonce = web3.eth.get_transaction_count(sender_address, 'pending')  # Mendapatkan nonce terbaru

    for attempt in range(max_retries):
        try:
            
            balance_before = web3.eth.get_balance(sender_address)
            print(Fore.YELLOW + f"Saldo pengirim {MONEY_BAG} sebelum transaksi: {web3.from_wei(balance_before, 'ether')} ETH")

           
            random_amount = random.uniform(min_amount, max_amount)
            amount = web3.to_wei(random_amount, 'ether')

            tx = {
                'nonce': nonce,
                'to': receiver_address,
                'value': amount,
                'gas': 21000,
                'gasPrice': gas_price,
                'chainId': 1301
            }

           
            print(Fore.MAGENTA + f"Gas Price {GAS_PUMP}: {gas_price_gwei} Gwei")
            print(Fore.YELLOW + f"Mengirim jumlah acak: {random_amount:.10f} ETH")

           
            signed_tx = web3.eth.account.sign_transaction(tx, private_key)
            tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
            
           
            balance_after = web3.eth.get_balance(sender_address)
            print(Fore.YELLOW + f"Saldo pengirim {MONEY_BAG} setelah transaksi: {web3.from_wei(balance_after, 'ether')} ETH")

           
            print(Fore.CYAN + f"{datetime.now()} - Transaksi berhasil dari {sender_address} ke {receiver_address}." + CHECK_MARK)
            print(Fore.CYAN + f"Tx Hash: {web3.to_hex(tx_hash)} " + SUCCESS_MARK)
            return tx_hash

        except ValueError as e:
            error_message = e.args[0]

            
            if 'nonce too low' in error_message['message']:
                print(Fore.RED + f"Nonce terlalu rendah untuk {sender_address}. Mencoba lagi." + CROSS_MARK)
                nonce = web3.eth.get_transaction_count(sender_address, 'pending')  # Dapatkan nonce terbaru lagi
            else:
                print(Fore.RED + f"Kesalahan saat mengirim transaksi: {error_message['message']}" + CROSS_MARK)
                break

        except Exception as e:
            print(Fore.RED + f"Kesalahan tidak terduga: {str(e)}. Percobaan ulang ({attempt+1}/{max_retries})" + CROSS_MARK)
            time.sleep(2 ** attempt) 
        
        time.sleep(1)  

    print(Fore.RED + "Transaksi gagal setelah beberapa percobaan." + CROSS_MARK)
    return None

while True:
    for account in accounts:
        for receiver in receivers:
            
            send_transaction(account['address'], account['private_key'], receiver, gas_price)
            time.sleep(10) 
    
    print(Fore.YELLOW + "Menunggu 1 menit sebelum pengiriman berikutnya...")
    time.sleep(60)
