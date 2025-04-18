from update_scores import fetch_external_scores, submit_onchain
import time

print("🧠 Oracle running...")

while True:
    users = fetch_external_scores()
    for addr, score in users.items():
        submit_onchain(addr, score)
    time.sleep(10)
