from django.contrib.auth.hashers import make_password
from django.test import TestCase

from user.models import User


# Create your tests here.

class UserTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            email="test_login@naver.com",
            nickname="test_nickname",
            name="test_name",
            password=make_password("test_password"),
            profile_image="default_profile.png",
        )

    def test(self):
        self.assertEqual(1, 1) # a랑 b랑 같으면 테스트 통과 아니면 실패


    # 정상적으로 회원가입 API를 호출했을 때 200이 나오는지 확인하는 테스트
    def test_join(self):
        response = self.client.post('/user/join', data=dict( # user/join 이라는 api를 post로 부른다
            email="test_email@naver.com",
            nickname="test_nickname",
            name="test_name",
            password="test_password",))
        self.assertEqual(response.status_code, 200)

        user = User.objects.filter(email="test_email@naver.com").first()

        self.assertEqual(user.nickname, "test_nickname")
        self.assertEqual(user.name, "test_name")
        #self.assertEqual(user.email, "test_email@naver.com")
        self.assertTrue(user.check_password("test_password"))


    def test_login(self):
        response = self.client.post('/user/login', data=dict(
            email="test_login@naver.com",
            password="test_password", ))

        self.assertEqual(response.status_code, 200)