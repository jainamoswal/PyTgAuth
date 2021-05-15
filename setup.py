import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytgauth",
    version="0.0.2",
    author="Jainam Oswal",
    author_email="Jainamoswal@gmail.com",
    description="A Wrapper to verify Telegram auth data while Web login.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jainamoswal/pytgauth",
    license="GPLv3",
    project_urls={
                "Documentation": "https://github.com/jainamoswal/pytgauth",
                "Channel": "https://t.me/j_projects",
                "Source Code": "https://github.com/jainamoswal/pytgauth",
                "Support": "https://t.me/j_projects_chat",
            },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Framework :: Flask"
    ],
    python_requires='>=3.6',
)
