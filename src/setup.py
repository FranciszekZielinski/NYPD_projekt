from setuptools import setup, find_packages

setup(
    name='projektNYPD',
    version='0.1',
    description='egzamin',
    author='Franciszek Zieliński',
    author_email='email@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'your_script_name=your_package_name.your_script_name:main'
        ]
    }
)
