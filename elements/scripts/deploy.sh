
#cd /data/elements
#git checkout .
#git pull
#git rev-parse HEAD > VERSION
#chmod +x /data/elements/scripts/deploy.sh
#
pip install -r ../requirements/production.txt

python manage.py makemigrations --settings=elements.settings.production
python manage.py migrate --settings=elements.settings.production

python manage.py makemigrations engine --settings=elements.settings.production
python manage.py migrate engine --settings=elements.settings.production

uwsgi --ini ./elements/settings/configs/uwsgi/engine.ini

