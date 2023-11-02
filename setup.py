from setuptools import setup
setup(
    name='yummarize',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'yummarize=yummarize:main'
        ]
    }
)