

#
python ../manage.py makemigrations  --settings=elements.settings.development
python ../manage.py migrate --settings=elements.settings.development
#
python ../manage.py makemigrations engine --settings=elements.settings.development
python ../manage.py migrate engine --settings=elements.settings.development
#
python ../manage.py runserver 8000 --settings=elements.settings.development
#python manage.py shell_plus --settings=elements.settings.development
