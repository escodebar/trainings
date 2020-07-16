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

* Gitception
* Git objects
* Git branches
* Merge conflicts

Notes:

There are going to be excercises after or during each block!

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

* Have you been using other version control systems?
* How long have been using Git?
* What challenges you the most when using Git?
* How do you solve the tangled working copy problem?

---

# Discussion

---

## Slides

[https://escodebar.github.io/trainings/git/bison/](https://escodebar.github.io/trainings/git/bison/)

Notes:
* You can find the speaker notes in the slides, which allows you to go through the training at home
* Pass the slides to your coworkers, your friends, etc., the more people understand Git the better
* If a slide needs clarification, please let me know!

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

## Exercises

* Run the commands in the previous slides
* Why can we add a repository in the repository?

---

# Discussion

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
* Add two different changes to a file and commit them separatedly
* Restore a file from a blob object
* Create a commit with two files but only one blob object
* Take a look at the sizes of blob objects in a mature project.

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

## Exercises

* Run the commands in the previous slides
* Create a merge commit with 3 parents
* Try using `git mergetool`
* How do you currently deal with conflicts?

---

# Discussion

* Silent conflicts

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
