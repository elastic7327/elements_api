

#
#python manage.py makemigrations  --settings=elements.settings.testing
#python manage.py migrate --settings=elements.settings.testing
#
#python manage.py makemigrations engine --settings=elements.settings.testing
#python manage.py migrate engine --settings=elements.settings.testing
#
python manage.py runserver 8000 --settings=elements.settings.acceptance
#python manage.py shell_plus --settings=elements.settings.testing
