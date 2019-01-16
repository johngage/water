# water
Modified: 2019.Jan.16
Pushed from water
Three branches: master, develop, gh-pages

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

``$ git submodule add https://github.com/getpelican/pelican-themes.git
$ git submodule init
$ git submodule update --init --recursive ``

``$ pwd

$ git submodule add https://github.com/getpelican/pelican-plugins.git
$ git submodule init
$ git submodule update --init --recursive``
