from django.test import TestCase
from django.contrib.auth.models import User
import json

test_user = {"username": "testuser", "password": "testpassword"}

# class allowing users to create a username and password
# and then to be allowed to log in
class UsersTest(TestCase):
    def setUp(self):
        new_user = User.objects.create(
            username=test_user["username"])
        new_user.set_password(test_user["password"])
        new_user.save()

    def get_token(self):
        res = self.client.post('/api/token/',
            data=json.dumps({
                'username': test_user["username"],
                'password': test_user["password"],
            }),
        content_type='application/json',
        )
        result = json.loads(res.content)
        self.assertTrue("access" in result)
        return result["access"]

    # test should return 401 error
    # Make sure that unauthorized users are not allowed to POST
    def test_unauthorized_cant_add_dailies(self):
        res = self.client.post('/api/dailies/',
        data=json.dumps({
            "label": "Read book club chapter",
            "category_id": 9,
            "user_id": 4
        }),
        content_type='application/json',
        )
        self.assertEquals(res.status_code, 400)
        res = self.client.post('/api/dailies/',
        data=json.dumps({
        "label": "20 push-ups",
        "category_id": 8,
        "user_id": 3
        }),
        content_type='application/json',
        HTTP_AUTHORIZATION=f'Bearer WRONG TOKEN'
        )
        self.assertEquals(res.status_code, 400)

        # Authorized users are allowed to POST
    def test_authorized_can_add_dailes(self):
        token = self.get_token()
        res = self.client.post('/api/dailies/',
                                data=json.dumps({
                                    "label": "Read book club chapter",
                                    "category_id": 9,
                                    "user_id": 4
                                }),
                                content_type='application/json',
                                HTTP_AUTHORIZATION=f'Bearer {token}'
                                )
        self.assertEquals(res.status_code, 201)
        result = json.loads(res.content)["data"]
        self.assertEquals(result["label"], '20 push-ups')
        self.assertEquals(result["category_id"], 8)
        self.assertEquals(result["user_id"], 4)
