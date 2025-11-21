
#this file will make setup.py after using github colin-i test/pyp/pypre
# python3 setup.py install --user will install egg, pip install --user . will install plain files

pkname='actionswf'

from setuptools import setup
setup(name=pkname,
	version=ver,
	packages=[pkname],
	#opt
	python_requires='>=3',
	#install_requires=["appdirs>=1","b"],
	#extras_require={'bin': ['a>=1'],},
	description='ActionSwf bindings',
	long_description=README,
	long_description_content_type="text/markdown",
	url='https://github.com/colin-i/actionswf',
	author='cb',
	author_email='costin.botescu@gmail.com',
	license='MIT'
)
