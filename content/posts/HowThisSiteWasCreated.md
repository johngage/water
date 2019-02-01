Title: How This Site Was Created
Date: 2018-11-12 17:00
Modified: 2018-12-29
Category: Tools
Tags: Guide
Author: John Gage
Summary: Site Design
Status: published
Series: Site-creation-series


#### This site was patterned on the site created by Peter Kazarinoff, Professor of Engineering at Portland Community College ##

- He describes the tools, the editors, and the templates needed for a static web site. His site is
- He has intriguing tools for conversion of Jupyter notebooks into LaTex.
- Using his list of Pelican plugins.
- Using a modification of his pelicanconf.py files.  Some problems with final rendering, and with publishconf.py

##### Mysteries of cloning github repositories of themes and plugins

Kazarinoff describes the sequence of git calls to bring all the themes and plugins into a directory, but seems to make an error.

```
$ git submodule add https://github.com/getpelican/pelican-themes.git
$ git submodule init
$ git submodule update --init --recursive
```




### November 13, 2018: CRITICAL:  ###

The author of Pelican, Alexis Metaireau, and the current maintainer of the pelican github site, Justin Meyer and 35 others, just released Pelican 4.0.

*My site could not build new html pages, and gave the error:*


```
ERROR: Cannot load plugin `i18n_subsites`
  | ImportError: cannot import name 'Draft'
/Users/johngage/Documents/blog/pelican-plugins/liquid_tags/notebook.py:70: UserWarning: Pelican plugin is not designed to work with IPython versions greater than 1.x. CSS styles have changed in later releases.
  warnings.warn("Pelican plugin is not designed to work with IPython "

 ** Writing styles to _nb_header.html: this should be included in the theme. **

CRITICAL: UndefinedError: 'gettext' is undefined

```
Hack to fix this: insert two lines in generators.py, a program in the pelican site-package, under python3.6; now, under python3.7

I added two lines to the basic Python for Pelican in  */Users/johngage/anaconda3/lib/python3.6/site-packages/pelican/generators.py*

On line 28, just after


```
from pelican.utils import (DateFormatter, copy, mkdir_p, order_content,
                           posixize_path, process_translations,
                           python_2_unicode_compatible)
```

add (on line 27)


```
import gettext
```



and in the same file, on line 78, just after



```
self.env = Environment(
        loader=ChoiceLoader([
            FileSystemLoader(self._templates_path),
            simple_loader,  # implicit inheritance
            PrefixLoader({
                '!simple': simple_loader,
                '!theme': theme_loader
            })  # explicit ones
        ]),
        **self.settings['JINJA_ENVIRONMENT']
    )
```

add:


```
#insert fix for gettext error,using Baky's Blog code Nov 2018
#self.env.install_gettext_translations( gettext )

```


This seemed to get rid of the *gettext undefined* error, and the site rendered.

Friday, Feb 1, 2019

#### Fix for gettext problem seem to be load new plugin versions.  Need to understand submodule way with git.

Worked when cloned all plugins in new directory.  Then could install i18n_sites; added Jinja2 environment.

To install plugin for pelican-ipynb:
```
git submodule add git://github.com/danielfrg/pelican-ipynb.git pelican-plugins/ipynb
```


Commands for virtual environments:

```
conda install -n myenv pip
source activate myenv
pip <pip_subcommand>
```

```
conda list  #lists all packages and versions
conda info --envs
```
```
conda list --explicit > spec-file.txt

```
```
conda create --name myenv --file spec-file.txt

```
```
conda create --name myenv

```
```
source activate myenv
```

```
source activate (base, b1, bsite, virtsite)
```

Using virtual environments with this modification--b1 and bsite--
big blog site renders, but still has error about loading i18n module.

Using these VE, setting up new Pelican instance:

```CRITICAL: AttributeError: 'Environment' object has no attribute 'install_gettext_translations'```
  - Error from prior inserted line in generators.py

New experiment: try changing pelicanconf.py, removing all refs to i18n.....

2016 github error entries refer to jinja, and gettext, and plugins.  Others get exactly the same errors: cannot load plugin i18n; get gettext error;

reloaded all plugins, turned on i18n, jinja2;
- First Critical: CRITICAL: AttributeError: module 'multi_neighbors' has no attribute 'register'
  - comment out multi-neighbor plugin

Run again:
  - many errors, but **it ran**
    - no complaint about i18n_sites not loading;
    - no 'gettext' error
    -
  - ERROR: Cannot load plugin `pelican-ipynb.markup`
  | ModuleNotFoundError: No module named 'pelican-ipynb.markup'
  ```
  ERROR: Could not process posts/2019-01-18-jnb-tests.markdown
  | TypeError: store() got an unexpected keyword argument 'safe'
ERROR: Could not process posts/2019-01-23-table-of-classes.markdown
  | TypeError: store() got an unexpected keyword argument 'safe'
ERROR: Could not process posts/2019-01-21-berkeley-classes-spring-2019-data-science-and-the-real-world.markdown
  | TypeError: store() got an unexpected keyword argument 'safe'
ERROR: Could not process posts/Battery.md
  | TypeError: store() got an unexpected keyword argument 'safe'
ERROR: Could not process posts/UCB DS8.1x.md
  | TypeError: store() got an unexpected keyword argument 'safe'
  ```

  Have seen this 'safe' error before.  Use `shift-command-f' in Atom to find all instances of `safe=True`.
    - found in liquid tags plugin; removed `safe=True` from notebook.py, `_*fixed it *_`; now all the notebooks are processed by Pelican.
