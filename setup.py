from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='chanloader',
    packages=find_packages(),
    version='0.1.5',
    description='Download pictures/ webms / gifs from 4chan.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/IronicUsername/chanloader',
    keywords=['4chan', 'utilities', 'download', 'lol'],
    install_requires=[
        'requests',
        'tqdm',
        'click',
        'urllib3',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: End Users/Desktop',
        "Natural Language :: English",
        'Topic :: Utilities',
        'Topic :: Internet',
        'Topic :: Multimedia :: Graphics',

        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        "Programming Language :: Python",
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',

    ],
    python_requires='>=3.5',
    entry_points={'console_scripts': ['chanloader=chanloader.__main__:main']},
)
