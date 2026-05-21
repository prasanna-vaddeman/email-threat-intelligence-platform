"""
Email Preprocessing
"""

import re
import string

import nltk

from nltk.corpus import stopwords

from nltk.stem import PorterStemmer


try:

    STOPWORDS = set(

        stopwords.words(

            "english"

        )

    )

except LookupError:

    nltk.download(

        "stopwords",

        quiet=True

    )

    STOPWORDS = set(

        stopwords.words(

            "english"

        )

    )


STEMMER = PorterStemmer()


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


def clean_text(

    text:str

):

    """
    Clean email text.
    """

    if not isinstance(

        text,

        str

    ):

        return ""

    text = text.lower()

    text = URL_PATTERN.sub(

        " ",

        text

    )

    text = EMAIL_PATTERN.sub(

        " ",

        text

    )

    text = HTML_PATTERN.sub(

        " ",

        text

    )

    text = NUMBER_PATTERN.sub(

        " ",

        text

    )

    text = text.translate(

        str.maketrans(

            "",

            "",

            string.punctuation

        )

    )

    tokens = []

    for word in text.split():

        if word not in STOPWORDS:

            tokens.append(

                STEMMER.stem(

                    word

                )

            )

    return " ".join(

        tokens

    )