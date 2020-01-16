import unittest
import sys
import os

current_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]
sys.path.insert(0, parent_dir)

import ptestcs


class DemoTest(unittest.TestCase):
    def test_readme_content(self):
        # print(ptestcs.readme())
        self.assertFalse(ptestcs.readme().find('test') == -1)
        
if __name__ == '__main__':
    unittest.main()