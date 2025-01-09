

# Django Project

Acest fișier oferă instrucțiuni pentru clonarea, instalarea și configurarea unui proiect Django.

## Cerințe prealabile

Înainte de a începe, asigură-te că ai următoarele instalate pe sistemul tău:

- Python 3.8 sau mai recent
- Git
- Virtualenv
- Un manager de pachete precum pip

## Clonarea proiectului

Clonează acest repository din GitHub utilizând următoarea comandă:

```bash
git clone https://github.com/username/nume-proiect.git
```

Înlocuiește `username` cu numele utilizatorului GitHub și `nume-proiect` cu numele repository-ului.

După ce ai clonat repository-ul, navighează în directorul proiectului:

```bash
cd nume-proiect
```

## Configurarea mediului virtual

Creează un mediu virtual pentru a izola dependențele proiectului:

```bash
python -m venv venv
```

Activează mediul virtual:

- **Pe Linux/MacOS:**
  ```bash
  source venv/bin/activate
  ```

- **Pe Windows:**
  ```bash
  venv\Scripts\activate
  ```

## Instalarea dependențelor

Instalează pachetele necesare utilizând `pip` și fișierul `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Configurarea proiectului

1. Creează un fișier `.env` în directorul rădăcină al proiectului (dacă nu există deja). Adaugă variabilele de mediu necesare, cum ar fi:

   ```env
   SECRET_KEY=cheia_ta_secreta
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1,localhost
   DATABASE_URL=postgres://user:password@localhost:5432/database_name
   ```

   Poți utiliza `django-environ` pentru a citi aceste variabile în proiect.

2. Aplică migrațiile bazei de date:

   ```bash
   python manage.py migrate
   ```

3. (Opțional) Creează un superuser pentru a accesa panoul de administrare Django:

   ```bash
   python manage.py createsuperuser
   ```

## Rularea proiectului

Porneste serverul de dezvoltare utilizând comanda:

```bash
python manage.py runserver
```

Accesează proiectul în browser la adresa:

```
http://127.0.0.1:8000/
```

## Testare

Pentru a rula testele existente în proiect:

```bash
python manage.py test
```

## Contribuție

Dacă dorești să contribui la acest proiect:

1. Creează un fork al repository-ului.
2. Creează o ramură pentru modificările tale:

   ```bash
   git checkout -b feature/noua-functie
   ```

3. Fă commit și push modificările:

   ```bash
   git commit -m "Descriere modificări"
   git push origin feature/noua-functie
   ```

4. Creează un pull request pentru a trimite modificările tale.

## Licență

Acest proiect este distribuit sub licența [MIT](LICENSE).

