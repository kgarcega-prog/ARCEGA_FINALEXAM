from abc import ABC, abstractmethod
from typing import List


class ProcessingStrategy(ABC):
    @abstractmethod
    def process(self, data: List[int]) -> List[float]:
        pass


class EncryptionStrategy(ProcessingStrategy):
    """Applies Strategy A: XOR Encryption with Key: 004F"""
    def __init__(self, key: str = "004F"):
        self.key = int(key, 16)  # Converts 004F hex to integer 79

    def process(self, data: List[int]) -> List[float]:
        return [float(val ^ self.key) for val in data]


class CompressionStrategy(ProcessingStrategy):
    """Applies Strategy B: Compression with Factor: 0.85"""
    def __init__(self, factor: float = 0.85):
        self.factor = factor

    def process(self, data: List[int]) -> List[float]:
        return [round(val * self.factor, 2) for val in data]


class ServiceFactory:
    """Factory Pattern to handle dynamic service discovery"""
    @staticmethod
    def get_strategy(strategy_type: str) -> ProcessingStrategy:
        strategies = {
            "encryption": EncryptionStrategy,
            "compression": CompressionStrategy
        }
        target = strategies.get(strategy_type.lower())
        if not target:
            raise ValueError(f"Unknown strategy type: {strategy_type}")
        return target()
        