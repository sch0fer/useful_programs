# Programy użytkowe - pierwsze starcie

## Czym są Programy użytkowe?
Programy użytkowe to zajęcia przygotowujące studentów do odpowiedzialnego korzystanie z dobrodziejstw XXI-wiecznej technologii.

## Zakres materiału
Na zajęciach studenci będą pracować z licznymi technologiami, takimi jak: 
1. **markdown** - do tworzenia sformatowanego tekstu,
2. [**Colab**](http://colab.research.google.com/) - do tworzenia kodu w języku Python prosto z przeglądarki oraz wiele więcej,
3. **Git oraz [GitHub](https://github.com/)** - do zarządzania i publikowania projektów,
4. **VSCode** - do edytowania tekstu.

## Markdown
Markdown to tzw. *język znaczników*. Pozwala on na tworzenie sformatowanych dokumentów tekstowych za pomocą stosunkowo prostej składni. Do podstawowych znaczników formatujących należą:
- Nagłówki tworzy się za pomocą znaków "#" - im więcej, ~~maksymalnie 6~~, tym "mniejszy" nagłówek: 
```md
# Nagłówek 1
## Nagłówek 2
### Nagłówek 3
#### Nagłówek 4
##### Nagłówek 5
###### Nagłówek 6
```
- Tekst można też formatować za pomocą "*":
```md
*Ten tekst będzie pochylony*
**Ten tekst będzie pogrubiony**
***Ten tekst będzie i pochylony, i pogrubiony***
```
- Przydatne mogą być też przekreślenia:
```md
~~Tak się tworzy przekreślony tekst~~
```

## Zadania
- [x] Stworzyć plik README.md
- [ ] Użyć podstawowych formatowań formatu .md
- [ ] Napisać kod Python

## Zwykły tekst vs Markdown vs HTML

# Porównanie formatów plików: TXT, Markdown i HTML

| Cecha | Zwykły tekst (TXT) | Markdown (MD) | HTML |
|---------|---------|---------|---------|
| **Łatwość użycia** | ⭐⭐⭐⭐⭐ Bardzo łatwy | ⭐⭐⭐⭐ Łatwy | ⭐⭐ Wymaga znajomości składni |
| **Learning curve** | Minimalna | Niska | Średnia do wysokiej |
| **Czytelność w surowej postaci** | Bardzo wysoka | Wysoka | Średnia |
| **Obsługa nagłówków** | ❌ | ✅ | ✅ |
| **Obsługa list** | ❌ | ✅ | ✅ |
| **Obsługa tabel** | ❌ | ✅ | ✅ |
| **Obsługa obrazów** | ❌ | ✅ | ✅ |
| **Obsługa linków** | Tylko jako tekst | ✅ | ✅ |
| **Obsługa stylów (kolory, czcionki)** | ❌ | Ograniczona | ✅ |
| **Możliwość tworzenia układów stron** | ❌ | ❌ | ✅ |
| **Rozmiar plików** | Najmniejsze | Małe | Zwykle większe |
| **Popularne zastosowania** | Notatki, logi, konfiguracje | Dokumentacja, README, notatki techniczne | Strony internetowe, aplikacje webowe |
| **Wsparcie przez edytory** | Praktycznie wszystkie | Bardzo szerokie | Bardzo szerokie |
| **Możliwość automatycznej konwersji** | Ograniczona | Łatwa konwersja do HTML, PDF, DOCX | Łatwa konwersja do PDF |

## Python
Python to interpretowany język skryptowy, który dzięki swojej prostej składni jest idealnym wyborem dla początkujących użytkowników, którzy chcą zacząć tworzyć proste programy. Dzięki szerokiej bazie bibliotek można go użyć do niemal wszystkiego.

Prosty program liczący średnią ocen napisany w języku Python:
```python
grades = [3,4,2,5,1,3]
grades_sum = 0
for grade in grades:
  grades_sum += grade
average = grades_sum/len(grades)
print(average)
```

## LaTeX
Format markdown pozwala na embedowanie formatu LaTeX wprost do dokumentów .md. Pozwala to na tworzenie np. prac naukowych czy też książek. Format LaTeX może występować w jednej linii z tekstem: 
- Twierdzenie Pitagorasa: $a^2+b^2=c^2$
- Wzór na miejsca zerowe funkcji kwadratowej: $x_0=\frac{-b \pm \sqrt{b^2-4ac}}{2a}$
- Definicja sinusa dowolnego kąta: $\sin{\alpha}=\frac{y}{r}$

lub być zupełnie osobnym blokiem tekstu:

$$
a^2+b^2=c^2
$$

$$
x_0=\frac{-b \pm \sqrt{b^2-4ac}}{2a}
$$

$$
\sin{\alpha}=\frac{y}{r}
$$

## Obrazki
W formacie markdown można wyświetlać również obrazy:

![Wykres zależności y od x](wykres.png)





