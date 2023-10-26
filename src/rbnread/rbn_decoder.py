from datetime import datetime, UTC
import re
from .models import RBNRecord

CALL_RE = re.compile(r"(?P<call>.+)-\#:")


def _strip_out_dx_call(raw_data: str) -> str:
    """
    pulls the DX callsign out from the raw data
    example:
    # AC0C-2-#:   --> AC0C, AC0C-2
    # KM4SII-#:   --> KM4SII, KM4SII
    """
    m = CALL_RE.match(raw_data)
    if m and m.groups():
        return m.groups()[0].split("-")[0]
    return ""


def _decode_rbn_time_str(time_str: str) -> datetime | None:
    """
    takes string in "####Z" format and returns a proper datetime
    """
    if len(time_str) == 5 and time_str[-1] == "Z":
        now = datetime.now(UTC)
        try:
            hours = int(time_str[0:2])
            mins = int(time_str[2:4])
            return datetime(now.year, now.month, now.day, hours, mins, 0, tzinfo=UTC)
        except (TypeError, ValueError) as err:
            # invalid string
            ...
    return None


def decode_rbn_message(data: bytes) -> RBNRecord | None:
    """
    take raw data and split into appropriate fields
    """
    fields = data.decode().split()
    if fields and len(fields) >= 12:
        call = _strip_out_dx_call(fields[2])
        rbn_ts = _decode_rbn_time_str(fields[11])
        if call and rbn_ts:
            rbn_record = RBNRecord(
                ts=datetime.now(UTC),
                receiving_station=call,
                frequency=fields[3],
                calling_station=fields[4],
                mode=fields[5],
                snr_db=fields[6],
                wpm=fields[8],
                msg=fields[10],
                rbn_ts=rbn_ts,
            )
            return rbn_record
        else:
            print(f"invalid message: {fields}")
    return None
