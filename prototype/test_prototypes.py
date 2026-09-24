#!/usr/bin/env python3
"""Unit tests for the teaching prototypes (standard library only).

Run from the repository root: python -m unittest discover -s prototype -v
"""
import unittest
from hashlib import sha256

from fri_query_transcript import query_indices
from merkle_commitment import h, root
from rollup_state_transition import apply, digest


class MerkleCommitmentTest(unittest.TestCase):
    def test_root_is_deterministic(self):
        leaves = [b"a", b"b", b"c", b"d"]
        self.assertEqual(root(leaves), root(list(leaves)))

    def test_single_leaf_root_is_the_leaf_hash(self):
        self.assertEqual(root([b"a"]), h(b"\x00" + b"a"))

    def test_changing_a_leaf_changes_the_root(self):
        self.assertNotEqual(root([b"a", b"b"]), root([b"a", b"x"]))

    def test_leaf_order_matters(self):
        self.assertNotEqual(root([b"a", b"b"]), root([b"b", b"a"]))

    def test_empty_input_is_rejected(self):
        with self.assertRaises(ValueError):
            root([])

    def test_domain_separation_between_leaves_and_nodes(self):
        # Without the 00/01 prefixes, a leaf equal to the concatenation of two
        # child hashes could be confused with the internal node above them.
        forged_leaf = h(b"\x00" + b"a") + h(b"\x00" + b"b")
        self.assertNotEqual(root([forged_leaf]), root([b"a", b"b"]))

    def test_duplicated_last_leaf_is_a_known_limitation(self):
        # Documented in merkle_commitment.py: duplicating the last node on odd
        # levels makes these two lists share a root.
        self.assertEqual(root([b"a", b"b", b"c"]), root([b"a", b"b", b"c", b"c"]))


class FriQueryTranscriptTest(unittest.TestCase):
    commitment = sha256(b"example polynomial commitment").digest()

    def test_indices_are_deterministic_and_in_range(self):
        first = query_indices(self.commitment, 0, 32, 16)
        self.assertEqual(first, query_indices(self.commitment, 0, 32, 16))
        self.assertEqual(len(first), 32)
        self.assertTrue(all(0 <= i < 16 for i in first))

    def test_round_and_commitment_are_bound(self):
        base = query_indices(self.commitment, 0, 16, 1 << 20)
        self.assertNotEqual(base, query_indices(self.commitment, 1, 16, 1 << 20))
        other = sha256(b"another commitment").digest()
        self.assertNotEqual(base, query_indices(other, 0, 16, 1 << 20))

    def test_zero_queries(self):
        self.assertEqual(query_indices(self.commitment, 0, 0, 16), [])

    def test_invalid_arguments_are_rejected(self):
        with self.assertRaises(ValueError):
            query_indices(self.commitment, 0, -1, 16)
        with self.assertRaises(ValueError):
            query_indices(self.commitment, 0, 4, 0)


class RollupStateTransitionTest(unittest.TestCase):
    genesis = digest("genesis", "rollup-demo")

    def test_transition_is_deterministic(self):
        self.assertEqual(
            apply(self.genesis, "alice", "bob", 7, 0),
            apply(self.genesis, "alice", "bob", 7, 0),
        )

    def test_every_field_is_bound(self):
        base = apply(self.genesis, "alice", "bob", 7, 0)
        variants = [
            apply(digest("genesis", "other"), "alice", "bob", 7, 0),
            apply(self.genesis, "carol", "bob", 7, 0),
            apply(self.genesis, "alice", "carol", 7, 0),
            apply(self.genesis, "alice", "bob", 8, 0),
            apply(self.genesis, "alice", "bob", 7, 1),
        ]
        self.assertNotIn(base, variants)

    def test_transitions_are_chained(self):
        first = apply(self.genesis, "alice", "bob", 7, 0)
        self.assertNotEqual(
            apply(first, "bob", "carol", 3, 0),
            apply(self.genesis, "bob", "carol", 3, 0),
        )

    def test_negative_values_are_rejected(self):
        with self.assertRaises(ValueError):
            apply(self.genesis, "alice", "bob", -1, 0)
        with self.assertRaises(ValueError):
            apply(self.genesis, "alice", "bob", 1, -1)

    def test_separator_in_names_is_rejected(self):
        # "alice|bob" -> "carol" and "alice" -> "bob|carol" would otherwise
        # produce the same root.
        with self.assertRaises(ValueError):
            apply(self.genesis, "alice|bob", "carol", 7, 0)
        with self.assertRaises(ValueError):
            apply(self.genesis, "alice", "bob|carol", 7, 0)


if __name__ == "__main__":
    unittest.main()
