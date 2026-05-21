"""
TXT + EML Parser
"""

from email import policy

from email.parser import BytesParser


def parse_uploaded_file(

    uploaded_file

):

    if uploaded_file is None:

        return ""

    extension=(

        uploaded_file.name

        .split(".")

        [-1]

        .lower()

    )

    if extension=="txt":

        return (

            uploaded_file

            .read()

            .decode(

                "utf-8",

                errors="ignore"

            )

        )

    if extension=="eml":

        msg=(

            BytesParser(

                policy=

                policy.default

            )

            .parse(

                uploaded_file

            )

        )

        text=[]

        for part in msg.walk():

            content_type=(

                part.get_content_type()

            )

            if (

                content_type

                =="text/plain"

            ):

                try:

                    text.append(

                        part.get_content()

                    )

                except:

                    pass

        return "\n".join(

            text

        )

    return ""