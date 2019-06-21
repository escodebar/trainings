---
theme: solarized
title: Git meetup
revealOptions:
    transition: 'fade'
---

# Dr. Git-love

## or: How I learned to stop worrying and love the rebase
<!-- .element: class="fragment" -->

Notes:
* Most of the things we discuss here are not only achievable with Git, but can be made with other VCS as well
* I am a total Git-Fanboy, whatever I say during this meetup is totally opinionated
* I want to make this a fun experience for all of us!

---

## A few words about
# this training

Notes:
* It all started when I was asked to give a full day introduction to Git for a CAS
* I prepared a training trying to add something useful for several levels of Git knowledge
* The intended audience was PhD students with basic to no Git experience and technicians
* The training was very successful, receiving a lot of good feedback
* I gave this training a few more times
* At the last SoCraTes conference I rushed through the training
* Then we decided to host this meetup
* It is going to be tough (for all of us) but rewarding
* I hope you do not mind the bad jokes

---

## Schedule

* Gitception: Reaching into the substructure
* Of trees, branches and pieces of fruit
* It's a backup system... It's a patch system... It's Git!
* Change distribution using the remote control

Notes:
* Gitception is about using Git to understand Git and understanding the structure of Git
* The concept of Gitception is used throught the training
* The second block introduces branching and "merging" branches
* The third block treats in more detail how to create patches using Git
* This block is about cleaning up the Git history before a feature is released
* The last block discusses using Git as a distributed version control system
* I do not know yet if we can go through these 4 blocks within 3 hours (including questions)
* I expect to discuss each block in within 40 minutes leaving around 5 minutes for questions
* I prefer answering questions between the blocks rather than rushing through it
* I consider hosting a second event if the interest is high and we do not make it through

---

## Requirements

If you know how to type commands in a terminal and parse its output, this traning is made for you!

Notes:
* Reading is crucial here, by the end of the training you'll be using the *man*-pages a lot!
* No specific Git editor integration is discussed, since none of them covers all of Git's features
* For the same reason, no Git GUI is discussed
* I recommend using the terminal all of the time and start using other tools, if they make you more efficient than when using the console
* In many occasions you'll find yourself connected to a server with a Git repository, knowing the commands in that situation is crucial
* For some features, an integration for your favorite editor might be useful, yet start using the terminal

---

## Slides

[https://escodebar.github.io/trainings/git/meetup/](https://escodebar.github.io/trainings/git/meetup/)

---

# Are you ready?

---

![Git](https://imgs.xkcd.com/comics/git_2x.png)<!-- .element: height="500px" -->

Notes:
* The goal of this meetup is to show what Git does when it is used, to allow you to choose when and how to use it
* This training covers theory for using Git, however brain muscle (training) is needed
* Use *all* the commands and ask yourself how you can improve your workflows
* This meetup is made for people who did not use Git in depth before, but includes information for more experencied users
* This meetup covers using Git when there is no *happy path*
* Some parts of this training are rather technical and go deep into Git's internals
* It also introduces a method to learn Git by your own

---

## Setup

Create a repository:

```shell
$ mkdir -p ~/working/directory/ && cd $_ && git init .
Initialized empty Git repository in ~/working/directory/.git/
```

```shell
$ ls -blah
total 0
drwxr-xr-x 3 escodebar escodebar  60 Aug  2 10:39 .
drwxr-xr-x 3 escodebar escodebar  60 Aug  2 10:38 ..
drwxr-xr-x 7 escodebar escodebar 200 Aug  2 10:39 .git
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
$ ls -blah .git
total 12K
drwxr-xr-x 7 escodebar escodebar 200 Aug  2 10:39 .
drwxr-xr-x 3 escodebar escodebar  60 Aug  2 10:39 ..
drwxr-xr-x 2 escodebar escodebar  40 Aug  2 10:39 branches
-rw-r--r-- 1 escodebar escodebar  92 Aug  2 10:39 config
-rw-r--r-- 1 escodebar escodebar  73 Aug  2 10:39 description
-rw-r--r-- 1 escodebar escodebar  23 Aug  2 10:39 HEAD
drwxr-xr-x 2 escodebar escodebar 260 Aug  2 10:39 hooks
drwxr-xr-x 2 escodebar escodebar  60 Aug  2 10:39 info
drwxr-xr-x 4 escodebar escodebar  80 Aug  2 10:39 objects
drwxr-xr-x 4 escodebar escodebar  80 Aug  2 10:39 refs
```

This is deep enough for now!

Notes:
* Be aware of the listed objects
* HEAD, config, description are files
* The rest are folders

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
$ git init . && git add . && git commit -m "Add the repository"
Initialized empty Git repository in ~/working/directory/.git/.git/
[master (root-commit) 1c2f932] Add the repository
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
* Git keeps track of all the changes in the repository, it is therefore a perfect analysis tool
* Most Git commands go up the directory path to the point where they find a ``.git`` folder, but "ignore" its contents
* Therefore we can create a repository in the repository to track the changes and understand Git's behaviour
* If you do not remember what happens when you run a specific command, you can look it up later in the "Gitception" repository
* Ignore the added files for now, most of them are discussed later during the training
* Also ignore the "new" commands, as they're discussed in the next few slides
* I haven't seen an other Git training doing this!

---

![Gitception](https://i.imgflip.com/2f33xj.jpg)

Notes:
* Xzibit shows up on every slide which uses the repository in the repository to set you in the right context
* Open a second terminal window and navigate to the repository's repository to switch context easier
* You do not need to run the commands of these slides, since they're only for comprehension
* The repository is publicly available, you can clone it and take a look at its history

---

## What's the status?

To get an overview of the repository run:
```shell
$ git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
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
$ echo "# My awwwesome training" > README.md
```

What's the status now?
```shell
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        README.md

nothing added to commit but untracked files present (use "git add" to track)
```
<!-- .element: style="font-size: 0.465em;" -->

Notes:
* You can tell Git to ignore files using ``.gitignore``, then they won't be listed in the "Untracked files" section
* Ignore large files and non-project specific files:
  - backup files
  - binary files
  - data files
  - system specific files (like .DS_Store, or local configurations)
  - files containing (personal) passwords (move passwords to enivornment variables and use the environment variables)
* We want to track changes to the current untracked file!

---

## The index

aka. *the staging area*

![The index](http://web.archive.org/web/20090210020404id_/http://whygitisbetterthanx.com/images/index1.png) <!-- .element: height="250px" style="background: white" -->

"*...is an intermediate area which allows to setup the change before making the commit.*"

Notes:
* Not all VCS have this feature!

---

## Let's stage!

Put files in the staging area:
```shell
$ git add README.md && git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   README.md
```

Notes:
* The file is now in the ``changes to be committed``
* You can add whole directories (double check that there are no files which should not be included)
* You can also add parts of files (we will see the patch mode later), unless they're not tracked yet
* The Git integration of your editor may allow to stage a selection of lines (similar to the patch mode)

---


## What happened in the repository?

```shell
$ git add . && git commit -m "Add files to index"
[master 6147d79] Add files to index
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 index
 create mode 100644 objects/b2/7501ade65f39bc91a5e6eb0d707903ba225a00
```
<!-- .element: style="font-size: 0.51em;" -->

![Gitception](https://imgflip.com/s/meme/Serious-Xzibit.jpg)<!-- .element: style="width: 150px;" -->

Notes:
* The index file is a binary file and it is not discussed in this training
* The name of the objects is given by their (SHA1) hash
* To improve file-system usage, the objects are stored in folders
* You can add any kind of content into a Git repository, yet some objects shouldn't be added (large files which change a lot)
* Git will store this content in an object.
* Git objects are seen as part of the Git internals!
* Understanding objects is relevant for using Git well

Questions:
* How many folders will be created at max?
* How many files can be created?
* What's the probability to have two files with the same hash?

---

## What's in the newly created object?

Inspect the created object
```shell
$ git cat-file -t b27501a
blob
```
```shell
$ git cat-file -p b27501a
# My awwwesome training
```

Notes:
* Files are stored as objects of type "blob" (Binary Large OBject)
* Not only files are stored in objects
* You can find the size of an object by using the ``-s`` flag
* Only the first few (min. 7) hexadecimal digits of a hash are required to determine the file
* More objects are discussed later
* Please remember, that the whole file and not only the diff is stored! (well... not really 😊)

---

## Ready to commit?

See staged changes to check if they are ready to be committed:
```shell
$ git diff --cached
diff --git a/README.md b/README.md
new file mode 100644
index 0000000..b27501a
--- /dev/null
+++ b/README.md
@@ -0,0 +1 @@
+# My awwwesome training
```

Notes:
* Take a look at the changes to be committed before doing so
* Make sure you know, what you commit
* Make commits as small as possible for easier reviewing
* If keeping track of what it's being committed is hard, then you might need to rethink your workflow

---

## A commit

aka. *a change*

"*...represents a complete version of your code.*"

Notes:
* Complete means: Tested, documented and ready to ship
* A commit comes with a commit message
* Guidelines for commit messages exist
* Expressive but short title and in imperative mode
* One empty line after the commit title
* Describe WHAT and WHY you are doing the change (HOW is described in the code)
* If you need to describe the how, you should probably rethink your code
* If a commit is not complete, you might want to stash the changes instead or the title can be provided with a [WIP]
* If you have a test driven workflow, you may commit the test first and then the rest, but then mark, the test as expected to fail

---

## Save the changes

Commit the changes to the repository
```shell
$ git commit -m "Describe the training"
[master (root-commit) 78d7aa6] Describe the training
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
```

Notes:
* See ``master``?
* ``root-commit``: This is a special one, it has no parent, well see that in a minute
* Create mode with permissions (not all permissions are stored in Git)
* You can also run just ``git commit``, then your editor will pop-up
* I did not describe the "why" here, do as I tell you, not as I do (here)

---

## Time to dig deeper

The repository's content must have changed,
commit the changes and go back to the main repository

```shell
$ git add . && git commit -m "Commit file"
[master 85240e8] Commit file
 7 files changed, 4 insertions(+)
 create mode 100644 COMMIT_EDITMSG
 create mode 100644 logs/HEAD
 create mode 100644 logs/refs/heads/master
 create mode 100644 objects/78/d7aa680e7ac5f3e851727ac29dd34afeb766f6
 create mode 100644 objects/a4/4f211c376b94d122c6429ef8e87ffa7856419d
 create mode 100644 refs/heads/master
```
<!-- .element: style="font-size: 0.51em;" -->

![Gitception](https://imgflip.com/s/meme/Serious-Xzibit.jpg)<!-- .element: style="width: 150px; transform: scalex(-1);" -->

Notes:
* The COMMIT_EDITMSG is used to store the message of the commit
* The logs are not discussed in this workshop, they become handy when branches are lost
* References (or refs here) are discussed later, see the ``master`` there?
* Notice: One of the objects has the same hash as the previously made commit

---

## Commit objects!

What is the object with the commit's hash?
```shell
$ git cat-file -t 78d7aa6
commit
```
```shell
$ git cat-file -p 78d7aa6
tree a44f211c376b94d122c6429ef8e87ffa7856419d
author Pablo Escodebar <escodebar@gmail.com> 1533199402 +0200
committer Pablo Escodebar <escodebar@gmail.com> 1533199402 +0200

Describe the training
```
...so this is what a commit looks like!

Notes:
* Git commits in objects as well
* The author and the committer are not necessarily the same person
* The first commit (also called root) has no parent
* Other commits are seen later in during the training

---

## Tree objects!

What is the object with the tree's hash?
```shell
$ git cat-file -t a44f211
tree
```

```shell
$ git cat-file -p a44f211
100644 blob b27501ade65f39bc91a5e6eb0d707903ba225a00	README.md
```
<!-- .element: style="font-size: 0.545em;" -->

...it's collection of references to objects!

Notes:
* The tree is an object containing references to the blobs (or other trees)
* The tree also stores the permissions and the names of the files, but you can't set all permissions!
* "Lost" objects can be found in the repository by looking by the date of creation using scripts

By now, you know more about Git internals than many who consider themselves proficient in Git.

---

## What was the last commit?

Take a look at a change using:
```shell
$ git show
commit 78d7aa680e7ac5f3e851727ac29dd34afeb766f6 (HEAD -> master)
Author: Pablo Escodebar <escodebar@gmail.com>
Date:   Thu Aug 2 10:43:22 2018 +0200

    Describe the training

diff --git a/README.md b/README.md
new file mode 100644
index 0000000..b27501a
--- /dev/null
+++ b/README.md
@@ -0,0 +1 @@
+# My awwwesome training
```
<!-- .element: style="font-size:0.5em;" -->

Notes:
* If no argument is passed, the commit currently checked out will be shown
* See ``HEAD``, ``master``, etc.? We met these already
* We will discuss ``HEAD`` in a couple of slides
* ``master`` is a branch, branches are discussed later
* More details about commits are discussed in a few slides
* A commit hash can be passed to the show command to show a specific commit

---

## Add in patch mode

...to select the changes you want to stage
```shell
$ echo 'This training will make you better!' >> README.md && git add -p
diff --git a/README.md b/README.md
index b27501a..22d2d62 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,2 @@
 # My awwwesome training
+This training will make you better!
Stage this hunk [y,n,q,a,d,/,e,?]?
```
<!-- .element: style="font-size: 0.485em;" -->

```shell
$ git commit -m "Motivate the participant"
[master 113b2fe] Motivate the participant
 1 file changed, 1 insertion(+)
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

---

## How does the new commit look like?

This second commit shouldn't be a root commit:
```shell
$ git cat-file -p 113b2fe
tree 10d06a676fb65acc4b1a2e57454039d904318393
parent 78d7aa680e7ac5f3e851727ac29dd34afeb766f6
author Pablo Escodebar <escodebar@gmail.com> 1534533899 +0200
committer Pablo Escodebar <escodebar@gmail.com> 1534533899 +0200

Motivate the participant
```
...it has a parent!

Notes:
* Think of the graph we saw before, every commit (with exception of root commits) point to another commit

---

## Commit in patch mode

My favorite way of committing!
```shell
$ echo "Buy me a beer if it made you better." >> README.md
$ git commit -p -m "Motivate the speaker"
diff --git a/README.md b/README.md
index 22d2d62..3f652ed 100644
--- a/README.md
+++ b/README.md
@@ -1,2 +1,3 @@
# My awwwesome training
 This training will make you better!
+Buy me a beer if it made you better.
Stage this hunk [y,n,q,a,d,/,e,?]?
```

Once all hunks are decided, a commit will be created
```shell
[master a894a8e] Motivate the speaker
 1 file changed, 1 insertion(+)
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
$ git log --oneline
a894a8e (HEAD -> master) Motivate the speaker
113b2fe Motivate the participant
78d7aa6 Describe the training
```
...so this is why we want short commit titles?

Notes:
* The newest commits are displayed on top
* Without the ``--oneline`` flag, each commit would use several lines
* We have a branch (called ``master``) with three commmits.
* This command is one of the reasons to choose short, meaningful commit titles

---

## Commit the repository's changes

Add the new objects to the repository's repository:
```shell
$ git add . && git commit -m "Add two more commits in patch mode"
[master 9b01029] Add two more commits
 11 files changed, 7 insertions(+), 2 deletions(-)
 create mode 100644 objects/10/d06a676fb65acc4b1a2e57454039d904318393
 create mode 100644 objects/11/3b2feae77a409de1c17d0c400490ac49b6a348
 create mode 100644 objects/22/d2d6223474b8b442b8aae05d4deab6f57a4a2a
 create mode 100644 objects/38/52d81df67551ce4174a25ce844cf690499f55c
 create mode 100644 objects/3f/652ededa8ed2a054ffa2c02bb34f99b53e94dd
 create mode 100644 objects/a8/94a8e197ea8e5a59323522ac9549a5f974f483
```
<!-- .element: style="font-size: 0.465em;" -->

![Gitception](https://imgflip.com/s/meme/Serious-Xzibit.jpg)<!-- .element: style="width: 150px;" -->

Notes:
* This is just keep the working directory clean, for better understanding the next steps

Questions:
* Why do we have 6 objects?

---

# Time for questions

---

![Graph theory](https://imgs.xkcd.com/comics/collatz_conjecture.png)

Notes:
Take a look at the graph in the comic:
* It is a directed graph
* No number appears twice
* There are no loops... it could be a valid graph of a Git repository.
* Each node in the comic could correspond to a commit
* No matter where you start, if you follow the arrows, you'll always finish at one!

Let's build such a graph!

---

## A branch

aka. *a reference*

"*References are pointers to commits.*"

* simplify complex workflows.
* allow to group the logic of a feature.
* allow to work in parallel on several features.

Notes:

Goal:
* Creating branches with diverging commits
* Add the changes of a branch to an other branch
* There are also other references: tags

---

## Create a branch

Branches are created using
```shell
$ git branch pe/new_branch
```

Notes:
* There are naming conventions for branches
* Prefix branches with your initials, to tell others not to touch it
* Reference the issue in the name if the branch is related to it
* If the branch name looks like a folder path, Git will create folders
* To work on a branch you need to check it out
* ``git checkout`` can also be to checkout commits
* Take a look at ``checkout``'s documentation

---

## Digging again!

How are branches stored in the repository?

```shell
$ git add . && git commit -m "Add a new branch"
[master ffce5ba] Add a new branch
 2 files changed, 2 insertions(+)
 create mode 100644 logs/refs/heads/pe/new_branch
 create mode 100644 refs/heads/pe/new_branch
```
```shell
$ cat refs/heads/pe/new_branch
a894a8e197ea8e5a59323522ac9549a5f974f483
```

![Gitception](https://imgflip.com/s/meme/Serious-Xzibit.jpg)<!-- .element: style="width: 150px; transform: scalex(-1);" -->

Notes:
* The logs are discussed in a more advanced training
* The logs are useful to find "lost" commits / branches

---

## Remember git show?

A branch is just a file with the hash of a commit
```shell
$ git show a894a8e197ea8e5a59323522ac9549a5f974f483
commit a894a8e197ea8e5a59323522ac9549a5f974f483 (HEAD -> pe/new_branch, master)
Author: Pablo Escodebar <escodebar@gmail.com>
Date:   Thu Aug 2 10:46:30 2018 +0200

    Motivate the speaker

diff --git a/README.md b/README.md
index 22d2d62..3f652ed 100644
--- a/README.md
+++ b/README.md
@@ -1,2 +1,3 @@
 # My awwwesome training
 This training will make you better!
+Buy me a beer if it made you better.
```
<!-- .element: style="font-size: 0.44em" -->

...that's why creating branches is so fast!

Notes:
* Deleting branches shouldn't scare you anymore!
* If you accidentally delete a branch, checkout the commit and create a new branch from that commit

Statistics:
* Who is experienced with branches in other VCS?

---

## Checkout the newly created branch

To checkout a branch, run:
```shell
$ git checkout pe/new_branch
Switched to branch "pe/new_branch"
```

---

## Create and checkout branches
## ...in one step!

Check out a *new* branch using checkout:
```shell
$ git checkout -b pe/add_list_of_favorite_beers master
Switched to branch "pe/add_list_of_favorite_beers"
```
...one command is faster than two!

Notes:
* If you leave the starting point, the current HEAD is used
* Read the commands documentation, it is very useful (similar to the reset command)
* `git checkout` might require some runtime, depending on the size of the files to be copied

---

## Add a commit to the new branch

```shell
$ cat << EOBL > beers.md && git add beers.md
* To Øl - 1 ton of Happiness
* Rokki - Muikea
* Felsenau - Bärner Müntschi
* Rokki - Happo
* Egger - Galopper
EOBL
$ echo "My list of [favorite beers](beers.md)." >> README.md
$ git commit -a -m "Let people know, what beer to buy"
[pe/add_list_of_favorite_beers 000ce0a] Let people know, what beer to buy
 2 files changed, 6 insertions(+)
 create mode 100644 beers.md
```
<!-- .element: style="font-size: 0.485em;" -->

Notes:
* The first command creates and adds a file called "beers.md" (take a minute to digest it)
* the ``-a`` flag commits adding all *tracked* and modified files to the staging area!

---

## Create another branch

...with another commit

```shell
$ git checkout -b pe/whiskey_is_also_an_option master
Switched to branch "pe/whiskey_is_also_an_option"
```
```shell
$ echo "Whiskey is also a good reward." >> README.md
$ cat << EOWL > whiskeys.md && git add whiskeys.md
* Lagavulin - 16
* Ledaig - 10
* Talisker - Storm
* Ledaig - 18
* Laphroaig - Quarter Cask
EOWL
$ echo '[These whiskeys](whiskeys.md) are great!' >> README.md
$ git commit -am "Accept whiskey as reward"
[pe/whiskey_is_also_an_option 68f2339] Accept whiskey as reward
 2 files changed, 7 insertions(+)
 create mode 100644 whiskeys.md
```

Notes:
* Now we should have a graph with two branches.
* Could you draw the graph of our Git repository?

---

## What a beautiful tree

Take a look at the graph of the repository using:
```shell
$ git log --oneline --all --graph
* 68f2339 (HEAD -> pe/whiskey_is_also_an_option) Accept whiskey as reward
| * 000ce0a (pe/add_list_of_favorite_beers) Let people know, what beer to buy
|/
* a894a8e (pe/new_branch, master) Motivate the speaker
* 113b2fe Motivate the participant
* 78d7aa6 Describe the training
```
<!-- .element: style="font-size: 0.46em;" -->
Our tree starts growing branches!

Notes:
* Using ``--all`` you can display commits of other branches as well.
* The graph a little bit more hard to read: the lines represent connections

---

## Clean up!

We do not want to have uncommitted changes!
```shell
$ git add . && git commit -m "Add branches with commits"
[master ccc7056] Add braches with commits
 16 files changed, 22 insertions(+), 12 deletions(-)
 create mode 100645 logs/refs/heads/pe/add_list_of_favorite_beers
 create mode 100644 logs/refs/heads/pe/whiskey_is_also_an_option
 create mode 100644 objects/00/0ce0a9703aebd0722e2ac3f285985b6b223312
 create mode 100644 objects/0d/f4281955475551ad1a4232fce76a5fb6d340d0
 create mode 100644 objects/21/990ee9610d1601649ca9c669f7f51ecad5358b
 create mode 100644 objects/68/f2339b23c674d3b288411a9754991145883e56
 create mode 100644 objects/7e/c764e3ac5af8a360fc2df5ac5c58aa5bffcd11
 create mode 100644 objects/9c/8d69a8414db1654a6c725de0c670fa28df33a4
 create mode 100644 objects/a2/8e0af61a8785cfec49e2ea707f8172d4b93b78
 create mode 100644 objects/d3/719373bb86bdd46c56e521135a1bd7f69d40ab
 create mode 100644 refs/heads/pe/add_list_of_favorite_beers
 create mode 100644 refs/heads/pe/whiskey_is_also_an_option
```
<!-- .element: style="font-size: 0.5em;" -->

![Gitception](https://imgflip.com/s/meme/Serious-Xzibit.jpg)<!-- .element: style="width: 150px;" -->

Notes:
* Now we are ready to go!

Questions:
* Where do all these objects come from?

---

![Git](https://assets.amuniversal.com/ddf1fa20315201378d0e005056a9545d)

Notes:
* There are several ways and workflows to achieve this.
* Conflicts often arise when combining changes of several files.
* You need to chose the workflow according to your projects' needs and developers' skills.

We created branches with diverging history, to simulate common situations.

---

## Adding features of a branch
## to another branch

---

## Wait... What?

# Conflicts?!

Notes:
* Conflicts happen when a file is changed and it is not obvious (to Git) how the changes should be applied
* The changes introduced to our branches were chosen to raise conflicts
* In many cases, git deals with the conflicts itself

---

## Git merge

![merge](https://wac-cdn.atlassian.com/dam/jcr:83323200-3c57-4c29-9b7e-e67e98745427/Branch-1.png?cdnVersion=lj) <!-- .element: height="380px" style="background: white;" -->


Join development histories

Notes:
* This results in a forked (non-linear) commit-history.
* Adds a merge-commit to the history
* Several branches can be merged at once

---

## Let's merge

Checkout a new branch for the merge
```shell
$ git checkout -b pe/merging pe/add_list_of_favorite_beers
Switched to a new branch "pe/merging"
```

Merge...
```shell
$ git merge pe/whiskey_is_also_an_option
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```
<!-- .element: style="font-size: 0.545em;" -->
...and run into conflicts!

Note:
* A new branch is not required, this just keeps the previous branches intact

---

## Merge conflicts are fun!

How does Git handle merge conflicts?
```shell
$ git add . && git commit -m "Commit during merge conflict"
[master cc2485f] Commit during merge conflict
 10 files changed, 14 insertions(+), 1 deletion(-)
 create mode 100644 MERGE_HEAD
 create mode 100644 MERGE_MODE
 create mode 100644 MERGE_MSG
 create mode 100644 ORIG_HEAD
 rewrite index (100%)
 create mode 100644 logs/refs/heads/pe/merging
 create mode 100644 objects/74/53e34d766307d5056d804f80e4cc2395fb4179
 create mode 100644 refs/heads/pe/merging
```
<!-- .element: style="font-size: 0.505em" -->

A further object?

![Gitception](https://imgflip.com/s/meme/Serious-Xzibit.jpg)<!-- .element: style="width: 150px; transform: scalex(-1);" -->

Notes:
* The MERGE_HEAD points to pe/whiskey_is_also_an_option's tip commit
* ORGI_HEAD points to pe/add_list_of_favorite_beers' tip commit
* The MERGE_MODE is not discussed here
* Take a look at the MERGE_MSG if you feel like it
* Also a new object is added for every conflicting file

---

## Take a look at that object!

We are getting used to this!
```shell
$ git cat-file -t 7453e34
blob
$ git cat-file -p 7453e34
# My awwwesome training
This training will make you better!
Buy me a beer if it made you better.
<<<<<<< HEAD
My list of [favorite beers](beers.md).
=======
Whiskey is also a good reward.
[These whiskeys](whiskeys.md) are great!
>>>>>>> pe/whiskey_is_also_an_option
```

Looks like the README file

Notes:
* Git stores conflicting files in objects as well
* The conflicting part is marked by <<<<<<<, ======= and >>>>>>>

---

## What's the status?

Let's take a look at the status:
```shell
$ git status
On branch pe/merging
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Changes to be committed:

        new file:   whiskeys.md

Unmerged paths:
  (use "git add <file>..." to mark resolution)

        both modified:   README.md
```
As expected, a file was modified by both branches!

Notes:
* ``README.md`` is modified by both branches, such that Git cannot tell how the changes should be merged.
* Git is telling you what to do: either fix the conflicts or abort the merge

---

## Conflict resolution

Take a look at the conflicting files:
```shell
$ git diff
diff --cc README.md
index d371937,a28e0af..0000000
--- a/README.md
+++ b/README.md
@@@ -1,4 -1,5 +1,9 @@@
  # My awwwesome training
  This training will make you better!
  Buy me a beer if it made you better.
++<<<<<<< HEAD
 +My list of [favorite beers](beers.md).
++=======
+ Whiskey is also a good reward.
+ [These](whiskeys.md) are great!
++>>>>>>> pe/whiskey_is_also_an_option
```

This conflict is easily solved!

Notes:
* To resolve a conflict, edit the conflicting files such that it fits the requirements of both changes
* I would consider testing the application after the conflicts are resolved before finish merging

---

## Finish merging

...once you resolved the conflicts:
```shell
$ git add README.md
$ git commit -m "Add the list of beers first"
[pe/merging 3a1f82c] Add the list of beers first
```
That was easy!

Notes:
* Depending on the complexity of the merge, you may consider studying the commits of both branches
* If the commit messages are of good quality, understanding the changes won't be a big deal
* if the commit messages are bad, I suggest you contact the author(s) of the conflicting changes

---

## Take a look at the merge commit

Merge commits are special...
```shell
$ git cat-file -t 3a1f82c
commit
$ git cat-file -p 3a1f82c
tree d5a29e72348dd06004654c605f561d7d6fc32e6c
parent 000ce0a9703aebd0722e2ac3f285985b6b223312
parent 68f2339b23c674d3b288411a9754991145883e56
author Pablo Escodebar <escodebar@gmail.com> 1534559548 +0200
committer Pablo Escodebar <escodebar@gmail.com> 1534559548 +0200

Add the list of beers first
```
...since they have more than one parent!

Notes:
* This makes error analysis a little bit more complex
* You need to follow up the changes of several parents now when looking for errors
* This can be accomplished by using ^1, ^2 or ^N (to reach the N-th parent)

---

## Clean up!

Commit the changes into the repository's repository
```shell
$ git add . && git commit -m "Add the merge"
[master 5dbb9d5] Add the merge
 11 files changed, 8 insertions(+), 7 deletions(-)
 delete mode 100644 MERGE_HEAD
 delete mode 100644 MERGE_MODE
 delete mode 100644 MERGE_MSG
 rewrite index (100%)
 create mode 100644 objects/3a/1f82cf3b89824878b6844f5752a0b28ab95284
 create mode 100644 objects/93/d56bde8cd7e1ac44d1f4f454a189b71b7b0d1f
 create mode 100644 objects/d5/a29e72348dd06004654c605f561d7d6fc32e6c
```
<!-- .element: style="font-size: 0.51em;" -->

The merge files are gone!

![Gitception](https://imgflip.com/s/meme/Serious-Xzibit.jpg)<!-- .element: style="width: 150px;" -->

Notes:
* Take a look at ORIG_HEAD

Questions:
* How many new objects are added?

---

## Git cherry-pick

![cherry pick](https://wac-cdn.atlassian.com/dam/jcr:8d62148d-ba03-4762-bd3a-06ddc465b07f/hero.svg?cdnVersion=jo) <!-- .element: height="300px" style="background: white" -->


Apply the changes introduced by some existing commits

Notes:
* This results in a linear commit-history
* This is not handy if the changes of many commits need to be introduced
* Your working tree needs to be clean
* Merge commits can be cherry-picked! (But you need to specify the mainline)

---

## Pick a cherry

Let's add another branch for cherry picking
```shell
$ git checkout -b pe/cherry_picking pe/add_list_of_favorite_beers
Switched to branch "pe/cherry_picking"
```
<!-- .element: style="font-size: 0.545em;" -->

Find the hash of the cherry (commit) to be picked
```shell
$ git log --oneline pe/whiskey_is_also_an_option
68f2339 (pe/whiskey_is_also_an_option) Accept whiskey as reward
a894a8e (pe/new_branch, master) Motivate the speaker
113b2fe Motivate the participant
78d7aa6 Describe the training
```

---

...then pick it up!
```shell
$ git cherry-pick 68f2339
error: could not apply 68f2339... Accept whiskey as reward
hint: after resolving the conflicts, mark the corrected paths
hint: with "git add <paths>" or "git rm <paths>"
hint: and commit the result with "git commit"
```

Notes:
* The better documented your commits are, the better you can work with them.
* Boom, conflict!

---

## Sweet sweet conflicts

Dig, dig, dig, dig
```shell
$ git add . && git commit -m "Commit a cherry pick conflict"
[master 8bb838d] Commit during cherry pick conflict
 8 files changed, 10 insertions(+), 1 deletion(-)
 create mode 100644 CHERRY_PICK_HEAD
 create mode 100644 MERGE_MSG
 rewrite index (100%)
 create mode 100644 logs/refs/heads/pe/cherry_picking
 create mode 100644 objects/77/047a805c055408b0f9a6ef2a96ef932d677efb
 create mode 100644 refs/heads/pe/cherry_picking
```
<!-- .element: style="font-size: 0.495em" -->

Another object!

![Gitception](https://imgflip.com/s/meme/Serious-Xzibit.jpg)<!-- .element: style="width: 150px; transform: scalex(-1);" -->

Notes:
* This is again the conflicting file

Question:
* Why do we have an other object?

---

## Use a mergetool

...to fix the conflict!

```shell
$ git mergetool

This message is displayed because 'merge.tool' is not configured.
See 'git mergetool --tool-help' or 'git help config' for more details.
'git mergetool' will now attempt to use one of the following tools:
[...] meld [...] vimdiff [...]
Merging:
README.md

Normal merge conflict for 'README.md':
  {local}: modified file
  {remote}: modified file
Hit return to start merge resolution tool (vimdiff):
```
<!-- .element: style="font-size: 0.505em" -->

Conflict resolution with assistance!

---

## A safety net

...in case something went wrong!
```shell
$ git status
On branch pe/cherry_picking
You are currently cherry-picking commit 2fe20c0.
  (all conflicts fixed: run "git cherry-pick --continue")
  (use "git cherry-pick --abort" to cancel the cherry-pick operation)

Changes to be committed:

        modified:   README.md
        new file:   whiskeys.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        README.md.orig

```
<!-- .element: style="font-size: 0.51em" -->


Therefore clean up!
```shell
$ rm README.md.orig
```

Notes:
Also notice, that the README.md file was already added to the staging area.
You can configure Git not to create this backup file.

---

## Finish cherry-picking

```shell
$ git cherry-pick --continue
[pe/cherry_picking b7083bf] Accept whiskey as reward
 Date: Fri Jun 29 19:47:30 2018 +0200
 2 files changed, 7 insertions(+)
 create mode 100644 whiskeys.md
```

---

## Clean up!

Once again...
```shell
$ git add . && git commit -m "Add the cherry-pick"
[master a5f2863] Add the cherry-pick
 8 files changed, 26 insertions(+), 7 deletions(-)
 delete mode 100644 CHERRY_PICK_HEAD
 rewrite COMMIT_EDITMSG (100%)
 delete mode 100644 MERGE_MSG
 rewrite index (100%)
 create mode 100644 objects/b7/083bff4b2604a3d5669cdf73ed3629d53bfcfc
```
<!-- .element: style="font-size: 0.505em;" -->

![Gitception](https://imgflip.com/s/meme/Serious-Xzibit.jpg)<!-- .element: style="width: 150px;" -->

Notes:
* There are only 2 new objects... How many would you expect?

---

## Git rebase

![rebase](https://wac-cdn.atlassian.com/dam/jcr:e4a40899-636b-4988-9774-eaa8a440575b/02.svg?cdnVersion=lj) <!-- .element: height="350px" style="background: white" -->

> Reapply commits on top of another branch<!-- .element: style="font-size: 0.95em;" -->

Notes:
* This generates a linear history-tree without forks
* The golden rule of rebasing: Never rebase a public branch!

---

## Rebase yourself!

```shell
$ git checkout -b pe/rebasing pe/whiskey_is_also_an_option
Switched to branch "pe/rebasing"
```
```shell
$ git rebase pe/add_list_of_favorite_beers
First, rewinding head to replay your work on top of it...
Applying: Let people know, what beer to buy
Using index info to reconstruct a base tree...
M       README.md
Falling back to patching base and 3-way merge...
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
error: Failed to merge in the changes.
Patch failed at 0001 Let people know, what beer to buy
hint: Use 'git am --show-current-patch' to see the failed patch
Resolve all conflicts manually, mark them as resolved with
"git add/rm <conflicted_files>", then run "git rebase --continue".
You can instead skip this commit: run "git rebase --skip".
To abort and get back to the state before "git rebase", run "git rebase --abort".
```
<!-- .element: style="font-size: 0.43em" -->

Notes:
* This time "the point of view" changes, therefore we checkout the branch which will be rebased

---

## Rebasing

...is slightly more complicated:
```shell
$ git add . && git commit -m "Commit a rebase conflict"
[master cd7d697] Commit a rebase conflict
 29 files changed, 79 insertions(+), 2 deletions(-)
 create mode 100644 REBASE_HEAD
 rewrite index (100%)
 create mode 100644 logs/refs/heads/pe/rebasing
 create mode 100644 objects/85/c2d4e6fc7a00c7e49bd1d851f54863fd39605f
 create mode 100644 rebase-apply/0001
 create mode 100644 rebase-apply/abort-safety
 create mode 100644 rebase-apply/apply-opt
 create mode 100644 rebase-apply/author-script
 create mode 100644 rebase-apply/final-commit
 create mode 100644 rebase-apply/head-name
 create mode 100644 rebase-apply/keep
 create mode 100644 rebase-apply/last
 create mode 100644 rebase-apply/messageid
 create mode 100644 rebase-apply/next
 create mode 100644 rebase-apply/onto
 create mode 100644 rebase-apply/orig-head
 create mode 100644 rebase-apply/original-commit
 create mode 100644 rebase-apply/patch
 create mode 100644 rebase-apply/patch-merge-index
 create mode 100644 rebase-apply/quiet
 create mode 100644 rebase-apply/rebasing
 create mode 100644 rebase-apply/scissors
 create mode 100644 rebase-apply/sign
 create mode 100644 rebase-apply/threeway
 create mode 100644 rebase-apply/utf8
 create mode 100644 refs/heads/pe/rebasing
```
<!-- .element: style="font-size:0.5em;" -->

![Gitception](https://imgflip.com/s/meme/Serious-Xzibit.jpg)<!-- .element: style="width: 150px; transform: scalex(-1);" -->

---

## Finish rebasing

...once you resolved the conflicts:
```shell
$ git add README.md && git rebase --continue
Applying: Accept whiskey as reward
```

---

## What about the rebase files?

```shell
$ git add . && git commit -m "Add the rebase"
[master 46da891] Add the rebase
 28 files changed, 5 insertions(+), 75 deletions(-)
 delete mode 100644 REBASE_HEAD
 rewrite index (100%)
 create mode 100644 objects/c9/6224a8837cfd2996396e0e523032e09ebb461a
 delete mode 100644 rebase-apply/0001
 delete mode 100644 rebase-apply/abort-safety
 delete mode 100644 rebase-apply/apply-opt
 delete mode 100644 rebase-apply/author-script
 delete mode 100644 rebase-apply/final-commit
 delete mode 100644 rebase-apply/head-name
 delete mode 100644 rebase-apply/keep
 delete mode 100644 rebase-apply/last
 delete mode 100644 rebase-apply/messageid
 delete mode 100644 rebase-apply/next
 delete mode 100644 rebase-apply/onto
 delete mode 100644 rebase-apply/orig-head
 delete mode 100644 rebase-apply/original-commit
 delete mode 100644 rebase-apply/patch
 delete mode 100644 rebase-apply/patch-merge-index
 delete mode 100644 rebase-apply/quiet
 delete mode 100644 rebase-apply/rebasing
 delete mode 100644 rebase-apply/scissors
 delete mode 100644 rebase-apply/sign
 delete mode 100644 rebase-apply/threeway
 delete mode 100644 rebase-apply/utf8
```
<!-- .element: style="font-size: 0.5em" -->

They are gone!

![Gitception](https://imgflip.com/s/meme/Serious-Xzibit.jpg)<!-- .element: style="width: 150px;" -->

Notes:
* There are only 2 new objects... How many would you expect?

---

# Time for questions

---

![Git log](https://imgs.xkcd.com/comics/git_commit_2x.png)<!-- .element: height="400px" -->

Notes:
* Please do not do this!
* Keep a clean history
* This is important for later code analysis
* Think of the people who will deal with your repository
* Think of the repositories you will deal with
* There are several strategies to clean such a history

---

## Preparing the branch of backups

Add a branch with a few commits
```shell
$ git checkout -b pe/backups pe/rebasing
$ echo "I would also love some feedback." >> README.md
$ git commit -am "Ask for feedback"
[pe/backups c16a824] Ask for feedback
 1 file changed, 1 insertion(+)
$ echo "Personal feedback is the best." >> README.md
$ git commit -am "Ask for personal feedback"
[pe/backups 450dc77] Ask for personal feedback
 1 file changed, 1 insertion(+)
$ echo "Helpful feedback is awarded with great coffee." >> README.md
$ git commit -am "Trade feedback for coffee"
[pe/backups 1603ef5] Trade feedback for coffee
 1 file changed, 1 insertion(+)
```
<!-- .element: style="font-size: 0.52em" -->

Notes:
* You might want to drop a commit or squash several commits

---

## Commit the changes in the repository

```shell
$ git add . && git commit -m "Add the branch of backups"
[master 000b173] Add the branch of backups
 15 files changed, 19 insertions(+), 24 deletions(-)
 rewrite COMMIT_EDITMSG (100%)
 create mode 100644 logs/refs/heads/pe/backups
 create mode 100644 objects/34/96ebedc52ee70e2b129e315084623c7deea6a2
 create mode 100644 objects/44/09126657b95c9c83a73ac6d730ae7353b6aac1
 create mode 100644 objects/4f/56584f94dc324de2c2ffd66b4e145a6912f480
 create mode 100644 objects/58/ad30ba9d86b178e9c878ac031b1217d89ac4a7
 create mode 100644 objects/a9/f13a5d39e490577cca3e7af6a579c15dd9c546
 create mode 100644 objects/ba/1cdecffc9b11e65b5b58077ceeaef2fd417bbf
 create mode 100644 objects/c3/2f3348d4d95fed6ff7c80054daf3690c50e390
 create mode 100644 objects/e3/d06c425b6a61e3c8b97f4343ef4bc15366108f
 create mode 100644 objects/f1/c24400178f30d7f56ac2967d2fd796968197d5
 create mode 100644 refs/heads/pe/backups
```
<!-- .element: style="font-size: 0.5em" -->

![Gitception](https://imgflip.com/s/meme/Serious-Xzibit.jpg)<!-- .element: style="width: 150px; transform: scalex(-1);" -->

---

## Rebasing in interactive mode

"Change" the commit history during rebase!

```shell
$ git checkout -b pe/interactive_rebase pe/backups
Switched to a new branch "pe/interactive_rebase"
$ git rebase -i pe/rebasing
```
<!-- .element: style="font-size: 0.52em" -->

Your editor now lists all the commits of your branch!

Notes:
* This is a really powerful tool to organize the commit history and make it more meaningful

---

```text
pick c16a824 Ask for feedback
pick 450dc77 Ask for personal feedback
pick 1603ef5 Trade feedback for coffee

# Rebase c96224a..1603ef5 onto c96224a (3 commands)
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
#a
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
* The first command cannot be a squash or a fixup!
* Drop, squash, fix up or change the order of the commits as required
* Mastering the interactive rebase is worth a salary raise!
* There are commit commands to create automtic fixup and squash commands!

---

## Commit the changes in the repository

```shell
$ git add . && git commit -m "Rebase in interactive mode"
[master dabfcec] Rebase in interactive mode
 6 files changed, 7 insertions(+), 2 deletions(-)
 create mode 100644 logs/refs/heads/pe/interactive_rebase
 create mode 100644 refs/heads/pe/interactive_rebase
```

![Gitception](https://imgflip.com/s/meme/Serious-Xzibit.jpg)<!-- .element: style="width: 150px; transform: scalex(-1);" -->

Notes:
This output is expected if you only used the command "pick".
If you squashed or fixed up commits, more objects would have been created.

---

## There's a shortcut!

To fix up and squash commits together!

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

---

## But what if

* ...it is more complex?
* ...commits need to be split?
* ...part of a commit sneaked into another commit?

`reset`, `checkout` and `stash` to the help!

Notes:
* The reset and checkout commands are two of the most confusing parts of Git when first encountered
* They do many different things depending on the used arguments
* Once you think you understood them, you will find another usage which will change your concept of these commands completely (or to a big part)
* Let's therefore "demystify" these commands!

---

## The Three Trees

* the HEAD
* the Index
* Working Directory

Notes:
* We took a quick look at these when discussing the index
* HEAD: Last commit snapshot, next parent, what we called "the repository" before.
* Index: Proposed next commit snapshot
* Working directory: Sandbox

---

## Reset vs checkout vs stash

Reset will move what your HEAD is pointing to

Checkout will move your HEAD

Stash will change your index and working directory

Notes:

---

## Reset in detail

The following steps are executed when resetting:

```raw
1. Move the branch HEAD points to (--soft)
2. Make the index look like HEAD (--mixed, default)
3. Make the working directory look like the index (--hard)
```

Notes:
If reset is used with a path, the first step is skipped!

---

## Let's see it in action!

```shell
$ git checkout -b pe/reset pe/backups && git reset pe/rebasing
Switched to a new branch 'pe/reset'
Unstaged changes after reset:
M   README.md
```

```shell
$ git status
On branch pe/reset
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```
<!-- .element: style="font-size: 0.47em;" -->

---

## Let's commit the changes!

```shell
$ git add . && git commit -m "Commit the reset"
[master 3127cce] Commit the reset
 6 files changed, 7 insertions(+), 2 deletions(-)
 create mode 100644 logs/refs/heads/pe/reset
 create mode 100644 refs/heads/pe/reset
```

![Gitception](https://imgflip.com/s/meme/Serious-Xzibit.jpg)<!-- .element: style="width: 150px; transform: scalex(-1);" -->

---

## Create a more meaningful commit

```shell
$ git diff
diff --git a/README.md b/README.md
index 93d56bd..58ad30b 100644
--- a/README.md
+++ b/README.md
@@ -4,3 +4,6 @@ Buy me a beer if it made you better.
 My list of [favorite beers](beers.md).
 Whiskey is also a good reward.
 [These whiskeys](whiskeys.md) are great!
+I would also love some feedback.
+Personal feedback is the best.
+Helpful feedback is awarded with great coffee.
```

```shell
$ git commit -am "Trade coffee for personal feedback"
[pe/reset 08be0f2] Trade coffee for personal feedback
 1 file changed, 3 insertions(+)
```

---

## Commit the changes in the repository

```shell
$ git add . && git commit -m "Reset to improve the log"
[master 2c0f85b] Reset to improve the log
 7 files changed, 10 insertions(+), 3 deletions(-)
 create mode 100644 logs/refs/heads/pe/resetting
 create mode 100644 objects/84/45a59c91529fbb551e2e7e5f9318dd2c144705
 create mode 100644 refs/heads/pe/resetting
```
<!-- .element: style="font-size: 0.51em" -->

![Gitception](https://imgflip.com/s/meme/Serious-Xzibit.jpg)<!-- .element: style="width: 150px; " -->

---

## Checkout in detail

The following steps are executed when checking out:

```raw
1. Try a trivial merge with chosen commit
2. Move the HEAD
3. Make the working directory look like the HEAD
```

But used with a path the following happens:
```raw
1. Make the index look like chosen commit
2. Make the working directory look like the index
```

Notes:
* If checkout is used with a path is not working directory safe!
* This means, that you can use `git checkout -p` to selectively discard edits from your current working tree.

---

## Use the checkout command

...to clean up the backup history

```shell
$ git checkout -b pe/checkingout pe/rebasing
Switched to a new branch 'pe/checkout'
```

```shell
$ git checkout -p pe/backups
diff --git b/README.md a/README.md
index 93d56bd..58ad30b 100644
--- b/README.md
+++ a/README.md
@@ -4,3 +4,6 @@ Buy me a beer if it made you better.
 My list of [favorite beers](beers.md).
 Whiskey is also a good reward.
 [These whiskeys](whiskeys.md) are great!
+I would also love some feedback.
+Personal feedback is the best.
+Helpful feedback is awarded with great coffee.
Apply this hunk to index and worktree [y,n,q,a,d,e,?]? 
```

---

## What did the checkout do?

```shell
$ git status
On branch pe/checkout
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   README.md
```

...it put the files in the index!

---

## Create the new commit

```shell
$ git commit -m "Trade coffee for personal feedback"
[pe/checkout 92fd5bb] Trade coffee for personal feedback
 1 file changed, 3 insertions(+)
```

---

## And what happened in the repository?

```shell
$ git add . && git commit -m "Checkout to improve the log"
[master 3b1465c] Checkout to improve the log
 6 files changed, 4 insertions(+), 2 deletions(-)
 create mode 100644 objects/92/fd5bb1c51339c8fda4f6584543d96b1a19aca2
```
<!-- .element: style="font-size: 0.51em" -->

![Gitception](https://imgflip.com/s/meme/Serious-Xzibit.jpg)<!-- .element: style="width: 150px; " -->

---

## The change stash 

...can also be used for changes which
* are "work in progress"
* do not belong to the current branch
* do not require a commit but need to be kept

---

## Let's see what stash does

Create a new branch
```shell
$ git checkout -b pe/stashing pe/rebasing
Switched to a new branch 'pe/stashing'
```

...and add a change not worth committing
```shell
$ echo "You can use [beerpay](TODO: activate beerpay) to buy me a beer." >> README.md
```
<!-- .element: style="font-size: 0.41em" -->

---

## Put in the stash

...what prevents you from continue working
```shell
$ git stash push -m "Mention beerpay (TODO: activate account)"
Saved working directory and index state On stashing: Mention beerpay (TODO: activate account)
```
<!-- .element: style="font-size: 0.38em" -->

and the working directory is clean again!
```shell
$ git status
On branch pe/stashing
nothing to commit, working tree clean
```

Notes:
Changes in the index which differ from the working directory will not be taken into account.

---

## No muscle soreness yet

...so let's check what happened in the repository:
```shell
$ git add . && git commit -m "Commit the stashed changes"
[master 29f0dc5] Commit the stashed changes
 12 files changed, 10 insertions(+), 2 deletions(-)
 create mode 100644 logs/refs/heads/pe/stashing
 create mode 100644 logs/refs/stash
 create mode 100644 objects/09/935986918f82200d5c17821e30065969cfa0b7
 create mode 100644 objects/71/451e45b521185acf42faf83b5af5e9a2a1a973
 create mode 100644 objects/89/148ed3bf53ccbaada4ec301d3a0a52e7cc7feb
 create mode 100644 objects/e0/413b19ca77279ce47926db500dad21578e439d
 create mode 100644 refs/heads/pe/stashing
 create mode 100644 refs/stash
```
<!-- .element: style="font-size: 0.51em" -->
![Gitception](https://imgflip.com/s/meme/Serious-Xzibit.jpg)<!-- .element: style="width: 150px; transform: scalex(-1);" -->

---

## Getting stashed changes back

...as soon as you need them
```shell
$ git stash list
stash@{0}: On stashing: Mention beerpay (TODO: activate account)
```

```shell
$ git stash pop
On branch pe/stashing
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (89148ed3bf53ccbaada4ec301d3a0a52e7cc7feb)
```
<!-- .element: style="font-size: 0.47em" -->

Notes:
If you want to keep the change in the stash for later use, you can use "apply" instead of "pop"

---

## No blisters either

...so check the repository again!
```shell
$ git add . && git commit -m "Commit the stash pop"
[master ad59e16] Commit the stash pop
 3 files changed, 2 deletions(-)
 delete mode 100644 logs/refs/stash
 delete mode 100644 refs/stash
```
![Gitception](https://imgflip.com/s/meme/Serious-Xzibit.jpg)<!-- .element: style="width: 150px;" -->

---

# Time for questions

---

## Connect other repositories

...by declaring them as your remote

```shell
$ git remote add origin git@github.com/escodebar/awwwesome.git
```

---

## How are remotes stored in the repository?

```shell
$ git add . && git commit -m "Add the origin remote"
```

---

## Push the objects to the remote

```shell
$ git push -u origin --all
```

---

## See the new references?

```shell
$ git add . && git commit -m "Push everything to the remote"
```

---

## Local branches?

What do we need them for? We have the references in the remote!

```shell
$ git checkout origin/master && git branch | xargs git branch -D 
```

Now we're in detached `HEAD`!

---

## Automatize tasks using hooks

---

## Prevent hidden hidden commits

...by using the fetch command

---

## Resources
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
