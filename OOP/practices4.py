from dataclasses import dataclass
@dataclass(frozen = True)
class Transaction():
    amount : float
    description: str


    