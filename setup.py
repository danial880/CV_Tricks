import pip
import logging
import pkg_resources
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def _parse_requirements(file_path):
    pip_ver = pkg_resources.get_distribution('pip').version
    pip_version = list(map(int, pip_ver.split('.')[:2]))
    if pip_version >= [6, 0]:
        raw = pip.req.parse_requirements(file_path,
                                         session='hack')
    else:
        raw = pip.req.parse_requirements(file_path)
    return [str(i.req) for i in raw]

try:
    install_reqs = _parse_requirements("requirements.txt")
    print("install_reqs",install_reqs)
except Exception:
    logging.warning('Fail load requirements file, so using default ones.')
    install_reqs = ['opencv_contrib_python', 'tqdm', 'setuptools']

setup(
    name='CV_Tricks',
    version='0.0.3',
    url='https://github.com/danial880/CV_Tricks',
    author='Danial',
    author_email='danialkhan1594@gmail.com',
    license='MIT',
    description='Tricks for Computer Vision Developers',
    readme="README.md",
    packages=["CV_Tricks"],
    scripts=["CV_Tricks/img_frm_vid.py"],
    install_requires=install_reqs,
    include_package_data=True,
    python_requires='>=3.7',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering",
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords="ComputerVision",
)
