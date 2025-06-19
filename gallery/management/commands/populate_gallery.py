from django.core.management.base import BaseCommand
from gallery.models import Gallery
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Create sample gallery items'

    def handle(self, *args, **options):
        # Check if gallery items already exist
        if Gallery.objects.exists():
            self.stdout.write(
                self.style.SUCCESS(f'Gallery already has {Gallery.objects.count()} items')
            )
            return

        # Create sample gallery items using existing media files
        sample_items = [
            {
                'title': 'Beautiful Wedding Ceremony',
                'description': 'A magical wedding celebration with stunning decorations',
                'image': 'gallery_images/1.png'
            },
            {
                'title': 'Corporate Event Excellence',
                'description': 'Professional corporate event management',
                'image': 'gallery_images/482354892_17857941756379721_5207919914261393666_n.webp'
            },
            {
                'title': 'Birthday Party Celebration',
                'description': 'Colorful and joyful birthday party setup',
                'image': 'gallery_images/482717563_17857941768379721_4914421544574644284_n.webp'
            },
        ]

        created_count = 0
        for item_data in sample_items:
            # Check if the image file exists
            image_path = os.path.join(settings.MEDIA_ROOT, item_data['image'])
            if os.path.exists(image_path):
                gallery_item, created = Gallery.objects.get_or_create(
                    title=item_data['title'],
                    defaults={
                        'description': item_data['description'],
                        'image': item_data['image']
                    }
                )
                if created:
                    created_count += 1
                    self.stdout.write(f'Created: {gallery_item.title}')
            else:
                self.stdout.write(f'Image not found: {item_data["image"]}')

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} gallery items')
        )
