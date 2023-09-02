# Build documentation with mkdocs

## Commands

Execute the following commands in powershell.

``` ps
cd docs
python -m venv venv
venv\Scripts\activate
python -m pip install mkdocs
python -m pip install "mkdocstrings[python]"
python -m pip install mkdocs-material

mkdocs new .
mkdocs serve
```

For a full tutorial see [python-project-documentation-with-mkdocs].

### Publish mkdocs to github pages

Execute this command locally on your branch you want to publish: `mkdocs gh-deploy`.

Full documentation here [Deploy mkdocs to GitHub Pages].

## Cinder Theme

[cinder] is a theme we used to build our documentation.  

[cinder]: https://twardoch.github.io/clinker-mktheme/
[python-project-documentation-with-mkdocs]: https://realpython.com/python-project-documentation-with-mkdocs/
[Deploy mkdocs to GitHub Pages]: https://www.mkdocs.org/user-guide/deploying-your-docs/
