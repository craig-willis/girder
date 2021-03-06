import os
from .fixtures import *  # noqa


def pytest_configure(config):
    """
    Create the necessary directories for coverage. This is necessary because neither coverage nor
    pytest-cov have support for making the data_file directory before running.
    """
    covPlugin = config.pluginmanager.get_plugin('_cov')

    if covPlugin is not None:
        covPluginConfig = covPlugin.cov_controller.cov.config
        covDataFileDir = os.path.dirname(covPluginConfig.data_file)

        try:
            os.makedirs(covDataFileDir)
        except OSError:
            pass


def pytest_addoption(parser):
    group = parser.getgroup('girder')
    group.addoption('--mock-db', action='store_true', default=False,
                    help='Whether or not to mock the database using mongomock.')
    group.addoption('--mongo-uri', action='store', default='mongodb://localhost:27017',
                    help=('The base URI to the MongoDB instance to use for database connections, '
                          'default is mongodb://localhost:27017'))
    group.addoption('--keep-db', action='store_true', default=False,
                    help='Whether to destroy testing databases after running tests.')
