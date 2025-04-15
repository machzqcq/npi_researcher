# Notes

## Prompt
Prepare a reveal.js slide deck (graphs, charts, and tables) that provides detailed insights about a doctor: Jorge Sanchez-Masiques with speciality in pulmonary disease, using myDuckDB. The report should include the following sections:

### Section 1 (using DuckDB tool):
- Total claims and total patients treated by year.
- Specialties and drugs prescribed by the doctor.

### Section 2 (using Tavily tool research):
- Related to the drugs prescribed, find papers published by the doctor and list them as bullet points with hyperlinks (search the web using tavily online research).
- List conferences attended with dates and topics.
- Include a word map of keywords found about the doctor's research online.

### Section 3 (using email tool):
- Search my email inbox for keywords: `riociguat`, `PDE5 inhibitor`, and `Endothelin Receptor Antagonist`. Provide a brief summary of the latest two emails for each keyword.

### Section 4 (using my filesystem tool):
- For the keywords: `riociguat`, `PDE5 inhibitor`, and `Endothelin Receptor Antagonist`, search my private knowledge base and list all the file names as a bullet list (do not read the content).

---

### Query:
```sql
SELECT 
    Prscrbr_NPI,
    Prscrbr_Last_Org_Name,
    Prscrbr_First_Name,
    SUM(Tot_Clms) AS Total_Claims,
    COUNT(DISTINCT Brnd_Name) AS Unique_Drugs
FROM medicare_data
WHERE Prscrbr_Type = 'Pulmonary Disease'
GROUP BY Prscrbr_NPI, Prscrbr_Last_Org_Name, Prscrbr_First_Name
ORDER BY SUM(Tot_Clms) DESC
LIMIT 10;
```

### Results:
- **Dr. Jorge Sanchez-Masiques (NPI: 1376541961)**  
  - Total Claims: 67,157  
  - Unique Drugs Prescribed: 58  

- **Dr. James Pike (NPI: 1366443400)**  
  - Total Claims: 45,966  
  - Unique Drugs Prescribed: 308  

- **Dr. Huan Le (NPI: 1780797381)**  
  - Total Claims: 42,483  
  - Unique Drugs Prescribed: 163  

- **Dr. Hossam Amin (NPI: 1437221207)**  
  - Total Claims: 42,111  
  - Unique Drugs Prescribed: 214  

- **Dr. Manoj Majmudar (NPI: 1659336097)**  
  - Total Claims: 38,291  
  - Unique Drugs Prescribed: 330  

- **Dr. Mark Lipham (NPI: 1437192697)**  
  - Total Claims: 32,622  
  - Unique Drugs Prescribed: 249  

- **Dr. Thomas Schneider (NPI: 1003875360)**  
  - Total Claims: 20,506  
  - Unique Drugs Prescribed: 213  

- **Dr. Thomas Chan (NPI: 1548333552)**  
  - Total Claims: 20,409  
  - Unique Drugs Prescribed: 86  

- **Dr. Juan Acevedo-Crespo (NPI: 1720074545)**  
  - Total Claims: 19,261  
  - Unique Drugs Prescribed: 30  

- **Dr. Sergio Martinez (NPI: 1336171040)**  
  - Total Claims: 18,267  
  - Unique Drugs Prescribed: 217  



### Technical
- Install Graphviz tools from [here](https://graphviz.org/download/)