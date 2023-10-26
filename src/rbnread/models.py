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

    def jsonify(self):
        return {
            "ts": self.ts.isoformat().replace("+00:00", "Z"),
            "calling_station": self.calling_station,
            "receiving_station": self.receiving_station,
            "frequency": str(self.frequency),
            "mode": self.mode,
            "snr_db": self.snr_db,
            "wpm": self.wpm,
            "msg": self.msg,
            "rbn_ts": self.rbn_ts.isoformat().replace("+00:00", "Z"),
        }
