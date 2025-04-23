set -o errexit

pip install -r requirements.txt

python Project/mange.py migrate
if [[ $CREATE_SUPERUSER ]];
then
    python Project/mange.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"
fi