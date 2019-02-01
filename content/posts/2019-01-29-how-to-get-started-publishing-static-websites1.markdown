---
layout: "post"
title: "How to get started publishing static websites"
date: 2019-01-29 11:45
slug: Build Site
---
#### How to get started publishing static websites: Macintosh


For a quick overview, read
  - [Kazarinoff: How I built this site](`https://pythonforundergradengineers.com/how-i-built-this-site-1.html`)

Kazarinoff outlines the basic steps to set up the proper environment, using the command line interface in the Terminal application. First, he installs Anaconda. Then, he creates a virtual environment, which is just a listing of all the versions of software you are using, and populates it with the packages you need; when you start it, it puts you in a walled-off environment that doesn't affect anything else. Confusingly, he names it 'staticsite', which he also uses as the name of the directory where he puts the website. When you create it, give it any name, like `2019A`; then you will start work by activating it: (the $ is the command line prompt)

```
$ conda activate 2019A
```

Now that you're in the environment with all the correct software, move into your working directory where you keep your website.  Notice that now the virtual environment tells you that you are inside it...so you know you have a stable, unchanged environment with all the same packages or applications installed.
```
(2019A) $ cd ~     #this takes you to your home directory
(2019A) $ cd Documents/myblog #this drops you down into the Documents directory, and then into the myblog subdirectory
```


  -  If you're not familiar with those commands, or Unix and the command line, jump down to `Preparatory` -->. [Jump to Preparatory](#abcd)

  - read the suggested tutorials or guides to  setting up Anaconda and virtual environments, setting up Pelican, and setting up git environments:

    - _Chapter One: Orientation_ in Peter Kazarinoff's new book [Problem Solving in Python](https://www.amazon.com/dp/B07M7S6LTT/ref=sr_1_5?ie=UTF8&qid=1547223360&sr=8-5&keywords=kazarinoff)


  - note any puzzling statements. Reread tutorial.


Once you get the overall picture, you will first, set up directories, files and software to publish on your local machine; set up a way to save everything: git; then, you will export the site to run on an outside server, e.g, Github, for the world to see. For free.

- Goal: build an environment for writing, publishing and analyzing data based on Jupyter notebooks, Python code, and Internet access to world databases.  That is, complement the environment used for Data Science 8 and Data Science 100 at UC Berkeley.

Here are the first steps. Each step is expanded below:

1. Decide where all of this is going to go. Design a file structure that can be expanded to support any number of web sites. That is, set up a master directory to hold many separate sub-directories, each sub-directory holding a separate web site. Or, organize each of your projects into a separate directory, then put a subdirectory inside that project directory to hold the web site.  Choose where you put each separate web site repository so it's simple to remember. If many web sites share static directories holding images, or common PDF's, or common Jupyter notebooks, pick a location that is easy to remember and to link to from all the different website directories.

To begin, go to your home directory and create a new directory to hold your work.

```
(2019A) $ cd ~
(2019A) $ mkdir myblog
(2019A) $ cd myblog
```


To learn how to do this, jump to section 4 in the `Learn Enough Command Line to be Dangerous` tutorial, cited below. Later, it's easy to move your work to reorganize it, but start out in a new directory so you know where to find everything, and so your new work doesn't get mixed up with your other work.

2. Set up the publishing environment on your machine: editor, command-line interface, virtual environment, Git repository to track all changes, Pelican themes, plug-ins, local configuration files, and Python and Jupyter environments. A short list: Atom, iTerm, Anaconda, git (already on Mac), Pelican.

Set up Anaconda, as described in _Chapter One: Orientation_ in Peter Kazarinoff's new book [Problem Solving in Python](https://www.amazon.com/dp/B07M7S6LTT/ref=sr_1_5?ie=UTF8&qid=1547223360&sr=8-5&keywords=kazarinoff).

Downloading Anaconda will bring in the newest Python versions, and will let you easily create virtual environments; virtual environments should be started at the beginning of each work session (eg,

   ```
   $conda activate env1
   ```

   ), so all your work takes place in isolated, easily configured environments. There is a different way to do this, using `pip env`, but it's the same idea.
3. Experiment by building several iterations of a web site, to see what headings and side-bar structure you like.  The instructions for starting Pelican show how to run the program that sets up the relevant directories and configuration files.

By changing the settings in the main configuration file for Pelican, named `pelicanconf.py`, you can change what the web site looks like. It's simpler than it looks; by changing values of some variables, you decide what appears as headings and tabs for the web site, and what appears in the sidebars of the site.
4. Practice writing pages, saving them, backing them up in Git, using Pelican to convert them to HTML web pages, and serving them up on your local machine as if it's a published web site.

This cycle of daily work: invoking a virtual environment, starting with the current version of content, adding more content, making changes, saving the changes with Git, then exporting to the publishing site,  ensures you keep track of all changes. Later, this is the machinery we will use to move the web site out on the Internet, to be served by free, outside servers.
5. Prepare to export your local static web site to an external server, and manage updates and new entries.

Read the Git tutorial, and read the seven-part Kazarinoff document about how he set up his static web site for his Python book: [How I built this site](`https://pythonforundergradengineers.com/how-i-built-this-site-1.html`) to get a sense of how this work flow is organized.
1. A second Kazarinoff version of setting everything up: read `Chapter One: Orientation` in `Problem Solving With Python,` by Peter Kazarinoff:[Amazon preview of Chapter One](https://www.amazon.com/dp/B07M7S6LTT/ref=sr_1_5?ie=UTF8&qid=1547223360&sr=8-5&keywords=kazarinoff)  .


2. This describes setting up Anaconda and Python and why. The mysterious reference to "Package Management", and "Virtual Environment" will make sense later, but refer to the standard way to add new programs and tools to the environment you're working in (packages), and how to set up an environment with tools that work with each other, totally isolated from other environments.  It's good to set a virtual environment up at the beginning, so you know how to keep everything updated.




####  <a name="abcd">Preparatory</a> work, if many of these terms used above have little meaning to you.

Read the `Learn Enough to Be Dangerous` tutorials at `https://www.learnenough.com/`. They're long; the `Development Environment` is an overview; the other three cover the command line, the editor, and the way to keep track of changes using Git.


- First, quickly scan the overview of what a software developer needs as tools, which describes tools every software developer needs, and outlines basic general computer knowledge, referring to the other tutorials for details.

  - [Development Environment Tutorial](https://www.learnenough.com/dev-environment-tutorial#sec-native_os_setup)

  - Just read it. Don't follow its instructions to do anything yet; note that the references to Ruby will be replaced with references to Python and Jupyter notebooks, later, so skip them. Ruby is great, but we're going to use Python and Jupyter notebooks (which can run Ruby as well as Python).


- Then read the three tutorials that cover the basics:
    - [Command line:](https://www.learnenough.com/command-line-tutorial/basics) `https://www.learnenough.com/command-line-tutorial/basics`
    - [Editor:](https://www.learnenough.com/text-editor-tutorial/vim) `https://www.learnenough.com/text-editor-tutorial/vim`.
    - [Git, the basic machinery of keeping track of what you do:](https://www.learnenough.com/git-tutorial/getting_started)  `https://www.learnenough.com/git-tutorial/getting_started`


- After reading the three basic tutorials, Command Line, Text Editor, and Git, you can make sense of the step-by-step guides to make the static web site. You'll know about using a Google search for help when things make no sense, and what to do when you hit an error.
