from result import Result

def test_result_is_correctly_created():
    r = Result("2026-01-01", "LMS", 30, "15:01:01")
    assert r.date == "2026-01-01"
    assert r.detector == "LMS"
