# PokeService

---

```bash
python3 -m venv env
source env/bin/activate
(env) pip install -r requirements.txt
```

## Show datas 
```bash
service postgresql start
-u postgres psql battle_log_db
SELECT * FROM main_battlelog ORDER BY id DESC LIMIT 10;
```

## Set email&password. Smtp - mail.ru
```bash
(env) export DJANGO_SMTP_EMAIL='$youremail' && export DJANGO_SMTP_EMAIL_PASSWORD='$yourpassword'
```

## ftp connect
```bash
(env) export DJANGO_FTP_HOST='$yourhost' && export DJANGO_FTP_USER='$yourname' && export DJANGO_FTP_PASS='$yourpssw'
service vsftpd start
ftp -p 127.0.0.1

lcd
get
```

todos:
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
- [ ] Docker v0.6