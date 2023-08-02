# setup

1. clone the repo

```
> git clone git@github.com:omerk42/drf_task.git
```

> Note: you need to set ssh keys if you dont use https or download repo as zip from here:
> https://github.com/omerk42/drf_task

2. setup env

```
> cd drf_task
> python3 -m venv <venv name>
> . <venv name>/bin/activate
```

> Note: these commands used in lunix , if you are using windows please check :
> https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html

3. install requirement

```
> pip install -r requirements.txt
```

4. setup .env

```
> cp env.example .env
```

5. make migration

```
> python3 manage.py migrate
```

6. run the project

```
> python3 manage.py runserver
```

# how to use

there is multiple ways to use the API fell free top use any but i made simple way to use the API which is simple cli program , to use it :

```
> cd client
> python3 client.py
```

using the program is very simple. as each operation is self-explanatory.
