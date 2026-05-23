from sqlalchemy import text
from backend.storage.postgres import SessionLocal
import logging


LOGGER = logging.getLogger(__name__)


def save_prediction(

    prediction,
    spam_probability,
    threat_score,
    latency_ms,
    links_found,
    uppercase_ratio

):

    if SessionLocal is None:

        LOGGER.warning(

            "Database unavailable"

        )

        return


    db = SessionLocal()

    try:

        query = text("""

        INSERT INTO predictions(

            prediction,
            spam_probability,
            threat_score,
            latency_ms,
            links_found,
            uppercase_ratio

        )

        VALUES(

            :prediction,
            :spam_probability,
            :threat_score,
            :latency_ms,
            :links_found,
            :uppercase_ratio

        )

        """)

        db.execute(

            query,

            {

                "prediction": str(prediction),

                "spam_probability": float(spam_probability),

                "threat_score": float(threat_score),

                "latency_ms": float(latency_ms),

                "links_found": int(links_found),

                "uppercase_ratio": float(uppercase_ratio)

            }

        )

        db.commit()

        LOGGER.info(

            "Prediction stored successfully"

        )

    except Exception as e:

        db.rollback()

        LOGGER.exception(

            f"Prediction storage failed: {e}"

        )

    finally:

        db.close()