Projekt LOGGER został stworzony z myślą o ewidencjonowaniu czasów lotu personelu latającego w wojsku.
Opiera się na strukturze chronometrażu. Z założenia, użytkownikami serwisu będą wojskowi.

<br>
Przygotowanie środowiska:
1) Zainstaluj wymienione biblioteki : django, django-crispy-forms,crispy-bootstrap4, requests
2) skopiuj plik logger do folderu gdzie masz przygotowane środowisko do projektu i wejdź do tego folderu. W tym miejscu powienien znajdować się plik manage.py.
3) utwórz konto administratora wpisując w terminalu: <code>python manage.py createsuperuser</code>. Tym kontem należy zalogować się do panelu administratora na adres 
localhostu tj. http://127.0.0.1:8000/admin/
4) następnie utwórz migracje <code>python manage.py makemigrations</code>.
5) zapisz migracje <code>python manage.py migrate</code>.
W tym momencie utworzysz z pomocą Django bazę danych potrzebną do prawidłowego działania.


<br>
Administator zmuszony jest wcześniej utworzyć bazę osób, które są personelem latającym oraz dostępnych statków 
powietrznych. 
Jest to konieczne by prawidłowo utworzyć Log, gdyż należy podać skład załogi biorącej udział w locie.  
Można dokonać tego z panelu administratra.

<br>
Adres pod którym należy wejść na stronę to: http://127.0.0.1:8000/logger/
Do serwisu należy założyć konto oraz się zalogować. Od tego momentu wszystkie zarejestrowane logi w serwisie, 
w których użytkownik brał udział 
będą wyświetlały się w zakładce Logi. Każdy z użytkowników będzie widział tylko te logi, w których został wpisany. 
Dostęp do wszytkich logów w bazie ma administrator z panelu administratora.
<br>
Dodatkowo kazdy ma możliwość napisać notatki/uwagi bezpośrednio do administratora.
<br>


OBOWIĄZKOWE PRZYGOTOWANIE Z POZIOMU PANELU ADMINISTRATORA
<BR>
1) TWORZENIE PRESONELU LATAJĄCEGO

Po zalogowaniu nalezy kliknąć w zakladkę po lewej stronie o nazwie " Personale latający ", następnie
"Add personel" po prawej stronie w szarym przycisku i postępować zgodnie z formularzem.
Administrator w późniejszym czasie ma możliwość połączyć utworzony profil presonelu z właściwym kontem użytkownika jeśli ten 
wcześniej się nie zarejestrował w serwisie. Pomimo nie wymaganego pola "function on board" należy wybrać właściwą funkcję 
dla towrzonego profilu i zapisać. Od tego momentu ten profil będzie widoczny przu tworzeniu logu.

<br>

2) TWORZENIE ŚMIGŁOWCA

Po zalogowaniu nalezy kliknąć w zakladkę po lewej stronie o nazwie " Śmigłowce ", następnie
"Add śmigłowiec" po prawej stronie w szarym przycisku i postępować zgodnie z formularzem i zapisać.
Od tego momentu ten śmigłowiec będzie widoczny przy tworzeniu logu.

<br>


TWORZENIE LOGU z panelu administratora

By móc utworzyć nowy log korzystając z panelu administratora nalezy kliknąć w zakladkę po lewej stronie o nazwie 
" Logi ", następnie "Add log" po prawej stronie w szarym przycisku i postępować zgodnie z formularzem i zapisać.<br>
WAŻNE! Pamiętaj by podać czas z sekundami równymi zeru, np.: <i> 08:08:00 , NIE 08:08:23</i></b> 



SPIDERPOINTs 

Jest to dodatkowa funkcjonalność nie wymagająca zalogowania do serwisu. 
Należy zainstalować w środowisku wirtualnym paczkę 'spiderpoints-0.0.12.tar.gz' znajdującą się pod 
ścieżką 'logger/logger/spiderpoints-0.0.12.tar.gz'. 
Ścieżka do kodu paczki na githubie:  https://github.com/retti57/gridOfPoints/
Alternatywnie można utworzyć API i się połączyć do punktu bez konieczności instalowania. Kod dostępny na githubie:
https://github.com/retti57/SpiderPoints_api


Funkcjonalnośc ta tworzy plik z listą punktów 
do zapisania w nawigacji lotniczej.
Plik ten składa się z siatki punktów w kształcie kwadratu.
By utworzyć plik należy podać :
1) współrzędne punktu będącego lewym górny narożnikiem siatki
2) liczbę punktów występujących w rzędzie 
3) odległość miedzy punktami w kilometrach
Czyli podając współrzędne np z google maps 52.41242 18.31424 , odległość 3 oraz ilość powtórzeń 5 otrzymamy plik,
w którym znajdzie się lista 25 punktów w kształcie kwadratu 5x5 punktów, a każdy punkt będzie miał odległość 
od siebie 3 km. 
Nie wspiera pozostałych formatów współrzędnych tj. UTM i MGRS.
