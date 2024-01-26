#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None  # Use a private attribute to store page_count initially
        self.page_count = page_count  # Use the property to set the actual page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
        