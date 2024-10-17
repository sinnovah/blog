import os


class Configuration:
    """Class for site configuration."""

    def __init__(self):
        """
        Set site configuration values from .env file.

        Adds default value if there is no environment variable specified.
        """
        self.__blog_name = os.getenv("BLOG_NAME", "My Blog")
