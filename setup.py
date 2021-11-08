from distutils.core import setup

setup(
    name='TestLibrary',  # How you named your package folder (MyLib)
    packages=['TestLibrary'],  # Chose the same as "name"
    version='0.1',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Just a test module',  # Give a short description about your library
    author='Md. Masudur Rahman',  # Type in your name
    author_email='masudurhimel@gmail.com',  # Type in your E-Mail
    url='https://masudurhimel.github.io/',  # Provide either the link to your github or to your website
    download_url='https://github.com/masudurHimel/TestLibrary/archive/refs/tags/v_01.tar.gz',  # I explain this later on
    keywords=['test'],  # Keywords that define your package best
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
    ],
)
