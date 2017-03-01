


python manage.py makemigrations  --settings=elements.settings.testing
python manage.py migrate --settings=elements.settings.testing

python manage.py makemigrations engine --settings=elements.settings.testing
python manage.py migrate engine --settings=elements.settings.testing

python manage.py runserver 7000 --settings=elements.settings.testing
#python manage.py shell_plus --settings=elements.settings.testing
