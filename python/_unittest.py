#!/usr/bin/env python
"""
_unittest.py - Recipes using unittest
"""
import os
import shutil
import unittest
import unittest.mock


def clear_dir(path):
    """Recursively delete files in a directory.

    Raise FileNotFoundError if the input path does not exist.
    Raise ValueError if the input path is not a directory.
    """
    if not os.path.exists(path):
        raise FileNotFoundError
    elif not os.path.isdir(path):
        raise ValueError('{} is not a directory'.format(path))

    for root, _, files in os.walk(path):
        for filename in files:
            os.remove(os.path.join(root, filename))


# Helper method for test cases.
def touch_file(path):
    """Touch the file at the given path."""
    open(path, 'w').close()


class TempDirTestCase(unittest.TestCase):
    """Base TestCase that creates a temporary directory.

    The temporary directory path is stored in the temp_dir attribute.
    The setUp method creates the temporary directory before each
      test and the tearDown method recursively deletes the contents
      of the temporary directory afterward.
    """
    def __init__(self, *args, **kwargs):
        """Determine which testing path to use."""
        super().__init__(*args, **kwargs)
        if os.path.isdir('/tmp'):
            self.temp_dir = '/tmp/unittest_temp_dir'
        else:
            self.temp_dir = './unittest_temp_dir'

    def setUp(self):
        """Create temporary directory.

        Throw an error if the testing directory existed before.
        """
        os.mkdir(self.temp_dir)

    def tearDown(self):
        """Clear temporary directory."""
        shutil.rmtree(self.temp_dir)
        assert not os.path.exists(self.temp_dir)


class ClearDirTest(TempDirTestCase):
    """Test case for clear_dir function."""
    # Test paths should be relative to a root temp_dir.
    TEST_SUBDIRS = ['sub', 'sub/dir', 'sub/sub']
    TEST_FILES = ['A.txt', 'B.txt', 'sub/C.txt', 'sub/sub/D.txt']

    def __init__(self, *args, **kwargs):
        """Calculate full paths of testing files."""
        super().__init__(*args, **kwargs)
        self.test_file_paths = [os.path.join(self.temp_dir, rel_path)
                                for rel_path in self.TEST_FILES]

    def setUp(self):
        """Create testing files."""
        super().setUp()
        for subdir in self.TEST_SUBDIRS:
            os.makedirs(subdir, exist_ok=True)
            assert os.path.isdir(subdir)
        for path in self.test_file_paths:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            touch_file(path)
            assert os.path.isfile(path)

    def test_clear_dir(self):
        """Test that clear_dir removes all files but no subdirectories."""
        clear_dir(self.temp_dir)
        for path in self.test_file_paths:
            self.assertFalse(os.path.exists(path))
        for subdir in self.TEST_SUBDIRS:
            self.assertTrue(os.path.isdir(subdir))


class ClearDirMissingInputTest(unittest.TestCase):
    """Test nonexistent input to clear_dir."""
    def test_nonexistant_input(self):
        """Test that FileNotFoundError is thrown for nonexistant input."""
        with self.assertRaises(FileNotFoundError):
            clear_dir('./nonexistant_path')


class ClearDirFileInputTest(TempDirTestCase):
    """Test passing a file path to clear_dir."""
    def __init__(self, *args, **kwargs):
        """Calculate testing file path."""
        super().__init__(*args, **kwargs)
        self.test_file = os.path.join(self.temp_dir, 'testfile.txt')

    def setUp(self):
        """Create the testing file."""
        super().setUp()
        touch_file(self.test_file)
        assert os.path.exists(self.test_file)

    def test_file_input(self):
        """Check that ValueError is raised when the input is a file."""
        with self.assertRaises(ValueError):
            clear_dir(self.test_file)


# Or use `python -m unittest [path]`
if __name__ == '__main__':
    unittest.main()
