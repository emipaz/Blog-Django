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


