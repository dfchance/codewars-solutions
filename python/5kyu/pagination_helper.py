# Kata: Pagination Helper
# Difficulty: 5 kyu
# URL: https://www.codewars.com/kata/515bb423de843ea99400000a
# 
# Description: 
# Create a class designed to take in an array of values and an integer indicating how many items will be allowed per page.  
# Develop functions to return the item_count, page_count, page_item_count and page_index for provided values.    
#
# Approach:
# Use division, floor division and modulo to determine and return the appropriate values.  

class PaginationHelper:
    
    # takes in an array of items and an integer indicating how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
    
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
    
    # returns the number of pages
    def page_count(self):
        pages = len(self.collection) // self.items_per_page
        if len(self.collection) % self.items_per_page != 0:
            # There is a page with less than items_per_page 
            pages += 1
        return pages
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        # check page_index in range
        if page_index < 0 or page_index > (self.page_count() - 1):
            return -1
        # check for edge cases
        elif len(self.collection) > 0 and self.items_per_page == len(self.collection):
            return len(self.collection)
        # check if final page
        elif page_index == (self.page_count() - 1):
            item_count = len(self.collection) % self.items_per_page
            # check for edge case where page is full (no remainder) 
            if item_count == 0:
                return self.items_per_page
            else: 
                return item_count
        else:
            return self.items_per_page
            
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        # check item_index is in range
        if item_index >= len(self.collection) or item_index < 0 or len(self.collection) <= 0:
            return -1
        else:
            return item_index // self.items_per_page
