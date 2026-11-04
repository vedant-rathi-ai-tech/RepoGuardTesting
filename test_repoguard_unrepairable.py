# test_repoguard_unrepairable.py

import os


def test_repoguard_max_repair_guardrail():
    """
    Synthetic failure used only to verify RepoGuard's
    maximum autonomous repair-attempt guardrail.
    """

    assert os.getenv("REPOGUARD_UNREPAIRABLE_TEST") == "PASS", (
        "Intentional unrepairable validation failure for "
        "RepoGuard repair-attempt guardrail testing."
    )
