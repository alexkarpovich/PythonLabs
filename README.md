ITA CV Builder
==========

How to install and run server:
----------
1. run "vagrant up" from rood directory
2. connect to vagrant (run "vagrant ssh")
3. go to folder "/var/www/local.cvbuilder.dev/api"
4. run "python manage.py migrate"
5. run "python manage.py runserver 0.0.0.0:8000" to start server
6. use http://192.168.33.60:8000 to see application in your browser
