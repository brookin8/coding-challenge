import json
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Referral
from .serializers import ReferralSerializer

# tests for views
client = Client();

class GetAllReferralsTest(TestCase):

    def setUp(self):
        # add test data
        Referral.objects.create(title="Spartans", clicks=0)
        Referral.objects.create(title="Wolverines", clicks=0)
        Referral.objects.create(title="Broncos", clicks=0)

    def test_get_all_referrals(self):
        # hit the API endpoint
        response = client.get(
            reverse("get_post_referrals")
        )
        # fetch the data from db
        expected = Referral.objects.all()
        serialized = ReferralSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleReferralTest(TestCase):

    def setUp(self):
        self.Spartans = Referral.objects.create(title="Spartans", clicks=0)
        self.Wolverines = Referral.objects.create(title="Wolverines", clicks=0)
        self.Broncos = Referral.objects.create(title="Broncos", clicks=0)

    def test_get_valid_single_referral(self):
        response = client.get(
            reverse("get_delete_update_referral", kwargs={'pk': self.Wolverines.pk})
        )
        expected = Referral.objects.get(pk=self.Wolverines.pk)
        expected.clicks += 1
        serialized = ReferralSerializer(expected)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_referral(self):
        response = client.get(
            reverse("get_delete_update_referral", kwargs={'pk': 100})
        )
        expected = Referral.objects.get(pk=self.Wolverines.pk)
        serialized = ReferralSerializer(expected)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewReferralTest(TestCase):

	def setUp(self):
		self.valid_payload = {
			'title': 'Chips'
		}
		self.invalid_payload = {
			'title': ''
		}

	def test_create_valid_referral(self):
		response = client.post(
			reverse('get_post_referrals'),
			data=json.dumps(self.valid_payload),
			content_type='application/json'
		)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class UpdateSingleReferralTest(TestCase):

	def setUp(self):
		self.Spartans = Referral.objects.create(title="Spartans", clicks=0)
		self.Wolverines = Referral.objects.create(title="Wolverines", clicks=0)
		self.Broncos = Referral.objects.create(title="Broncos", clicks=0)
		self.valid_payload = {
			'title': 'Chips'
		}
		self.invalid_payload = {
			'title': ''
		}

	def test_valid_update_referral(self):
		response = client.put(
			reverse("get_delete_update_referral", kwargs={'pk': self.Wolverines.pk}),
			data=json.dumps(self.valid_payload),
			content_type='application/json'
		)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

	def test_invalid_update_referral(self):
		response = client.put(
			reverse("get_delete_update_referral", kwargs={'pk': self.Wolverines.pk}),
			data=json.dumps(self.invalid_payload),
			content_type='application/json'
		)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleReferralTest(TestCase):

	def setUp(self):
		self.Spartans = Referral.objects.create(title="Spartans", clicks=0)
		self.Wolverines = Referral.objects.create(title="Wolverines", clicks=0)

	def test_valid_delete_referral(self):
		response = client.delete(
			reverse("get_delete_update_referral", kwargs={'pk': self.Wolverines.pk}),
		)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

	def test_invalid_delete_referral(self):
		response = client.delete(
			reverse("get_delete_update_referral", kwargs={'pk': 100}),
		)
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
