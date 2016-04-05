from setuptools import setup, Extension, find_packages

setup(name='gitgud',
      version='1.1',
      author='Filip Sufitchi',
      author_email="fsufitchi@gmail.com",
      description="Git Gud - a utility for when you are told to 'get good'",
      url="https://github.com/fsufitch/git-gud",
      package_dir={'':'src'},
      packages=['gitgud'],
      entry_points = {
          "console_scripts": [
              "git-gud=gitgud.gitgud:git.gud",
              "git-job=gitgud.gitgud:git.job",
              "git-rekt=gitgud.gitgud:git.rekt",
              "git-spooked=gitgud.gitgud:git.spooked",
              "git-money=gitgud.gitgud:git.money",
              ],
        },

      install_requires=['argparse', 'pyfiglet'],
      )
