def calculate_risk(

    threat_score

):

    if threat_score < 40:

        return "LOW"

    elif threat_score < 70:

        return "MEDIUM"

    return "HIGH"