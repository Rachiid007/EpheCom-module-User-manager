import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tests_rachid
import tests_arnaud
import tests_Roles
import tests_unitaire

import unittest

if __name__ == "__main__":
    unittest.main()
