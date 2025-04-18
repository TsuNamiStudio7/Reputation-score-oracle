// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ReputationOracle {
    address public oracle;

    mapping(address => uint256) public reputationScores;
    mapping(address => bool) public verified;

    event ScoreSubmitted(address indexed user, uint256 score);
    event Verified(address indexed user);

    modifier onlyOracle() {
        require(msg.sender == oracle, "Not authorized");
        _;
    }

    constructor() {
        oracle = msg.sender;
    }

    function submitScore(address user, uint256 score) public onlyOracle {
        reputationScores[user] = score;
        emit ScoreSubmitted(user, score);
        if (score > 70) {
            verified[user] = true;
            emit Verified(user);
        }
    }

    function getScore(address user) external view returns (uint256) {
        return reputationScores[user];
    }

    function isVerified(address user) external view returns (bool) {
        return verified[user];
    }
}
