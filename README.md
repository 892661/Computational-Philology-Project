## Overview

Questo lavoro nasce all’interno di un progetto più ampio di codifica TEI-XML e visualizzazione tramite TEI Publisher del testo _Nota quod sacro concilio non est detrahendum_ di Johannes Hildessen, nell’ambito di Antidote. Il notebook qui presentato si concentra sul trasformare parte della codifica TEI in dati comparabili e usare misure computazionali per analizzare la variazione tra due dei sei testimoni.

## Repository structure

```text
computational-philology-project/
├── README.md
├── data/
│   ├── raw/
│   │   └── merged_manuscripts.xml
│   └── processed/
│       └── segments_dataset.csv
├── notebooks/
│   └── textual_variation_workflow.ipynb
├── outputs/
│   ├── similarity_by_segment.csv
│   ├── comparison_by_segment.csv
│   ├── similarity_extended_by_segment.csv
│   ├── argument3_alignment.csv
│   ├── argument3_alignment_differences.csv
│   ├── variant_classification.csv
│   ├── variant_type_counts.csv
│   └── linguistic_level_counts.csv
└── docs/
    ├── TEIP_screenshot
    └── methodological_notes.md
   ```
