import pytest
from src.strategies import ServiceFactory
from src.auth import generate_token, verify_token


def test_dataset_strategies():
    # Mandated raw data stream from exam parameters
    dataset = [78, 82, 91, 65, 40, 99, 88]
    
    # Verify Strategy A: Encryption (Key: 004F -> 79 decimal)
    enc_strat = ServiceFactory.get_strategy("encryption")
    encrypted_data = enc_strat.process(dataset)
    assert encrypted_data[0] == float(78 ^ 0x004F)  # 78 XOR 79 = 1.0
    
    # Verify Strategy B: Compression (Factor: 0.85)
    comp_strat = ServiceFactory.get_strategy("compression")
    compressed_data = comp_strat.process(dataset)
    assert compressed_data[0] == round(78 * 0.85, 2)


def test_jwt_cryptographic_handshake():
    token = generate_token("senior_engineer")
    decoded = verify_token(token)
    assert decoded["sub"] == "senior_engineer"


def test_invalid_jwt():
    assert verify_token("invalid.token.string") == {}