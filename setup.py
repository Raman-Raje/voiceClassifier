from setuptools import setup

with open("README.md", 'r') as f:
  long_description = f.read()


setup(
  name = 'voiceClassifier',
  packages = ['voiceClassifier'],
  version = '1.1',
  license='MIT',        # https://help.github.com/articles/licensing-a-repository
  description = long_description,   # Give a short description about your library
  author = 'Raman Shinde',
  author_email = 'raman.shinde15@gmail.com',
  url = 'https://github.com/Raman-Raje/voiceClassifier',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Raman-Raje/voiceClassifier/archive/v_01.tar.gz',
  
  install_requires=[
          'astroid==2.3.3',
          'audioread==2.1.8',
          'cffi==1.14.0',
          'decorator==4.4.1',
          'isort==4.3.21',
          'joblib==0.14.1',
          'lazy-object-proxy==1.4.3',
          'librosa==0.7.2',
          'llvmlite==0.31.0',
          'mccabe==0.6.1',
          'numba==0.48.0',
          'numpy==1.18.1',
          'pandas==1.0.1',
          'pycparser==2.19',
          'pylint==2.4.4',
          'python-dateutil==2.8.1',
          'pytz==2019.3',
          'resampy==0.2.2',
          'scikit-learn==0.22.1',
          'scipy==1.4.1',
          'six==1.14.0',
          'SoundFile==0.10.3.post1',
          'typed-ast==1.4.1',
          'wrapt==1.11.2',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)