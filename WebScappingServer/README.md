# README for WebScappingServer
## UML:
![](https://i.imgur.com/H4nopnB.png)




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
.Scapping/bin/activate
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
- [ ] Zrobienie połączenie do bazy danych dla TopFx
- [ ] Zrobienie połączenia do bazy danych dla InternetowegoKantoru
- [ ] Zrobienie klasy main
- [ ] Zrobienie w klasie main funkcji która odpowiada za działanie w pętli 
- [ ] Zrobienie w klasie main funkcji która odpowiada za testy poprawnego działania



