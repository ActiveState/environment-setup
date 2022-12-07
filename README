# Demonstrating keeping your depdencies in sync

Ever try diving into someone elses software development project and get frustrated about what it takes to setup a development
enviroment? Often the instructions are vague, don't cover your specific setup, are out of date or  are completely missing!
   

This simple project demonstrates how you can streamline setting up development environments for members of your team.

With the ActiveState platform, you can setup all the dependecies needed to run and develop your project regardless
of operating system and reduce complicated development enivronment setup down to single command.

In our hypothetical python project, we've setup a simple unit test that ensure's you're using the right version of Python. On the
main branch, which simulates your current production release, we require Python 3.9. There is also a branch where we're working on
a new feature that requires you to upgrade to Python 3.10, aplty named awesome-new-feature.

It does not matter whether you have Python installed or or if you have the wrong version of Python. The ActiveState platform
will ensure you have the right right depdencies for the given git commit you're working on.


To try this simply run the appropriate shell command based on your operating system.


##  Linux and Mac, run this command 

```bash
$ sh <(curl -q https://platform.activestate.com/dl/cli/655424048.1642518345_pdli01/install.sh) -c'state activate --default scottr/onboarding'
```

## Windows users, run this command

```powershell

c:\> powershell -Command "& $([scriptblock]::Create((New-Object Net.WebClient).DownloadString('https://platform.activestate.com/dl/cli/655424048.1642518345_pdli01/install.ps1'))) -c'state activate --default scottr/onboarding'"

```

## Users with state tool (our package manager for teams)

`state activate scottr/onboarding`





