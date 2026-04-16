import platform
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openwakeword_ubuntu_deps",

    version="0.0.1",  # until it works will iterate on 0.0.* then bump directly to 0.6.0
    install_requires=[
        # --- base dependencies ---
        "onnxruntime>=1.17.1,<2",
        "ai-edge-litert>=2.0.2,<3",
        "speexdsp-ns>=0.1.2,<1",
        "tqdm>=4.0,<5.0",
        "scipy>=1.3,<2",
        "scikit-learn>=1,<2",
        "requests>=2.0,<3",

        # --- ["full"] dependencies ---
        "mutagen>=1.47.0,<2",
        "torch>=2.4.0,<3",
        "torchaudio>=2.4.0,<3",
        "torchinfo>=1.8.0,<2",
        "torchmetrics>=0.11.4,<1",
        "speechbrain>=0.5.16,<1",
        "audiomentations>=0.38.0,<1",
        "torch-audiomentations>=0.11.1,<1",
        "acoustics>=0.2.6,<1",
        "protobuf>=4.25.3,<5",
        "onnx>=1.19.1,<2",
        "pronouncing>=0.2.0,<1",
        "deep-phonemizer>=0.0.19,<1"
        "torchcodec>=0.9.1,<1",
        "onnxscript>=0.5.7,<1",
        "datasets>=4.1.1,<5",
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
