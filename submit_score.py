from config import CONTRACT, ACCOUNT, w3
from utils import send_transaction

address = input("User address: ")
score = int(input("Reputation score: "))

tx = CONTRACT.functions.submitScore(address, score).buildTransaction({
    "from": ACCOUNT.address,
    "nonce": w3.eth.get_transaction_count(ACCOUNT.address),
    "gas": 150000
})

tx_hash = send_transaction(tx)
print("✅ Score submitted:", w3.toHex(tx_hash))
