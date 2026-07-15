import re


class ConstitutionParser:
    """
    Stateful parser for the Constitution of India.

    Keeps track of the current Part and Article while reading pages
    sequentially.
    """

    def __init__(self):

        self.current_part = None
        self.current_article = None
        self.started = False

    # -----------------------------------------------------

    def detect_start(self, text):
        """
        Ignore Preface, Contents etc.

        Parsing begins only after PREAMBLE or Article 1.
        """

        if self.started:
            return

        if "PREAMBLE" in text.upper():
            self.started = True

        elif re.search(r"^\s*1\.\s", text, re.MULTILINE):
            self.started = True

    # -----------------------------------------------------

    def update_part(self, text):

        match = re.search(
            r"^\s*PART\s+([IVXLCDM]+)",
            text,
            re.MULTILINE | re.IGNORECASE
        )

        if match:

            self.current_part = f"PART {match.group(1).upper()}"

    # -----------------------------------------------------

    def update_article(self, text):

        """
        Detect actual Article headings only.

        Example:

        19.
        Protection of...

        NOT

        under article 19
        """

        pattern = re.compile(
            r"^\s*(\d+[A-Z]?)\.\s+[A-Z]",
            re.MULTILINE
        )

        match = pattern.search(text)

        if match:

            self.current_article = match.group(1)

    # -----------------------------------------------------

    def parse_page(self, page):

        text = page["text"]

        self.detect_start(text)

        if self.started:

            self.update_part(text)

            self.update_article(text)

        metadata = {

            "part": self.current_part,

            "article": self.current_article

        }

        return metadata