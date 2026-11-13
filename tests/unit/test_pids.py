import pytest

from vehicle_telemetry.obd.pids import decode_mode01


def test_rpm() -> None:
    pid, value = decode_mode01(bytes([0x41, 0x0C, 0x1A, 0xF8]))
    assert pid.name == "rpm"
    assert value == 1726.0


def test_coolant() -> None:
    _, value = decode_mode01(bytes([0x41, 0x05, 0x7B]))
    assert value == 83


def test_rejects_non_mode01() -> None:
    with pytest.raises(ValueError):
        decode_mode01(bytes([0x62, 0x0C, 0x00]))
