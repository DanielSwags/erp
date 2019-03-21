
class PaginationHelper:
    collection = (['a', 'b', 'c', 'd', 'e', 'f'], 4)
    items_per_page = 2

    def __init__(self, collection, items_per_page, ):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return self.collection

    def page_count(self):
        return self.limit

    def page_item_count(self,page_index):



paginationHelper = PaginationHelper()
paginationHelper.item_count()
