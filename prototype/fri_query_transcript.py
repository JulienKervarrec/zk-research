#!/usr/bin/env python3
"""Deterministic Fiat-Shamir query sampler for a FRI teaching model.

This is transcript plumbing only, not a complete FRI proof or verifier.
"""
from hashlib import sha256


def query_indices(commitment: bytes, round_number: int, count: int, domain_size: int) -> list[int]:
    if count < 0 or domain_size <= 0:
        raise ValueError("count must be non-negative and domain_size positive")
    seed = sha256(b"FRI/query/v1" + commitment + round_number.to_bytes(4, "big")).digest()
    return [int.from_bytes(sha256(seed + i.to_bytes(4, "big")).digest()[:8], "big") % domain_size for i in range(count)]


def demo() -> None:
    commitment = sha256(b"example polynomial commitment").digest()
    print(query_indices(commitment, round_number=0, count=4, domain_size=16))
    print("bind the commitment before sampling; domain separation identifies this transcript")


if __name__ == "__main__":
    demo()
