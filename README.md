# Project Scripts for CI/CD

#### version: 0.0.2

## Ansible

## Bash

---
**NOTE**

this is a note
---

## Python

```python
s = "Python syntax highlighting"
print(s)
```

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |


> Blockquotes are very handy in email to emulate reply text.
> This line is part of the same quote.

## Git

In order to trigger the cicd pipeline without creating a fake
commit, use the following command. Warning, do not use this on
a shared repository.

```console
git commit --amend --no-edit ; git push home master -f
```

```console
starts ssh-agent
eval "$(ssh-agent -s)"
```

Wildcard Let’s Encrypt Certificate
Made easy using DNS-01 challenge

https://itnext.io/wildcard-lets-encrypt-certificate-2b6133a1acdf


```console
                                              _  _
                                             ' \/ '
   _  _                        <|
    \/              __'__     __'__      __'__
                   /    /    /    /     /    /
                  /\____\    \____\     \____\               _  _
                 / ___!___   ___!___    ___!___               \/
               // (      (  (      (   (      (
             / /   \______\  \______\   \______\
           /  /   ____!_____ ___!______ ____!_____
         /   /   /         //         //         /
       /    /   |         ||         ||         |
     /_____/     \         \\         \\         \
           \      \_________\\_________\\_________\
            \         |          |         |
             \________!__________!_________!________/
              \|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_/|
               \    _______________                /
~~~~~~~~~~~~~~~~\_________________________________/~~~~~~~~~~~~~~~~~~~~~
```
# to change shell for user git

sudo chsh git

# Changing the login shell for git
# Enter the new value, or press ENTER for the default
# change the user shell to /bin/sh

Login Shell [/usr/bin/git-shell]: /bin/sh

```console
cd /opt/git
mkdir devops.git
cd devops.git
ls -als
total 8
4 drwxrwxr-x 2 git git 4096 May  5 21:10 .
4 drwxr-xr-x 4 git git 4096 May  5 21:10 ..
git init --bare .
Initialized empty Git repository in /opt/git/devops.git/
ls -als
total 40
4 drwxrwxr-x 7 git git 4096 May  5 21:11 .
4 drwxr-xr-x 4 git git 4096 May  5 21:10 ..
4 drwxrwxr-x 2 git git 4096 May  5 21:11 branches
4 -rw-rw-r-- 1 git git   66 May  5 21:11 config
4 -rw-rw-r-- 1 git git   73 May  5 21:11 description
4 -rw-rw-r-- 1 git git   23 May  5 21:11 HEAD
4 drwxrwxr-x 2 git git 4096 May  5 21:11 hooks
4 drwxrwxr-x 2 git git 4096 May  5 21:11 info
4 drwxrwxr-x 4 git git 4096 May  5 21:11 objects
4 drwxrwxr-x 4 git git 4096 May  5 21:11 refs

sudo chsh git
Changing the login shell for git
Enter the new value, or press ENTER for the default
	Login Shell [/bin/sh]: /usr/bin/git-shell
```
git remote -v
origin	git@github.com:NicDevOps/devops.git (fetch)
origin	git@github.com:NicDevOps/devops.git (push)
nick@ubuntu:~/projects/devops$ git remote add home git@gitserver:/opt/git/devops.git
