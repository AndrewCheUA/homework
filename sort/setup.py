from setuptools import setup

setup(name='sort',
      version='1.0',
      description='Folder sort by files types',
      author='Andrii Cheban',
      author_email='andreicheban@gmail.com',
      url='https://github.com/AndrewCheUA/homework/blob/4f60adf764bf433c87f254faccae8e5e5b485d8f/sort.py',
      packages=['sort'],
      entry_points={'console_scripts': ['clean-folder = sort.sort:main']}
     )
