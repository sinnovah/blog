import os


class Configuration:
    def __init__(self):

        self.__blog_name = os.getenv("BLOG_NAME", "My Blog")

