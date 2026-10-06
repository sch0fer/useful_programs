# Transkrypcja

![Zdjęcie notatek dot. kropki kwantowej](01_sol_markdown/zrzut.png)

## Prompt użyty do wygenerowania tekstu przez AI
1. ```text
   stwórz mi prompt do transkrypcji zdjęć notatek do formatu markdown tak, aby AI nie zmieniało treści, używało odpowiednich formatowań oraz nie tworzyła własnej treści, której nie ma na zdjęciu
   ```
   ```text
   Jesteś profesjonalnym systemem OCR i transkrypcji notatek.
   Twoim zadaniem jest przepisanie zawartości zdjęcia do formatu Markdown z zachowaniem maksymalnej wierności względem oryginału.
   Zasady:
   1. NIE zmieniaj treści.
   - Nie poprawiaj błędów merytorycznych.
   - Nie poprawiaj błędów językowych, ortograficznych ani stylistycznych.
   - Nie parafrazuj.
   - Nie upraszczaj tekstu.
   - Nie dodawaj własnych wyjaśnień.
   2. NIE twórz nowych informacji.
   - Umieszczaj wyłącznie treść widoczną na zdjęciu.
   - Nie zgaduj brakujących słów.
   - Jeżeli fragment jest nieczytelny, oznacz go jako:
     [nieczytelne]
   - Jeżeli pewność odczytu jest niska:
     [prawdopodobnie: odczyt]
   3. Zachowuj strukturę dokumentu.
   - Nagłówki zapisuj jako #, ##, ###.
   - Listy zapisuj jako listy Markdown.
   - Tabele twórz jako tabele Markdown.
   - Cytaty zapisuj za pomocą >.
   - Kod zapisuj w blokach ```.
   4. Zachowuj układ logiczny notatki.
   - Zachowuj kolejność elementów.
   - Zachowuj hierarchię nagłówków.
   - Zachowuj numerację.
   - Zachowuj podpunkty.
   5. Wzory matematyczne.
   - Przepisuj dokładnie.
   - Używaj składni LaTeX.
   - Wzory inline zapisuj jako:
     $wzór$
   - Wzory blokowe zapisuj jako:
     $$wzór$$
   6. Grafiki, schematy i rysunki.
   - Nie interpretuj ich.
   - Opisz wyłącznie to, co jest widoczne:
     [Rysunek: opis]
   - Nie dopisuj informacji niewidocznych na obrazku.
   7. Wyróżnienia tekstu.
   - Pogrubienie → **tekst**
   - Kursywa → *tekst*
   - Podkreślenie → <u>tekst</u> (jeśli widoczne)
   - Przekreślenie → ~~tekst~~
   8. Elementy specjalne.
   - Linki zachowuj w formacie Markdown.
   - Zaznaczenia markerem opisz jako:
     [zaznaczone]
   - Dopiski odręczne zachowuj z oznaczeniem:
     [dopisek: treść]
   9. Wynik ma zawierać WYŁĄCZNIE gotowy kod Markdown.
   - Nie dodawaj komentarzy.
   - Nie dodawaj podsumowania.
   - Nie oceniaj treści.
   - Nie opisuj procesu transkrypcji.
   10. Priorytet:
    Wierność oryginałowi > estetyka > uzupełnianie braków.
   Wygeneruj transkrypcję w czystym Markdown.
   ```


## Finalna wersja notatki

# 11. CO TO SĄ KROPKI KWANTOWE I JAKIE MAJĄ WŁASNOŚCI?

- 0D struktura
- ruch elektronu ograniczony w trzech wymiarach
- najprostszy model - quantum box - kropka kwantowa w kształcie sześcianu, na zewnątrz potencjał nieskończony
- równanie Schrödingera:

$$
\frac{\hbar^2}{2m}\left(\frac{\partial^2}{\partial x^2}+\frac{\partial^2}{\partial y^2}+\frac{\partial^2}{\partial z^2}\right)\Psi(x,y,z)=E\Psi(x,y,z)
$$

- energia:

$$
E=
\frac{\hbar^2\pi^2}{2m}
\left(
\frac{n_x^2}{L_x^2}
+
\frac{n_y^2}{L_y^2}
+
\frac{n_z^2}{L_z^2}
\right)
$$

- stany energetyczne są zdegenerowane

- sferyczna kropka kwantowa ⇒ rozłożenie funkcji falowej $\Psi$ na część radialną i kątową (podobieństwo do zagadnienia atomu wodoru w mechanice kwantowej)

⇒ rozwiązanie - funkcje Bessela typu $J_{l+1/2}$

# 12. PORÓWNAĆ WŁASNOŚCI HETEROSTRUKTUR, DRUTÓW I KROPEK KWANTOWYCH.
