# Foobar

VideoSubs is a Python CLI tool for dealing with extracting comments into a text
using thidr party libs

## Installation


Install the package manager [miniconda](https://docs.anaconda.com/free/miniconda/)
Create and activte the new virtual environment
    conda create --name videosubs
    conda activate videosubs 

Add channels:
    conda config --add channels conda-forge
    conda config --add channels microsoft

conda install -c conda-forge playwright

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PyVimeo.
    pip install PyVimeo

```bash
pip install VideoSubs
```
pip freeze > requirements.txt
conda list -e > requirements.txt
conda install --file requirements.txt
#List all packages and versions installed in the current active environment:

conda list

#Search for a package:

conda search PACKAGENAME
## Usage

```python
import videosubs

:TODO describe functions 

# returns 'words'
videosubs.pluralize('word')

# returns 'geese'
videosubs.pluralize('goose')

# returns 'phenomenon'
videosubs.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
:TODO make tests

## License
:TODO learn licence