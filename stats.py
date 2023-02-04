import pytest

from stats import DataCapture

def test_stats():
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()
    
    assert stats.less(4) == 2
    assert stats.greater(4) == 2
    assert stats.between(3, 6) == 4
    
def test_stats_exceptions():
    with pytest.raises(Exception) as excinfo:
        capture = DataCapture()
        capture.less(1)
    assert str(excinfo.value) == "Statistics not built yet. Call build_stats() first."

    with pytest.raises(Exception) as excinfo:
        capture = DataCapture()
        capture.add("n")
    assert str(excinfo.value) == "Invalid input. Value must be an integer between 1 and 1000."

    with pytest.raises(Exception) as excinfo:
        capture = DataCapture()
        capture.add(0)
    assert str(excinfo.value) == "Invalid input. Value must be an integer between 1 and 1000."

    with pytest.raises(Exception) as excinfo:
        capture = DataCapture()
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        stats.less(0)
    assert str(excinfo.value) == "Invalid input. Value must be an integer between 1 and 1000."

    with pytest.raises(Exception) as excinfo:
        capture = DataCapture()
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        stats.less("n")
    assert str(excinfo.value) == "Invalid input. Value must be an integer between 1 and 1000."
