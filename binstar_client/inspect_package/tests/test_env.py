from os import path
import unittest
from ..env import EnvInspector, inspect_env_package


def data_path(filename):
    return path.join(path.dirname(__file__), 'data', filename)


class EnvInspectorTestCase(unittest.TestCase):
    def test_package_name(self):
        with open(data_path('environment.yml')) as fileobj:
            assert EnvInspector('environment.yml', fileobj).name == 'stats'

    def test_version(self):
        with open(data_path('environment.yml')) as fileobj:
            self.assertIsInstance(EnvInspector('environment.yml', fileobj).version, str)


class InspectEnvironmentPackageTest(unittest.TestCase):
    def test_inspect_env_package(self):
        with open(data_path('environment.yml')) as fileobj:
            package_data, release_data, file_data = inspect_env_package(
                'environment.yml', fileobj)

        self.assertEqual({
            'name': 'stats',
            'summary': 'Environment file'
        }, package_data)

        self.assertEqual({
            'basename': 'environment.yml',
            'attrs': {}
        }, file_data)


if __name__ == '__main__':
    unittest.main()
