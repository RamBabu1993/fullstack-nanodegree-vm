# Tournament Results
This is my solution for project Tournament Results. This project is part of <a href="https://www.udacity.com/nanodegree"> 
Udacity's Full stack Web developer nanodegree </a> 

The project uses Python and postgreSQL to implement <a href="https://en.wikipedia.org/wiki/Swiss-system_tournament">Swiss-system Tournament </a> and keeps track of matches and players in a tournament.

## Install
<ul>
<li> <a href="https://www.python.org/downloads/"> python</a> 2.7 or higher.</li>
<li> <a href="http://initd.org/psycopg/"> psycopg</a> package already installed on VM</li>
<li> <a href="https://www.vagrantup.com/"> Vagrant </a> and <a href="https://www.virtualbox.org/wiki/Downloads"> VM</a></li>
</ul>

## Required files
<ul>
<li> <strong>tournament.py </strong> - Contains functions to interact with database</li>
   <li> <strong>tournament.sql</strong> - To create database, table and views </li>
   <li> <strong>tournament_test.py</strong> - Tests the implementation of functions defined in **tournament.py** </li>
</ul>

## Steps to run the project
clone or download repository on local machine.

### using Vagrant VM
- install vagrant and VM. Vagrant VM has installed and configured postgreSQL and psql command line interface. so no need to install on local machine.
- used terminal and navigate to the directory that contains repository.
- start VM by running
``` 
vagrant up 
```
this will take some time as it download Linux ubuntu OS on VM
- login into by running
```
vagrant ssh
```
now you are logged into VM as user vagrant.
### using tournament.sql
- on VM navigate to tournament directory by running
```
cd /vagrant/tournament
```
- connet to the database and to use tables and views from **tournament.sql** use command given below:
```
psql tournament '\i tournament.sql'
```
### using tournament_test.py
- to test the functions define in **tournament.py** run command given below on terminal
```
python tournament_test.py
```
this command will show that all test run successfully.
- you can use `ctld+d` to logout from VM and run `vagrant halt` to shut down the VM.

