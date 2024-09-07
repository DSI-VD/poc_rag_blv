# File structure

Few points about file structure

## Find all possibles

`find . -type f | sed -n 's/.*\.\([^.]*\)$/\1/p' | sort | uniq -c | sort -rn`

```text
9086 akn
1313 pdf
1 gitignore
``` 

## Samples

`tree Actes/8df99d51-8df8-49ed-9ef5-2fa4817d0004`

```text
Actes/8df99d51-8df8-49ed-9ef5-2fa4817d0004
├── Version 01.01.2004.akn
├── Version 01.01.2005.akn
├── Version 01.01.2006.akn
├── Version 01.01.2007.akn
├── Version 01.01.2008.akn
├── Version 01.01.2009.akn
├── Version 01.01.2010.akn
├── Version 01.01.2011.akn
├── Version 01.01.2012.akn
├── Version 01.01.2013.akn
├── Version 01.01.2014.akn
├── Version 01.01.2015.akn
├── Version 01.01.2016.akn
├── Version 01.01.2017.akn
├── Version 01.01.2018.akn
├── Version 01.01.2019.akn
├── Version 01.01.2020.akn
├── Version 01.01.2021.akn
├── Version 01.01.2022.akn
├── Version 01.01.2023.akn
├── Version 01.01.2024.akn
├── Version 01.01.2025.akn <-- dans le futur
├── Version 01.04.2011.akn
├── Version 01.05.2005.akn
├── Version 01.07.2005.akn
├── Version 01.07.2019.akn
├── Version 01.07.2023.akn
├── Version 01.09.2018.akn
└── Version 01.10.2004.akn
```

`tree Actes/4a37f8a0-02b0-4a84-9e68-deae4495e02e`

```text
Actes/4a37f8a0-02b0-4a84-9e68-deae4495e02e
├── PDF FAO.pdf  <-- version pdf
├── Version 01.11.2024.akn
├── Version 02.09.2024.akn
├── Version 25.07.2024.akn
└── Version archivée.akn <-- Version sans date
```

# Content

`./Actes/9c77db6b-3c5b-4a4a-9fdb-2313882a9ffa/Version 01.12.2004.akn`

## Attachement

Find actes with attachment

`find ../Actes -type f -exec grep -l "<attachment>" {} + | sed -E 's|/[^/]+$||' | sort -u`

<details>
<summary>Content view</summary>

```xml
<?xml version="1.0" encoding="UTF-8"?><akomaNtoso xmlns="http://docs.oasis-open.org/legaldocml/ns/akn/3.0">
  <act name="9c77db6b-3c5b-4a4a-9fdb-2313882a9ffa">
    
      <p>
        <docType>RÈGLEMENT</docType>
        <docNumber>172.215.1</docNumber>
      </p>
      
    <attachments>
      <attachment>
        <num>1</num><heading>172.215.1.Commentaires</heading><documentRef eId="id-389f5fed-6fe4-4514-9c46-83a830e03d8e" href="data:application/pdf;base64,JVBERi0xLjMKJaqrrK0KNCAwIG9iago8PCAvVHlwZSAvSW5mbwovUHJvZHVjZXIgKEZPUCAwLjIwLjUpID4+CmVuZG9iago1IDAgb2JqCjw8IC9MZW5ndGggNTIyIC9GaWx0ZXIgWyAvQVNDSUk4NURlY29kZSAvRmxhdGVEZWNvZGUgXQogPj4Kc3RyZWFtCkdhczFcOWxsZFgnWU8jZmhDV11OV2kmWUI+RVZQZ1NLOnQkYWVlRGtNJXRhXzBJYiRBXko+W19SQ1hDS1AqI0QpQ0E2dGRiISgyPiIvbSZsbDdNJTlHZy80dCkkNl1INW9YRishMzdeIyoyMlpVOCYhZU5jMEk5MGlAbCVPJk5ccUJqKFZVMkQpYS8rNGU5Vzs1RSQ3ImgkPT5IY0w4Qy1jbEMqQk8laysrRyc8XClXYzVeJyRNWHFYaz8wWDU3Ql90K18rSD8rOSkjNlskanFebUJNQzo7Y0lvYlo7akk8TURMQjguKUA8VTtAR0U4ZS80NHJzbHMnMSZaJkBMT2spLjBIcTxKUzxxc05ScUwuLTdcKFkwLTUsb0RFPVpucUVcbWxHVzdlSjYvLkIlTl5RczAzXVU5WlwlLyxDLSVAQVdNcSZsJ2lyYWU/c2xKTkwiUmljV1U3Tl1eTC9NOElLaDIuRG8vO0J1LmpoRSIjSTFHKSRYZ0MlUG8ocGJMYFVJbm5NRy5FImY/cm1NQUMjUyE+RmpxPUIjKTU0VlpARUY/cVNGKS88IWQzUXNQKXEyKFheamNXIkVeSiMsSENrY0gwU2JqaShuJ3ItYSFEQCk6TipiJUc9NCVqbHRXJV9kQGsxUUtjI2JfYzkjQkNKJi1DZTwraSpmW21DSGltO1ZsQURGMH4+CmVuZHN0cmVhbQplbmRvYmoKNiAwIG9iago8PCAvVHlwZSAvUGFnZQovUGFyZW50IDEgMCBSCi9NZWRpYUJveCBbIDAgMCA1OTUgODQyIF0KL1Jlc291cmNlcyAzIDAgUgovQ29udGVudHMgNSAwIFIKPj4KZW5kb2JqCjcgMCBvYmoKPDwgL1R5cGUgL0ZvbnREZXNjcmlwdG9yCi9Gb250TmFtZSAvVGltZXNOZXdSb21hbixJdGFsaWMKL0ZvbnRCQm94ICBbLTQ5NyAtMzA2IDExMjAgMTAyM10gCi9GbGFncyA5NwovQ2FwSGVpZ2h0IDY2MgovQXNjZW50IDg5MQovRGVzY2VudCAtMjE2Ci9JdGFsaWNBbmdsZSAwCi9TdGVtViAwCiA+PgplbmRvYmoKOCAwIG9iago8PCAvVHlwZSAvRm9udAovU3VidHlwZSAvVHJ1ZVR5cGUKL05hbWUgL0YxOAovQmFzZUZvbnQgL1RpbWVzTmV3Um9tYW4sSXRhbGljCi9FbmNvZGluZyAvV2luQW5zaUVuY29kaW5nCi9GaXJzdENoYXIgMAovTGFzdENoYXIgMjU1Ci9XaWR0aHMgOSAwIFIKL0ZvbnREZXNjcmlwdG9yIDcgMCBSID4+CmVuZG9iago5IDAgb2JqClsgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyAyNTAgMzMzIDQxOSA1MDAgNTAwIDgzMyA3NzcgMjEzIDMzMyAzMzMgNTAwIDY3NCAyNTAgMzMzIDI1MCAyNzcgNTAwIDUwMCA1MDAgNTAwIDUwMCA1MDAgNTAwIDUwMCA1MDAgNTAwIDMzMyAzMzMgNjc0IDY3NCA2NzQgNTAwIDkxOSA2MTAgNjEwIDY2NiA3MjIgNjEwIDYxMCA3MjIgNzIyIDMzMyA0NDMgNjY2IDU1NiA4MzMgNjY2IDcyMiA2MTAgNzIyIDYxMCA1MDAgNTU2IDcyMiA2MTAgODMzIDYxMCA1NTYgNTU2IDM4OSAyNzcgMzg5IDQyMSA1MDAgMzMzIDUwMCA1MDAgNDQzIDUwMCA0NDMgMjc3IDUwMCA1MDAgMjc3IDI3NyA0NDMgMjc3IDcyMiA1MDAgNTAwIDUwMCA1MDAgMzg5IDM4OSAyNzcgNTAwIDQ0MyA2NjYgNDQzIDQ0MyAzODkgMzk5IDI3NCAzOTkgNTQxIDM1MCA1MDAgMzUwIDMzMyA1MDAgNTU2IDg4OSA1MDAgNTAwIDMzMyAxMDAwIDUwMCAzMzMgOTQzIDM1MCA1NTYgMzUwIDM1MCAzMzMgMzMzIDU1NiA1NTYgMzUwIDUwMCA4ODkgNTQxIDk3OSAzODkgMzMzIDY2NiAzNTAgMzg5IDU1NiAyNTAgMzg5IDUwMCA1MDAgNTAwIDUwMCAyNzQgNTAwIDMzMyA3NTkgMjc1IDUwMCA2NzQgMzMzIDc1OSA1MDAgMzk5IDU0OCAyOTkgMjk5IDMzMyA1NzYgNTIyIDI1MCAzMzMgMjk5IDMxMCA1MDAgNzUwIDc1MCA3NTAgNTAwIDYxMCA2MTAgNjEwIDYxMCA2MTAgNjEwIDg4OSA2NjYgNjEwIDYxMCA2MTAgNjEwIDMzMyAzMzMgMzMzIDMzMyA3MjIgNjY2IDcyMiA3MjIgNzIyIDcyMiA3MjIgNjc0IDcyMiA3MjIgNzIyIDcyMiA3MjIgNTU2IDYxMCA1MDAgNTAwIDUwMCA1MDAgNTAwIDUwMCA1MDAgNjY2IDQ0MyA0NDMgNDQzIDQ0MyA0NDMgMjc3IDI3NyAyNzcgMjc3IDUwMCA1MDAgNTAwIDUwMCA1MDAgNTAwIDUwMCA1NDggNTAwIDUwMCA1MDAgNTAwIDUwMCA0NDMgNTAwIDBdCmVuZG9iagoxMCAwIG9iago8PCAvVHlwZSAvRm9udAovU3VidHlwZSAvVHlwZTEKL05hbWUgL0YxCi9CYXNlRm9udCAvSGVsdmV0aWNhCi9FbmNvZGluZyAvV2luQW5zaUVuY29kaW5nID4+CmVuZG9iagoxMSAwIG9iago8PCAvVHlwZSAvRm9udERlc2NyaXB0b3IKL0ZvbnROYW1lIC9UaW1lc05ld1JvbWFuCi9Gb250QkJveCAgWy01NjggLTMwNiAyMDAwIDEwMDZdIAovRmxhZ3MgMzMKL0NhcEhlaWdodCA2NjIKL0FzY2VudCA4OTEKL0Rlc2NlbnQgLTIxNgovSXRhbGljQW5nbGUgMAovU3RlbVYgMAogPj4KZW5kb2JqCjEyIDAgb2JqCjw8IC9UeXBlIC9Gb250Ci9TdWJ0eXBlIC9UcnVlVHlwZQovTmFtZSAvRjE1Ci9CYXNlRm9udCAvVGltZXNOZXdSb21hbgovRW5jb2RpbmcgL1dpbkFuc2lFbmNvZGluZwovRmlyc3RDaGFyIDAKL0xhc3RDaGFyIDI1NQovV2lkdGhzIDEzIDAgUgovRm9udERlc2NyaXB0b3IgMTEgMCBSID4+CmVuZG9iagoxMyAwIG9iagpbIDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgMjUwIDMzMyA0MDggNTAwIDUwMCA4MzMgNzc3IDE4MCAzMzMgMzMzIDUwMCA1NjMgMjUwIDMzMyAyNTAgMjc3IDUwMCA1MDAgNTAwIDUwMCA1MDAgNTAwIDUwMCA1MDAgNTAwIDUwMCAyNzcgMjc3IDU2MyA1NjMgNTYzIDQ0MyA5MjAgNzIyIDY2NiA2NjYgNzIyIDYxMCA1NTYgNzIyIDcyMiAzMzMgMzg5IDcyMiA2MTAgODg5IDcyMiA3MjIgNTU2IDcyMiA2NjYgNTU2IDYxMCA3MjIgNzIyIDk0MyA3MjIgNzIyIDYxMCAzMzMgMjc3IDMzMyA0NjkgNTAwIDMzMyA0NDMgNTAwIDQ0MyA1MDAgNDQzIDMzMyA1MDAgNTAwIDI3NyAyNzcgNTAwIDI3NyA3NzcgNTAwIDUwMCA1MDAgNTAwIDMzMyAzODkgMjc3IDUwMCA1MDAgNzIyIDUwMCA1MDAgNDQzIDQ3OSAyMDAgNDc5IDU0MSAzNTAgNTAwIDM1MCAzMzMgNTAwIDQ0MyAxMDAwIDUwMCA1MDAgMzMzIDEwMDAgNTU2IDMzMyA4ODkgMzUwIDYxMCAzNTAgMzUwIDMzMyAzMzMgNDQzIDQ0MyAzNTAgNTAwIDEwMDAgNTQxIDk3OSAzODkgMzMzIDcyMiAzNTAgNDQzIDcyMiAyNTAgMzMzIDUwMCA1MDAgNTAwIDUwMCAyMDAgNTAwIDMzMyA3NTkgMjc1IDUwMCA1NjMgMzMzIDc1OSA1MDAgMzk5IDU0OCAyOTkgMjk5IDMzMyA1NzYgNDUzIDI1MCAzMzMgMjk5IDMxMCA1MDAgNzUwIDc1MCA3NTAgNDQzIDcyMiA3MjIgNzIyIDcyMiA3MjIgNzIyIDg4OSA2NjYgNjEwIDYxMCA2MTAgNjEwIDMzMyAzMzMgMzMzIDMzMyA3MjIgNzIyIDcyMiA3MjIgNzIyIDcyMiA3MjIgNTYzIDcyMiA3MjIgNzIyIDcyMiA3MjIgNzIyIDU1NiA1MDAgNDQzIDQ0MyA0NDMgNDQzIDQ0MyA0NDMgNjY2IDQ0MyA0NDMgNDQzIDQ0MyA0NDMgMjc3IDI3NyAyNzcgMjc3IDUwMCA1MDAgNTAwIDUwMCA1MDAgNTAwIDUwMCA1NDggNTAwIDUwMCA1MDAgNTAwIDUwMCA1MDAgNTAwIDBdCmVuZG9iagoxNCAwIG9iago8PCAvVHlwZSAvRm9udERlc2NyaXB0b3IKL0ZvbnROYW1lIC9UaW1lc05ld1JvbWFuLEJvbGQKL0ZvbnRCQm94ICBbLTU1OCAtMzA2IDIwMDAgMTAyNV0gCi9GbGFncyAzMwovQ2FwSGVpZ2h0IDY2MgovQXNjZW50IDg5MQovRGVzY2VudCAtMjE2Ci9JdGFsaWNBbmdsZSAwCi9TdGVtViAwCiA+PgplbmRvYmoKMTUgMCBvYmoKPDwgL1R5cGUgL0ZvbnQKL1N1YnR5cGUgL1RydWVUeXBlCi9OYW1lIC9GMTYKL0Jhc2VGb250IC9UaW1lc05ld1JvbWFuLEJvbGQKL0VuY29kaW5nIC9XaW5BbnNpRW5jb2RpbmcKL0ZpcnN0Q2hhciAwCi9MYXN0Q2hhciAyNTUKL1dpZHRocyAxNiAwIFIKL0ZvbnREZXNjcmlwdG9yIDE0IDAgUiA+PgplbmRvYmoKMTYgMCBvYmoKWyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDc3NyA3NzcgNzc3IDI1MCAzMzMgNTU1IDUwMCA1MDAgMTAwMCA4MzMgMjc3IDMzMyAzMzMgNTAwIDU2OSAyNTAgMzMzIDI1MCAyNzcgNTAwIDUwMCA1MDAgNTAwIDUwMCA1MDAgNTAwIDUwMCA1MDAgNTAwIDMzMyAzMzMgNTY5IDU2OSA1NjkgNTAwIDkzMCA3MjIgNjY2IDcyMiA3MjIgNjY2IDYxMCA3NzcgNzc3IDM4OSA1MDAgNzc3IDY2NiA5NDMgNzIyIDc3NyA2MTAgNzc3IDcyMiA1NTYgNjY2IDcyMiA3MjIgMTAwMCA3MjIgNzIyIDY2NiAzMzMgMjc3IDMzMyA1ODEgNTAwIDMzMyA1MDAgNTU2IDQ0MyA1NTYgNDQzIDMzMyA1MDAgNTU2IDI3NyAzMzMgNTU2IDI3NyA4MzMgNTU2IDUwMCA1NTYgNTU2IDQ0MyAzODkgMzMzIDU1NiA1MDAgNzIyIDUwMCA1MDAgNDQzIDM5NCAyMjAgMzk0IDUyMCAzNTAgNTAwIDM1MCAzMzMgNTAwIDUwMCAxMDAwIDUwMCA1MDAgMzMzIDEwMDAgNTU2IDMzMyAxMDAwIDM1MCA2NjYgMzUwIDM1MCAzMzMgMzMzIDUwMCA1MDAgMzUwIDUwMCAxMDAwIDUyMCAxMDAwIDM4OSAzMzMgNzIyIDM1MCA0NDMgNzIyIDI1MCAzMzMgNTAwIDUwMCA1MDAgNTAwIDIyMCA1MDAgMzMzIDc0NyAyOTkgNTAwIDU2OSAzMzMgNzQ3IDUwMCAzOTkgNTQ4IDI5OSAyOTkgMzMzIDU3NiA1NDAgMjUwIDMzMyAyOTkgMzMwIDUwMCA3NTAgNzUwIDc1MCA1MDAgNzIyIDcyMiA3MjIgNzIyIDcyMiA3MjIgMTAwMCA3MjIgNjY2IDY2NiA2NjYgNjY2IDM4OSAzODkgMzg5IDM4OSA3MjIgNzIyIDc3NyA3NzcgNzc3IDc3NyA3NzcgNTY5IDc3NyA3MjIgNzIyIDcyMiA3MjIgNzIyIDYxMCA1NTYgNTAwIDUwMCA1MDAgNTAwIDUwMCA1MDAgNzIyIDQ0MyA0NDMgNDQzIDQ0MyA0NDMgMjc3IDI3NyAyNzcgMjc3IDUwMCA1NTYgNTAwIDUwMCA1MDAgNTAwIDUwMCA1NDggNTAwIDU1NiA1NTYgNTU2IDU1NiA1MDAgNTU2IDBdCmVuZG9iagoxIDAgb2JqCjw8IC9UeXBlIC9QYWdlcwovQ291bnQgMQovS2lkcyBbNiAwIFIgXSA+PgplbmRvYmoKMiAwIG9iago8PCAvVHlwZSAvQ2F0YWxvZwovUGFnZXMgMSAwIFIKID4+CmVuZG9iagozIDAgb2JqCjw8IAovRm9udCA8PCAvRjEgMTAgMCBSIC9GMTggOCAwIFIgL0YxNSAxMiAwIFIgL0YxNiAxNSAwIFIgPj4gCi9Qcm9jU2V0IFsgL1BERiAvSW1hZ2VDIC9UZXh0IF0gPj4gCmVuZG9iagp4cmVmCjAgMTcKMDAwMDAwMDAwMCA2NTUzNSBmIAowMDAwMDA1MTMyIDAwMDAwIG4gCjAwMDAwMDUxOTAgMDAwMDAgbiAKMDAwMDAwNTI0MCAwMDAwMCBuIAowMDAwMDAwMDE1IDAwMDAwIG4gCjAwMDAwMDAwNzEgMDAwMDAgbiAKMDAwMDAwMDY4NCAwMDAwMCBuIAowMDAwMDAwNzkwIDAwMDAwIG4gCjAwMDAwMDA5NzUgMDAwMDAgbiAKMDAwMDAwMTE2MCAwMDAwMCBuIAowMDAwMDAyMjAxIDAwMDAwIG4gCjAwMDAwMDIzMDkgMDAwMDAgbiAKMDAwMDAwMjQ4OCAwMDAwMCBuIAowMDAwMDAyNjY5IDAwMDAwIG4gCjAwMDAwMDM3MTMgMDAwMDAgbiAKMDAwMDAwMzg5NyAwMDAwMCBuIAowMDAwMDA0MDgzIDAwMDAwIG4gCnRyYWlsZXIKPDwKL1NpemUgMTcKL1Jvb3QgMiAwIFIKL0luZm8gNCAwIFIKPj4Kc3RhcnR4cmVmCjUzNTQKJSVFT0YK" showAs="172.215.1.Commentaires.pdf" shortForm="0" />
      </attachment>
    </attachments>
  </act>
</akomaNtoso>
```
</details>
## Table

`find ../Actes -type f -exec grep -l "<table" {} + | sed -E 's|/[^/]+$||' | sort -u`

`../Actes/f83c68cf-d48b-4d7d-a7af-4c6702c2fba6/Version%2004.12.2012.akn`

with table and attachment

<details>
<summary>Content with table and attachment</summary>

```xml
<?xml version="1.0" encoding="UTF-8"?><akomaNtoso xmlns="http://docs.oasis-open.org/legaldocml/ns/akn/3.0">
  <act name="f83c68cf-d48b-4d7d-a7af-4c6702c2fba6">
    <meta>
      <identification source="#sjl">
        <FRBRWork>
          <FRBRthis value="" eId="frbrwork__frbrthis" />
          <FRBRuri value="" eId="frbrwork__frbruri" />
          <FRBRdate date="2018-11-30" name="Generation" />
          <FRBRauthor href="#sjl" as="#author" />
          <FRBRcountry value="ch" />
        </FRBRWork>
        <FRBRExpression>
          <FRBRthis value="" eId="frbrexpression__frbrthis" />
          <FRBRuri value="" eId="frbrexpression__frbruri" />
          <FRBRdate date="2018-11-30" name="Generation" />
          <FRBRauthor href="#sjl" as="#editor" />
          <FRBRlanguage language="fra" />
        </FRBRExpression>
        <FRBRManifestation>
          <FRBRthis value="" eId="frbrmanifestation__frbrthis" />
          <FRBRuri value="" eId="frbrmanifestation__frbruri" />
          <FRBRdate date="2018-11-30" name="Generation" />
          <FRBRauthor href="#sjl" as="#editor" />
        </FRBRManifestation>
      </identification>
      <references source="#SIEL">
        <TLCOrganization eId="sjl" href="/ch/vd/ontology/organization/sjl" showAs="Service juridique et législatif du Canton de Vaud" />
        <TLCReference eId="SIEL" href="/ch/vd/ontology/software/SIEL" showAs="Système d'information de l'exécutif et du législatif du Canton de Vaud" name="SIEL" />
      </references>
    </meta>
    <preface>
      <p>
        <docType>ARRÊTÉ</docType>
        <docNumber>101.01</docNumber>
      </p>
      <p>
        <docTitle>proclamant les résultats de la votation cantonale du&#xa0;25&#xa0;novembre&#xa0;2012&#xa0;sur les modifications de terminologie des articles&#xa0;74&#xa0;et&#xa0;142&#xa0;de la Constitution du Canton de Vaud du&#xa0;14&#xa0;avril&#xa0;2003</docTitle>
      </p>
      <p>du<docDate date="2012-11-28">28 novembre 2012</docDate>
      </p>
    </preface>
    <preamble>
      <p>LE CONSEIL D'ÉTAT DU CANTON DE VAUD</p>
      <recitals>
        <recital eId="id-2c4688bf-180d-4645-842c-3130a2794bd1">
          <p>vu l'arrêté de convocation du&#xa0;26&#xa0;septembre&#xa0;2012</p>
        </recital>
        <recital eId="id-602a8200-001d-44c2-904c-9f01be5b1457">
          <p>vu les procès-verbaux communaux</p>
        </recital>
        <recital eId="id-3ef37102-d5b5-48a3-b834-20fbc4d1fed0">
          <p>vu le préavis du Département de l'intérieur</p>
        </recital>
      </recitals>
      <formula name="formula">
        <p>arrête</p>
      </formula>
    </preamble>
    <body>
      <article eId="id-cb638bad-61b2-4261-8500-5bab0b4cc8e4">
        <num>Art. 1</num>
        <heading />
        <alinea eId="id-94ed303b-2638-43f5-9a38-38d649423bad">
          <num>1</num>
          <heading />
          <paragraph eId="id-bad71dbe-66eb-46f8-bc49-9b0d0eda1ec7">
            <content>
              <p>Les résultats de la votation sont les suivants:</p>
              <table eId="id-9d00ed59-f3b8-4773-9907-82040fe349c7" border="0">
                <tr>
                  <td>
                    <p>Electeurs inscrits&#xa0;: </p>
                  </td>
                  <td>
                    <p>398'996&#xa0;</p>
                  </td>
                  <td>
                    <p>Bulletins nuls&#xa0;: </p>
                  </td>
                  <td>
                    <p>189</p>
                  </td>
                </tr>
                <tr>
                  <td>
                    <p>Cartes de vote reçues&#xa0;: </p>
                  </td>
                  <td>
                    <p>107'122&#xa0;</p>
                  </td>
                  <td>
                    <p>Bulletins valables&#xa0;: </p>
                  </td>
                  <td>
                    <p>102'174</p>
                  </td>
                </tr>
                <tr>
                  <td>
                    <p>Bulletins rentrés&#xa0;: </p>
                  </td>
                  <td>
                    <p>104'914</p>
                  </td>
                  <td>
                    <p>Participation&#xa0;: </p>
                  </td>
                  <td>
                    <p>26,29&#xa0;% </p>
                  </td>
                </tr>
                <tr>
                  <td>
                    <p>Bulletins blancs&#xa0;: </p>
                  </td>
                  <td>
                    <p>2'551&#xa0;</p>
                  </td>
                  <td>
                    <p></p>
                  </td>
                  <td>
                    <p></p>
                  </td>
                </tr>
              </table>
              <table eId="id-7888e6f7-3999-4a97-8d36-88b61cefc316" border="0">
                <tr>
                  <td>
                    <p>Nombre total&#xa0;:</p>
                  </td>
                  <td>
                    <p>a) des acceptants&#xa0;: </p>
                  </td>
                  <td>
                    <p>97'704&#xa0;</p>
                  </td>
                  <td>
                    <p>(95,63&#xa0;% </p>
                  </td>
                </tr>
                <tr>
                  <td>
                    <p></p>
                  </td>
                  <td>
                    <p>b) des rejetants&#xa0;:</p>
                  </td>
                  <td>
                    <p>4'470&#xa0;</p>
                  </td>
                  <td>
                    <p>(4,37&#xa0;%) </p>
                  </td>
                </tr>
              </table>
            </content>
          </paragraph>
        </alinea>
        <alinea eId="id-37bf7aaf-40bc-400f-8783-6e02ad12e360">
          <num>2</num>
          <heading />
          <paragraph eId="id-7fcbbba5-4643-46a3-8894-760eb2564782">
            <content>
              <p>En conséquence, les modifications de terminologie des articles&#xa0;74&#xa0;et&#xa0;142&#xa0;de la Constitution du Canton de Vaud du&#xa0;14&#xa0;avril&#xa0;2003&#xa0;sont acceptées.</p>
            </content>
          </paragraph>
        </alinea>
      </article>
      <article eId="id-5dd91b02-fee6-4cd9-aa6d-38249f21c886">
        <num>Art. 2</num>
        <heading />
        <alinea eId="id-b3c26ec0-ba23-4465-b4fa-80644cd3db8d">
          <num>1</num>
          <heading />
          <paragraph eId="id-d51e5f6b-6558-4604-870d-5638cbb442fa">
            <content>
              <p>Les réclamations au sujet de la régularité et de la validité de cette votation doivent être adressées à la Chancellerie d'Etat, par mémoire motivé et sous pli recommandé, dans un délai expirant le&#xa0;7&#xa0;décembre&#xa0;2012.</p>
            </content>
          </paragraph>
        </alinea>
      </article>
      <article eId="id-4b894482-3fca-4e05-aa8a-4897bdda201e">
        <num>Art. 3</num>
        <heading />
        <alinea eId="id-ac0cb5d7-fc48-4843-9f17-18d52cc4a8dd">
          <num>1</num>
          <heading />
          <paragraph eId="id-0cf48eae-dae6-4030-a546-ad742d8159c5">
            <content>
              <p>Le présent arrêté sera publié dans la "Feuille des avis officiels du Canton de Vaud" et communiqué au Grand Conseil.</p>
            </content>
          </paragraph>
        </alinea>
      </article>
    </body>
    <attachments>
      <attachment>
        <num>1</num><heading>Récapitulation par district</heading><documentRef eId="id-1962c036-82f3-45a7-bdae-909e76b95335" href="data:application/pdf;base64,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ago2IDAgb2JqCjI2MTcKZW5kb2JqCjQgMCBvYmoKPDwvVHlwZS9QYWdlL01lZGlhQm94IFswIDAgNTk1IDg0Ml0KL1JvdGF0ZSAwL1BhcmVudCAzIDAgUgovUmVzb3VyY2VzPDwvUHJvY1NldFsvUERGIC9UZXh0XQovRm9udCA5IDAgUgo+PgovQ29udGVudHMgNSAwIFIKPj4KZW5kb2JqCjMgMCBvYmoKPDwgL1R5cGUgL1BhZ2VzIC9LaWRzIFsKNCAwIFIKXSAvQ291bnQgMQo+PgplbmRvYmoKMSAwIG9iago8PC9UeXBlIC9DYXRhbG9nIC9QYWdlcyAzIDAgUgovTWV0YWRhdGEgMTEgMCBSCj4+CmVuZG9iago5IDAgb2JqCjw8L1I3CjcgMCBSL1I4CjggMCBSPj4KZW5kb2JqCjcgMCBvYmoKPDwvQmFzZUZvbnQvVGltZXMtQm9sZC9UeXBlL0ZvbnQKL0VuY29kaW5nIDEwIDAgUi9TdWJ0eXBlL1R5cGUxPj4KZW5kb2JqCjEwIDAgb2JqCjw8L1R5cGUvRW5jb2RpbmcvRGlmZmVyZW5jZXNbCjM5L3F1b3Rlc2luZ2xlCjIzMy9lYWN1dGVdPj4KZW5kb2JqCjggMCBvYmoKPDwvQmFzZUZvbnQvVGltZXMtUm9tYW4vVHlwZS9Gb250Ci9TdWJ0eXBlL1R5cGUxPj4KZW5kb2JqCjExIDAgb2JqCjw8L1R5cGUvTWV0YWRhdGEKL1N1YnR5cGUvWE1ML0xlbmd0aCAxNTI5Pj5zdHJlYW0KPD94cGFja2V0IGJlZ2luPSfvu78nIGlkPSdXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQnPz4KPD9hZG9iZS14YXAtZmlsdGVycyBlc2M9IkNSTEYiPz4KPHg6eG1wbWV0YSB4bWxuczp4PSdhZG9iZTpuczptZXRhLycgeDp4bXB0az0nWE1QIHRvb2xraXQgMi45LjEtMTMsIGZyYW1ld29yayAxLjYnPgo8cmRmOlJERiB4bWxuczpyZGY9J2h0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMnIHhtbG5zOmlYPSdodHRwOi8vbnMuYWRvYmUuY29tL2lYLzEuMC8nPgo8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0nNmE5Y2Y3NDMtNDAzZC0xMWUyLTAwMDAtNGQ1ODhjZWUzNWRjJyB4bWxuczpwZGY9J2h0dHA6Ly9ucy5hZG9iZS5jb20vcGRmLzEuMy8nPjxwZGY6UHJvZHVjZXI+R1BMIEdob3N0c2NyaXB0ICA5LjA8L3BkZjpQcm9kdWNlcj4KPHBkZjpLZXl3b3Jkcz4oKTwvcGRmOktleXdvcmRzPgo8L3JkZjpEZXNjcmlwdGlvbj4KPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9JzZhOWNmNzQzLTQwM2QtMTFlMi0wMDAwLTRkNTg4Y2VlMzVkYycgeG1sbnM6eG1wPSdodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvJz48eG1wOk1vZGlmeURhdGU+MjAxMi0xMi0wNFQwODoxMjowMyswMTowMDwveG1wOk1vZGlmeURhdGU+Cjx4bXA6Q3JlYXRlRGF0ZT4yMDEyLTEyLTA0VDA4OjEyOjAzKzAxOjAwPC94bXA6Q3JlYXRlRGF0ZT4KPHhtcDpDcmVhdG9yVG9vbD5QREZDcmVhdG9yIFZlcnNpb24gMS4yLjA8L3htcDpDcmVhdG9yVG9vbD48L3JkZjpEZXNjcmlwdGlvbj4KPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9JzZhOWNmNzQzLTQwM2QtMTFlMi0wMDAwLTRkNTg4Y2VlMzVkYycgeG1sbnM6eGFwTU09J2h0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8nIHhhcE1NOkRvY3VtZW50SUQ9JzZhOWNmNzQzLTQwM2QtMTFlMi0wMDAwLTRkNTg4Y2VlMzVkYycvPgo8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0nNmE5Y2Y3NDMtNDAzZC0xMWUyLTAwMDAtNGQ1ODhjZWUzNWRjJyB4bWxuczpkYz0naHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8nIGRjOmZvcm1hdD0nYXBwbGljYXRpb24vcGRmJz48ZGM6dGl0bGU+PHJkZjpBbHQ+PHJkZjpsaSB4bWw6bGFuZz0neC1kZWZhdWx0Jz5Sw6ljYXBfY2FudDwvcmRmOmxpPjwvcmRmOkFsdD48L2RjOnRpdGxlPjxkYzpjcmVhdG9yPjxyZGY6U2VxPjxyZGY6bGk+empscnZ5PC9yZGY6bGk+PC9yZGY6U2VxPjwvZGM6Y3JlYXRvcj48ZGM6ZGVzY3JpcHRpb24+PHJkZjpTZXE+PHJkZjpsaT4oKTwvcmRmOmxpPjwvcmRmOlNlcT48L2RjOmRlc2NyaXB0aW9uPjwvcmRmOkRlc2NyaXB0aW9uPgo8L3JkZjpSREY+CjwveDp4bXBtZXRhPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCjw/eHBhY2tldCBlbmQ9J3cnPz4KZW5kc3RyZWFtCmVuZG9iagoyIDAgb2JqCjw8L1Byb2R1Y2VyKEdQTCBHaG9zdHNjcmlwdCAgOS4wKQovQ3JlYXRpb25EYXRlKEQ6MjAxMjEyMDQwODEyMDMrMDEnMDAnKQovTW9kRGF0ZShEOjIwMTIxMjA0MDgxMjAzKzAxJzAwJykKL1RpdGxlKFwzNzZcMzc3XDAwMFJcMDAwXDM1MVwwMDBjXDAwMGFcMDAwcFwwMDBfXDAwMGNcMDAwYVwwMDBuXDAwMHQpCi9DcmVhdG9yKFwzNzZcMzc3XDAwMFBcMDAwRFwwMDBGXDAwMENcMDAwclwwMDBlXDAwMGFcMDAwdFwwMDBvXDAwMHJcMDAwIFwwMDBWXDAwMGVcMDAwclwwMDBzXDAwMGlcMDAwb1wwMDBuXDAwMCBcMDAwMVwwMDAuXDAwMDJcMDAwLlwwMDAwKQovQXV0aG9yKFwzNzZcMzc3XDAwMHpcMDAwalwwMDBsXDAwMHJcMDAwdlwwMDB5KQovS2V5d29yZHMoKQovU3ViamVjdCgpPj5lbmRvYmoKeHJlZgowIDEyCjAwMDAwMDAwMDAgNjU1MzUgZiAKMDAwMDAwMjkyMiAwMDAwMCBuIAowMDAwMDA0ODUzIDAwMDAwIG4gCjAwMDAwMDI4NjMgMDAwMDAgbiAKMDAwMDAwMjcyMiAwMDAwMCBuIAowMDAwMDAwMDE1IDAwMDAwIG4gCjAwMDAwMDI3MDIgMDAwMDAgbiAKMDAwMDAwMzAyNSAwMDAwMCBuIAowMDAwMDAzMTgxIDAwMDAwIG4gCjAwMDAwMDI5ODcgMDAwMDAgbiAKMDAwMDAwMzEwNiAwMDAwMCBuIAowMDAwMDAzMjQ3IDAwMDAwIG4gCnRyYWlsZXIKPDwgL1NpemUgMTIgL1Jvb3QgMSAwIFIgL0luZm8gMiAwIFIKL0lEIFs8NjJEQzYzOTJEREQwODkwOTFCQzg5M0M0RUM5NzI2MDQ+PDYyREM2MzkyREREMDg5MDkxQkM4OTNDNEVDOTcyNjA0Pl0KPj4Kc3RhcnR4cmVmCjUyNTYKJSVFT0YK" showAs="Récapitulation par district.pdf" shortForm="0" />
      </attachment>
    </attachments>
  </act>
</akomaNtoso>
```
</details>