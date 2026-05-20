# =========================================================
# IMPORT LIBRARIES
# =========================================================

import re
import string
import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


# =========================================================
# LOAD NLTK RESOURCES SAFELY
# =========================================================

try:

    STOP_WORDS = set(

        stopwords.words(

            "english"
        )
    )

except LookupError:

    nltk.download(

        "stopwords",

        quiet=True
    )

    STOP_WORDS = set(

        stopwords.words(

            "english"
        )
    )


# =========================================================
# NLP OBJECTS
# =========================================================

# Load once during startup

STEMMER = PorterStemmer()


# =========================================================
# REGEX PATTERNS
# =========================================================

# Precompile regex patterns
# for faster inference

URL_PATTERN = re.compile(

    r"http\S+|www\S+"
)

EMAIL_PATTERN = re.compile(

    r"\S+@\S+"
)

HTML_PATTERN = re.compile(

    r"<[^>]+>"
)

NUMBER_PATTERN = re.compile(

    r"\d+"
)

WHITESPACE_PATTERN = re.compile(

    r"\s+"
)


# =========================================================
# HTML ARTIFACT PATTERN
# =========================================================

# Common email extraction artifacts

HTML_NOISE_PATTERN = re.compile(

    r"\b(?:"

    r"nbsp|"

    r"href|"

    r"font|"

    r"color|"

    r"html|"

    r"http"

    r")\b"
)


# =========================================================
# PUNCTUATION TABLE
# =========================================================

# Build once at startup

PUNCT_TRANSLATION = (

    str.maketrans(

        "",

        "",

        string.punctuation
    )
)


# =========================================================
# CLEAN TEXT FUNCTION
# =========================================================

def clean_text(

    text: str

) -> str:

    """

    Cleans raw email text
    for NLP inference.

    Processing pipeline:

    1. Lowercase normalization

    2. URL removal

    3. Email removal

    4. HTML tag removal

    5. HTML artifact cleanup

    6. Number removal

    7. Punctuation removal

    8. Whitespace normalization

    9. Stopword removal

    10. Word stemming

    Args:

        text (str):

            Raw email content

    Returns:

        str:

            Cleaned text
            ready for TF-IDF vectorization

    """

    # =====================================================
    # HANDLE INVALID INPUT
    # =====================================================

    if not isinstance(

        text,

        str
    ):

        return ""

    # =====================================================
    # NORMALIZATION
    # =====================================================

    text = text.lower()

    # =====================================================
    # REMOVE URLS
    # =====================================================

    text = URL_PATTERN.sub(

        " ",

        text
    )

    # =====================================================
    # REMOVE EMAILS
    # =====================================================

    text = EMAIL_PATTERN.sub(

        " ",

        text
    )

    # =====================================================
    # REMOVE HTML TAGS
    # =====================================================

    text = HTML_PATTERN.sub(

        " ",

        text
    )

    # =====================================================
    # REMOVE HTML ARTIFACTS
    # =====================================================

    text = HTML_NOISE_PATTERN.sub(

        " ",

        text
    )

    # =====================================================
    # REMOVE NUMBERS
    # =====================================================

    text = NUMBER_PATTERN.sub(

        " ",

        text
    )

    # =====================================================
    # REMOVE PUNCTUATION
    # =====================================================

    text = text.translate(

        PUNCT_TRANSLATION
    )

    # =====================================================
    # NORMALIZE SPACES
    # =====================================================

    text = WHITESPACE_PATTERN.sub(

        " ",

        text

    ).strip()

    # =====================================================
    # STOPWORDS + STEMMING
    # =====================================================

    cleaned_tokens = [

        STEMMER.stem(

            token
        )

        for token in text.split()

        if token not in STOP_WORDS
    ]

    # =====================================================
    # RETURN CLEANED TEXT
    # =====================================================

    return " ".join(

        cleaned_tokens
    )