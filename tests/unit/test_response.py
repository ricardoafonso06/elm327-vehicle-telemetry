from vehicle_telemetry.elm327.response import parse_response


def test_parses_simple_frame() -> None:
    assert parse_response("41 0C 1A F8 \r\r>") == [bytes([0x41, 0x0C, 0x1A, 0xF8])]


def test_ignores_status_lines() -> None:
    assert parse_response("SEARCHING...\r41 0D 32\r\r>") == [bytes([0x41, 0x0D, 0x32])]
    assert parse_response("NO DATA\r\r>") == []
