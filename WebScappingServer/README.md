# README for WebScappingServer
## UML:
![](https://i.imgur.com/nXcgI5P.png)





## Pierwsza instalacja środowiska wirtualnego:

Żeby utworzyć środowisko wirtualne potrzebujemy venva.
Odpowiada ono za to, żeby zależności jakie wykorzystuje dany skrypt nie mieszały się w projecie. Każdy program ma mieć swój **setup**.

Pierwsze uruchomienie:
```
python3 -m venv Scapping
```

Gdy już utworzymy venva musimy go **włączyć**:
Dla linuxa/maca:
```
source Scapping/bin/activate
```
Dla windowsa:
```
Scapping/scripts/activate
```

Teraz możemy zainstalować zależności:
```
pip install -r requirements.txt
```
lub:
```
pip3 install -r requirements.txt
```


## TODO: 
- [ ] Zrobienie main loop 
- [x] Zrobienie połączenie do bazy danych dla TopFx
- [x] Zrobienie połączenia do bazy danych dla InternetowegoKantoru
- [x] Zrobienie main loop 
- [x] Zrobienie w klasie main funkcji która odpowiada za działanie w pętli 
- [x] Zrobienie w klasie main funkcji która odpowiada za testy poprawnego działania
- [x] Zminić PATH do bazy danych
- [x] Poprawić indexowanie
- [x] Poprawić dodawanie rekordów - tak żeby kazdy nowy rekord nie miał nowych kolumn
- [x] Poprawić strzałki na uml



