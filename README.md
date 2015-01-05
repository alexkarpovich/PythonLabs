ITA CV Builder
==========

How to install and run server (with virtualenv):
----------
1. run "vagrant up" from rood directory
2. connect to vagrant (run "vagrant ssh")
3. run "sudo pip install virtualenv"
4. run "sudo mkdir /home/venv"
4. go to folder "/home/venv/"
5. run "sudo virtualenv cvbuilder"
6. run "sudo chmod 777 -R /home/venv/cvbuilder/"
7. run "sudo apt-get install postgresql-server-dev-9.3"
8. run "sudo apt-get install build-essential autoconf libtool pkg-config python-opengl python-imaging python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev"
9. go to folder "/var/www/local.cvbuilder.dev/api"
10. run "source /home/venv/cvbuilder/bin/activate" 
11. run "python manage.py migrate"
12. run "python manage.py runserver 0.0.0.0:8000" to start server
13. use http://192.168.33.60:8000 to see application in your browser

How to install and run server (without virtualenv):
----------
1. run "vagrant up" from rood directory
2. run "vagrant provision" to be make sure that all software was installed
2. connect to vagrant (run "vagrant ssh")
3. go to folder "/var/www/local.cvbuilder.dev/api"
4. run "python manage.py migrate"
5. run "python manage.py runserver 0.0.0.0:8000" to start server
6. use http://192.168.33.60:8000 to see application in your browser
