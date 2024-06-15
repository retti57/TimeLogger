Projekt LOGGER został stworzony z myślą o ewidencjonowaniu czasów lotu personelu latającego w wojsku.
Opiera się na strukturze chronometrażu. Z założenia, użytkownikami serwisu będą wojskowi.
<br>

Administator zmuszony jest wcześniej utworzyć bazę osób, które są personelem latającym. 
Jest to konieczne by prawidłowo utworzyć Log, gdyż należy podać skład załogi biorącej udział w locie.  
Można dokonać tego z panelu administratra.

<br>
Do serwisu należy założyć konto oraz się zalogować. Od tego momentu wszystkie zarejestrowane logi w serwisie, 
w których użytkownik brał udział 
będą wyświetlały się w zakładce Logi. Każdy z użytkowników będzie widział tylko te logi, w których został wpisany. 
Dostęp do wszytkich logów w bazie ma administrator z panelu administratora.
<br>
Dodatkowo kazdy ma możliwość napisać notatki/uwagi bezpośrednio do administratora.
<br>

SPIDERPOINTs 

Jest to dodatkowa funkcjonalność nie wymagająca zalogowania do seriwsu. Funkcjonalnośc ta tworzy plik z listą punktów 
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
