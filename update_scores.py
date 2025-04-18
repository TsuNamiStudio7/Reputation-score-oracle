from mock_data import external_scores
from config import CONTRACT, ACCOUNT, w3
from utils import send_transaction

def fetch_external_scores():
    return external_scores()

def submit_onchain(user, score):
    tx = CONTRACT.functions.submitScore(user, score).buildTransaction({
        "from": ACCOUNT.address,
        "nonce": w3.eth.get_transaction_count(ACCOUNT.address),
        "gas": 150000
    })
    tx_hash = send_transaction(tx)
    print(f"Submitted {user} => {score} | tx: {w3.toHex(tx_hash)}")
