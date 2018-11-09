"""Test model file for users."""
from app.api.v1.models.user_models import UserModel, database

from .import BaseClass


class TestUserModel(BaseClass):
    """docstring for TestUserModel."""

    def test_can_save_user(self):
        """Test if we can save a user."""
        user = self.user1.save()
        self.assertEqual(1, len(database.users))
        self.assertTrue(isinstance(user, dict))

    def test_can_delete_user(self):
        """Test suucessful deletion of user."""
        self.user1.save()
        self.assertEqual(1, len(database.users))
        user = UserModel.get_all_user(id=1)
        user.delete()
        self.assertEqual(0, len(database.users))

    def test_get_a_none_registered_user(self):
        """Test cannot get a non registerd user."""
        user = UserModel.get(id)
        self.assertEqual('User does not exist', user['message'])

    def test_get_user(self):
        """Test successfully get a user."""
        self.user1.save()
        user = UserModel.get(id=1)
        self.assertIsInstance(user, UserModel)

    def test_user_password_match(self):
        """Test if the user password matches."""
        pass
