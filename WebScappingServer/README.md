# README for WebScappingServer

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

