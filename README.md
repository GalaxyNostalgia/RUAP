Life Expectancy Predictor

Web aplikacija za predviđanje životnog vijeka temeljena na WHO podacima. Korisnik unosi zdravstvene i socioekonomske pokazatelje, a model vraća predviđeni životni vijek u godinama.

Ulazne značajke modela

Model koristi 5 najkoreliranih značajki s životnim vijekom:

1. HIV/AIDS – smrtnost od HIV/AIDS-a na 1000 stanovnika
2. Income Composition of Resources – HDI indeks raspodjele prihoda (0–1)
3. Adult Mortality – stopa smrtnosti odraslih na 1000 stanovnika
4. BMI – prosječni indeks tjelesne mase populacije
5. Schooling – prosječan broj godina školovanja

Instalacija

pip install -r requirements.txt

Pokretanje:

Pokrenuti dva terminala:

Terminal 1 – proxy server:

    python proxy_server.py

Terminal 2 – lokalni web server:

    python -m http.server 8000


Zatim otvoriti u pregledniku: http://localhost:8000/index.html


- Juraj Birović

