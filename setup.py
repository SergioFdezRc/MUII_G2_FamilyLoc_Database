from setuptools import setup

with open("requirements.txt") as f:
    install_requires = f.read().split("\n")

setup(
    name='FamilyLock_Database',
    version='1.0',
    url='https://github.com/SergioFdezRc/MUII_G2_FamilyLock_Database',
    license='Creative Commons',
    author='Sergio Fernández Rincón',
    author_email='s.fernandez.rincon@gmail.com',
    description='Proyecto con una base de datos común para todas las APIs del proyecto.',
    packages=[
        'muii_g2_family_lock_database',
        'muii_g2_family_lock_database/queries',
        'muii_g2_family_lock_database/constants',
    ],
    install_requires=install_requires
)
