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


## Bootstraping your environment

To try this simply run the appropriate shell command based on your operating system. 

It will: 
* Install the *state tool*, our package manager for teams, if it not already present on the machine.
* Checkout this git repository
* Configure git hooks
* Install your needed depdencies


###  Linux and Mac, run this command 

```bash
$ sh <(curl -q https://platform.activestate.com/dl/cli/655424048.1642518345_pdli01/install.sh) -c'state activate --default scottr/onboarding'
```

### Windows users, run this command

```powershell

c:\> powershell -Command "& $([scriptblock]::Create((New-Object Net.WebClient).DownloadString('https://platform.activestate.com/dl/cli/655424048.1642518345_pdli01/install.ps1'))) -c'state activate --default scottr/onboarding'"

```

### Users with state tool (our package manager for teams)

`state activate scottr/onboarding`


## Running the unit tests 

Once installations is finished, you can run the unit tests.. we've set up a simple entrypoint in the activestate.yaml called  `testit`
that invokes pytest for you.

```bash

$ testit                
Running Script: testit


Script Output
─────────────
================================================================ test session starts =================================================================
platform darwin -- Python 3.9.15, pytest-7.1.3, pluggy-1.0.0 -- /Users/srobertson/Library/Caches/activestate/6e54892e/usr/bin/python3
cachedir: .pytest_cache
rootdir: /private/tmp/onboarding
collected 1 item

test_me.py::test_python PASSED                                                                                                                 [100%]

================================================================= 1 passed in 0.01s ==================================================================
```


Note from the output that it's using Python 3.9.15.

## See dynamic enviorment provisioning in work

Now, let's try the other branch which requires Python 3.10.




