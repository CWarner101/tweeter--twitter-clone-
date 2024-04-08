"""
Connor Warner
CIS 218
2/28/24
"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Twit, Comment

class TwitsTests(TestCase):
    """Twit Tests"""
    
    @classmethod
    def setUpTestData(cls):
        cls.author = get_user_model().objects.create_user(
            username="testuser", password="secret"
        )
        cls.twit = Twit.objects.create(
            body="Test Twit",
            author=cls.author,
            image_url="image.png",
        )

        cls.comment = Comment.objects.create(
            twit= cls.twit,
            author = cls.author,
            comment = "Test comment",
        )

    # Twit Tests
    def test_twit_model(self):
        """Test twit model"""
        self.assertEqual(self.twit.body, "Test Twit")
        self.assertEqual(str(self.twit), "Test Twit")
        self.assertEqual(self.twit.author.username, "testuser")
        self.assertEqual(self.twit.image_url, "image.png")

    def test_twit_url_exists_at_correct_location_listview(self):
        """Test url exists at correct location list view"""
        response = self.client.get("")
        self.assertEqual(response.status_code, 302)

    def test_twit_listview(self):
        """Test twit list view"""
        response = self.client.get(reverse("twit_list"))
        self.assertContains(response, "Test Twit")
        self.assertTemplateUsed(response, "twit_list.html")

    # def test_twit_detailview(self):
    #     """Test twit detail view"""
    #     response = self.client.get(reverse("twit_detail", kwargs={"pk": self.twit.pk}))
    #     no_response = self.client.get("/twit/100000/")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(no_response.status_code, 404)
    #     self.assertContains(response, "Test twit")
    #     self.assertTemplateUsed(response, "twit_detail.html")

    
    # # Comment Tests
    # def test_review_model(self):
    #     """Test the review model"""
    #     self.assertEqual(self.review.twit.name, "Test Restaurant")
    #     self.assertEqual(str(self.review), "Test review")
    #     self.assertEqual(self.review.rating, 3)
    #     self.assertEqual(self.review.get_absolute_url(), "/review/1/")


    # def test_review_url_exists_at_correct_location_detailview(self):
    #     """Test url exists at correct location detail view"""
    #     response = self.client.get("/review/1/")
    #     self.assertEqual(response.status_code, 200 )
        
    # def test_review_detailview(self):
    #     """Test review detail view"""
    #     response = self.client.get(reverse("review_detail", kwargs={"pk": self.restaurant.pk}))
    #     no_response = self.client.get("/review/100000/")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(no_response.status_code, 404)
    #     self.assertContains(response, "Test review")
    #     self.assertTemplateUsed(response, "review_detail.html")


    # def test_review_url_exists_at_correct_location_createview(self):
    #     """Test url exists at correct location create view"""
    #     response = self.client.get("/review/create/")
    #     self.assertEqual(response.status_code, 200 )

    # def test_review_createview(self):
    #     """Test review create view"""
    #     response = self.client.get(reverse("review_create"))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "Write a Review")
    #     self.assertTemplateUsed(response, "review_create.html")


    # def test_review_url_exists_at_correct_location_updateview(self):
    #     """Test url exists at correct location update view"""
    #     response = self.client.get("/review/1/update/")
    #     self.assertEqual(response.status_code, 200 )

    # def test_review_createview(self):
    #     """Test review create view"""
    #     response = self.client.get(reverse("review_update", kwargs={"pk": self.review.pk}))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "Test Restaurant - Edit Review")
    #     self.assertTemplateUsed(response, "review_update.html")

    
    # def test_review_url_exists_at_correct_location_deleteview(self):
    #     """Test url exists at correct location delete view"""
    #     response = self.client.get("/review/1/delete/")
    #     self.assertEqual(response.status_code, 200 )

    # def test_review_deleteview(self):
    #     """Test review delete view"""
    #     response = self.client.get(reverse("review_delete", kwargs={"pk": self.review.pk}))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "Are you sure you want to delete this review?")
    #     self.assertTemplateUsed(response, "review_delete.html")
