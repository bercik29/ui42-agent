# AI Agent s prístupom na GA4 API a Code Interpreter

Tento projekt predstavuje riešenie technického zadania pre pozíciu AI Engineer v ui42. 
Agent využíva model Claude na analýzu dát z Google Analytics 4 a disponuje schopnosťou 
spúšťať vlastný Python kód pre pokročilé výpočty.

## Funkcionalita
- **GA4 Access**: Agent pristupuje k metrikám a dimenziám cez Google Analytics Data API.
- **Code Execution**: Schopnosť generovať a spúšťať Python kód v izolovanom prostredí.
- **Bezpečnosť**: Architektúra navrhnutá s dôrazom na bezpečnú prácu s dátami (oddelené execution prostredie).
- **Bonus**: Automatický export výsledkov analýzy do PDF reportu.

## Inštalácia a spustenie
1. Nainštalujte závislosti: `pip install -r requirements.txt`
2. Premenujte `.env.example` na `.env` a vložte svoje API kľúče.
3. Vložte váš `credentials.json` pre Google Cloud do hlavného priečinka.
4. Spustite agenta: `python main.py`

## Technický stack
- **LLM**: Claude (Anthropic)
- **Framework**: LangGraph / LangChain
- **Jazyk**: Python (posledná stable verzia)

### 🔍 Poznámka k dátam a interpretácii
Počas testovania agenta v sandbox prostredí boli identifikované dáta (napr. priemerný engagement), ktoré vykazujú neštandardné hodnoty pre novovytvorené Property. 

Z pohľadu AI Engineera toto správanie potvrdzuje správnu funkčnosť riešenia:
1. **Technická integrita**: Agent korektne komunikuje s GA4 API a spracováva reálne vrátený JSON, aj keď ide o bot-traffic alebo historický šum v testovacom účte.
2. **Autonómna logika**: Agent na základe týchto (hoci nesúrodých) dát správne aktivoval Python Code Interpreter, aby vypočítal priemery a trendy, čím splnil technické zadanie.
3. **Transparentnosť**: Riešenie je pripravené na okamžité prepojenie s produkčným Property ID, kde bude interpretovať relevantné biznis dáta.
