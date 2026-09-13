#!/usr/bin/env python3
"""Toy rollup state transition with explicit state-root chaining.

The model separates user operations from the published root; it is not a bridge or sequencer.
"""
from hashlib import sha256


def digest(*parts: str) -> str:
    return sha256("|".join(parts).encode()).hexdigest()


def apply(state_root: str, sender: str, recipient: str, amount: int, nonce: int) -> str:
    if amount < 0 or nonce < 0:
        raise ValueError("amount and nonce must be non-negative")
    return digest("state-v1", state_root, sender, recipient, str(amount), str(nonce))


def demo() -> None:
    initial = digest("genesis", "rollup-demo")
    next_root = apply(initial, "alice", "bob", 7, 0)
    print("initial:", initial)
    print("next:   ", next_root)
    print("the published root commits to the ordered transition and its nonce")


if __name__ == "__main__":
    demo()
