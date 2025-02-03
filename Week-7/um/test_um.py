from um import count


def test_count():
    assert count("ola todos") == 0
    assert count("yumi") == 0
    assert count("umum") == 0

    assert count("oi, um, todos") == 1
    assert count("um um um") == 3
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2