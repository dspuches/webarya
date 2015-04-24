from distutils.core import setup
setup(
  name = 'webarya',
  packages = ['webarya'],
  version = '0.0.3',
  install_requires = [
      'arya',
      'argparse',
      'flask',
      'wtforms',
       ],
  description = 'Flask front-end for Arya',
  author = 'Kevin Corbin',
  author_email = 'kecorbin@cisco.com',
  url = 'https://github.com/kecorbin/webarya', # use the URL to the github repo
  download_url = 'https://github.com/kecorbin/webarya/tarball/0.1', # I'll explain this in a second
  keywords = ['arya', 'apic', 'aci', 'cisco'],
  classifiers = [],
  entry_points={
        "console_scripts": [
            "webarya=webarya.webarya:main",
        ],
        }
)
