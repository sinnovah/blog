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
    __database_port = int(os.getenv("DATABASE_PORT", 5432))
    __database_host = os.getenv("DATABASE_HOST", "localhost")
    __database_user = os.getenv("DATABASE_USER", "postgres")
    __database_password = os.getenv("DATABASE_PASSWORD", None)
    __database_name = os.getenv("DATABASE_NAME", None)

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

    @staticmethod
    def get_database_port():
        """
        Get the database port from the configuration.

        Returns:
            int: The database port, defaulting to 5432
            if not set in the environment.
        """
        return Configuration.__database_port

    @staticmethod
    def get_database_host():
        """
        Get the database host from the configuration.

        Returns:
            str: The database host, defaulting to "localhost"
            if not set in the environment.
        """
        return Configuration.__database_host

    @staticmethod
    def get_database_user():
        """
        Get the database user from the configuration.

        Returns:
            str: The database user, defaulting to "postgres"
            if not set in the environment.
        """
        return Configuration.__database_user

    @staticmethod
    def get_database_password():
        """
        Get the database password from the configuration.

        Returns:
            str: The database password, defaulting to None
            if not set in the environment.
        """
        return Configuration.__database_password

    @staticmethod
    def get_database_name():
        """
        Get the database name from the configuration.

        Returns:
            str: The database name, defaulting to None
            if not set in the environment.
        """
        return Configuration.__database_name
