from django.test import TestCase

class SmokeTest(TestCase):
    def test_django_works(self):
        """Verify Django can run a test without exploding"""
        self.assertEqual(1 + 1, 2)
    
    def test_admin_page(self):
        """Check if admin page is accessible (built into Django)"""
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)  # Redirects to login