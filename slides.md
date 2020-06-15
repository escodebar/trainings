---
theme: league
title: Git workshop
revealOptions:
    transition: 'fade'
---

## Learning Git
# the hard way

Notes:
* Most of the things we discuss here are not only achievable with Git, but can be made with other VCS as well
* I am a total Git-Fanboy, whatever I say during this workshop is totally opinionated
* I want to make this a fun experience for all of us!

---

## Who am I

---

## Schedule

* The Good, the Bad and the Ugly
* Gitception: Reaching into the substructure
* Of trees, branches and pieces of fruit
* Gitbreak: Try to keep the holistic view
* Workfellas: Five ways to contribute to the code base

Notes:

There are going to be excercises after or during each block!

* The Good, the Bad and the Ugly
  - discusses the strengths, weaknesses, opportunities and threads of using Git
  - This discussion should lead to determining how you want to use Git and how you can get there
* Gitception
  - is about using Git to understand Git and understanding the structure of Git
  - The concept of Gitception is used throughtout the training
  - Knowing Git as a tool removes the constraints for the applied methods
* Of trees, branches and pieces of fruit
  - Git's branching mechanism
  - combining changes implemented in seperate branches into one branch
* Gitbreak
  - Introduction into distributed Git
  - Working with remotes
* Workfellas
  - Introduction to possible workflows with Git

---

## Requirements

If you know how to type commands in a terminal and parse its output, this training is made for you!

Notes:
* Reading is crucial here, by the end of the training you'll be using the *man*-pages a lot!
* No specific Git editor integration is discussed, since none of them covers all of Git's features (and none of them does it in the same way)
* For the same reason, no Git GUI is discussed
* I recommend using the terminal all of the time and start using other tools, if they make you more efficient than when using the console (there are many situations in which other tools are more efficient)
* In many occasions you'll find yourself connected to a server with a Git repository doing analysis, knowing the commands in that situation is crucial

---

## The Tangled Working Copy Problem

---

## Version Control Systems

What is a VCS and why do I need it?

* Version Control
* Collaboration
* Run automated tasks
* Error analysis

---

## Some VCS

ArX, Bazaar, BitKeeper, Codeville, CVS, Darcs, DCVS, Fossil, Git, GNU arch, Mercurial, Monotone, Perforce, Subversion, TFVCS, Veracity, ...

---

# Git

---

![The Good](https://upload.wikimedia.org/wikipedia/it/5/50/Il_biondo.png)<!-- .element: height="500px" -->

---

## Git

"... is oddly liberal with how and when you use it."

* is a powerful analysis tool
* allows running automated tasks
* allows many collaboration workflows
* allows patch management

Notes:
* Git does not force you to suit certain workflows, it doesn't get in your way
* This liberty requires understanding Git
* This liberty also allows to evolve your development workflow

---

![The Ugly](https://upload.wikimedia.org/wikipedia/it/e/e7/Il_brutto.png)<!-- .element: height="500px" -->

---

## Git

... is utterly complex

* has crazy command line syntax
* has a leaky abstraction
* requires many different concepts
* requires a holistic picture

Notes:
* no distinction between implementation detail and user interface
* beginners are confronted with internal details

---

![The Bad](https://upload.wikimedia.org/wikipedia/it/6/68/Il_cattivo.png)<!-- .element: height="500px" -->

---

## Git

... is really hard to learn

* has a complex information model
* comes with complex workflows
* has crappy documentation

Notes:
* Git has a very steep learning curve

---

...but once you're there

---

# Git

##  will make you

# a better

# programmer

Notes:
* But only if you're willing to change!
* Improvement always comes with change!

---

## Exercises

* How long have been programming?
* What kind of software do you work on?
* What kind of tasks do you solve?
* What challenges you the most when writing software?
* Have you been using other version control systems?
* How long have been using Git?
* What challenges you the most when using Git?

---

# Discussion

Notes:
* Context - Cynefin
* Primary vs. secondary needs
* Handling complexity
* Values > Principles > Methods > Tools & Activities

---

## Slides

[https://escodebar.github.io/trainings/git/](https://escodebar.github.io/trainings/git/)

Notes:
* You can find the speaker notes in the slides, which allows you to go through the training at home
* Pass the slides to your coworkers, your friends, etc., the more people understand Git the better
* If a slide needs clarification, please let me know!

---

## Setup

[Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and tell it who you are
```shell
$ {{ 'git config --global user.name "Pablo Escodebar"'|run }}
$ {{ 'git config --global user.email "escodebar@gmail.com"'|run }}
```

Then configure the editor you want to use
```shell
$ git config --global core.editor 'vim'
$ git config --global core.editor 'subl -n -w'
$ git config --global core.editor 'atom --wait'
$ git config --global core.editor 'code --wait'
```

Notes:
* Whenever you do something in Git, your user will be used to track your actions
* There are three levels of configuration:
  - The repository configuration
  - Your user configuration (using `--global`)
  - The system configuration (using `--system`)
* You can also configure the editor, the default editor is `vim`

---

## Setup

Create a repository:

```shell
$ mkdir -p ~/working/directory/ && cd $_ && {{ "git init ."|run }}
```

```shell
$ {{ "ls -blah"|run }}
```

See that `.git` folder there? That's the repository.

Notes:
* During this training a toy repository is used
* We will be adding changes to the repository during the training to confront you with typical Git situations
* Everything tracked by Git is inside the repository. Everything! Seriously... everything! Or almost everything!
* If there is something you want to backup, then it's the ``.git`` folder... but's let's discuss that later

---

## Digging deeper

Don't panic!

```shell
$ {{ "ls -blah .git"|run }}
```

This is deep enough for now!

Notes:
* Become aware of the list entries
* HEAD, config, description are files
* The rest are folders
* Studying what happens in here while using Git was very helpful to me

---

![Git](https://imgs.xkcd.com/comics/git_2x.png)<!-- .element: height="500px" -->

Notes:
* The goal of this block is to show what Git does when it is used, to allow you to choose how to use it
* This training covers theory for using Git, however brain muscle (training) is needed
* If you want more training and need help, do not hesitate to contact me
* Use and learn *all* the commands and ask yourself how they may help you improving your workflow in a given situation
* This block gives you the means to learn using Git when there is no *happy path*
* Some parts of this block are rather technical and go "deep" into Git's internals

---

## Gitception

Behold, run this in a separate terminal!
<!-- .element: class="fragment" -->

```shell
$ cd ~/working/directory/.git
```
<!-- .element: class="fragment" -->

We are creating a repository inside the repository
<!-- .element: class="fragment" -->
```shell
$ {{ 'git init . && git add -A && git commit -m "Add the repository"'|multirun(gitception=True, quiet=True) }}
[master (root-commit) {{ "HEAD"|commit_hash(gitception=True) }}] {{ "HEAD"|commit_hash(gitception=True)|commit_title(gitception=True) }}
 15 files changed, 653 insertions(+)
 create mode 100644 HEAD
 create mode 100644 config
 create mode 100644 description
 create mode 100755 hooks/applypatch-msg.sample
 [...]
 create mode 100755 hooks/update.sample
 create mode 100644 info/exclude
```
<!-- .element: class="fragment" style="font-size: 0.535em" -->

Don't do this at home!
<!-- .element: class="fragment" -->

Notes:
* Open a second terminal window and navigate to the repository's repository to switch context easier
* Git keeps track of all the changes, it is therefore a perfect analysis tool
* Most Git commands go up the directory path to the point where they find a ``.git`` folder, but "ignore" its contents
* Therefore we can create a repository in the repository to track the changes and understand Git's behavior
* If you do not remember what happens when you run a specific command, you can look it up later in the "Gitception" repository
* Ignore the added files for now, most of them are discussed later during the training
* I haven't seen an other Git training doing this! Let me know if you like this idea!

---

![Gitception](https://i.imgflip.com/2f33xj.jpg)

Notes:
* Xzibit shows up on every slide which uses the repository in the repository to set you in the right context
* You do not need to run the commands of these slides, since they're only for comprehension
* The repository is publicly available, you can clone it and take a look at its history

---

## What's the status?

To get an overview of the repository run:
```shell
$ {{ "git status"|run }}
```

Notes:
* The repository is on the master branch
* Branches are discussed later, for now, just remember that the master branch is (in most repositories) the default branch
* There are no commits
* Commits are discussed in detail in a few slides
* In many cases Git tells you what to do, you may configure these advices with the Git config command

---

## Let's do something!

Documentation first!

```shell
$ {{ 'echo "# My awwwesome training" > README.md'|shell }}
```

What's the status now?
```shell
$ {{ "git status"|run }}
```
<!-- .element: style="font-size: 0.465em;" -->

Notes:
* We want to track changes to the current untracked file!

---

## The index

aka. *the staging area*

![The index](http://web.archive.org/web/20090210020404id_/http://whygitisbetterthanx.com/images/index1.png) <!-- .element: height="250px" style="background: white" -->

"*...is an intermediate area which allows to setup the change before making the commit.*"

Notes:
* Not all VCS have this feature!
* I like comparing the staging area to a fork:
  The plate is the working directory, the repository is your tummy... and the fork allows you to:
  - ...pick up what you want to put in your tummy
  - ...take a look what you are going to eat before doing so

---

## Let's stage!

Put files in the staging area:
```shell
$ {{ "git add README.md && git status"|multirun }}
```

Notes:
* The file is now in the `changes to be committed`
* You can add whole directories (double check that there are no files which should not be included)
* You can also add parts of files (we will see the patch mode later), unless they're not tracked yet
* The Git integration of your editor may allow to stage a selection of lines (similar to the patch mode)

---

## What happened in the repository?

```shell
$ {{ 'git add . && git commit -m "Add files to index"'|multirun(gitception=True) }}
```
<!-- .element: style="font-size: 0.51em;" -->

{% filter gitception %}{% endfilter %}

Notes:
* The index file is a binary file and it is not discussed in this training
* The name of the objects is given by their (SHA1) hash (altough moving to another hashing algorithm is being discussed)
* To improve file-system usage, the objects are stored in folders
* You can add any kind of content into a Git repository, yet some objects shouldn't be added (large files which change a lot)
* Git will store this content in an object.
* Git objects are seen as part of the Git internals!
* Understanding objects is relevant for using and debugging Git well

Questions:
* How many folders will be created at max? [16^2]
* How many files can be created? [16^32]
* What's the probability to have two files with the same hash?

---

## What's in the newly created object?

Inspect the created object
```shell
$ {{ "git cat-file -t b27501a"|run }}
```
```shell
$ {{ "git cat-file -p b27501a"|run }}
```

Notes:
* Git categorizes commands into porcelain and plumbing commands
* This command is considered a plumbing command
* You can also use `git show`, the output will differ tough
* Files are stored as objects of type "blob" (Binary Large OBject)
* Not only files are stored in objects
* You can find the size of an object by using the ``-s`` flag
* Only the first few (min. 7) hexadecimal digits of a hash are required to determine the file
* More objects are discussed later
* Please remember, that the whole file and not only the diff is stored! (well... it depends! 😊)

---

## See staged changes

...to check if they are ready to be committed:
```shell
$ {{ "git diff --cached"|run }}
```

Are you ready to commit them?

Notes:
* Take a look at the changes to be committed before doing so
* Make sure you know, what you commit
* Think of the fork metaphore... do you want to eat a bad pea? or a bug hidden between them?
* Make commits as small as possible for easier reviewing, the easier the review, the less errors will slip through
* If keeping track of what it's being committed is hard, then you might want to rethink your workflow
* Think of slicing down you work!

---

## A commit

aka. *a change*

"*...represents a complete version of your code.*"

Notes:
* Complete means: Tested, documented and ready to ship (well... this depends!)
* A commit comes with a commit message
* Guidelines for commit messages exist (...but most ignore them)
* Read [How to write a Git Commit Message](https://chris.beams.io/posts/git-commit/):
  - Expressive but short title and in imperative mode
  - One empty line after the commit title
  - Describe WHAT and WHY you are doing the change (HOW is described in the code)
* If you need to describe the how, you should probably rethink your code
* If a commit is not complete, you might want to stash the changes instead (discussed later today)
* If you have a test driven workflow, you may commit the test first and then the rest, but then mark, the test as expected to fail or not implemented (and fixup the implementation in a further commit - also discussed later)

---

## Save the changes

...by commiting them to the repository
```shell
$ {{ 'git commit -m "Describe the training"'|run }}
```

Notes:
* `master` is the default branch name by default (the name of the default branch is configurable)
* `root-commit`: This is a special one, it has no parent, well see that in a minute
* `{{ "HEAD"|commit_hash }}` is part of the hash of the commit
* Git tells you the the number of files changed, lines inserted or deleted
* Create mode with permissions (not all permissions are stored in Git)
* You can also run just `git commit` without the `-m` argument, then your editor will pop-up
* I did not describe the "why" here, do as I tell you, not as I do (here)

---

## Time to dig deeper

The repository's content must have changed...

```shell
$ {{ 'git add . && git commit -m "Commit file"'|multirun(gitception=True) }}
```
<!-- .element: style="font-size: 0.51em;" -->

{% filter gitception %}{% endfilter %}

Notes:
* The `COMMIT_EDITMSG` is used to temporarily store the message of the commit
* The logs keep track of the commit hashes the references pointed to, they become handy when branches are lost (more about this later)
* There is also a log for the `HEAD` (more about the `HEAD` later)
* References (or refs here) are discussed later - see the `master` there again?
* One of the objects (`{{ "HEAD"|commit_hash }}`) has the same hash as the previously made commit
* ...and look! An other object!

---

## Commit objects!

What is the object with the commit's hash?
```shell
$ {{ "git cat-file -t LAST_COMMIT"|run }}
```
```shell
$ {{ "git cat-file -p LAST_COMMIT"|run }}
```
...so this is what a commit looks like!

Notes:
* Git stores commits in objects as well
* There is a reference to the tree (discussed in the next slide)
* The author and the committer are not necessarily the same person
* A timestamp is stored as well in the commit
* The title and the message are stored in the commit object
* The first commit (also called root) has no parent (more to parents later)

---

## Tree objects!

What is the object with the tree's hash?
```shell
$ {{ "git cat-file -t LAST_TREE"|run }}
```

```shell
$ {{ "git cat-file -p LAST_TREE"|run }}
```
<!-- .element: style="font-size: 0.545em;" -->

...it's collection of references to objects!

Notes:
* The tree is an object containing references to the blobs (or other trees)
* The tree also stores the permissions and the names of the files (but you can't set all permissions!)
* If a file happens to be more than once in the repository, Git will save it only once, since all the trees will reference the same file

By now, you know more about Git internals than many who consider themselves proficient in Git.
You will also be able to find "lost" files, folders and commits!

---

## What was the last commit?

Take a look at a change using:
```shell
$ {{ "git show"|run }}
```
<!-- .element: style="font-size:0.5em;" -->

Notes:
* If no argument is passed, the currently checked out commit will be shown
* You can also show trees, blobs and other commits by passing their hash
* More details about commits are discussed in a few slides
* The diff is also visible
* As you can see, this command is similar to `git cat-file`
* You can change the output using options

---

## Add in patch mode

...to select the changes you want to stage
```shell
$ {{ "echo 'This training will make you better!' >> README.md"|shell }} && {{ "git add -p"|run(input="y") }}
```
<!-- .element: style="font-size: 0.485em;" -->

```shell
$ {{ 'git commit -m "Motivate the participant"'|run }}
```

This is a great way to group your code!

Notes:
* This interactive process allow to select the hunks to add to the index.
* Possible command during interactive mode:
  - y - stage this hunk
  - n - do not stage this hunk
  - q - quit; do not stage this hunk or any of the remaining ones
  - a - stage this hunk and all later hunks in the file
  - d - do not stage this hunk or any of the later hunks in the file
  - g - select a hunk to go to
  - / - search for a hunk matching the given regex
  - j - leave this hunk undecided, see next undecided hunk
  - J - leave this hunk undecided, see next hunk
  - s - split the current hunk into smaller hunks
  - e - manually edit the current hunk
  - ? - print help
* You can always abort this command with ``Ctrl-c``
* Some editor integrations allow you to add hunks of code to the index as well
* Try to make groups of changes before adding them in patch mode
* Once you grouped your changes, think of their logical order
* Then add and commit them
* This way of adding changes to the index requires some training until you feel comfortable

---

## How does the new commit look like?

This second commit shouldn't be a root commit:
```shell
$ {{ "git cat-file -p LAST_COMMIT"|run }}
```
...it has a parent!

Notes:
* Every commit (with exception of root commits) point to (at least) an other commit

---

## Commit in patch mode

My favorite way of committing!
```shell
$ {{ 'echo "Buy me a beer if it made you better." >> README.md'|shell }}
$ {{ 'git commit -p -m "Motivate the speaker"'|run(input="y", store="motivate the speaker") }}{{  "motivate the speaker"|store|lines(0, -2) }}
```

Once all hunks are decided, a commit will be created
```shell
{{ "motivate the speaker"|store|lines(-2, None) }}
```


Notes:
* It is like adding in patch mode and commit in one step!
* Try adding in patch mode and committing while you feel insecure using the patch mode
* Once you feel comfortable enough, start committing directly in patch mode to save time
* The flags are the same as for the add command
  - y - stage this hunk
  - n - do not stage this hunk
  - q - quit; do not stage this hunk or any of the remaining ones
  - a - stage this hunk and all later hunks in the file
  - d - do not stage this hunk or any of the later hunks in the file
  - g - select a hunk to go to
  - / - search for a hunk matching the given regex
  - j - leave this hunk undecided, see next undecided hunk
  - J - leave this hunk undecided, see next hunk
  - s - split the current hunk into smaller hunks
  - e - manually edit the current hunk
  - ? - print help

---

## What did we do so far?

Take a look back at your work using:
```shell
$ {{ "git log --oneline"|run }}
```
...so this is why we want short commit titles?

Notes:
* The newest commits are displayed on top
* Without the ``--oneline`` flag, each commit would use several lines
* We have a branch with three commmits.
* This command is one of the reasons to choose short, meaningful commit titles

---

## Commit the repository's changes

Add the new objects to the repository's repository:
```shell
$ {{ 'git add . && git commit -m "Use the patch mode"'|multirun(gitception=True) }}
```
<!-- .element: style="font-size: 0.465em;" -->

{% filter gitception %}{% endfilter %}

Notes:
* This is just to keep the working directory clean, to understand the next steps better

---

## Exercises

* Run the commands in the previous slides
* What's your mindset? Do you commit backups or changes? Or both?
* Why can we add a repository in the repository?
* Add two different changes to a file and commit them separatedly
* Restore a file from a blob object
* Create a commit with two files but only one blob object

---

# Discussion

Notes:
* Backups vs Changes
* Slicing changes

---

![Graph theory](https://imgs.xkcd.com/comics/collatz_conjecture.png)

Notes:
Take a look at the graph in the comic:
* No number appears twice
* Each number points only to one number
* ...but several numbers can point to the same number
* There are no loops
* It is a directed graph
* No matter where you start, if you follow the arrows, you'll always finish at one!

This could be a valid graph of a Git repository!
* Each node in the comic could be a commit

We already started building such a graph! Now let's build branches!
* Creating branches with diverging commits
* Add the changes of a branch to an other branch

---

## A branch

aka. *a reference*

"*References are pointers to commits.*"

* simplify complex workflows.
* allow to group the logic of a feature.
* allow to work in parallel on several features.

Notes:
* There are also other references: tags

---

## Create a branch

Branches are created using
```shell
$ {{ "git branch pe/new_branch"|run }}
```

Notes:
* There are naming conventions for branches
* Prefix branches with your initials, to tell others not to touch it
* Reference the issue in the name if the branch is related to it
* If the branch name looks like a folder path, Git will create folders
* To work on a branch you need to check it out (or switch to it)

---

## Digging again!

How are branches stored in the repository?

```shell
$ {{ 'git add . && git commit -m "Add a new branch"'|multirun(gitception=True) }}
```
```shell
$ {{ "cat refs/heads/pe/new_branch"|run(gitception=True) }}
```

It's just a file with a hash

...that's why creating branches is so fast!

{% filter gitception %}{% endfilter %}

Notes:
* See how a further logfile was created? There is a log file for each branch!

---

## Remember git show?

Let's see what the hash is
```shell
$ {{ "git show LAST_COMMIT_FULL"|run }}
```
<!-- .element: style="font-size: 0.44em" -->

A branch is just a hash of a commit

Notes:
* Deleting branches shouldn't scare you anymore!
* If you accidentally delete a branch, you can create it again
* You just need to find the right commit!

---

## Now let's switch to it!

```shell
$ {{ "git switch pe/new_branch"|run }}
```

... to add further commit to it!

Notes:
* As noted before, it is necessary to switch to a branch to add commits

---

## What happened in the repo?

```shell
$ {{ 'git add . && git commit -m "Check out the branch"'|multirun(gitception=True) }}
```

2 files changed... but what changed?

{% filter gitception %}{% endfilter %}

---

### Let's take a closer look

`git show` comes with many options:
```shell
$ {{ 'git show --name-only'|run(gitception=True) }}
```

...ah! the `HEAD` changed!

{% filter gitception %}{% endfilter %}

Notes:
* Run `git help show` once, to see all of the options!
* We are discussing the `HEAD` more in detail later during this training
* We are also taking a look at the logs later

---

## Create and switch to branches
## ...in one step!

Switch to a *new* branch:
```shell
$ {{ "git switch -c pe/add_list_of_favorite_beers master"|run }}
```
...one command is faster than two!

Notes:
* If you leave the starting point (`master` here), the current `HEAD` is used
* `git checkout` was previously used for this purspose
* `git checkout` is criticized to be overloaded with functionality
* `git switch` might require some runtime, depending on the size of the files to be copied

Now that we know how to create branches, let's create two with diverging history!

---

## Add a commit to the new branch

```shell
$ {{ """cat << EOBL > beers.md && git add beers.md
* To Øl - 1 ton of Happiness
* Rokki - Muikea
* Felsenau - Bärner Müntschi
* Rokki - Happo
* Egger - Galopper
EOBL"""|shell }}
$ {{ 'echo "My list of [favorite beers](beers.md)." >> README.md'|shell }}
$ {{ 'git commit -a -m "Let people know, what beer to buy"'|run }}
```
<!-- .element: style="font-size: 0.47em;" -->

Notes:
* The first command creates and adds a file called "beers.md" (take a minute to digest it)
* The ``-a`` flag commits adding all *tracked* and modified files to the staging area!
* We created a new file and added a change to the existing one

---

## Create another branch

```shell
$ {{ "git switch -c pe/whiskey_is_also_an_option master"|run }}
```

...with another commit
```shell
$ {{ 'echo "Whiskey is also a good reward." >> README.md'|shell }}
$ {{ """cat << EOWL > whiskeys.md && git add whiskeys.md
* Lagavulin - 16
* Ledaig - 10
* Talisker - Storm
* Ledaig - 18
* Laphroaig - Quarter Cask
EOWL"""|shell }}
$ {{ "echo '[These whiskeys](whiskeys.md) are great!' >> README.md"|shell }}
$ {{ 'git commit -am "Accept whiskey as reward"'|run }}
```
<!-- .element: style="font-size: 0.545em;" -->

Notes:
* Options can also be put together `-a -m` is the same as `-am`
* We created a new file and added a change to the existing one, at the same place where the other branch introduce a change

---

## Clean up!

We do not want to have uncommitted changes 
```shell
$ {{ 'git add . && git commit -m "Add branches with conflicting commits"'|multirun(gitception=True) }}
```
<!-- .element: style="font-size: 0.5em;" -->

{% filter gitception %}{% endfilter %}

Notes:
* Now we should have a graph with two branches.
* Could you draw the graph of our Git repository?

---

## What a beautiful tree

Take a look at the graph of the repository using:
```shell
$ {{ "git log --oneline --all --graph"|run }}
```
<!-- .element: style="font-size: 0.46em;" -->
Our tree starts growing branches!

Notes:
* Using ``--all`` you can display commits of other branches as well (and the stash!)
* The graph is a little bit more hard to read: the lines represent connections

---

## Exercises

* Run the commands in the previous slides
* What is stored in the `HEAD` file?
* Take a look at the log files
* Can you switch to a specific commit?
* Delete and recover a branch with some commits
* Create a new branch based on a commit
* Take a look at the graph of a more mature project
* Create a new branch using then `--orphan` option

---

# Discussion

---

![Git](https://assets.amuniversal.com/ddf1fa20315201378d0e005056a9545d)

Notes:
* We are discussing how to add changes of branch to another branch
* There are several ways and workflows to achieve this
* Conflicts often arise when combining changes of several files
* You need to chose the workflow according to your projects' needs and developers' skills

We created branches with diverging history and a conflict, to simulate common situations.

---

## Wait... What?

# Conflicts?!

Notes:
* Conflicts happen when a file is changed and it is not obvious (to Git) how the changes should be applied
* There are also silent conflicts... let's discuss these later
* Let's introduce a change to our branch to provoque a conflict

---

## Git merge

![merge](https://wac-cdn.atlassian.com/dam/jcr:83323200-3c57-4c29-9b7e-e67e98745427/Branch-1.png?cdnVersion=lj)<!-- .element: height="380px" style="background: white;" -->


Join development histories

Notes:
* This (may) result in a forked (non-linear) commit-history (you have several ways to get to the root)
* If the changes are fast forward, then no merge commit is created
* You merge the changes of the other branch into your branch (the commit merge is added to the branch you are working on)
* Several branches can be merged at once

---

## Let's merge

Checkout a new branch for the merge
```shell
$ {{ "git switch -c pe/merging pe/add_list_of_favorite_beers"|run }}
```

Merge...
```shell
$ {{ "git merge pe/whiskey_is_also_an_option"|run }}
```
<!-- .element: style="font-size: 0.545em;" -->
...and run into conflicts!

Note:
* A new branch is not required, this just keeps the previous branches intact
* The output of the merge command is self explaining

---

## Merge conflicts are fun!

How does Git handle merge conflicts?
```shell
$ {{ 'git add . && git commit -m "Commit during merge conflict"'|multirun(gitception=True) }}
```
<!-- .element: style="font-size: 0.505em" -->

A further object?

{% filter gitception %}{% endfilter %}

Notes:
* The `MERGE_HEAD` points to `pe/whiskey_is_also_an_option`'s tip commit
* The `MERGE_MODE` is not discussed here
* Take a look at the `MERGE_MSG` if you feel like it
* `ORGI_HEAD` points to `pe/add_list_of_favorite_beers`' tip commit

---

## Take a look at that object!

We are getting used to this!
```shell
$ {{ "git cat-file -t 7453e34"|run }}
```
```shell
$ {{ "git cat-file -p 7453e34"|run }}
```

Looks like the `README` file... 

Notes:
* Git stores conflicting files in objects as well
* The conflicting part is marked by `<<<<<<<`, `=======` and `>>>>>>>`

---

## What's the status?

Let's take a look at the status:
```shell
$ {{ "git status"|run }}
```
As expected, a file was modified by both branches!

Notes:
* ``README.md`` is modified by both branches, such that Git cannot tell how the changes should be merged.
* Git is telling you what to do: either fix the conflicts or abort the merge
* Did you notice Git added `whiskeys.md` as a change to be commited?

---

## Understanding the conflict

Take a look at the conflicting files:
```shell
$ {{ "git diff"|run }}
```

This conflict is easily solved!

Notes:
If the conflict is not that easy, you can:
1. `git log` both branches
2. identify the commits which introduce the conflict
3. read the commit messages and understand why the changes were introduced
4. speak to the author of the change and find a solution

* If the commit messages are of good quality, understanding the changes won't be a big deal
* if the commit messages are bad, I suggest you contact the author(s) of the conflicting changes

---

## Conflict resolution

Just remove the 4th, 6th and last line.
```shell
$ {{ "sed -i '4d;6d;$d' README.md"|shell }}
```

```shell
$ {{ "cat README.md"|run }}
```

Use your favorite editor to do so!

Notes:
* To resolve a conflict, edit the conflicting files such that it fits the requirements of both changes
* I would consider testing the application after the conflicts are resolved before finish merging

---

## Finish merging

...once you resolved the conflicts:
```shell
$ {{ "git add README.md"|shell }}
```

and run
```shell
$ git merge --continue
```
to open your editor to write the commit's message

or commit yourself directly
```shell
$ {{ 'git commit -m "Add the list of beers first"'|run }}
```
That was easy!

Notes:
* You can also run `git merge --continue`, which checks if there is an (interrupted) merge in progress before calling `git commit`

---

## Take a look at the merge commit

Merge commits are special...
```shell
$ {{ "git cat-file -t LAST_COMMIT"|run }}
```
```shell
$ {{ "git cat-file -p LAST_COMMIT"|run }}
```
...since they have more than one parent!

Notes:
* This makes error analysis a little bit more complex
* You need to follow up the changes of several parents now when looking for errors
* This can be accomplished by using ^1, ^2 or ^N (to reach the N-th direct parent)

---

## Meet the parents

```shell
$ {{ "git show HEAD^1"|run }}
```

Notes:
You can also use `~` to see the parent of one of the parents:
* `git show HEAD^1~2` shows the first parents parents parent
* `git show HEAD^3~1` shows the third parents parent

---

## Meet the parents 2
```shell
$ {{ "git show HEAD^2"|run }}
```

Notes:
At some point it is easier to run:
1. `git log --oneline --graph --all` and identify the commit to see
2. `git show` using the commit's hash

---

## Clean up!

Commit the changes into the repository's repository
```shell
$ {{ 'git add . && git commit -m "Add the merge"'|multirun(gitception=True) }}
```
<!-- .element: style="font-size: 0.51em;" -->

The merge files are gone!

{% filter gitception %}{% endfilter %}

Notes:
* What do the new objects contain? [The merge commit, the new tree and the `README` file]

---

## Git cherry-pick

![cherry pick](https://wac-cdn.atlassian.com/dam/jcr:8d62148d-ba03-4762-bd3a-06ddc465b07f/hero.svg?cdnVersion=jo) <!-- .element: height="300px" style="background: white" -->


Apply the changes introduced by some existing commits

Notes:
* This results in a linear commit-history
* You can also cherry pick many commits
* Merge commits can be cherry-picked! (But you need to specify the mainline)
* Cherry picked commits are added (copied) to the current branch

---

## Pick a cherry

Let's add another branch for cherry picking
```shell
$ {{ "git switch -c pe/cherry_picking pe/add_list_of_favorite_beers"|run }}
```
<!-- .element: style="font-size: 0.545em;" -->

Find the hash of the cherry (commit) to be picked
```shell
$ {{ "git log --oneline pe/whiskey_is_also_an_option"|run }}
```

Notes:
* Before you cherry pick a commit, you need to identify it

---

...then pick it up!
```shell
$ {{ "git cherry-pick pe/whiskey_is_also_an_option"|run }}
```

Notes:
* The better documented your commits are, the better you can work with them.
* Here we are cherry-picking a branch, therefore we cherry-pick the commit to which the branch is pointing to
* We could have used the commit's hash
* Boom, conflict!

---

## Sweet sweet conflicts

Dig, dig, dig, dig
```shell
$ {{ 'git add . && git commit -m "Commit a cherry pick conflict"'|multirun(gitception=True) }}
```
<!-- .element: style="font-size: 0.495em" -->

Another object!

{% filter gitception %}{% endfilter %}

Notes:
* This is again the conflicting file

Question:
* Why is the conflicting file different? [See next slide]

---

## So what's the conflict now?

```shell
$ {{ "git diff"|run }}
```

as expected, the conflict looks almost the same!

Notes:
* The only difference is that the hash and commit title are used!

---

## Use a mergetool

...to fix the conflict!

```shell
$ git mergetool
```

Conflict resolution with assistance!

Or fix the conflict manually if you prefer
```shell
$ {{ "sed -i '4d;6d;$d' README.md && git add README.md"|multirun }}
```

Notes:
* If you use the `mergetool` backup files will be created in your working directory
* Also edited files will be added to the staging area automatically after closing the `mergetool`
* You can configure Git not to create the backup file

---

## Continue cherry-picking

...once you finished fixing the conflict
```shell
$ git cherry-pick --continue
```

...or commit the staged changes with an existing commit message
```shell
$ {{ "git commit -C pe/whiskey_is_also_an_option"|run }}
```

---

## Clean up!

Once again...
```shell
$ {{ 'git add . && git commit -m "Add the cherry-pick"'|multirun(gitception=True) }}
```
<!-- .element: style="font-size: 0.505em;" -->

{% filter gitception %}{% endfilter %}

Notes:
* There are only 2 new objects... How many would you expect?

---

## Git rebase

![rebase](https://wac-cdn.atlassian.com/dam/jcr:e4a40899-636b-4988-9774-eaa8a440575b/02.svg?cdnVersion=lj) <!-- .element: height="350px" style="background: white" -->

> Reapply commits on top of another branch<!-- .element: style="font-size: 0.95em;" -->

Notes:
* This generates a linear history-tree without forks
* This is handy if you need to cherry-pick all commits of a branch
* The golden rule of rebasing: Never rebase a public branch! (...or teach your coworkers Git)

---

## Rebase yourself!

```shell
$ {{ "git switch -c pe/rebasing pe/whiskey_is_also_an_option"|run }}
```
```shell
$ {{ "git rebase pe/add_list_of_favorite_beers"|run }}
```

Notes:
* This time "the point of view" changes, therefore we switch to the branch which will be rebased
* The branch onto which you are rebasing to remains untouched
* The history of the active branch is rewritten
* If there is more than one conflicting commit, `git rebase` will stop at each conflict

---

## Rebasing

...is "slightly" more complicated:
```shell
$ {{ 'git add . && git commit -m "Commit a rebase conflict"'|multirun(gitception=True) }}
```
<!-- .element: style="font-size:0.5em;" -->

{% filter gitception %}{% endfilter %}

Notes:
* A new object is added for the conflicting file
* Git keeps track of a lot of state to perform a rebase

---

## Take a closer look at the conflict

```shell
$ {{ "git diff"|run }}
```
The reference here is the commit's title!

Notes:
* This is helpful to determine how to solve the conflict

---

## Finish rebasing

...once you resolved the conflicts:
```shell
$ {{ "sed -i '4d;6d;$d' README.md && git add README.md"|multirun }}
```
```shell
$ {{ "git commit -m 'Accept whiskey as reward'"|run }}
```

```shell
$ {{ "git rebase --continue"|multirun }}
```
<!-- .element: style="font-size:0.47em;" -->

---

## What about the rebase files?

```shell
$ {{ 'git add . && git commit -m "Add the rebase"'|multirun(gitception=True) }}
```
<!-- .element: style="font-size: 0.5em" -->

They are gone!

{% filter gitception %}{% endfilter %}

Notes:
* There are only 2 new objects... How many would you expect?

---

## Non obvious conflicts

Sometimes conflicts are introduced, which are not obvious to Git:

If one of the branches changes the behavior of a part of the code and the old behavior is required for the other branch, but there is no conflict within the files... then Git won't alert you!

How do you solve this?

Notes:
* There are several ways to solve this, and it is not strictly Git related

---

## Tests to the rescue!

You can run your tests while rebasing:
```shell
$ git rebase -x "pytest" <newbase>
```

If the tests fail, Git will stop the rebase and allow you to fix your code

Notes:
* This requires to have a test which will break when such a conflict arises
* If you test your code for behavior, this kind of conflicts are catched
* Now go tell Fredrik V. Mørken how he should be using `git rebase`


---

## Exercises

* Run the commands in the previous slides
* Abort a `merge`, `cherry-pick` or a `rebase`
* Merge two branches with different roots
* Create a commit with 3 parents
* Cherry-pick two commits at once
* Cherry-pick a merge commit
* Use `git rebase --onto`
* Take a look at the `--interactive` option of `git rebase`

---

# Discussion

Notes:
* Cherry-picking using backups instead of changes
* Checking the change in test coverage of every commit
* Signs of bad architecture
* Rewriting the history
* Garbage collection

---

![Git log](https://imgs.xkcd.com/comics/git_commit_2x.png)<!-- .element: height="400px" -->

Notes:
* Please do not do this!
* Keep a the information to noise ratio high
* This is important for later code analysis
* Think of the people who will deal with your repository
* Think of the repositories you will deal with
* There are several strategies to clean such a history

---

## Backups vs. Patches

Version control is a system that records changes to a file or set of files over time ...so that you can recall specific *states* later.
<!-- .element: class="fragment" -->

Version control is a system that allows to write and manage sets of *patches* ...so that you can recall specific *versions* later.
<!-- .element: class="fragment" -->

Notes:
* The concept of backups is common and backups are widely-used
* The concept of changes / patches, requires a better overview

---

## Preparing the branch of backups

Add a branch with a few commits
```shell
$ {{ "git switch -c pe/backups pe/rebasing"|run }}
$ {{ 'echo "I would also love some feedback." >> README.md'|shell }}
$ {{ 'git commit -am "Ask for feedback"'|run }}
$ {{ 'echo "Personal feedback is the best." >> README.md'|shell }}
$ {{ 'git commit -am "Ask for personal feedback"'|run }}
$ {{ 'echo "Helpful feedback is awarded with great coffee." >> README.md'|shell }}
$ {{ 'git commit -am "Trade feedback for coffee"'|run }}
```
<!-- .element: style="font-size: 0.52em" -->

Notes:
* This is similar to the situation displayed in the comic

---

## Clean up! 

```shell
$ {{ 'git add . && git commit -m "Add the branch of backups"'|multirun(gitception=True) }}
```
<!-- .element: style="font-size: 0.5em" -->

{% filter gitception %}{% endfilter %}

Notes:
* Why were 9 objects created? [3 commits with each having a tree and a blob]
* Now we are going to discuss 3 different ways to combine or work with this commit history

---

## Rebasing in interactive mode

"Change" the commit history during rebase!

```shell
$ {{ "git switch -c pe/interactive_rebase pe/backups"|run }}
```

This is like rebasing
```shell
$ git rebase -i pe/rebasing
```
...on steroids!

Notes:
* This is a really powerful tool to organize the commit history and make it more meaningful

---

Your editor now lists all the commits of your branch!
```text
pick {{ "HEAD~2"|commit_hash }} {{ "HEAD~2"|commit_hash|commit_title }}
pick {{ "HEAD~1"|commit_hash }} {{ "HEAD~1"|commit_hash|commit_title }}
pick {{ "HEAD"|commit_hash }} {{ "HEAD"|commit_title }}

# Rebase {{ "HEAD~3"|commit_hash }}..{{ "HEAD"|commit_hash }} onto {{ "pe/rebasing"|commit_hash }} (3 commands)
#
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup <commit> = like "squash", but discard this commit's log message
# x, exec <command> = run command (the rest of the line) using shell
# d, drop <commit> = remove commit
# l, label <label> = label current HEAD with a name
# t, reset <label> = reset HEAD to a label
# m, merge [-C <commit> | -c <commit>] <label> [# <oneline>]
# .       create a merge commit using the original merge commit's
# .       message (or the oneline, if no original merge commit was
# .       specified). Use -c <commit> to reword the commit message.
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
#   However, if you remove everything, the rebase will be aborted.
#
#
# Note that empty commits are commented out
```
<!-- .element: style="font-size: 0.47em;" -->

Notes:
* You can:
  - Change the order of the commits
  - Edit the commit titles
  - Edit commits
  - Run commands between the commits
  ...
* The first command cannot be a squash or a fixup!
* Drop, squash, fix up or change the order of the commits as required
* Mastering the interactive rebase is worth a salary raise!
* There are commit commands to create automtic fixup and squash commands!

---

## There's a shortcut!

...to avoid having to move commits around
```shell
$ git help commit | grep "autosquash" -C 2

       --fixup=<commit>
           Construct a commit message for use with rebase --autosquash. The commit message will be
           the subject line from the specified commit with a prefix of "fixup! ". See git-rebase(1)
           for details.

       --squash=<commit>
           Construct a commit message for use with rebase --autosquash. The commit message subject
           line is taken from the specified commit with a prefix of "squash! ". Can be used with
           additional commit message options (-m/-c/-C/-F). See git-rebase(1) for details.

```
<!-- .element: style="font-size: 0.355em" -->

Notes:
* Use these two when you already know that a commit belongs to an other one

---

## Commit the changes in the repository

```shell
$ {{ 'git add . && git commit -m "Rebase in interactive mode"'|multirun(gitception=True) }}
```

{% filter gitception %}{% endfilter %}

Notes:
* This output is expected if you only used the command "pick".
* If you squashed or fixed up commits, more objects would have been created.

---

## Exercises

* Change the order of commits
* Create a `--fixup` or `--squash` commit
* Rebase a branch using the `--autosquash` flag
* Run an interactive rebase with the `-x` option
* Edit a commit during a rebase
* Study `git reset`, `git stash` and `git checkout`

---

# Discussion

Notes:
* Splitting commits
* Combining rebase, reset, checkout and stash
* Keeping the holistic picture

---

## I didn't find a decent comic for discussing distributed Git

## so you only get this lowsy slide

Notes:
* 100 internet points for the one who suggests a good comic for distributed repositories!
* 1000 internet points for the one who makes a good comic for distributed repositories!

---

![Local VCS](VCS/local_vcs.png)<!-- .element: height="400px" -->

Notes:
* This is a "Local Version Control System"
* Versions are associated to points in time
* Versions are usually not labeled / tagged
* Descriptions for the versions are usually not made

---

Let's add some...

*collaboration*
<!-- .element: class="fragment" -->

Notes:
* In within a company, it is pretty common to share files
* These shared files are not managed by every user individually
* Imagine the chaos (or waste of disk space) if everyone had to manage the backups individually
* Therefore it makes sense to setup a central file-share and make up backups of these files
---

![Centralized VCS](VCS/centralized_vcs.png)<!-- .element: height="400px" -->

Notes:
* This is called "Centralized Version Control System"
* You know this from file shares like backed up NFS or Dropbox
* An advantage of this is that it is pretty easy to setup
* And if you are thinking of it: No. This is not like Google Docs or Office 365, since they allow you to edit files at the same time (which is crazy!)

---

## Drawbacks of *centralized* vcs

* Connection to central server is required
* Remote commits are slow
* Worflows can be very complicated
* A central server introduces a single point of failure

Notes:
* This is a good solution if the documents are not edited frequently
* It is also helpful if files are not edited by people at the same time

Questions:
* Two people want to work on the same file? (ask Google about it)
* The server goes down for maintenance?
* The internet connection is down for maintenance?
* What do we do with software developers?

---

What if version control was...

*distributed?*<!-- .element: class="fragment" -->

Notes:
* I said before: Imagine the chaos (and waste of disk space) if everyone had to manage the backups individually
* When working in software development (or working with plain text files), development teams often work on the same files at the same time
* Unless very complicated workflows are introduced, chaos is inevitable
* But chaos can be minimised if propper tooling is used conveniently

---

![Decentralized VCS](VCS/decentralized_vcs.png)<!-- .element: height="400px" -->

Notes:
* This is what a distributed version control system looks like
* You use this every day without being aware of: Git

---

Development becomes *complex!*

Notes:
* Propper tooling is required to handle emerging situations
* Managing such a system requires great understanding of this tools (or introducing complicated workflows)
* But since workflows usually constraint the users development, it is usually better to learn the tools propperly

---

## Advantages of *distributed* VCS 

* Committing changesets can be done locally
* Committing changesets is extremely fast
* One can share the changes with others without having to publish them

...also: A centralized solution is not less complex.<!-- .element: class="fragment" -->

Notes:
* There are barely disadvantages (disk space is not an issue, since we're dealing with small files!)
* A distributed VCS can still be used like a central VCS (and in most cases it is!)
* Who already had a shared Git repository in a Dropbox folder?

How do we reduce complexity?

Think of patches!

---

Complexity is reduced if patches are well...
* self contained
* documented
* tested
* small

Notes:
* Patches should be self contained, to avoid questions and forgetting things which belong together
* Patches should be as small as possible, it is easier to patch twice than to split a patch
* Every patch should be documented and signed

---

Other conveniences of using patches:
* simpler error analysis
* simpler code review
* better code reusability
* faster development

Notes:
* Tools exist to find out which patch introduced errors, it is much much easier to find an error in within a few lines of code than in within hundreds of lines of code
* Correctly signed patches allow to ask the author in case of uncertainty
* Patches can be applied to several systems if the same or a similar logic is required

---

## Adding a remote

...is simple as running
```shell
$ {{ "git remote add gitception .git/"|run }}
```

Notes:
* Replace the folder path with an URL or a Git handle
* The default remote is called `origin`
* There are several subcommands which allow you to manage remotes

---

## Starting to feel like home

Let's see how Git deals with remotes:
```shell
$ {{ 'git add . && git diff --cached'|multirun(gitception=True)}}
```

Aha! They're stored in the repository's configuration!

{% filter gitception %}{% endfilter %}

Notes:

---

## Commit the changes

```shell
$ {{ 'git commit -m "Add Gitception as remote"'|run(gitception=True) }}
```

{% filter gitception %}{% endfilter %}

---

## Sync the repositories

...using

```shell
$ {{ 'git fetch gitception'|run }}
```

This will download all branches and their associated objects!

Notes:
* This is similar to `git pull`, there is an excersise to determine the differences!

---

## We could start building a bunker!

```shell
$ {{ 'git add . && git commit -m "Fetch the gitception remote"'|multirun(gitception=True) }}
```
<!-- .element: style="font-size: 0.42em" -->

What the $%#@! What are pack files?

{% filter gitception %}{% endfilter %}

Notes:
* I actually can't tell you much about packfiles!
* You can read about pack-files here: https://git-scm.com/book/en/v2/Git-Internals-Packfiles

---

!["Is this the real world?"](https://cdn.prod.www.spiegel.de/images/de945cc8-0001-0004-0000-000000115065_w920_r1.5005359056806002_fpx33.29_fpy49.95.jpg)<!-- .element: height="550px" -->

Notes:
* Ok, ok, ok... so now we have in our Git repository within our Git repository, our Git repository as commits of commits of commits in pack files!
* I think that's deep enough for today!

---

## Let's add a public repository

...to make our work accessible to others
```shell
$ {{ "git remote add github git@github.com:escodebar/trainings.git"|run }}
```

Notes:
* This is where you will find:
  - the commits and branches made so far
  - the Gitception repository

---

## Pushing all branches

...and changing their name on the remote
```shell
$ {{ 'git push -u github "refs/heads/*:refs/heads/git/unibe/repo/*"'|run }}
```

Notes:
* This was a lot of information at once!
* You can also just push single branches... but I am sure you will understand this command if you made it this far!
* When pushing a branch, you are pushing all associated objects
* You can also push all branches and associated objects with `--all`

---

## Remote branches in our repository?

...how does that work?
```shell
$ {{ 'git add . && git commit -m "Push the branch"'|multirun(gitception=True) }}
```
<!-- .element: style="font-size: 0.40em" -->

{% filter gitception %}{% endfilter %}

---

## But how...

...does it know which branches belong together?
```shell
$ {{ 'git show'|run(gitception=True) }}
```

{% filter gitception %}{% endfilter %}

Notes:
* Git keeps track of the associated branches in the repository's configuration!

---

## Let's also push the gitception branch

...for the sake of completeness

```shell
$ {{ "git fetch && git push -u github refs/remotes/gitception/master:refs/heads/git/unibe/gitception"|multirun }}
```
<!-- .element: style="font-size: 0.38em" -->

Now you know where to get the repositories for later analysis!

Notes:
* This allows you to push branches between remotes
* This workshop is self-contained!

---

## Excercises

* Run the commands in the previous slides
* Checkout a remote branch
* Create a new branch based on a remote branch
* Think about it: Do you need a local master branch?
* Add a second remote and push a branch to it
* Explain how `git pull` is different from `git fetch`
* Push a local commit to a remote branch
* Read about `git push --mirror`

---

# Discussion

---

![Workflows](https://imgs.xkcd.com/comics/90s_flowchart.png)<!-- .element: height="550px" -->

Notes:
* There are a lot of different workflows
* The workflow is a tool which has to be chosen according to the task and the people working on the task
* You do not necessarily have to use the same workflow all the time (think about Cynefin!)

---

## Centralized Workflow

![Centralized Workflow](https://git-scm.com/book/en/v2/images/centralized_workflow.png)

Notes:
* This is probably the simplest possible workflow
* This workflow is very common
* The complexity is handled in code and the deployment tools

---

## Integration-Manager Workflow

![Integration-Manager Workflow](https://git-scm.com/book/en/v2/images/integration-manager.png)

Notes:
* I like this workflow a lot
* Depending on the Integration-Manager, the developers are not forced to write nice patches

---

## Dictator and Lieutenants Workflow

![Dictator and Lieutenants Workflow](https://git-scm.com/book/en/v2/images/benevolent-dictator.png)<!-- .element: height="440px" -->

Notes:
* The Linux kernel developer community uses this workflow
* It is similar to the Integration-Manager workflow but with an additional layer

---

## GitHub Flow

The [GitHub Flow](https://guides.github.com/introduction/flow/) is a simple yet elegant workflow!

Notes:
* It includes:
  - Code review
  - Discussions
  - Deployment
  - Testing
* It is *pretty* lean!

---

![Technical Debt](https://i.pinimg.com/originals/07/07/f3/0707f39f910cbf3560b423910ec23e5a.gif)

---

## Gitflow Workflow

And then there is the [Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)!

Notes:
* To me, this workflow handles way too much complexity
* All developers need to have a good Git knowledge and a holistic picture

---

## Exercices

* Discuss in a group your current workflows
* Think of possible scenarios where these workflows may be useful
* Discuss where and who manages project complexity with these workflows
* Make a pull request
* Review the code of a pull request
* Add comments to a pull request

---

# Discussion

---

## Extra task

Share a public repository and implement FizzBuzz in TDD communicating only using Git commits.
Also think of a way to establish a common workflow using only Git commits!

---

## Resources

* [10 things I hate about Git](https://stevebennett.me/2012/02/24/10-things-i-hate-about-git/)
* [Cynefin](https://cognitive-edge.com/videos/cynefin-framework-introduction/)
* [Git Magic](http://www-cs-students.stanford.edu/~blynn/gitmagic/ch08.html)
* [Git Reference](https://git-scm.com/docs/)
* [Git is simpler](http://nfarina.com/post/9868516270/git-is-simpler)
* [Oh shit Git!](https://ohshitgit.com/)
* [Pro Git](https://git-scm.com/book/en/v2)
* [The thing about Git](https://tomayko.com/blog/2008/the-thing-about-git)
* [Think like a Git](http://think-like-a-git.net/)
* [Why Git is Better than X](http://web.archive.org/web/20090210020404id_/http://whygitisbetterthanx.com/#the-staging-area)

---

## Questions & Feedback

---

## Thank you!

🍺🍻🍺
