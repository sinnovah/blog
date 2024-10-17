import os
from dotenv import load_dotenv


class Configuration:
    """
    Class for site configuration.

    This class loads configuration values from environment variables.
    """

    # Load environment variables from the .env file
    load_dotenv()

    # Class variables to store configuration values
    __blog_name = os.getenv("BLOG_NAME", "My Blog")
    __environment = os.getenv("ENVIRONMENT", "Development")
    __server_port = int(os.getenv("SERVER_PORT", 8000))

    @staticmethod
    def get_blog_name():
        """
        Get the blog name from the configuration.

        Returns:
            str: The blog name, defaulting to "My Blog"
            if not set in the environment.
        """
        return Configuration.__blog_name

    @staticmethod
    def get_environment():
        """
        Get the environment (Development or Production).

        Returns:
            str: The environment, defaulting to "Development"
            if not set in the environment.
        """
        return Configuration.__environment

    @staticmethod
    def get_server_port():
        """
        Get the server port from the configuration.

        Returns:
            int: The server port, defaulting to 8000
            if not set in the environment.
        """
        return Configuration.__server_port
