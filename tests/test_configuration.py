from unittest import TestCase
import os
from configuration import Configuration


class TestConfiguration(TestCase):
    """Unit tests for the Configuration class."""

    def setUp(self):
        """
        Set up test environment.

        Clear environment variables to test default values.
        """
        # Clear environment variables to test default values
        os.environ.pop("BLOG_NAME", None)
        self.config = Configuration()

    def test_default_blog_name(self):
        """Test that the default blog name is 'My Blog'."""
        self.assertEqual(self.config.get_blog_name(), "My Blog")
