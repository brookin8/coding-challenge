from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Referral
from .serializers import ReferralSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_referral(title=""):
        if title != "":
            Referral.objects.create(title=title, clicks=0)

    def setUp(self):
        # add test data
        self.create_referral("Spartans")
        self.create_referral("Wolverines")
        self.create_referral("Broncos")
        self.create_referral("Chips")


class GetAllReferralsTest(BaseViewTest):

    def test_get_all_referrals(self):
        # hit the API endpoint
        response = self.client.get(
            reverse("referrals-all")
        )
        # fetch the data from db
        expected = Referral.objects.all()
        serialized = ReferralSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
