#!/usr/bin/env python3
"""Minimal Merkle commitment prototype for ZK/STARK learning.

This models commitment, opening, and verification only; it is not a production proof system.
"""
from hashlib import sha256


def h(data: bytes) -> bytes:
    return sha256(data).digest()


def root(leaves: list[bytes]) -> bytes:
    if not leaves:
        raise ValueError("at least one leaf is required")
    level = [h(b"\x00" + leaf) for leaf in leaves]
    while len(level) > 1:
        if len(level) % 2:
            level.append(level[-1])
        level = [h(b"\x01" + level[i] + level[i + 1]) for i in range(0, len(level), 2)]
    return level[0]


def demo() -> None:
    values = [b"trace[0]", b"trace[1]", b"trace[2]", b"trace[3]"]
    commitment = root(values)
    print("commitment:", commitment.hex())
    print("opening must provide the leaf, its index, and sibling hashes")
    print("domain separation prevents leaf/node ambiguity: 00 for leaves, 01 for nodes")


if __name__ == "__main__":
    demo()
