from class_permission import Permissions, id_p_is_None
import unittest

class testUnitaire(unittest.TestCase):

    def test_init_permissions(self):
        with self.assertRaises(id_p_is_None):
            Permissions()

if __name__ == '__main__':
    unittest.main()