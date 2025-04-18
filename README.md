# Reputation Score Oracle

A hybrid smart contract + Python oracle system for on-chain reputation scores.

## Features

- 🧠 Offchain data fetching
- ✅ Onchain verification logic
- 📊 Real-time scoring + leaderboard
- 🔐 Oracle-controlled updates

## Files

- `ReputationOracle.sol` — main smart contract
- `deploy_contract.py` — deployment script
- `submit_score.py` — manual score input
- `oracle_server.py` — auto-updating daemon
- `update_scores.py` — submission logic
- `mock_data.py` — simulated external data
- `get_reputation.py` — user score viewer
- `tests.py` — basic test
- `utils.py`, `config.py` — helper setup

## Run Oracle

```bash
python oracle_server.py
