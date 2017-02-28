

python manage.py migrate engine --settings=elements.settings.testing
python manage.py makemigrations engine --settings=elements.settings.testing

python manage.py runserver --settings=elements.settings.testing
#python manage.py shell_plus --settings=elements.settings.testing
