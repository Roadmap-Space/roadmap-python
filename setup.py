from distutils.core import setup

setup(
    name="roadmap-py",
    version="1.0.0",
    description="Python bindings for the Roadmap API",
    author="Roadmap",
    author_email="support@roadmap.space",
    url="https://github.com/roadmap-space/roadmap-python",
    license="MIT",
    keywords="roadmap api product",
    packages=["roadmap"],
    zip_safe=False,
    install_requires=[
        'requests >= 2.20; python_version >= "3.0"',
        'requests[security] >= 2.20; python_version < "3.0"',
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    project_urls={
        "Bug Tracker": "https://github.com/roadmap-space/roadmap-python/issues",
        "Documentation": "https://api.roadmap.space/?python",
        "Source Code": "https://github.com/roadmap-space/roadmap-python",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)