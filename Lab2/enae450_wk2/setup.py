from setuptools import setup

package_name = 'enae450_wk2'

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
    maintainer_email='jpham@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	"dummy = enae450_wk2.enae450_wk2_node:main",
        	"number_publisher = enae450_wk2.pubbernode:main",
        	"number_counter = enae450_wk2.subbernode:main"
        ],
    },
)
