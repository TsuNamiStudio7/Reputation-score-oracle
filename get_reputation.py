from config import CONTRACT

user = input("User address: ")
score = CONTRACT.functions.getScore(user).call()
verified = CONTRACT.functions.isVerified(user).call()

print(f"Score: {score} | Verified: {'✅' if verified else '❌'}")
