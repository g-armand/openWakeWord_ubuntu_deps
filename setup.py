import platform
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openwakeword_ubuntu_deps",

    version="0.6.0",  # placeholder since Conan installs from git@main
    install_requires=[
        'onnxruntime>=1.10.0,<2',
        'ai-edge-litert>=2.0.2,<3',
        'speexdsp-ns>=0.1.2,<1',
        'tqdm>=4.0,<5.0',
        'scipy>=1.3,<2',
        'scikit-learn>=1,<2',
        'requests>=2.0,<3',
    ],
    extras_require={},
    author="g-armand",
    author_email="",
    description="Fork on openwakeword to get rid of huge list of unused dependencies for ubuntu",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dscripka/openWakeWord",
    project_urls={
        "Source": "https://github.com/g-armand/openWakeWord_ubuntu_deps",
        "OriginalRepo": "https://github.com/dscripka/openWakeWord",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires=">=3.0",
)
