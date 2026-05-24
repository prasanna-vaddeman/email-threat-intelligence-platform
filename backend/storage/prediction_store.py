from sqlalchemy import text
from backend.storage.postgres import SessionLocal

import logging


LOGGER = logging.getLogger(__name__)


def save_prediction(

    prediction,
    spam_probability,
    threat_score,

    confidence,
    threat_level,

    latency_ms,

    links_found,

    url_count,
    html_tag_count,
    uppercase_ratio,

    special_char_count,
    spam_keyword_count,
    exclamation_count

):

    if SessionLocal is None:

        LOGGER.warning(

            "Database unavailable"

        )

        return


    db = SessionLocal()

    try:

        query = text("""

        INSERT INTO predictions (

            prediction,

            spam_probability,

            threat_score,

            confidence,

            threat_level,

            latency_ms,

            links_found,

            url_count,

            html_tag_count,

            uppercase_ratio,

            special_char_count,

            spam_keyword_count,

            exclamation_count

        )

        VALUES (

            :prediction,

            :spam_probability,

            :threat_score,

            :confidence,

            :threat_level,

            :latency_ms,

            :links_found,

            :url_count,

            :html_tag_count,

            :uppercase_ratio,

            :special_char_count,

            :spam_keyword_count,

            :exclamation_count

        )

        """)

        db.execute(

            query,

            {

                "prediction":

                    str(prediction),

                "spam_probability":

                    float(spam_probability),

                "threat_score":

                    float(threat_score),

                "confidence":

                    float(confidence),

                "threat_level":

                    str(threat_level),

                "latency_ms":

                    float(latency_ms),

                "links_found":

                    int(links_found),

                "url_count":

                    float(url_count),

                "html_tag_count":

                    float(html_tag_count),

                "uppercase_ratio":

                    float(uppercase_ratio),

                "special_char_count":

                    float(special_char_count),

                "spam_keyword_count":

                    float(spam_keyword_count),

                "exclamation_count":

                    float(exclamation_count)

            }

        )

        db.commit()

        LOGGER.info(

            "Prediction stored successfully"

        )

    except Exception as exc:

        LOGGER.exception(

            f"Prediction storage failed: {exc}"

        )

        try:

            db.rollback()

        except Exception:

            pass

    finally:

        db.close()