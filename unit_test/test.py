import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests_rachid import *
from tests_arnaud import *
from tests_Roles import *
from tests_unitaire import *


import unittest

if __name__ == "__main__":
    unittest.main()
