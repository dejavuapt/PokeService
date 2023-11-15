![pikachu](https://giphy.com/embed/7ISIRaCMrgFfa)


# PokeService 



## Docker run (debian):

1. Create Envariables.

- DJANGO VARIABLES
```bash
cat > dj_variables.env
```
Copy and paste next with your's variables:
```
DJANGO_SMTP_EMAIL=$email.mail.ru
DJANGO_SMTP_EMAIL_PASSWORD=$mailpassword
DJANGO_FTP_HOST=poke-ftp
DJANGO_FTP_USER=$yourusername
DJANGO_FTP_PASS=$password
```
Ctrl+D

- FTP VARIABLES
```bash
cat > ftp_variables.env
```
Copy and paste next with your's variables:
```
USERS="$yourusername|$password"
```
Ctrl+D

- POSTGRESQL VARIABLES
```bash
cat > psql_variables.env
```
Copy and paste next with your's variables:
```
POSTGRES_PASSWORD=$passwordofpostgre
POSTGRES_DB=$nameofdb
```
Ctrl+D

2. Run by docker compose
```bash
docker compose up -d
```
---
## Extra:

Show datas:
```bash
docker ps -a
docker exec -it [CONTAINER_ID_POSTGRES] bash
psql -U [USER_NAME] [DB_NAME]
SELECT * FROM [TABLE_NAME] ORDER BY id DESC LIMIT 10;
```

Ftp connect:
```bash
ftp -p 127.0.0.1
[AUTH YOUR NAME AND PASSWORD]
lcd
get ...
```

---
## To product:
1. Copy docker-compose.yml
2. Change in poke-django ["build: ." -> "image: dejavuapt/pokeservice"]
3. Create variables files. Part **"Docker run. 1p"**

---
## Todos:
- [x] catalog 
- [x] detailed_pokemon
- [x] search -> [ ] bug when you tried go to next page in searced pokemons
- [x] battle v0.2.4
    - [x] fast battle v0.3.1 | +[x]add logs in battle_end screen \ [x]shake pokemon
    - [x] send battle result on email v0.3.2
- [/] refactoring v0.3.3
- [x] git merging v0.4.1
- [x] FTP v0.4.2
- [x] Redis v0.5
- [x] Docker v0.6


---
## Resources

[Docker image of django-project](https://hub.docker.com/r/dejavuapt/pokeservice)