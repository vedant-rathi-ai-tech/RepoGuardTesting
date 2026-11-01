# test_repoguard_repair.py

from app import remediation_probe


def test_remediation_probe():
    assert remediation_probe() == "ok"
