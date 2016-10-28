from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='chinesepostman',
    version='0.0.1',
    description='Chinese-Postman network solver',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    url='https://github.com/supermitch/Chinese-Postman',
    author='Mitch LeBlanc',
    author_email='supermitch@gmail.com',
    packages=['chinesepostman'],
    license='MIT',
)
