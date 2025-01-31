import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 8):
    raise Exception("Python 3.8 or higher is required. Your version is %s." % sys.version)

__version__ = ""
exec(open('efb_qq_plugin_mirai/__version__.py').read())

long_description = open('README.rst').read()

setup(
    name='efb-qq-plugin-mirai',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    version=__version__,
    description='EQS plugin for mirai.',
    long_description=long_description,
    include_package_data=True,
    author='Milkice',
    author_email='milkice@milkice.me',
    url='https://github.com/milkice233/efb-qq-plugin-mirai',
    license='GPLv3',
    python_requires='>=3.6',
    keywords=['ehforwarderbot', 'EH Forwarder Bot', 'EH Forwarder Bot Slave Channel',
              'qq', 'chatbot', 'EQS', 'mirai'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Communications :: Chat",
        "Topic :: Utilities"
    ],
    install_requires=[
        "efb-qq-slave",
        "websocket_client",
        "ehforwarderbot",
        "python-magic",
        "requests",
        "python-mirai-core==0.9.0",
        "cachetools"
    ],
    entry_points={
        'ehforwarderbot.qq.plugin': 'mirai = efb_qq_plugin_mirai:mirai'
    }
)
