---
theme: solarized
title: Version control systems
revealOptions:
    transition: 'fade'
---

# Version control systems

PabV

---

## Schedule

* Version control systems
  * local
  * centralized
  * distributed

* Git

Notes:
* Concepts and mindsets of version control systems are introduced
* Three different types of version control systems are discussed
* Then Git its features and drawbacks are discussed

---

## Mindset

Version control is a system that records changes to a file or set of files over time

...so that you can recall specific versions later.
<!-- .element: class="fragment" -->

Notes:
* The concept of backups is common and backups are widely-used
* Who doesn't do backups?

---

![Local VCS](VCS/local_vcs.png)
<!-- .element: height="400px" -->

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

![Centralized VCS](VCS/centralized_vcs.png)
<!-- .element: height="400px" -->

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

![Decentralized VCS](VCS/decentralized_vcs.png)
<!-- .element: height="550px" -->

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

Let's introduce a new mindset!

---

## Mindset *improved*

Version control is a system that allows to write and manage sets of *changes*

...and allows you to recall specific versions later.<!-- .element: class="fragment" -->

Notes:
* Think of changes as patches! (Thanks to Peter for this!)

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

Other conveniences:
* simpler error analysis
* simpler code review
* better code reusability
* faster development

Notes:
* Tools exist to find out which patch introduced errors, it is much much easier to find an error in within a few lines of code than in within hundreds of lines of code
* Correctly signed patches allow to ask the author in case of uncertainty
* Patches can be applied to several systems if the same or a similar logic is required

---

## Some VCS

ArX,
Bazaar,
BitKeeper,
Codeville,
CVS,
Darcs,
DCVS,
Fossil,
Git,
GNU arch,
Mercurial,
Monotone,
Perforce,
Subversion,
TFVCS,
Veracity, ...

...not all of these are good for patches!<!-- .element: class="fragment" -->

Notes:
* You need to find a VCS which is well suited to your teams mindset

Statistics:
* Who worked with one of these version control system already?

---

# Git

But... what's so good about Git?<!-- .element: class="fragment" -->

Notes:
* I have little experience with subversion and no experience with all the other VCS (besides Git)
* I started using Git, because the company I worked for used Git
* I kept using Git because I found enough "Why is Git better than X"-blog entries
* I keep using Git because Git is all I need (...and because I am a total fanboy!)
* Try to find out what your needs are and find the VCS which suits your use case (which will be probably be Git)


---

## Git

"*... is oddly liberal with how and when you use it.*"

* is a powerful analysis tool<!-- .element: class="fragment" -->
* allows running automated tasks<!-- .element: class="fragment" -->
* simplifies collaboration<!-- .element: class="fragment" -->
* simplifies patch management<!-- .element: class="fragment" -->

Notes:
* Depending on your workflow, the development might be
  - chaotic (which is totally fine, think of eating)
  - organized
* Git has the necessary tools to work under borth circumstances (and the spectrum in between)

---

*Git allows you to evolve the way you develop without getting in your way!*

Notes:
* Git does not force you to suit certain workflows
* ... your team does!
* The tangled working copy problem

---

# Git
## makes you
# a better
# developer!

Notes:
* But only if you're willing to change! (Improvement always comes with change)
* This bold statement is my personal opinion (but I got a few testimonials aproving this)

---

## The problem about Git

![Git XKCD](https://imgs.xkcd.com/comics/git.png)

Notes:
* Many people don't know how to deal with it!
  * Naming seems complex
  * The mechanics seem complex
  * Dealing with other's patches seems complex
* Many people are not willing to learn how to deal with it!
* And it is only helpful if most contributors use it in a good manner

---

[10 things I hate about Git](https://stevebennett.me/2012/02/24/10-things-i-hate-about-git/)

---

How do we fix this?

Notes:
* Learn Git and learn it well!

---

# Git resources

* [Why Git is Better than X](http://web.archive.org/web/20090210020404id_/http://whygitisbetterthanx.com/)
* [The thing about Git](https://tomayko.com/blog/2008/the-thing-about-git)
* [Git is simpler than you think](http://nfarina.com/post/9868516270/git-is-simpler)
* [Think like a Git](http://think-like-a-git.net/)
* [Git Magic](http://www-cs-students.stanford.edu/~blynn/gitmagic/index.html)
* [Pro Git](https://git-scm.com/book/en/v2)
* [Git Reference](https://git-scm.com/docs/)

Notes:
* My approach is to learn how Git works and learn its internals, then use automatically in a better way
* A lot of reading is required

---

or

...join my Git trainings!<!-- .element: class="fragment" -->

---

## Git trainings

* Git basics or: How I learned to stop worrying and love the rebase
* Hitchhiker's guide to distributed Git

*save the date!*<!-- .element: class="fragment" -->

---

## Thank you!

---

## Questions & Feedback
