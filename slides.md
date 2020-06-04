---
theme: league
title: Gitception @ TechTalkThursday
revealOptions:
    transition: 'fade'
---

# Gitception

a different approach to learning Git

Notes:
* I want to make this a fun experience for all of us!

---

## Agenda

* Whois
* Gitception?
* Applying the concept
  - Git objects
  - Git branches

---

## Who am I?

![Pablo](pablo.png)<!-- .element: height="300px" width="300px" -->

Notes:
* Work as a Software Engineer for DECTRIS
* I also help organizations and individuals understanding Git
* Today I want to present one of the concepts I use in my workshops

----

## Who is Coders Only?

![Coders Only](codersonly.png)<!-- .element: height="300px" width="300px" -->

Notes:
* Association which promotes concepts and methods out of the field of software development within Switzerland
* Coders Only organizes events like the
  - Coders Monthly
  - Global day of Coderetreat
  - SoCraTes Day Switzerland
* Visit our website or contact us if you want to become a member or support us 

---

## What is Gitception?

Gitception is the idea of putting your Git repository in a Git repository to see what Git does when Git is used.
<!-- .element: class="fragment" -->

Notes:
* I was asked to give a full day introduction to Git for a CAS
* I prepared a training trying to add something useful for several levels of Git knowledge
* The intended audience was PhD students with basic to no Git experience and technicians
* I learned a lot while preparing the training
* The training was very successful, receiving a lot of good feedback
* The concept of Gitception was considered a power move

----

![Git](why.jpg)<!-- .element: height="500px" -->

----

![Git](https://imgs.xkcd.com/comics/git_2x.png)<!-- .element: height="500px" -->

Notes:
* Roughly 1/20 of the participants of my trainings just want to know "How to use Git"
* One of the major problems of Git is its user's interaction, which has close to no abstraction
* Some people compare Git to a Henry Ford Model T: If you don't know the mechanics, you won't be able to use it very long
* I found that knowing "How Git works" is a much better approach for this technology (Git is Shit)
* ...and Gitception empowers you to find "How Git works" by yourself!

---

# Gitception
## in practice

Notes:
* Enough talking
* Let's see how it works!
* Don't need to type the commands, for a real workshop, join the Coders Only Git series

---

##  Setup

----

### Create a repository

```shell
$ mkdir -p ~/working/directory/ && cd $_ && {{ "git init ."|run }}
```
<!-- .element: class="fragment" -->

<!-- {{ 'git config user.name "Pablo Escodebar"'|run }} -->
<!-- {{ 'git config user.email "escodebar@gmail.com"'|run }} -->

```shell
$ {{ "ls -blah"|run }}
```
<!-- .element: class="fragment" -->

See that `.git` folder there? That's the repository.
<!-- .element: class="fragment" -->

Notes:
* Besides of some information, everything is stored in the `.git` folder
* During my trainings, we are confronted with typical Git situations

----

### Create a repository in the repository's repository

```shell
$ cd ~/working/directory/.git
```
<!-- .element: class="fragment" -->

```shell
$ {{ 'git init .'|run(gitception=True) }}
```
<!-- .element: class="fragment" style="font-size: 0.53em" -->
<!-- {{ 'git config user.name "Pablo Escodebar"'|run(gitception=True) }} -->
<!-- {{ 'git config user.email "escodebar@gmail.com"'|run(gitception=True) }} -->


```shell
$ {{ 'git add -A && git commit -m "Add the repository"'|multirun(gitception=True, quiet=True) }}
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

Notes:
* This is for educational purpose only
* Git keeps track of all the changes, it is therefore a perfect analysis tool
* Most Git commands go up the directory path to the point where they find a ``.git`` folder, but "ignore" its contents
* Therefore we can create a repository in the repository to track the changes and understand Git's behavior
* I haven't seen an other Git training doing this! Let me know if you like this idea!

----

![Gitception](https://i.imgflip.com/2f33xj.jpg)

Notes:
* Xzibit shows up on every slide which uses the repository in the repository to set you in the right context

---

## Git objects

Notes:
* One of the first things we discuss during my trainings are Git objects
* Understanding how Git stores changes is critical to gain confidence using Git

----

### Let's stage a file

```shell
$ {{ 'echo "# My awwwesome training" > README.md'|shell }}
```
<!-- .element: class="fragment" -->

```shell
$ {{ "git add README.md"|run }}
```
<!-- .element: class="fragment" -->

----

### What happened in the repository?
<!-- .element: class="fragment" -->

```shell
$ {{ 'git add . && git commit -m "Add files to index"'|multirun(gitception=True) }}
```
<!-- .element: class="fragment" style="font-size: 0.51em;" -->

An object was created!
<!-- .element: class="fragment" -->

{% filter gitception %}{% endfilter %}

Notes:
* Notice Xzibit in the background!
* The name of the objects is given by their hash
* To improve file-system usage, the objects are stored in folders

----

### Let's take a closer look

```shell
$ {{ 'git show --name-only'|run(gitception=True) }}
```
<!-- .element: style="font-size: 0.51em;" -->

{% filter gitception %}{% endfilter %}

Notes:
* Commiting the changes in the repository allows to inspect its behavior
* Let's ingnore the index file for this talk

----

### What's that object?

Inspect the created object
```shell
$ {{ "git cat-file -t b27501a"|run }}
```
<!-- .element: class="fragment" -->

```shell
$ {{ "git cat-file -p b27501a"|run }}
```
<!-- .element: class="fragment" -->

Notes:
* `cat-file` is similar to `show`, but displays the information without processing
* Files are stored as objects of type "blob" (Binary Large OBject)
* More objects are discussed later
* Please remember, that the whole file and not only the diff is stored! (well... it depends! 😊)

----

### Now let's commit a change

```shell
$ {{ 'git commit -m "Describe the training"'|run }}
```

Notes:
* `root-commit`: This is a special one, it has no parent, well see that in a minute
* `{{ "HEAD"|commit_hash }}` is part of the hash of the commit

----

### Time to dig deeper

The repository's content must have changed...

```shell
$ {{ 'git add . && git commit -m "Commit file"'|multirun(gitception=True) }}
```
<!-- .element: style="font-size: 0.51em;" class="fragment" -->

{% filter gitception %}{% endfilter %}

Notes:
* The `COMMIT_EDITMSG` is used to temporarily store the message of the commit
* The logs keep track of the commit hashes the references pointed to, they become handy when branches are lost (more about this later)
* There is also a log for the `HEAD` (more about the `HEAD` later)
* References (or refs here) are discussed later - see the `master` there again?
* One of the objects (`{{ "HEAD"|commit_hash }}`) has the same hash as the previously made commit
* ...and look! An other object!

----

### Commit objects!

What is the object with the commit's hash?
```shell
$ {{ "git cat-file -t LAST_COMMIT"|run }}
```
<!-- .element: class="fragment" -->
```shell
$ {{ "git cat-file -p LAST_COMMIT"|run }}
```
<!-- .element: class="fragment" -->
...so this is what a commit looks like!
<!-- .element: class="fragment" -->

Notes:
* Git stores commits in objects as well
* There is a reference to the tree (discussed in the next slide)
* The author and the committer are not necessarily the same person
* A timestamp is stored as well in the commit
* The title and the message are stored in the commit object
* The first commit (also called root) has no parent (more to parents later)

----

### Tree objects!

What is the object with the tree's hash?
```shell
$ {{ "git cat-file -t LAST_TREE"|run }}
```
<!-- .element: class="fragment" -->

```shell
$ {{ "git cat-file -p LAST_TREE"|run }}
```
<!-- .element: class="fragment" style="font-size: 0.545em;" -->

...it's collection of references to objects!

Notes:
* The tree is an object containing references to the blobs (or other trees)
* The tree also stores the permissions and the names of the files (but you can't set all permissions!)
* If a file happens to be more than once in the repository, Git will save it only once, since all the trees will reference the same file

By now, you know more about Git internals than many who consider themselves proficient in Git.
You will also be able to find "lost" files, folders and commits!

---

## Branches

...is there enough time?
<!-- .element: class="fragment" -->

----

### Create a branch

```shell
$ {{ "git branch pe/new_branch"|run }}
```

Notes:
* Prefix branches with your initials, to tell others not to touch it
* Reference the issue in the name if the branch is related to it
* If the branch name looks like a folder path, Git will create folders
* To work on a branch you need to check it out (or switch to it)

----

### Digging again!

How are branches stored in the repository?

```shell
$ {{ 'git add . && git commit -m "Add a new branch"'|multirun(gitception=True) }}
```
<!-- .element: class="fragment" -->

Notes:
* See how a further logfile was created? There is a log file for each branch!

----

### Let's take another close look

```shell
$ {{ "cat refs/heads/pe/new_branch"|run(gitception=True) }}
```
<!-- .element: class="fragment" -->

It's just a file with a hash
<!-- .element: class="fragment" -->

...that's why creating branches is so fast!
<!-- .element: class="fragment" -->

{% filter gitception %}{% endfilter %}

---

## ...and this is just the

# Beginning

---

## Conclusion

Notes:
* Using Gitception I am able to learn how the commands I use work
* Knowing the inner model and behavior of the commands raised my confidence
* A series of Workshops using Gitception are going to take place at Coders Only

---

## Questions & Feedback
