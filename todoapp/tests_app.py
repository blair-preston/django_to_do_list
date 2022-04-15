from django.test import TestCase
from django.contrib.auth.models import User as Djuser
from .models import User
import json

# create a test django admin user:
test_djuser = {"username": "testuser", "password": "testpassword"}

# class allowing users to create a username and password for logging in
# a new_user of the User class is also created to be used in the test db for running the tests
class DjUsersTest(TestCase):
    def setUp(self):
        new_djuser = Djuser.objects.create(
            username= test_djuser["username"])
        new_djuser.set_password(test_djuser["password"])
        new_djuser.save()
        new_user = User.objects.create(
            name= 'Dragon'
        )
        new_user.save()

    def get_token(self):
        res = self.client.post('/api/token/',
            data=json.dumps({
                'username': test_djuser["username"],
                'password': test_djuser["password"],
            }),
        content_type='application/json',
        )
        result = json.loads(res.content)
        self.assertTrue("access" in result)
        return result["access"]

    # Make sure that unauthorized users are not allowed to POST (meaning they don't have the token)
    def test_unauthorized_cant_add_category(self):
        testuser = User.objects.last(),
        testid = int(testuser[0].id)
        # test category to add
        res = self.client.post('/api/categories/',
            data=json.dumps({
                "title": "Personal",
                "color": "Yellow",
                "user_id": testid 
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION=f'Bearer WRONG TOKEN'
            )
        self.assertEquals(res.status_code, 401)
        # test category to add
        res = self.client.post('/api/categories/',
                                data=json.dumps({
                                    "title": "House",
                                    "color": "Purple",
                                    "user_id": testid 
                                }),
                                content_type='application/json',
                                HTTP_AUTHORIZATION=f'Bearer WRONG TOKEN'
                                )
        self.assertEquals(res.status_code, 401)
        

    # Authorized users are allowed to POST (testing that they DO have the token)
    def test_authorized_can_add_category(self):
        testuser = User.objects.last(),
        testid = int(testuser[0].id)
        token = self.get_token()
        # test category to add
        res = self.client.post('/api/categories/',
                                data=json.dumps({
                                    "title": "House",
                                    "color": "Purple",
                                    "user_id": testid 
                                }),
                                content_type='application/json',
                                HTTP_AUTHORIZATION=f'Bearer {token}'
                                )
        self.assertEquals(res.status_code, 201)
        result = json.loads(res.content)
        self.assertEquals(result["title"], 'House')
        self.assertEquals(result["color"], 'Purple')

