## Data Fields

- **birth**: Character's birth date  
- **death**: Character's death date  
- **gender**: Character's gender  
- **hair**: Character's hair color  
- **height**: Character's height  
- **name**: Character's full name  
- **race**: Character's racial background  
- **realm**: Character's native realm  
- **spouse**: Character's spouse (if applicable)

## Data Cleaning Steps
- Removed extra whitespace and standardized formats in key fields.
- Filled missing values with "Unknown" and removed incomplete records where necessary.

## Shell and Regex Analyses
### Commands and Results
1. Count of total dialogue lines and unique words:
    ```bash
    wc -l lotr_characters_cleaned.csv
    awk '{ for (i=1;i<=NF;i++) words[$i]++ } END { print length(words) }' lotr_characters_cleaned.csv
    ```

2. Character count distribution by movie:
    ```bash
    grep -o 'Fellowship' lotr_characters_cleaned.csv | wc -l
    grep -o 'Two Towers' lotr_characters_cleaned.csv | wc -l
    grep -o 'Return of the King' lotr_characters_cleaned.csv | wc -l
    ```

3. Top 5 characters by number of mentions:
    ```bash
    awk -F',' '{names[$6]++} END {for (name in names) print names[name], name}' lotr_characters_cleaned.csv | sort -nr | head -5
    ```

4. Top 5 characters by dialogue count:
    ```bash
    awk -F',' '{dialogues[$6]+=$NF} END {for (char in dialogues) print dialogues[char], char}' lotr_characters_cleaned.csv | sort -nr | head -5
