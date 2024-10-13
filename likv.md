Spesifikasjon av Python versjonen av Likv
=========================================
Kjell Inge Tomren, kitomren@gmail.com, oktober 2027

## beskrivelse av likv
- utgangspunktet er en tekstfil med poster over ulike utgifter og inntekter
- utgiftene kan være faste eller variable
- variable kostnader ble beregnet etter en formel til dc
- perioden kan være ukentlig, månedlig, eller årlig
- ut fra postene genereres en liste med datoer og utgift/intekt
- listen sorteres etter dato og saldo genereres for hver dato med endring

## spec av Python-versjonen
- bruke csv først, XML er alternativ 
- arkitektur: datalag, forretningslogikk og presentsasjonslag
- MVP: faste månedlige utgifter og inntekter, resultater i CSV-fil

### versjon 0.1
- datoer og faste månedlige utgifter

### versjon 0.2
- årlige, månedlige og ukentlige utgifter

### versjon 0.3
- tekst-basert input-modul, list, edit, add, delete

### versjon 1.0
- web basert input-modul

## ønsker for framtidig versjoner
- nettsted for modellering av privatøkonomi
- legge inn inntekter og utgifter og umiddelbart se konsekvenser i likviditeten
- delt skjerm med inntekter og ugifter i et vindu og en graf som viser likviditeten under
- kan gjerne bli en mobilapp i tillegg til nettstedet
- modellering av privatøkonom med basis i normtall for utgifter
- brukergrensesnitt som er tilpasset mobil
