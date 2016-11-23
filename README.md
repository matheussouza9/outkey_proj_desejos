# outkey_proj_desejos
Um sistema de cadastro de desejos de pessoas

### Requisitos
  * Python 2.7.6
  * Django 1.8.2
  * Postgresql Server 9.3

### Dependências
Para instalar as dependências(necessário o gerenciador de pacotes `pip`):

```sh
$ cd outkey_proj
$ pip install -r requirements.txt
```

### Observações
Você deve relacionar os models do projeto com o banco de dados, para isso, realize as migrações e aplique-as:

```sh
$ cd outkey_proj
$ python manage.py makemigrations
$ python manage.py migrate
```
Você deve criar um superusuário:

```sh
$ cd outkey_proj
$ python manage.py createsuperuser
```