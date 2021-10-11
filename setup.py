from setuptools import setup,find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
  name="RIG-lolmantis",
  version="0.0.2",
  author="Lolmantis",
  author_email="support@yarndev.xyz",
  description="Random Inspiration Generator.",
  long_description_content_type="text/markdown",
  long_description=long_description,
  packages=find_packages(),
  url="https://github.com/lolmantis/RIG",

  project_urls={
        "Bug Tracker": "https://github.com/lolmantis/RIG/issues",
  },
  keywords=[
    'python',
    'Inspiration',
    'Random',
  ],
  classifiers=[
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
    "Operating System :: Unix",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft :: Windows",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English"
  ]
)