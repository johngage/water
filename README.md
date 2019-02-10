## water
Modified: 2019.Feb.10
Pushed from water
Three branches: master, develop, gh-pages

This is a learning site, reflecting steps I've taken to combine Jupyter notebooks, sensor data streams from the Kibera Town Centre (a 80-cubic-meter-per-day water project in Kibera, Nairobi, Kenya), and data science analysis at UC Berkeley.

I've drawn from Peter Kazarinoff, professor of engineering in Portland, Oregon, as he built a static web site for his new Python textbook.  He wrote the textbook completely in Jupyter notebooks, and posted a seven-part series detailing how he built the web site using Pelican, a Pelican theme, and a collection of Pelican plug-ins to modify the appearance and functionality of the resultant web site.  The site has survived several updates in Python, a major upgrade of Pelican to 4.02, and multiple updates of numerous plugins, with only a few conflicts and mysterious errors.  Want to clarify the procedure for updating submodules....does it happen on a pull? or do I need to go to each directory where I cloned a repository, and update?

https://github.com/johngage

Building website from scratch, utilizing .py files from 2 sources

* Portland Python textbook project
- https://pythonforundergradengineers.com/how-i-built-this-site-1.html
* pelican tutorial

Using this site to explore exactly which parameters cause specific behavior of Pelican.

E.g.,
- what shows up on menu? Controlled by pelicanconf.py entries
- what makes sidebar appear and disappear?
- What enables pointers to similar articles?
- What enables <next page> widgets?
- how to insert a [previous] [next] button.

15Oct: was on develop branch, so could not see webpage; merged develop into master, but now can only see this .md file.

- how to see the pelican-themed website?
### - 2019.Jan.16 : remaining issues
1. updating publishconf.py...get format error, possibly due to upgrade to pelican 4; need to update submodules, which may be accomplished by reloading from github.
2.


- Make github repository
- link the local directory to the remote github repository
- The local version of the site is in a folder: "blog" in the Documents folder. The blog folder will contain all the files used to build the site and the output files created by Pelican that are the site. The blog folder can be created using a terminal, or the Anaconda Prompt.
-The command git init creates the local repository. The command git remote add origin followed by the url of our GitHub repo links local folder on our computer to the remote repo on GitHub.com. Note the web address ends in .git
- Adding two submodules allows the most up-to-date versions to be called.
- $ pwd

``` $ git submodule add https://github.com/getpelican/pelican-themes.git
$ git submodule init
$ git submodule update --init --recursive ```

``` 
$ pwd

$ git submodule add https://github.com/getpelican/pelican-plugins.git
$ git submodule init
$ git submodule update --init --recursive . 

(staticsite) $ ghp-import output
(staticsite) $ git push origin gh-pages
```

