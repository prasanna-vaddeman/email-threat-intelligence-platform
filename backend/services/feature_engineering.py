# =========================================================
# IMPORT LIBRARIES
# =========================================================

import re

import pandas as pd


# =========================================================
# REGEX PATTERNS
# =========================================================

# Precompile regex for faster inference

URL_PATTERN = re.compile(

    r"http[s]?://\S+|www\.\S+"
)

HTML_PATTERN = re.compile(

    r"<[^>]+>"
)

SPECIAL_CHAR_PATTERN = re.compile(

    r"[^a-zA-Z0-9\s]"
)

TOKEN_PATTERN = re.compile(

    r"\b\w+\b"
)


# =========================================================
# SPAM KEYWORDS
# =========================================================

# Common spam indicators

SPAM_KEYWORDS = {

    "free",

    "win",

    "winner",

    "money",

    "offer",

    "urgent",

    "click",

    "buy",

    "cash",

    "prize"
}


# =========================================================
# FEATURE COLUMN ORDER
# =========================================================

# Must remain identical
# to training pipeline

FEATURE_COLUMNS = [

    "url_count",

    "exclamation_count",

    "uppercase_ratio",

    "html_tag_count",

    "special_char_count",

    "spam_keyword_count"
]


# =========================================================
# URL COUNT
# =========================================================

def count_urls(

    text: str

) -> int:

    """

    Counts URLs inside email.

    Args:

        text (str)

    Returns:

        int

    """

    return len(

        URL_PATTERN.findall(

            str(text)
        )
    )


# =========================================================
# EXCLAMATION COUNT
# =========================================================

def count_exclamations(

    text: str

) -> int:

    """

    Counts exclamation marks.

    """

    return str(text).count(

        "!"
    )


# =========================================================
# UPPERCASE RATIO
# =========================================================

def uppercase_ratio(

    text: str

) -> float:

    """

    Computes uppercase ratio.

    Ignores spaces,
    punctuation and numbers.

    """

    letters = [

        char

        for char

        in str(text)

        if char.isalpha()
    ]

    if not letters:

        return 0.0

    upper_count = sum(

        char.isupper()

        for char

        in letters
    )

    return (

        upper_count

        /

        len(letters)
    )


# =========================================================
# HTML TAG COUNT
# =========================================================

def count_html_tags(

    text: str

) -> int:

    """

    Counts HTML tags.

    """

    return len(

        HTML_PATTERN.findall(

            str(text)
        )
    )


# =========================================================
# SPECIAL CHARACTER COUNT
# =========================================================

def count_special_chars(

    text: str

) -> int:

    """

    Counts special characters.

    """

    return len(

        SPECIAL_CHAR_PATTERN.findall(

            str(text)
        )
    )


# =========================================================
# SPAM KEYWORD COUNT
# =========================================================

def count_spam_keywords(

    text: str

) -> int:

    """

    Counts suspicious spam words.

    Uses token matching.

    Examples:

    FREE!!! -> counted

    window -> ignored

    """

    tokens = TOKEN_PATTERN.findall(

        str(

            text

        ).lower()
    )

    return sum(

        1

        for token

        in tokens

        if token in SPAM_KEYWORDS
    )


# =========================================================
# THREAT LEVEL
# =========================================================

def get_threat_level(

    probability: float

) -> str:

    """

    Converts probability
    into threat severity.

    """

    if probability >= 0.90:

        return "HIGH"

    elif probability >= 0.60:

        return "MEDIUM"

    return "LOW"


# =========================================================
# BUILD FEATURE DATAFRAME
# =========================================================

def build_manual_features(

    email_text: str

) -> pd.DataFrame:

    """

    Builds manual features.

    Used before scaler.

    Args:

        email_text (str)

    Returns:

        pd.DataFrame

    """

    features = pd.DataFrame([{

        "url_count":

            count_urls(

                email_text
            ),

        "exclamation_count":

            count_exclamations(

                email_text
            ),

        "uppercase_ratio":

            uppercase_ratio(

                email_text
            ),

        "html_tag_count":

            count_html_tags(

                email_text
            ),

        "special_char_count":

            count_special_chars(

                email_text
            ),

        "spam_keyword_count":

            count_spam_keywords(

                email_text
            )
    }])

    # Maintain training consistency

    return features[

        FEATURE_COLUMNS
    ]