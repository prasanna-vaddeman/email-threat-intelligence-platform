from prometheus_client import Counter
from prometheus_client import Histogram


PREDICTION_COUNTER = Counter(

    "email_predictions_total",

    "Total predictions"

)


SPAM_COUNTER = Counter(

    "spam_predictions_total",

    "Spam predictions"

)


ERROR_COUNTER = Counter(

    "prediction_errors_total",

    "Prediction errors"

)


LATENCY = Histogram(

    "prediction_latency_ms",

    "Prediction latency"

)