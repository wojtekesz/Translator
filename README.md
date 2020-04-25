# Translator
Translator jest implementacją translatora gaderypoluki oraz szyfru Cezara w Pythonie. Zawiera logikę biznesową w formie klasy.
## Technologie
* Python 3.7 i wyżej
* unittest
* pytest

### pytest
Przed użyciem biblioteki pytest należy upewnić się co do wcześniejszej instalacji za pomocą modułu pip, np.: `py -m pip install pytest`.

### Uruchamianie testów
#### unittest

`py -m unittest tests/unittest_catalogtest.py`
#### pytest

`py -m pytest tests/pytest_catalogtest.py`

#### skryptem
./run_tests.sh

#### Docker
```
docker-compose up
docker-compose run --rm app ./run_tests.sh
```
