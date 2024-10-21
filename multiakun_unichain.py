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
'0xbD8c6c92e3e78bB4fE1148a0Cba08ad91BABc524',
'0xc2dD6Ea96369213e6dB99E5cB95579000959B9Fd',
'0x552D59a2c8E691E959FFE56166a338E04D572dEb',
'0xF6Eebb6929b3F0cEc6812DB24fa45E5e0d42Cc9f',
'0x56A2dCd8c72561f2BE9cdA98e3139B97411f7848',
'0x4AE2bcf7D81d19b54bc6957ae41077D3DF8c5a84',
'0xBB084c2e463cebcE22aCF84658d2c9f3bE143bEF',
'0x0F8e8Ad1f488acbD36e06BDC198Bbe5f821B7A66',
'0x83849e6603A0eec98aa9478266dc811D50B1e7dF',
'0x3cC3B1871CE9b9E5FC2E4e87dfE9F85a05f816db',
'0x21e48801378a94F436ED59d534b826add0F084b0',
'0xE5D95B67B21c3Df7F2f7752648e9d1EB8a80fb33',
'0xB6E287964fbeb10FC4283823191217BdeAcA65C1',
'0x8Cd3D03acFd9557464790cd23724d6A84b7A1A83',
'0xA3BfC2E641827e63735468709cEA9Ab85419768b',
'0xF2C7f4ea6740A990d09998DD63C31FAd2cCa085A',
'0x58724EBB4004dC9143f5AcA4249560767831B064',
'0x0a3cf48Ed8Df141782A3db8Ad9608b77Da97adab',
'0x91541263D95266B9a6cb44d4937B66388135aBa9',
'0x8D25C322a1F6391Cfa4c13B5cc40e4fadB75504C',
'0x1dd9fc53e14221c60c88341439E7513c13a546fa',
'0xa75e3994AAa98AcE1D6B87b3Ce3a0AAD363D044e',
'0xA8D5f82295F1A175D0634a9dFa1bb1cbAfAB530e',
'0xC1Bb6e64Bb5c80B8efe10aa9FB60678B2420837D',
'0x4680160419686A149bD7E57C6849B0eAe94992B1',
'0x04B8476210ffD70Bd982f950C85e717523724303',
'0x58E2cF1880759bedd074981783AA6F2A4153509A',
'0x11e4D8D3C46C4B3De35E55d4fE25BBa165682781',
'0x98f5ea542a9a0BFa9fcb0192Bfa0737797Ba3fAb',
'0x8877966B5667D97CA58D3a867bAc9788892b28ae',
'0x2F358F97c90471E1943CA7CC1AA7C72290fb165E',
'0x02b4C844417E0726918056AAC4093cd8B021821E',
'0x02b4C844417E0726918056AAC4093cd8B021821E',
'0xA2203B0EbF9DddA200461420c45eC1514f065407',
'0x058D4b74BdF2fBCee4088A2C227A5CEf7e8eD68C',
'0xfcB567b3deB2255dBc1B24FEE2688D0FBD9427C3',
'0x501D049ae9dCc7B2D5A79B9Ed0bfEbBc8b781Bf7',
'0x1cE13c6D1246DC0f738420FB7266244B382a3088',
'0x403a5def5E591eBF336Ea4D0F5AA487a0dD1F4E3',
'0xf8eC6a276E8b924c3B1A3CbFb034f55b8B362cd9',
'0xABb65c378E87229caD36AE559D7adca31bc2B7e6',
'0x89E29eBA4fe74714FaeDdD0acf75fCCa73520Fcb',
'0x3eB43C03ef20Beb8FC751f84067684f1Bc7Aa98f',
'0xC1be665245fCAADb0b3177E6C37843F38A0dEBAD',
'0x4cCB8F734a01AF8d1b6583B71c3Da182C3372d77',
'0x45642cf8eA33E21031A35da0c7a6d51B9aB452Df',
'0xe1e6eCCd1DbF0B7604bE89a329037AA6f36e7AA1',
'0xE892f66Feb9a1c93b69b5DfcDF4d805AA68a647b',
'0x8F8Dd182A530Cf41252C594de6c45b7859fb4AE5',
'0x8c7138f235B22EF9E1Ca01FfFE806c58D1C0B571',
'0x4647e3f02982099Dc66c131C868D67D84143173e',
'0x86398B1DE0641613B24D676d2af8bfd78D713ecE',
'0x9818732B543DccD2cc9202FcCD6976FBaE079c3c',
'0xEd4C5D08407412abbdF0882972E1D9665C4EB531',
'0x236a95108E56774FE264857f6ea9e5dC6b058F2d',
'0x43d74A59A786103D75E1EF3b0dF56FB9e6907234',
'0xE90213c05eE6eB828D6da4e9a83b9D49d994Cd0D',
'0x6BEFe9501B00CEBE3c0fbD6F2da6ea4e68bf6a0E',
'0xCF5A61a4EA84099D25D31Ef9ABe99E0C77C7b26f',
'0x8e299D29650e3e0359a98E019dfE6b17f98bD5a6',
'0x1DcD9CbfDF87F66195dD71B82920bBBee186077A',
'0xeC92C00961bFa60AE51cEA15513050dFBfa4cD84',
'0x6D2C60F40270B71E77430dc3Af99eD6F0e82bE2A',
'0x0BeE0a7262ED7B2804eB02900aC757a3A0925E36',
'0xA17aacb3155024F96eF2fa18C96019d13549e95d',
'0x1851E41Fbdd5a66AA73908B2BC516Dfc77a52872',
'0xAc3E0Fc53163A9AB367A1878bE18a80742B6E505',
'0xeFB9EEb9F27184425f367cF5dEDd635790E4e6d2',
'0x8b6BDba15c7E377E087E6bf3B0b2b75b17a92800',
'0x4D680E41FA10E09c136fc44719fAf39677cA7fEF',
'0xFea9b25a4f86D6BB3cFb11E5c6F70Cb6b066794C',
'0x3532a6BD51fFdcEA3031Fa2C1a856B77C5bCA0e3',
'0x699a11D93A8eD1E560504E4331E01e578359BAae',
'0x6bf7e47a5B5Be49aeB0B15a0E86622cA702C3Cf4',
'0x2929dd4452d33c81dA8f8A76cc9cAF020Ecc59d6',
'0xd1ACEb25020B16c3553f4286204f2BeA7258AEA6',
'0xd203D7c3E76B91B88F1d60252bC94C8932243507',
'0xa6c977Da9ca1Ac90679d1f78a910ea050CC614F9',
'0x326EC03bB9B92Eedad2809dFdb51db80CE6C3E35',
'0x4F0EC63cCe0Ef25d2a1faCbC6ceBa7d0164952ee',
'0x5AA204083e7fbc1307EBB60b8a38c0244eD42418',
'0x686Cb28e5A7AA201D8363948890b831c00E2ae27',
'0x1dc9E5f4315bEc27938133D2b71F964AEC9266e2',
'0xb0e2bc5AFaF6D98Bfb1a25dEDeA5daB9C77Ba19a',
'0x9dc68391D13327A4D354811Dc5e919484e9453A6',
'0x3CF544F77c4687b02ff37606ef09c1F928B10644',
'0x070A9BED86dCb8a4FdF6C40F3Dd7f44083914c93',
'0xBeA5Fa84662D5D8F3c029aF6433d447d499786b8',
'0x8aB0836723c9abb71943449295ECbCA12adf2202',
'0xc7727eE0Bd8ee85F0c9c123c38ec48319c921286',
'0x7F6101c6de5aa5CaD8a72eB4dd04e91712E88BC7',
'0xc760B9dDB312546C405e86F069997e737219A6b8',
'0x44A65B4fd82210A0E053BE01A81d54d78EAC6fac',
'0xEb02C52702494975f9700a860f03873A95Cc166A',
'0x95CE10A5D21d4a2CFc6DdE344bd781F3a3deA962',
'0xE29FA30fA2c9cEf4cf068aE82197f8459d2Fb151',
'0xd3A9283624742aCed09c15f6AeC40717a0d31bb8',
'0x48916206b4D37bD9c7061be9abc4e1daEf29383f',
'0xf6dC61be80D3A0F56161bBCa25b30b900BA38C28',
'0xC90a2252d4Ab594f02c0fC34fB2E80AAAc6BcFd3',
'0xa8efA5F0caD5AE9e699b904C5e08c6410B3a3151',
'0xF354593459Cd184D935797687e2c1c5cba9d2EA0',
'0x4AbA4472b462CCFD70066769938dac4Ae43d6A78',
'0xfA0e446D584fFB76790428dBE2eA313Df3d0f029',
'0xC2F8c71c249c42e8E0649b198C2278A3c96B8Bd4',
'0xd5085dad64E0800F72Fb0f87f695797B0f583EE0',
'0x37A4788C89A112f1d2F0D24e1F5A6Ac4580B5794',
'0x0C414dDEa4a4AE30C5f8df711C52848e7771FDA0',
'0x1d1e8d88B95c53D596D51A1888Ae246b8781E4dB',
'0xBbbE17eBF4406140962973A048e40AccecDa1b2b',
'0xbc2560A7e5f269cD8c26425CFA032b604cD973e9',
'0x4b057C7b1C3FF7C590332F06DB1eCBD91AbeDCfb',
'0xa3b5C726631EEB2978DEf608cA0C8b0B5ca1B157',
'0x868030A9079b1419cf7A1c9F42e3C6C0A549A2EB',
'0xaB9C6775eD4238Fb4fd6a546daC393eA40Cc616B',
'0x3783af92b1F244c1428bb34C21ACE1A4de7A042d',
'0xd285c00E5a7e1a45Cc66EB162306aEA42f085451',
'0x505EB601aEdFDe2650b79f1C49561627DB319474',
'0x29cEA192761F4076cc8657CC6e0cB8CEBB3622aA',
'0x0875F739d9574e9411e84e9AC80BB4a59AE7b421',
'0xFbDe8f8A9b9BC1Cd8c1723cA804975B5DcfC4a9C',
'0xE5fCbfA2B711acCa57dE3F764e86323C128397E3',
'0xAb9c6b2C92Ad1A0a8b7BE6c384042Be5001d8402',
'0xB45bF3935bEB3FCe15C7198430ae73bF74f235D3',
'0x72D07c49DDAF102c38Dbcc992faf156b5a973254',    
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
