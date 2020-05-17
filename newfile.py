cd mysite
python manage.py runserver


cd mysite
python manage.py createsuperuser

action="{% url 'post:delete' post.id %}" 

cd mysite
python manage.py makemigrations

<a href="{% url 'post:add_comment' id=post.id %}">Leave a comment </a>
cd mysite
python manage.py migrate

