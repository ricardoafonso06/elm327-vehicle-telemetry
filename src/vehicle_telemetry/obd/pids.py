"""Decoding of a few standard SAE J1979 mode 01 PIDs."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass


@dataclass(frozen=True)
class Pid:
    code: int
    name: str
    unit: str
    decode: Callable[[bytes], float]


PIDS: dict[int, Pid] = {
    0x04: Pid(0x04, "engine_load", "%", lambda d: d[0] * 100 / 255),
    0x05: Pid(0x05, "coolant_temp", "°C", lambda d: d[0] - 40),
    0x0C: Pid(0x0C, "rpm", "rpm", lambda d: (256 * d[0] + d[1]) / 4),
    0x0D: Pid(0x0D, "speed", "km/h", lambda d: d[0]),
    0x0F: Pid(0x0F, "intake_air_temp", "°C", lambda d: d[0] - 40),
}


def decode_mode01(frame: bytes) -> tuple[Pid, float]:
    """Decode a mode 01 response frame such as ``41 0C 1A F8``."""
    if len(frame) < 3 or frame[0] != 0x41:
        raise ValueError("not a mode 01 response")
    pid = PIDS.get(frame[1])
    if pid is None:
        raise KeyError(f"unsupported PID 0x{frame[1]:02X}")
    return pid, pid.decode(frame[2:])
