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
* At the last SoCraTes unconference in Ftan I rushed through the training
* Then we decided to host this meetup
* It is going to be tough (for all of us) but rewarding
* I hope you do not mind the bad jokes

---

## Schedule

* Gitception: Reaching into the substructure
* Of trees, branches and pieces of fruit
* It's a backup system... It's a patch system... It's Git!

Notes:
* Gitception
  - is about using Git to understand Git and understanding the structure of Git
  - The concept of Gitception is used throughtout the training
* The second block introduces
  - Git's branching mechanism
  - combining changes implemented in branches
* The last block treats in more detail:
  - how to create patches using Git
  - cleaning up the Git history before a feature is released
* I do not know yet if we can go through these 3 blocks within 3 hours (including questions)
* I expect to discuss each block in within 40 minutes leaving around 15 minutes for questions
* I prefer answering questions between the blocks rather than rushing through it
* I consider hosting a second event if the interest is high and we do not make it through or interesting questions remain unanswered

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

Notes:
* The slides are updated from time to time
* You can find the speaker notes in the slides, which allows you to go through the training at home (without forcing you to hear my annoying voice)
* Pass the slides to your coworkers, your friends, etc., the more people understand Git better
* If a slide needs clarification, please let me know!

---

# Are you ready?

---

![Git](https://imgs.xkcd.com/comics/git_2x.png)<!-- .element: height="500px" -->

Notes:
* The goal of this meetup is to show what Git does when it is used, to allow you to choose when and how to use it
* I don't will not impose a workflow, it's up to you how you use Git
* My goal is to empower you to chose how you are going to use Git
* This training covers theory for using Git, however brain muscle (training) is needed
* If you want more training and need help, do not hesitate to contact me
* Use and learn *all* the commands and ask yourself how they may help you improveing your workflows
* This meetup is made for people who did not use Git in depth before, but includes information for more experencied users
* This meetup covers using Git when there is no *happy path*
* Some parts of this training are rather technical and go deep into Git's internals
* It also introduces a method to learn Git by your own

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

Questions:
* Who has taken a look into the `.git` before?

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
* Therefore we can create a repository in the repository to track the changes and understand Git's behaviour
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
* You can tell Git to ignore files using ``.gitignore``, then they won't be listed in the "Untracked files" section
* Ignore large files and non-project specific files (well... this depends on what you're using Git for):
  - backup files
  - binary files
  - data files
  - system specific files (like .DS_Store, or local configurations)
  - files containing (personal) passwords (move passwords to enivornment variables and use the environment variables)
* We want to track changes to the current untracked file!
* The amount of output displayed by Git can be configured!

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
  - ...take a look what you are going to eat

---

## Let's stage!

Put files in the staging area:
```shell
$ {{ "git add README.md && git status"|multirun }}
```

Notes:
* The file is now in the ``changes to be committed``
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

Questions:
* What happens if I change the file and add it again? [A new object is created]
* What happens to the previous object? [It remains in the repository until it is garbage collected]

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
* Think of the fork metaphore... do you want to eat a bad pea? or a bug?
* Make commits as small as possible for easier reviewing, the easier the review, the less errors will slip through
* If keeping track of what it's being committed is hard, then you might need to rethink your workflow

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
* If a commit is not complete, you might want to stash the changes instead or the title can be provided with a [WIP]
* If you have a test driven workflow, you may commit the test first and then the rest, but then mark, the test as expected to fail or not implemented

---

## Save the changes

...by commiting them to the repository
```shell
$ {{ 'git commit -m "Describe the training"'|run }}
```

Notes:
* `master` is the default branch name by default
* `root-commit`: This is a special one, it has no parent, well see that in a minute
* `{{ "HEAD"|commit_hash }}` is part of the hash of the commit
* Git tells you the the number of files changed, lines insterted or deleted
* Create mode with permissions (not all permissions are stored in Git)
* You can also run just `git commit`, then your editor will pop-up
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
* The COMMIT_EDITMSG is used to temporarily store the message of the commit
* The logs are keep track of the commit hashes the references pointed to, they become handy when branches are lost (more about this later)
* There is also a log for the `HEAD` (more about the `HEAD` later)
* References (or refs here) are discussed later - see the `master` there again?
* One of the objects has the same hash as the previously made commit
* ...and look! Two more objects! One containing starting with the hash of the last commit!

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
* Then add them and commit them
* This way of adding changes to the index requires some training until you feel comfortable

---

## How does the new commit look like?

This second commit shouldn't be a root commit:
```shell
$ {{ "git cat-file -p LAST_COMMIT"|run }}
```
...it has a parent!

Notes:
* Every commit (with exception of root commits) point to (at least) another commit

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

Questions:
* Why do we have 6 objects? [2 commits, 2 trees and 2 blobs]

---

# Time for questions

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
* Each node in the comic could correspond to a commit

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

## Now let's check, check, check it out!

```shell
$ {{ "git checkout pe/new_branch"|run }}
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

## Create and checkout branches
## ...in one step!

Switch to a *new* branch using checkout:
```shell
$ {{ "git checkout -b pe/add_list_of_favorite_beers master"|run }}
```
...one command is faster than two!

Notes:
* If you leave the starting point (`master` here), the current `HEAD` is used
* `git checkout` is criticized to be overloaded with functionality, we are discussing this in more detail later
* `git checkout` might require some runtime, depending on the size of the files to be copied

Now that we know how to create branches, let's create two with conflicting changes!

---

## Wait... What?

# Conflicts?!

Notes:
* Conflicts happen when a file is changed and it is not obvious (to Git) how the changes should be applied
* There are also silent conflicts... let's discuss these later
* Let's introduce a change to our branch to provoque a conflict

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
$ {{ "git checkout -b pe/whiskey_is_also_an_option master"|run }}
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

Questions:
* Where do all these objects come from? [2 commits, 2 trees, 2 new blobs, 2 changes to `README`]

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

![Git](https://assets.amuniversal.com/ddf1fa20315201378d0e005056a9545d)

Notes:
* We are discussing how to add changes of branch to another branch
* There are several ways and workflows to achieve this
* Conflicts often arise when combining changes of several files
* You need to chose the workflow according to your projects' needs and developers' skills

We created branches with diverging history, to simulate common situations.

---

## Git merge

![merge](https://wac-cdn.atlassian.com/dam/jcr:83323200-3c57-4c29-9b7e-e67e98745427/Branch-1.png?cdnVersion=lj) <!-- .element: height="380px" style="background: white;" -->


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
$ {{ "git checkout -b pe/merging pe/add_list_of_favorite_beers"|run }}
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
$ {{ "git checkout -b pe/cherry_picking pe/add_list_of_favorite_beers"|run }}
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
$ {{ "git checkout -b pe/rebasing pe/whiskey_is_also_an_option"|run }}
```
```shell
$ {{ "git rebase pe/add_list_of_favorite_beers"|run }}
```
<!-- .element: style="font-size: 0.43em" -->

...that's a lot of output!

Notes:
* This time "the point of view" changes, therefore we checkout the branch which will be rebased
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
$ {{ "sed -i '4d;6d;$d' README.md && git add README.md && git rebase --continue"|multirun }}
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
$ {{ "git checkout -b pe/backups pe/rebasing"|run }}
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
$ {{ "git checkout -b pe/interactive_rebase pe/backups"|run }}
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

* the `HEAD`
* the index
* Working Directory

Notes:
* The `HEAD` is the last commit (also the next parent), what we called "the repository" before
* The index is the proposed next commit, what's on our fork
* The working directory is our sandbox

---

![The three trees](https://git-scm.com/book/en/v2/images/reset-workflow.png)

Notes:
* We saw a similar image before

---

## Reset vs checkout vs stash

* Reset will move what your `HEAD` is pointing to
* Checkout will move your `HEAD`
* Stash will move your index and change the working directory

Notes:
* This is the general case
* Depending on the options passed to these commands, these will behave differently
* Let's discuss these therefore in detail

---

## Reset in detail

The following steps are executed when resetting:

```raw
1. Move the branch HEAD points to (--soft)
2. Make the index look like HEAD (--mixed, default)
3. Make the working directory look like the index (--hard)
```

[Here's a less compact explanation!](https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified)

Notes:
If reset is used with a path, the first step is skipped! Read the link for more information

---

## Let's see it in action!

Create a new branch
```shell
$ {{ "git checkout -b pe/reset pe/backups"|run }}
```

...and reset to where your "backup history" starts
```shell
$ {{ "git reset pe/rebasing"|run }}
```

Notes:
* The `README` is now modified?

---

## What's the status now?

```shell
$ {{ "git status"|run }}
```
<!-- .element: style="font-size: 0.47em;" -->

...but we did not modify anything?

---

## What's modified?

```shell
$ {{ "git diff"|run }}
```

All the changes from the `backups` branch are now in the working directory!

Notes:
* `git reset` will not change your working directory (unless you use the `--hard` option)
* The `HEAD` (and index) now differs from the working directory
* Therefore the `README` looks modified to Git

---

## So what happened? 

```shell
$ {{ 'git add . && git commit -m "Commit the reset"'|multirun(gitception=True) }}
```

...this is not enough information!

{% filter gitception %}{% endfilter %}

---

## Let's take a closer look!

```shell
$ {{ "git show --name-only"|run(gitception=True) }}
```

{% filter gitception %}{% endfilter %}

Notes:
* The `HEAD` changed, since that's what `git reset` does
* The `ORIG_HEAD` contains a reference to where the branch was pointing to before the reset
* The index was changed to match the `HEAD`
* The logs contain information about the changes to `HEAD` and `pe/reset`

---

## Let's look even closer!

```shell
$ {{ "cat ORIG_HEAD"|run(gitception=True) }}
```
This is the last commit in the `pe/backups` branch!

```shell
$ {{ "cat logs/refs/heads/pe/reset"|run(gitception=True) }}
```
These where `pe/reset` pointed to

{% filter gitception %}{% endfilter %}

Notes:
* Please take also a look at `logs/HEAD`, it will contain similar information as `pe/reset`

---

## (

You can access this information using
```shell
$ {{ "git reflog pe/reset"|run }}
```
...parsing it for readability

## )

Notes:
* Who used `git reflog` before?

---

## Create a new commit

...by commiting the change
```shell
$ {{ 'git commit -am "Trade coffee for personal feedback"'|run }}
```
with a more meaninful message.

Notes:
* You could also chose to "git commit -C <existing_commit>" to prevent rewriting the commit message
* You can also make more than one commit
* Use `git reflog`s information to restore the branch if you need to

---

## Commit the changes in the repository

```shell
$ {{ 'git add . && git commit -m "Reset to improve the log"'|multirun(gitception=True) }}
```
<!-- .element: style="font-size: 0.51em" -->

{% filter gitception %}{% endfilter %}

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
* `git checkout` is criticized to be overloaded with functionality
* Depending on the options it will behave in a different way, making it hard to understand
* Yet it is a very handy tool!
* If checkout is used with a path is not working directory safe!
* This means, that you can use `git checkout -p` to selectively discard edits from your current working tree

---

## Using the checkout command

...to clean up the backup history

```shell
$ {{ "git checkout -b pe/checkingout pe/rebasing"|run }}
```

Notes:
This is similar to what we did with `git reset`:
We go to the point from where we want to rewrite the history

---

## Checkout the changes

...which you want to commit
```shell
$ {{ "git checkout -p pe/backups"|run(input="y") }}
```

Notes:
* The difference to `git reset` is that we created a new branch, leaving the previous instact

---

## What did the checkout do?

```shell
$ {{ "git status"|run }}
```

...it put the files in the index!

Notes:
* Checkout (in patch mode) makes the index (and the working directory) look like the checked out change

---

## Create the new commit

```shell
$ {{ 'git commit -m "Trade coffee for personal feedback"'|run }}
```

Notes:
* You can checkout changes from several branches, joining changes into a single branch

---

## And what happened in the repository?

```shell
$ {{ 'git add . && git commit -m "Checkout to improve the log"'|multirun(gitception=True) }}
```
<!-- .element: style="font-size: 0.51em" -->

{% filter gitception %}{% endfilter %}

Notes:
* All in all, this is pretty similar to using the reset command to clean up the history

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
$ {{ "git checkout -b pe/stashing pe/rebasing"|run }}
```
...as we did in the other steps

---

## Add changes not worth committing

```shell
$ {{ 'echo "[Beerpay](TODO: activate beerpay) is cool!" >> README.md'|shell }}
```

Let's have some fun staging part of it
```shell
$ {{ "git add README.md"|run }}
```

...and keeping another part in the working directory
```shell
$ {{ 'echo "I also love mechanical keyboards" >> README.md'|shell }}
```

---

## Put in the stash

...what prevents you from continue working
```shell
$ {{ 'git stash push -m "WIP beerpay"'|run }}
```

and the working directory is clean again!
```shell
$ {{ "git status"|run }}
```

Notes:
Changes in the index which differ from the working directory will not be taken into account.

---

## No muscle soreness yet

...so let's check what happened in the repository:
```shell
$ {{ 'git add . && git commit -m "Commit the stashed changes"'|multirun(gitception=True) }}
```
<!-- .element: style="font-size: 0.51em" -->

6 new objects?! But we only changed one file!

{% filter gitception %}{% endfilter %}

Notes:
Feel free to use `git cat-file` to see the contents of these objects.
There is a:
* Commit, tree and blob for the state of the index
* Commit, tree and blob for the state of the working directory

---

## Getting stashed changes back

...as soon as you need them
```shell
$ {{ "git stash list"|run }}
```

```shell
$ {{ "git stash pop"|run }}
```
<!-- .element: style="font-size: 0.5em" -->

Notes:
* If you want to keep the change in the stash for later use, you can use "apply" instead of "pop"
* Take a closer look at the output, part of it is equivalent to `git status`
* The index changed, it does not contain the changes added before
* Git will try to reconstruct the index when using "git stash pop" and "git stash apply"
* But under certain circumstances, Git will not set the index

---

## No blisters either

...so check the repository again!
```shell
$ {{ 'git add . && git commit -m "Commit the stash pop"'|multirun(gitception=True) }}
```

{% filter gitception %}{% endfilter %}

---

## Combining them all!

You can use

`git checkout` and `git stash`

during a `git rebase -i`

Notes:
* BOOM!

---

# Time for questions

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

🍺🍻🍺
