# Build documentation with mkdocs

## Commands

Execute the following commands in powershell.

PS> mkdir mkdocs-documentation
PS> cd mkdocs-documentation
PS> python -m venv venv
PS> venv\Scripts\activate
(venv) PS> python -m pip install mkdocs
(venv) PS> python -m pip install "mkdocstrings[python]"
(venv) PS> python -m pip install mkdocs-material

mkdocs new .
mkdocs serve

For a full tutorial click [here].

## Cinder Theme

[cinder] is a theme we used to build our documentation.  

[cinder]: https://twardoch.github.io/clinker-mktheme/

[here]: https://realpython.com/python-project-documentation-with-mkdocs/
