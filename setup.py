import setuptools

setuptools.setup (
   include_package_data = True,
  name = 'mycalculator0001',
  version='1.0.0',
  description = 'oss-dev my calculator',
  author='TayJeong',
  author_email='2052862@donga.ac.kr',
  url = 'https://github.com/TayJeong/mycalculator/',
  download_url = "https://github.com/TayJeong/mycalculator/archive/refs/tags/v.1.0.0.zip",
  install_requires=['pytest'],
  long_description = 'oss-dev calculator python module',
  long_description_content_type = 'text/markdown',
  classifiers = [
      "Programming Language :: Python :: 3",
      "Operating System :: OS Independent",
  ],
)
