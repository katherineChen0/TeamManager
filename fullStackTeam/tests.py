from django.test import TestCase, Client
from django.urls import reverse
from .models import Member

class TeamMemberTests(TestCase):
    def setUp(self):
        # Create a test client
        self.client = Client()
        
        # Create a test member
        self.test_member = Member.objects.create(
            first_name="John",
            last_name="Doe",
            phone="123-456-7890",
            email="john@example.com",
            role="Regular"
        )

    def test_member_list_view(self):
        # Test that the member list page loads
        response = self.client.get(reverse('members'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")
        self.assertContains(response, "123-456-7890")

    def test_add_member(self):
        # Test adding a new member
        new_member_data = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'phone': '987-654-3210',
            'email': 'jane@example.com',
            'role': 'Admin'
        }
        response = self.client.post(reverse('add_member'), new_member_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        
        # Verify the member was created
        self.assertTrue(Member.objects.filter(email='jane@example.com').exists())

    def test_edit_member(self):
        # Test editing an existing member
        updated_data = {
            'first_name': 'John',
            'last_name': 'Updated',
            'phone': '123-456-7890',
            'email': 'john.updated@example.com',
            'role': 'Admin'
        }
        response = self.client.post(
            reverse('details', args=[self.test_member.id]), 
            updated_data
        )
        self.assertEqual(response.status_code, 302)  # Redirect after successful update
        
        # Verify the member was updated
        updated_member = Member.objects.get(id=self.test_member.id)
        self.assertEqual(updated_member.last_name, 'Updated')
        self.assertEqual(updated_member.email, 'john.updated@example.com')

    def test_delete_member(self):
        # Test deleting a member
        response = self.client.post(
            reverse('details', args=[self.test_member.id]),
            {'delete': 'true'}
        )
        self.assertEqual(response.status_code, 302)  # Redirect after successful deletion
        
        # Verify the member was deleted
        self.assertFalse(Member.objects.filter(id=self.test_member.id).exists())

    def test_phone_number_format(self):
        # Test phone number format validation
        invalid_phone_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'phone': '1234567890',  # Invalid format
            'email': 'test@example.com',
            'role': 'Regular'
        }
        response = self.client.post(reverse('add_member'), invalid_phone_data)
        self.assertEqual(response.status_code, 200)  # Should stay on the same page
        
        # Verify the member wasn't created
        self.assertFalse(Member.objects.filter(email='test@example.com').exists())

    def test_required_fields(self):
        # Test that all required fields must be filled
        incomplete_data = {
            'first_name': 'Test',
            # missing last_name
            'phone': '123-456-7890',
            'email': 'test@example.com',
            'role': 'Regular'
        }
        response = self.client.post(reverse('add_member'), incomplete_data)
        self.assertEqual(response.status_code, 200)  # Should stay on the same page
        
        # Verify the member wasn't created
        self.assertFalse(Member.objects.filter(email='test@example.com').exists())