from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class RBNRecord:
    ts: datetime
    receiving_station: str
    frequency: Decimal
    calling_station: str
    mode: str
    snr_db: int
    wpm: int
    msg: str
    rbn_ts: datetime
