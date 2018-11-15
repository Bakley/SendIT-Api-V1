"""Test file for parcel model."""
from app.api.v1.models.parcel_models import ParcelModel, parcel

from .import BaseClass


class TestUserModel(BaseClass):
    """docstring for TestUserModel."""

    def test_can_save_a_parcel(self):
        """Test if we can save a parcel."""
        parcel_orders = self.parcel_order1.save()
        self.assertEqual(1, len(parcel))
        self.assertTrue(isinstance(parcel_orders, list))

    def test_can_delete_parcel(self):
        """Test suucessful deletion of parcel."""
        self.parcel_order1.save()
        self.assertEqual(1, len(parcel))
        parcel_order = ParcelModel.get_all_parcels(id)
        parcel_order.pop()
        self.assertEqual(0, len(parcel))

    def test_get_all_parcel(self):
        """Test if we can get all parcels."""
        pass

    def test_weight_cannot_be_string(self):
        """Test if weight cannot be a string."""
        pass
