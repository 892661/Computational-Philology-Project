# Methodological Notes

## Dataset selection

The original corpus included six manuscript witnesses. Three of them had a more advanced TEI encoding, but this project focuses on two witnesses in order to build a small, coherent and reproducible workflow.

The selected witnesses are:

- D.54
- 4941

The selected section is the first argumentative unit: *Nota quod sacro concilio non est detrahendum*.

The unit of comparison is the TEI element `<seg type="argument">`.

## First encoding issue

The raw TEI file contains the identifier `xml:id="4941"`. Since XML identifiers should not begin with a digit, this issue is documented rather than silently corrected in the raw data.
