# Project Scripts for CI/CD

#### version: 0.0.2

### Ansible

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

```console
git remote -v
origin	git@github.com:NicDevOps/devops.git (fetch)
origin	git@github.com:NicDevOps/devops.git (push)
git remote add home git@gitserver:/opt/git/devops.git
```

# scan your network for the new rpi ip address
# watch nmap -sP 192.168.0.0/24

# editing hosts file for rpi
sudo vim /etc/hosts # update rpi ip address

# fixing known_hosts error
ssh-keygen -f "/home/<user>/.ssh/known_hosts" -R "rpi"
ssh-keygen -f "/home/<user>/.ssh/known_hosts" -R "192.168.0.120"

# ssh into rpi
defaults
user: ssh pi@rpi
password: raspberry

# copy ssh public key
ssh-copy-id pi@rpi

# congrats!!!!


ssh-keygen -t rsa -b 4096 -C "pi@rpi"

# install docker and docker-compose

curl -sSL https://get.docker.com | sh

# fix user permissions to use docker

sudo usermod -aG docker pi

# run a test container using docker

# x86
docker run hello-world

# arm32v6

docker run --rm -it arm32v6/bash



sudo apt-get install -y libffi-dev libssl-dev

sudo apt-get install -y python3 python3-pip

sudo apt-get remove python-configparser

sudo pip3 install docker-compose

# Architectures other than amd64?

https://github.com/docker-library/official-images#architectures-other-than-amd64