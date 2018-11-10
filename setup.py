from setuptools import setup

with open('README.md') as README:
    long_description = README.read()
setup(
    name='pycrypt_dev',
    version='0.1.dev1',
    packages=['py', ],
    license='MIT',
    description='A Python packege for Cryptographic algorithms',
    long_description=long_description,
    author='Ayan Bag',
    author_email='ayanbag9474@gmail.com',
    install_requires=[
        'pyperclip',
    ],
    python_requires='>=3.4',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points=dict(console_scripts=[
        'pycrypt =py.pycrypt:main', ]),
    url='https://github.com/ayanbag/pycrypt',

)