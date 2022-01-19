
[![Binder](http://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/munkm/npre247/22-spring)


[![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/80x15.png)](http://creativecommons.org/licenses/by/4.0/)

# NPRE 247: Modeling Nuclear Reactor Systems

This is the repository that holds ipython notebooks, python scripts, a 
syllabus, and other materials for Madicken Munk's NPRE247 course at UofI. 


## Syllabus

The syllabus will be kept up to date in this repository. It is subject to 
change, so please keep checking it.

## Running the Notebooks Online

The easiest way to run the notebooks is to let mybinder.org do it for you. Just 
go to 
[mybinder.org:/repo/munkm/npre247](http://mybinder.org:/repo/munkm/npre247). 

If you have trouble, it may be due to the mybinder servers being overloaded. 
This is a fairly common occurance, because their servers are funded entirely by 
the research budget of [Dr. Jeremy Freeman.](http://thefreemanlab.com/).
You can find out the status of mybinder [on their status 
page](http://mybinder.org/status).

## Running the Notebooks Locally

To run them on your own computer, where you can save changes, you will need to
install python and install git.

### Installing Python
 
Download and install the scientific python distribution called
[anaconda](https://www.continuum.io/downloads). You will need python version
3.5 or greater. 

### Installing Git (optional)

I recommend gaining access to the course notebooks via the version control
program, `git`. Instructions for installing git on different platforms can be
found [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

### Acquiring the notebooks

**If you have installed git,** open a terminal program (or the Git Bash For Windows
program if you are on windows and execute the command:

```
git clone https://github.com/munkm/npre247.git
```

**If you have not installed git,** you can download the notebooks as a zip file
from [here](https://github.com/munkm/npre247/archive/master.zip). Then,
unzip the directory. 


### Running the notebooks 


You should now have a directory somewhere on your computer called npre247. Open
a terminal (or the git bash for windows program) and type the following command inside that directory:

```
jupyter notebook
```

Alternatively, you can choose to use a Jupyter Lab instance

```
jupyter lab
```

Your browser should open to a localhost:8888 url. Navigate to the notebooks to
run, edit, and save them.

If you are on Windows and didn't install the Git Bash for Windows program,
follow these instructions [to run the
notebooks](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html).


## Updating the notebooks

Periodically, I will make changes to the notebooks and add new ones throughout
the semester. If you have not installed git, you will need to re-download the
zip file. If you *have* installed git, navigate to your npre247 directory and
type the following:

```
git pull origin 22-spring
```

**Note that most conventions you will see in git instructions will use `master` 
rather than `22-spring` like I have here.**

You may run into errors at this point if you have made edits and not committed
your changes.  Or, indeed, if you have made changes to the same lines to which
I have made changes, you may have a conflict. In either case, try to follow the
instructions that `git` gives you. Usually, it will tell you exactly what to
do.  If that's not enough, [here](http://swcarpentry.github.io/git-novice/) is
a great tutorial on using git effectively.


## Attribution of re-used materials

Much of this content is a reflection of the course materials originally
developed by Prof. Kathryn Huff (@katyhuff) at the University of Illinois at Urbana
Champaign. Specifically the lecture notes and the syllabus are heavily
influenced by this content. You can find it at:
https://github.com/katyhuff/npre247 . It, like this version of the course, is
CC-BY-4.0 licensed.  

Two notebooks in the `finite_diff` direcory, regarding finite 
differences, are borrowed directly from David Kechison (@ketch) who is the 
author of the repository: https://github.com/ketch/finite-difference-course. 
These are CC-BY Licensed.  You can learn more about his numerical methods 
courses from his scipy paper on the topic:

```latex
@article{ketcheson2014teaching,
  title={Teaching numerical methods with IPython notebooks and inquiry-based learning},
  author={Ketcheson, David I},
  year={2014},
  publisher={SciPy. org}
}
```

Also, one notebook regarding timestepping, by Brian E.J. Rose, is used in the 
`finite_diff` directory. That notebook falls under the MIT license included in 
the notebook itself.

