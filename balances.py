from web3 import Web3
from web3.middleware import geth_poa_middleware
from contractinfo import abi, contract_adress

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware,layer=0)
contract = w3.eth.contract(address=contract_adress,abi = abi)

def get_balance():
    for i in w3.eth.accounts:
        try:
            balance = contract.functions.GetBalance().call({
                "from": i
            })
            print(f" {i} баланс: {balance[1]} WEI")
        except Exception as e:
            print(f"Ошибка при отправке эфира: {e}")

s = ""
while s != "2":
    s = input(f"1. Получение балансов аккаунтов\n2. Выход\n")
    match s:
        case "1":
            get_balance()
        case "2":
            break