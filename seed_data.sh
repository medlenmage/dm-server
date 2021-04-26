rm -rf dmApi/migrations
rm db.sqlite3
python manage.py makemigrations dmApi
python manage.py migrate
python manage.py loaddata user
python manage.py loaddata tokens
python manage.py loaddata dmuser
python manage.py loaddata monster
python manage.py loaddata npc
python manage.py loaddata note
python manage.py loaddata playercharacter
python manage.py loaddata campaigns