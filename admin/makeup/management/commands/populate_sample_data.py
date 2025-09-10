from django.core.management.base import BaseCommand
from makeup.models import Makeup, Service, User, Feedback

class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **options):
        # Create sample services
        services_data = [
            {'name': 'Hair Styling', 'description': 'Professional hair styling services', 'price': 1500.00},
            {'name': 'Garment Draping', 'description': 'Traditional garment draping', 'price': 800.00},
            {'name': 'Eye Lenses', 'description': 'Colored contact lenses', 'price': 500.00},
            {'name': 'Hair Extensions', 'description': 'High-quality hair extensions', 'price': 2000.00},
            {'name': 'Eye Lashes', 'description': 'Eyelash extensions and styling', 'price': 1200.00},
            {'name': 'Nail Extensions', 'description': 'Professional nail art and extensions', 'price': 1000.00},
        ]

        for service_data in services_data:
            Service.objects.get_or_create(
                name=service_data['name'],
                defaults=service_data
            )

        # Create sample makeup data
        makeup_data = []
        for i in range(60):
            makeup = {
                'name': f'Makeup {i+1}',
                'type': 'bridal' if i % 2 == 0 else 'party',
                'description': 'Beautiful makeup for events and special occasions.',
                'price': [2000.00, 6000.00, 12000.00, 18000.00][i % 4],
                'is_special_deal': i % 5 == 0,
                'is_award_winner': i % 7 == 0,
            }
            makeup_data.append(makeup)

        for makeup_item in makeup_data:
            Makeup.objects.get_or_create(
                name=makeup_item['name'],
                defaults=makeup_item
            )

        # Create sample feedback data
        feedback_data = [
            {'name': 'Priya Sharma', 'email': 'priya@example.com', 'rating': 5, 'message': 'Amazing service! The makeup artist was professional and the results were stunning. Highly recommend!'},
            {'name': 'Rahul Verma', 'email': 'rahul@example.com', 'rating': 5, 'message': 'Best bridal makeup experience ever. They made me feel so beautiful on my special day.'},
            {'name': 'Anjali Patel', 'email': 'anjali@example.com', 'rating': 4, 'message': 'Great attention to detail. The hairstyling was perfect for my wedding.'},
            {'name': 'Vikram Singh', 'email': 'vikram@example.com', 'rating': 5, 'message': 'Outstanding nail art! Creative and long-lasting. Will definitely come back.'},
            {'name': 'Sneha Gupta', 'email': 'sneha@example.com', 'rating': 5, 'message': 'Professional team, excellent results. Made my party look unforgettable.'},
        ]

        for feedback_item in feedback_data:
            Feedback.objects.get_or_create(
                name=feedback_item['name'],
                email=feedback_item['email'],
                defaults=feedback_item
            )

        # Create admin user if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@glamourstudio.com',
                password='admin123',
                phone_number='1234567890'
            )

        self.stdout.write(self.style.SUCCESS('Sample data populated successfully!'))
