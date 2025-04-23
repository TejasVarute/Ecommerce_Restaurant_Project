set -o errexit

pip install -r requirements.txt

python mange.py migrate
if [[ $CREATE_SUPERUSER ]];
then
    python mange.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"
fi