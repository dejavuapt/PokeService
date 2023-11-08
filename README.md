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

##Set email&password. Smtp - mail.ru
```bash
(env) export DJANGO_SMTP_EMAIL='$youremail' && export DJANGO_SMTP_EMAIL_PASSWORD='$yourpassword'
```



todos:
- [x] catalog 
- [x] detailed_pokemon
- [x] search -> [ ] bug when you tried go to next page in searced pokemons
- [x] battle v0.2.4
    - [x] fast battle v0.3.1 | +[x]add logs in battle_end screen \ [x]shake pokemon
    - [x] send battle result on email v0.3.2
- [ ] refactoring v0.3.3
- [ ] git merging v0.4.1
- [ ] FTP v0.4.2
- [ ] Docker v0.5