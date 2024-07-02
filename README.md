# Projekt Kodowania ANS

Ten projekt to zadanie programistyczne zrealizowane przez trzyosobowy zespół w trakcie studiów. Głównym celem projektu jest implementacja algorytmów kodowania i dekodowania Asymmetric Numeral Systems (ANS), wraz z dodatkowymi funkcjonalnościami, takimi jak obliczanie entropii i generowanie plików.

## Spis Treści
- [Struktura Projektu](#struktura-projektu)
- [Pliki i Katalogi](#pliki-i-katalogi)
- [Instalacja](#instalacja)
- [Użycie](#użycie)
- [Autorzy](#autorzy)

## Struktura Projektu

Projekt jest zorganizowany w różne skrypty Python, z których każdy odpowiada za określoną część procesu kodowania i dekodowania ANS. Dodatkowo, istnieją katalogi zawierające obrazy testowe i rozkłady używane w projekcie.

## Pliki i Katalogi

- **obrazy_testowe/**: Katalog zawierający obrazy testowe używane w projekcie.
- **rozklady_testowe/**: Katalog zawierający testowe rozkłady.
- **ans_coder.py**: Skrypt implementujący algorytm kodowania ANS.
- **ans_decoder.py**: Skrypt implementujący algorytm dekodowania ANS.
- **communication.py**: Skrypt realizujący funkcje do zapisu oraz odczytu danych z pliku .txt.
- **entropy.py**: Skrypt do obliczania entropii danych.
- **generate_txt_file.py**: Skrypt do odczytu plików .pgm.
- **histogram.py**: Skrypt do tworzenia histogramów z danych.
- **main.py**: Główny skrypt, który integruje wszystkie funkcjonalności i uruchamia projekt.

## Instalacja

Aby uruchomić ten projekt, musisz mieć zainstalowany Python na swoim komputerze. Możesz go pobrać ze strony [python.org](https://www.python.org/).

1. Sklonuj repozytorium:
    ```sh
    git clone https://github.com/twoje-repo/ans-coding-project.git
    ```
2. Przejdź do katalogu projektu:
    ```sh
    cd ans-coding-project
    ``'

## Użycie
Proces kodowania oraz dekodowania został zrealizowany w pliku main.py.
Przed odpaleniem pliku main.y należy przekonwertować plik .pgm. Aby to zrealizować należy w 36 linijce pliku generate_txt_file.py wprowadzić odpowiednią ścieżkę dostępu.

## Autorzy

Projekt został wykonany przez trzyosobowy zespół. W skład zespołu wchodzą:
- Banach Maksymilian
- Przesmycki Jakub
- Bogumił Karol
