from setuptools import setup,find_packages


setup(
    name="auto_chromedriver",
    version="0.1.4",
    packages=find_packages(),
    install_requires=["requests","bs4",],
    url="https://github.com/AzizKpln/auto_chromedriver",
    license="GPL-3.0",
    author="Aziz Kaplan",
    author_email="AzizKpln@protonmail.com",
    keywords=["chromedriver","auto_chromedriver","selenium_chromedriver","chromedriverinstall","chromedriver_install"],
    description="""
        Auto chromedriver installer. Most of selenium projects does not start  because of the chromedriver version issue.
		with 2 codes you can fix that error without making any efforts.
                
		For the usage and more information check out the README.""",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
)
