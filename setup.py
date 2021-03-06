from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='piptree',
    version='0.1.3a',
    description='List your ',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
    ],
    keywords='pip requirements tree',
    url='http://github.com/mightym/piptree',
    author='Mark Wirblich',
    author_email='mark@wirblich.com',
    license='MIT',
    py_modules=['piptree'],
    install_requires=[
        'pip',
    ],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['piptree = piptree:main'],
    }
    )
