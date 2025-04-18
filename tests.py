from config import CONTRACT

def test_user(addr):
    score = CONTRACT.functions.getScore(addr).call()
    assert 0 <= score <= 100
    print(f"{addr} ✅ Score OK: {score}")

test_user("0x0000000000000000000000000000000000000001")
