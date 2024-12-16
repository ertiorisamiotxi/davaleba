from django.core.management.base import BaseCommand
from shop.models import Category, Item, Tag

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        categories = Category.categories.with_item_count()
        for i in categories:
            print(f"{i.name},{i.item_count}")
        
        items = Item.items.with_tag_count()
        for i in items:
            print(f"items {i.name}, {i.tag_count}")
        
        popular = Tag.tags.popular_tags(6.9)
        for i in popular:
            print(f" popualr niggas :{i.name} {i.item_count}" )