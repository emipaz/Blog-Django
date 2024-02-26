# Projecto Blog con Django


## instalacion de entorno

```powershell
PS C:\Users\Usuario\Desktop\Blog-Django> python
Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
PS C:\Users\Usuario\Desktop\Blog-Django> python -m venv env_blog
PS C:\Users\Usuario\Desktop\Blog-Django> ls


    Directorio: C:\Users\Usuario\Desktop\Blog-Django


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         26/2/2024     12:00                env_blog
                                                  801813051.EBooksWorld.ir.pdf
-a----         9/11/2023     09:50        2632263 get-pip.py
-a----         25/2/2024     17:12             32 requierement.txt


PS C:\Users\Usuario\Desktop\Blog-Django> .\env_blog\Scripts\Activate.ps1
(env_blog) PS C:\Users\Usuario\Desktop\Blog-Django> pip install -r .\requierement.txt
Collecting django==4.2
  Downloading Django-4.2-py3-none-any.whl (8.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.0/8.0 MB 4.9 MB/s eta 0:00:00
Collecting django-taggit==3.0.0
  Downloading django_taggit-3.0.0-py3-none-any.whl (59 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 59.9/59.9 KB 3.3 MB/s eta 0:00:00
  Using cached asgiref-3.7.2-py3-none-any.whl (24 kB)
Collecting sqlparse>=0.3.1
  Using cached sqlparse-0.4.4-py3-none-any.whl (41 kB)
Collecting tzdata
  Downloading tzdata-2024.1-py2.py3-none-any.whl (345 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 345.4/345.4 KB 5.4 MB/s eta 0:00:00
Collecting typing-extensions>=4
  Downloading typing_extensions-4.10.0-py3-none-any.whl (33 kB)
Installing collected packages: tzdata, typing-extensions, sqlparse, asgiref, django, django-taggit
Successfully installed asgiref-3.7.2 django-4.2 django-taggit-3.0.0 sqlparse-0.4.4 typing-extensions-4.10.0 tzdata-2024.1
WARNING: You are using pip version 22.0.4; however, version 24.0 is available.
You should consider upgrading via the 'C:\Users\Usuario\Desktop\Blog-Django\env_blog\Scripts\python.exe -m pip install --upgrade pip' command.
(env_blog) PS C:\Users\Usuario\Desktop\Blog-Django> pip list
Package           Version
----------------- -------
asgiref           3.7.2
Django            4.2
django-taggit     3.0.0
pip               22.0.4
setuptools        58.1.0
sqlparse          0.4.4
typing_extensions 4.10.0
tzdata            2024.1
WARNING: You are using pip version 22.0.4; however, version 24.0 is available.
You should consider upgrading via the 'C:\Users\Usuario\Desktop\Blog-Django\env_blog\Scripts\python.exe -m pip install --upgrade pip' command.

```
## Cracion de proyecto y la app de Blog

```powershell
(env_blog) PS C:\Users\Usuario\Desktop\Blog-Django> django-admin startproject mysite

    Directorio: C:\Users\Usuario\Desktop\Blog-Django


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         26/2/2024     12:00                env_blog
d-----         26/2/2024     12:09                mysite
-a----         17/2/2024     12:29       42166911 Django.4.By.Example.4th.Edition.Antonio.Mele.Bob.Belderbos.Packt.9781
                                                  801813051.EBooksWorld.ir.pdf
-a----         9/11/2023     09:50        2632263 get-pip.py
-a----         25/2/2024     17:12             32 requierement.txt


    Directorio: C:\Users\Usuario\Desktop\Blog-Django\mysite


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         26/2/2024     12:09                mysite
-a----         26/2/2024     12:09            684 manage.py


(env_blog) PS C:\Users\Usuario\Desktop\Blog-Django\mysite> python manage.py startapp blog
(env_blog) PS C:\Users\Usuario\Desktop\Blog-Django\mysite> ls


    Directorio: C:\Users\Usuario\Desktop\Blog-Django\mysite


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         26/2/2024     12:10                blog
d-----         26/2/2024     12:10                mysite
-a----         26/2/2024     12:09            684 manage.py

```

## inicio de repositorio git

```powershell
(env_blog) PS C:\Users\Usuario\Desktop\Blog-Django> git init
Initialized empty Git repository in C:/Users/Usuario/Desktop/Blog-Django/.git/
(env_blog) PS C:\Users\Usuario\Desktop\Blog-Django> git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   .gitignore
        new file:   mysite/blog/__init__.py
        new file:   mysite/blog/admin.py
        new file:   mysite/blog/apps.py
        new file:   mysite/blog/migrations/__init__.py
        new file:   mysite/blog/models.py
        new file:   mysite/blog/tests.py
        new file:   mysite/blog/views.py
        new file:   mysite/manage.py
        new file:   mysite/mysite/__init__.py
        new file:   mysite/mysite/asgi.py
        new file:   mysite/mysite/settings.py
        new file:   mysite/mysite/urls.py
        new file:   mysite/mysite/wsgi.py
        new file:   requierement.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        comandos.md

```
## Primera migracion

```cmd

(env_blog) C:\Users\Usuario\Desktop\Blog-Django\mysite>python manage.py migrate        
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK

```

### Probar el modelo Post e hacer las migraciones

```powershell

(env_blog) PS C:\Users\Usuario\Desktop\Blog-Django\mysite> python .\manage.py shell
Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from blog.models import Post
>>> Post.Status.choices
[('B', 'Borrador'), ('P', 'Publicado')]
>>> Post.Status.labels
['Borrador', 'Publicado']
>>> Post.Status.names
['BORRADOR', 'PUBLICADO']
>>>


(env_blog) PS C:\Users\Usuario\Desktop\Blog-Django\mysite> python .\manage.py makemigrations blog
Migrations for 'blog':
  blog\migrations\0001_initial.py
    - Create model Post
    - Create index blog_post_publica_176893_idx on field(s) -publicado of model post

(env_blog) PS C:\Users\Usuario\Desktop\Blog-Django\mysite> python .\manage.py sqlmigrate blog 0001
BEGIN;
--
-- Create model Post
--
CREATE TABLE "blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "titulo" varchar(250) NOT NULL, "slug" varchar(250) NOT NULL, "cuerpo" text NOT NULL, "publicado" datetime NOT NULL, "creado" datetime NOT NULL, "actualizado" datetime NOT NULL, "estado" varchar(1) NOT NULL, "autor_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create index blog_post_publica_176893_idx on field(s) -publicado of model post
--
CREATE INDEX "blog_post_publica_176893_idx" ON "blog_post" ("publicado" DESC);
CREATE INDEX "blog_post_slug_b95473f2" ON "blog_post" ("slug");
CREATE INDEX "blog_post_autor_id_8811ea21" ON "blog_post" ("autor_id");
COMMIT;
(env_blog) PS C:\Users\Usuario\Desktop\Blog-Django\mysite> python .\manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying blog.0001_initial... OK

```
### ipython en la shellde django

```powershell
(env_blog) PS C:\Users\Usuario\Desktop\Blog-Django\mysite> pip install ipython
WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<pip._vendor.urllib3.connection.HTTPSConnection object at 0x00000288A336DCC0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed')': /simple/ipython/
Collecting ipython
  Downloading ipython-8.22.1-py3-none-any.whl (811 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 812.0/812.0 KB 3.7 MB/s eta 0:00:00
Collecting pygments>=2.4.0
  Using cached pygments-2.17.2-py3-none-any.whl (1.2 MB)
Collecting traitlets>=5.13.0
  Using cached traitlets-5.14.1-py3-none-any.whl (85 kB)
Collecting exceptiongroup
  Using cached exceptiongroup-1.2.0-py3-none-any.whl (16 kB)
Collecting stack-data
  Using cached stack_data-0.6.3-py3-none-any.whl (24 kB)
Collecting jedi>=0.16
Collecting matplotlib-inline
  Using cached matplotlib_inline-0.1.6-py3-none-any.whl (9.4 kB)
Collecting prompt-toolkit<3.1.0,>=3.0.41
  Using cached prompt_toolkit-3.0.43-py3-none-any.whl (386 kB)
Collecting decorator
  Using cached decorator-5.1.1-py3-none-any.whl (9.1 kB)
Collecting colorama
  Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Collecting parso<0.9.0,>=0.8.3
  Using cached parso-0.8.3-py2.py3-none-any.whl (100 kB)
Collecting wcwidth
  Using cached wcwidth-0.2.13-py2.py3-none-any.whl (34 kB)
Collecting pure-eval
  Using cached pure_eval-0.2.2-py3-none-any.whl (11 kB)
Collecting executing>=1.2.0
  Using cached executing-2.0.1-py2.py3-none-any.whl (24 kB)
Collecting asttokens>=2.1.0
  Using cached asttokens-2.4.1-py2.py3-none-any.whl (27 kB)
Collecting six>=1.12.0
  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: wcwidth, pure-eval, traitlets, six, pygments, prompt-toolkit, parso, executing, exceptiongroup, decorator, colorama, matplotlib-inline, jedi, asttokens, stack-data, ipython
Successfully installed asttokens-2.4.1 colorama-0.4.6 decorator-5.1.1 exceptiongroup-1.2.0 executing-2.0.1 ipython-8.22.1 jedi-0.19.1 matplotlib-inline-0.1.6 parso-0.8.3 prompt-toolkit-3.0.43 pure-eval-0.2.2 pygments-2.17.2 six-1.16.0 stack-data-0.6.3 traitlets-5.14.1 wcwidth-0.2.13
WARNING: You are using pip version 22.0.4; however, version 24.0 is available.
You should consider upgrading via the 'C:\Users\Usuario\Desktop\Blog-Django\env_blog\Scripts\python.exe -m pip install --upgrade pip' command.
(env_blog) PS C:\Users\Usuario\Desktop\Blog-Django\mysite> python .\manage.py shell -i ipython
Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.22.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from django.contrib.auth.models import User

In [2]: from blog.models import Post

In [3]: user = User.objectsj.get(username="emi")
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[3], line 1
----> 1 user = User.objectsj.get(username="emi")

AttributeError: type object 'User' has no attribute 'objectsj'

In [4]: user = User.objects.get(username="emi")

In [5]: user
Out[5]: <User: emi>

In [6]: post = Post(
   ...: titulo = "Instalacion de ipython para django shell",
   ...: slug = "django-ipython-shell",
   ...: cuerpo = """
   ...: pip install ipython
   ...: despues una vez instalado ipython
   ...: ejecutar :
   ...: python manage.py shell -i ipython
   ...: """,
   ...: autor=user)

In [7]: post.save()

In [8]: post
Out[8]: <Post: Instalacion de ipython para django shell>

In [9]: Post.objects.create(titulo = "Un nuevo post",
   ...: slug = "post-nuevo",
   ...: cuerpo="post creado usando Post.objects.create",
   ...: autor=user)
Out[9]: <Post: Un nuevo post>

In [10]: post.titulo = "Un Nuevo Post"

In [11]: post.save()

In [12]: posteos = Post.objects.all()

In [13]: posteos
Out[13]: <QuerySet [<Post: Un nuevo post>, <Post: Un Nuevo Post>]>

In [14]: post.titulo=("ipython en shell de django")

In [15]: post.save()

In [16]: posteos = Post.objects.all()

In [17]: posteos
Out[17]: <QuerySet [<Post: Un nuevo post>, <Post: ipython en shell de django>]>

In [18]: post.cuerpo
Out[18]: '\npip install ipython\ndespues una vez instalado ipython\nejecutar :\npython manage.py shell -i ipython\n'

```
