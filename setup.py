from distutils.core import setup

setup(
    name='signal-separation',
    packages=['signal-separation'],
    version='0.0.1',
    license='MIT',
    description='Algorithm for generating and separating analytical chemistry signal.',
    author='Mieszko Pasierbek',
    author_email='mieszko.pasierbek@gmail.com',
    url='https://github.com/MieszkoP',
    download_url='https://github.com/MieszkoP/signal-separation/archive/refs/tags/0.0.1.tar.gz',
    keywords=['CNN', 'Deep Learning', 'signal', 'SVR', 'chemometrics', 'chemistry'],
    install_requires=[
        'numpy',
        'matplotlib.pyplot',
        'scipy.stats',
        'tensorflow'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)