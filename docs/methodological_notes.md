# Note metodologiche

## Selezione del dataset

Il corpus di partenza comprendeva sei testimoni manoscritti, ma per questa fase del progetto si è scelto di concentrarsi su due testimoni:

- Prague D.54
- Wien 4941

La sezione selezionata corrisponde alla prima unità argomentativa del testo _Nota quod sacro concilio non est detrahendum_, per poter, almeno inizialemente, focalizzarci su un confronto controllabile e limitato 

## Correzioni preliminari del file XML-TEI

Prima dell’elaborazione computazionale, il file XML-TEI ha richiesto alcune correzioni tecniche per poter essere letto correttamente in Python. In particolare, sono emersi due problemi relativi agli identificatori XML:
- un valore di xml:id iniziava con un numero (4941);
- alcuni valori di xml:id non erano unici all’interno del documento.

Sono quindi stati corretti per rendere il documento parsabile e utilizzabile in un workflow computazionale riproducibile.

## Selezione delle unità di confronto

In una prima fase è stata considerata la possibilità di usare i paragrafi (<p>) come unità di confronto. Tuttavia, l’analisi del file TEI ha mostrato che la segmentazione in paragrafi non è parallela nei due testimoni. Il progetto utilizza quindi gli elementi TEI: <seg type="argument">

La prima sezione selezionata contiene sei segmenti argomentativi per ciascun testimone. Il dataset elaborato contiene quindi dodici righe complessive: sei segmenti per Prague D.54 e sei segmenti per Wien 4941.

## Estrazione del testo

La funzione di estrazione tramite Python preserva il contenuto testuale leggibile degli elementi, includendo le espansioni abbreviative, ed esclude i commenti XML. Il risultato dell’estrazione è stato organizzato in un dataset tabellare con le seguenti colonne principali:

- witness: identificatore tecnico del testimone;
- manuscript: etichetta leggibile del manoscritto;
- section_title: titolo della sezione;
- argument_n: numero del segmento argomentativo;
- text_expanded: testo estratto in forma leggibile;
- text_normalized: testo normalizzato per la comparazione computazionale.

Il dataset viene esportato come: data/processed/segments_dataset.csv

## Normalizzazione

Il workflow distingue tra text_expanded e text_normalized. La colonna text_expanded conserva il testo estratto dal TEI in forma leggibile. La colonna text_normalized viene invece usata per il calcolo della similarità.

La normalizzazione applicata comprende:
- conversione in minuscolo;
- rimozione della punteggiatura;
- normalizzazione degli spazi;
- ricomposizione selettiva di parole divise da fine riga o da divisione grafica.

Durante l’estrazione, alcune parole risultavano separate perché nel manoscritto o nella trascrizione erano divise a fine riga: _con cilium, difficul tates, obe diunt, Im perator_. 
Queste divisioni sono state mantenute nella colonna text_expanded, ma ricomposte nella colonna text_normalized, perché avrebbero inciso artificialmente sulle misure basate sui token.

## Valutazione della similarità

La similarity evaluation confronta i segmenti argomentativi corrispondenti nei due testimoni (D54 argument 1 con 4941 argument 1 ecc).

L’obiettivo è rispondere a due domande complementari:_i due segmenti condividono lo stesso materiale lessicale?_ _le parole condivise compaiono nello stesso ordine?_

Per questo motivo sono state selezionate due misure di similarità: Jaccard similarity, che misura la sovrapposizione lessicale tra due testi, indipendentemente dall’ordine delle parole e Longest Common Subsequence similarity, che misura quanta parte del materiale condiviso appare nello stesso ordine nei due testi.

## Risultati della similarity evaluation

Dopo la normalizzazione, i risultati principali sono i seguenti:

Argument	Jaccard similarity	LCS similarity	D54 tokens	4941 tokens	Interpretazione
- 1	0.273	0.429	7	7	bassa similarità
- 2	0.760	0.857	28	28	alta similarità lessicale e sequenziale
- 3	0.875	0.609	23	14	alto overlap lessicale, minore similarità sequenziale
- 4	0.882	0.944	18	18	alta similarità lessicale e sequenziale
- 5	0.632	0.783	20	23	minore overlap lessicale, ma sequenza relativamente stabile
- 6	0.913	0.909	22	22	alta similarità lessicale e sequenziale

Questi risultati vengono esportati nel file: outputs/similarity_by_segment.csv

## Interpretazione dei risultati

Qui di seguito una prima analisi condotta partire dai risultati ottenuti: 

I segmenti più stabili, e quindi con valori più alti, sono 6, 4 e 2.

L’argomento 6 presenta il valore più alto della Jaccard similarity (0.913) e un valore molto alto di LCS similarity (0.909). Questo indica che i due testimoni condividono quasi lo stesso materiale lessicale (notiamo la variante grafica concilium/consilium) e mantengono una sequenza testuale molto simile (est prima e dopo tam magnus), con pochissime differenze che non alterano la struttura complessiva del segmento.

L’argomento 4 presenta invece il valore più alto di LCS similarity (0.944), insieme a una Jaccard similarity molto alta (0.882); questo perchè i due testimoni conservano lo stesso ordine testuale, cambia solo il tempo verbale confirmarunt/confirmaventur.

Anche l’argomento 2 mostra valori abbastanza alti in entrambe le misure: Jaccard = 0.760 e LCS = 0.857. In questo caso, la sequenza rimane intatta, cambiano le varianti grafiche o morfologiche.

Gli argomenti 1, 3 e 5 mostrano risultati più problematici o meno uniformi, ma per ragioni diverse.

Quello con i valori più bassi è l'argomento 1: Jaccard similarity = 0.273 e LCS similarity = 0.429. Tuttavia, questo segmento è molto breve, con 7 token in entrambi i testimoni. Di conseguenza, le misure sono particolarmente sensibili anche a piccole variazioni. La differenza tra forme come instituunt/instituerunt e celebravunt/celebrarunt pesano sul punteggio abbassandolo.

L’argomento 3 è particolarmente interessante perché presenta una Jaccard similarity alta (0.875), ma una LCS similarity più bassa (0.609). Questo significa che i due testimoni condividono molto materiale lessicale, ma non lo conservano nella stessa estensione sequenziale. Inoltre, la differenza di lunghezza è significativa: D54 contiene 23 token, mentre 4941 ne contiene 14 poichè include anche la parte et dampnare omnes hereses que surgunt in ecclesia dei. Il risultato suggerisce quindi una possibile omissione o compressione in 4941.

L’argomento 5 mostra un caso diverso: la Jaccard similarity è più bassa (0.632), mentre la LCS similarity è relativamente alta (0.783). Questo suggerisce che la sequenza resta riconoscibile, ma con differenze lessicali e con materiale aggiuntivo in 4941: il troncamento di episcopi nel testimone 1 e l'aggiunta della formula finale quod nos obediamus nel testimone 2.
