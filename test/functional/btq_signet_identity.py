#!/usr/bin/env python3
# Copyright (c) 2026 The BTQ Core developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.
"""Verify the read-only signet identity exposed to custody clients."""

from test_framework.test_framework import BTQTestFramework
from test_framework.util import assert_equal


DEFAULT_CHALLENGE = (
    "522103ad5e0edad18cb1f0fc0d28a3d4f1f3e445640337489abb10404f2d1e086be43"
    "0210359ef5021964fe22d6f8e05b2463c9540ce96883fe3b278760f048f5189f2e6c452ae"
)


class BTQSignetIdentityTest(BTQTestFramework):
    def set_test_params(self):
        self.chain = "signet"
        self.num_nodes = 3
        self.setup_clean_chain = True
        self.extra_args = [
            [],
            ["-signetchallenge=51"],
            [f"-signetchallenge={DEFAULT_CHALLENGE}"],
        ]

    def setup_network(self):
        self.setup_nodes()

    def run_test(self):
        assert_equal(self.nodes[0].getmininginfo()["signet_challenge"], DEFAULT_CHALLENGE)
        assert_equal(self.nodes[1].getmininginfo()["signet_challenge"], "51")
        assert_equal(self.nodes[2].getmininginfo()["signet_challenge"], DEFAULT_CHALLENGE)


if __name__ == "__main__":
    BTQSignetIdentityTest().main()
