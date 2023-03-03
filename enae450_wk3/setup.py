from setuptools import setup

package_name = 'enae450_wk3'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jpham',
    maintainer_email='james20902@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "pub = enae450_wk3.publisher:main",
            "sub = enae450_wk3.subscriber:main",
            "reset = enae450_wk3.reset:main",
            "fib = enae450_wk3.fibonacci:main"
        ],
    },
)
