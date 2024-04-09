"""
Connor Warner
CIS 218
2/28/24
"""

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from .models import Twit, Comment

class TwitsTests(TestCase):
    """Twit Tests"""
    
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", password="secret"
        )
        cls.twit = Twit.objects.create(
            body="Test Twit",
            author=cls.user,
            image_url="image.png",
        )

        cls.comment = Comment.objects.create(
            twit= cls.twit,
            author = cls.user,
            comment = "Test comment",
        )

        cls.client = Client()
        cls.client.force_login(cls.user)


    # Twit Tests
    def test_twit_model(self):
        """Test twit model"""
        self.assertEqual(self.twit.body, "Test Twit")
        self.assertEqual(str(self.twit), "Test Twit")
        self.assertEqual(self.twit.author.username, "testuser")
        self.assertEqual(self.twit.image_url, "image.png")


    def test_url_exists_at_correct_location_listview(self):
        """Test url exists at correct location list view"""
        self.client.force_login(self.user)
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_twit_listview(self):
        """Test twit list view"""
        self.client.force_login(self.user)
        response = self.client.get(reverse("twit_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Twit")
        self.assertTemplateUsed(response, "twit_list.html")

    
    def test_url_exists_at_correct_location_updateview(self):
        """Test url exists at correct location update view"""
        self.client.force_login(self.user)
        response = self.client.get("/1/edit/")
        self.assertEqual(response.status_code, 200 )

    def test_twit_updateview(self):
        """Test review create view"""
        self.client.force_login(self.user)
        response = self.client.get(reverse("twit_edit", kwargs={"pk": self.twit.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Twit - Edit")
        self.assertTemplateUsed(response, "twit_edit.html")

    
    def test_twit_url_exists_at_correct_location_deleteview(self):
        """Test url exists at correct location delete view"""
        self.client.force_login(self.user)
        response = self.client.get("/1/delete/")
        self.assertEqual(response.status_code, 200 )

    def test_twit_deleteview(self):
        """Test twit delete view"""
        self.client.force_login(self.user)
        response = self.client.get(reverse("twit_delete", kwargs={"pk": self.twit.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Are you sure you want to delete the following Twit?")
        self.assertTemplateUsed(response, "twit_delete.html")


    def test_url_exists_at_correct_location_createview(self):
        """Test url exists at correct location create view"""
        self.client.force_login(self.user)
        response = self.client.get("/new/")
        self.assertEqual(response.status_code, 200 )

    def test_twit_createview(self):
        """Test twit create view"""
        self.client.force_login(self.user)
        response = self.client.get(reverse("twit_new"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "New")
        self.assertTemplateUsed(response, "twit_new.html")

    

    # Comment Tests
    def test_comment_model(self):
        """Test Comment Model"""
        self.client.force_login(self.user)
        self.assertEqual(self.comment.comment, "Test comment")
        self.assertEqual(str(self.comment), "Test comment")
        self.assertEqual(self.comment.author.username, "testuser")

    
    def test_url_exists_at_correct_location_twit_comment_view(self):
        """Test url exists at correct location comment view"""
        self.client.force_login(self.user)
        response = self.client.get("/1/")
        self.assertEqual(response.status_code, 200 )

    def test_comment_twit_comment_view(self):
        """Test twit comment view"""
        self.client.force_login(self.user)
        response = self.client.get(reverse("twit_comment", kwargs={"pk": self.twit.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Add New Comment")
        self.assertTemplateUsed(response, "twit_comment.html")



    # Profile Tests
    def test_twit_url_exists_at_correct_location_profile_public_view(self):
        """Test url exists at correct location delete view"""
        self.client.force_login(self.user)
        response = self.client.get("/accounts/profile_public/1/")
        self.assertEqual(response.status_code, 200 )

    def test_profile_public_view(self):
        """Test Profile Public View"""
        self.client.force_login(self.user)
        response = self.client.get(reverse("profile_update", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Update Profile")
        self.assertTemplateUsed(response, "registration/profile_update.html")


    def test_twit_url_exists_at_correct_location_profile_update_view(self):
        """Test url exists at correct location delete view"""
        self.client.force_login(self.user)
        response = self.client.get("/accounts/profile/1/")
        self.assertEqual(response.status_code, 200 )

    def test_profile_update_view(self):
        """Test Profile Update View"""
        self.client.force_login(self.user)
        response = self.client.get(reverse("profile_public", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Public Profile")
        self.assertTemplateUsed(response, "registration/profile_public.html")