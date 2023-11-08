# PokeService

---

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

```bash
service postgresql start
-u postgres psql battle_log_db
SELECT * FROM main_battlelog
```


todos:
- [x] catalog 
- [x] detailed_pokemon
- [x] search -> [ ] bug when you tried go to next page in searced pokemons
- [x] battle v0.2.4
    - [ ] fast battle v0.3.1 | +[x]add logs in battle_end screen \ [x]shake pokemon
    - [ ] send battle result on email v0.3.2
- [ ] refactoring v0.3.3
- [ ] git merging v0.4.1
- [ ] FTP v0.4.2
- [ ] Docker v0.5