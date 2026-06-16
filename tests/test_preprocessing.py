from backend.services.preprocessing import (
    clean_text
)


def test_clean_text():

    text = (
        "HELLO!!! "
        "Visit HTTP://ABC.COM"
    )

    result = clean_text(
        text
    )

    assert isinstance(
        result,
        str
    )

    assert result != text

    assert len(result) > 0