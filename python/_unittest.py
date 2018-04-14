#!/usr/bin/env python
"""
_unittest.py - Recipes using unittest
"""
import os
import shutil
from pathlib import Path
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
        self.temp_dir = Path('/tmp')
        if not self.temp_dir.exists():
            self.temp_dir = Path('unittest_temp_dir')

    def setUp(self):
        """Create temporary directory.

        Throw an error if the testing directory existed before.
        """
        self.temp_dir.mkdir()

    def tearDown(self):
        """Clear temporary directory."""
        shutil.rmtree(self.temp_dir)
        assert not os.path.exists(self.temp_dir)


class ClearDirTest(TempDirTestCase):
    """Test case for clear_dir function."""
    # Test paths should be relative to a root temp_dir.
    TEST_SUBDIRS = [Path('sub'), Path('sub', 'dir'), Path('sub', 'sub')]
    TEST_FILES = [Path('A.txt'), Path('B.txt'), Path('sub', 'C.txt'),
                  Path('sub', 'sub', 'D.txt')]

    def __init__(self, *args, **kwargs):
        """Calculate full paths of testing files."""
        super().__init__(*args, **kwargs)
        self.test_file_paths = [self.temp_dir.joinpath(rel_path)
                                for rel_path in self.TEST_FILES]


    def setUp(self):
        """Create testing files."""
        super().setUp()
        for subdir in self.TEST_SUBDIRS:
            subdir.mkdir(exist_ok=True)
            assert subdir.is_dir()
        for path in self.test_file_paths:
            path.parent.mkdir(exist_ok=True)
            path.touch()
            assert path.is_file()

    def test_clear_dir(self):
        """Test that clear_dir removes all files but no subdirectories."""
        clear_dir(self.temp_dir)
        for path in self.test_file_paths:
            self.assertFalse(path.exists())
        for subdir in self.TEST_SUBDIRS:
            self.assertTrue(subdir.exists())


class ClearDirMissingInputTest(unittest.TestCase):
    """Test nonexistent input to clear_dir."""
    def test_nonexistant_input(self):
        """Test that FileNotFoundError is thrown for nonexistant input."""
        with self.assertRaises(FileNotFoundError):
            clear_dir('nonexistant_path')


class ClearDirFileInputTest(TempDirTestCase):
    """Test passing a file path to clear_dir."""
    def __init__(self, *args, **kwargs):
        """Calculate testing file path."""
        super().__init__(*args, **kwargs)
        self.test_file = self.temp_dir.joinpath('testfile.txt')

    def setUp(self):
        """Create the testing file."""
        super().setUp()
        self.test_file.touch()
        assert self.test_file.is_file()

    def test_file_input(self):
        """Check that ValueError is raised when the input is a file."""
        with self.assertRaises(ValueError):
            clear_dir(self.test_file)


class MockClearDirTest(ClearDirTest):
    """Mock out os.remove in clear_dir."""
    def __init__(self, *args, **kwargs):
        """Store a path to a temporary file in the temp_dir."""
        super().__init__(*args, **kwargs)
        self.manifest_file = self.temp_dir.joinpath('removed_files')

    def test_clear_dir(self):
        def track_file(path):
            """Append the input path to the manifest file."""
            with self.manifest_file.open('a') as manifest:
                print(path, file=manifest)

        with unittest.mock.patch('os.remove', track_file):
            clear_dir(self.temp_dir)

        cleared_files = self.manifest_file.read_text().split('\n')

        for path in self.test_file_paths:
            self.assertIn(str(path), cleared_files)


# Or use `python -m unittest [path]`
if __name__ == '__main__':
    unittest.main()
