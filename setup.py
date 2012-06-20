from setuptools import setup, find_packages
 
setup(
    name='phantomjs-printer',
    version='0.1',
    description='A Django pdf generator using PhantomJS.',
    long_description=open('docs/index.txt').read(),
    author='Carlo Smouter',
    author_email='lockwooddev@gmail.com',
    url='',
    packages=find_packages(exclude=['',]),
    package_data = {},
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
