"""Parsing of raw ELM327 responses into byte frames."""

from __future__ import annotations


def parse_response(raw: str) -> list[bytes]:
    """Convert a raw ELM327 reply into a list of frames.

    Lines that are not made of 2-digit hex tokens (``SEARCHING...``,
    ``NO DATA``, ``STOPPED``, the ``>`` prompt) are ignored.
    Assumes spaces are enabled (``ATS1``, the ELM327 default).
    """
    frames: list[bytes] = []
    for line in raw.replace("\r", "\n").split("\n"):
        tokens = line.replace(">", " ").split()
        if not tokens or any(len(t) != 2 for t in tokens):
            continue
        try:
            frames.append(bytes(int(t, 16) for t in tokens))
        except ValueError:
            continue
    return frames
