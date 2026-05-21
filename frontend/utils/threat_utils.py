"""
Threat Utilities
"""


def calculate_risk(

spam_probability

):

    if spam_probability<40:

        return "LOW"

    if spam_probability<70:

        return "MEDIUM"

    return "HIGH"