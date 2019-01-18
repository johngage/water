Title: How This Site Was Created
Date: 2018-11-12 17:00
Modified: 2018-12-29
Category: Tools
Tags: Guide
Author: John Gage
Summary: Site Design
Status: published
Series: Site-creation-series


## This site was patterned on the site created by Peter Kazarinoff, Professor of Engineering at Portland Community College ##

- He describes the tools, the editors, and the templates needed for a static web site. His site is
- He has intriguing tools for conversion of Jupyter notebooks into LaTex.
- Using his list of Pelican plugins.
- Using a modification of his pelicanconf.py files.  Some problems with final rendering, and with publishconf.py
-


### November 13, 2018 ###

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
self.env.install_gettext_translations( gettext )

```


This seemed to get rid of the *gettext undefined* error, and the site rendered.
