import pandas as pd
import sys

if len(sys.argv) > 1:
    file_path = sys.argv[1]
else:
    print('Usage: python make_table.py <file_path>')
    sys.exit(1)

# Load the CSV file
table_name = file_path.split('.')[0]
data = pd.read_csv(file_path, header=None)
# Function to generate LaTeX table from a DataFrame
def df_to_latex(df):
    latex_code = "\\begin{table}[H]\n\\centering\n\\begin{tabular}{" + "|c" * (len(df.columns)) + "|}\n\\hline\n"
    
    
    # Add rows
    for _, row in df.iterrows():
        latex_code += " & ".join([str(item) for item in row]) + " \\\\\n\\hline\n"
    
    latex_code += "\\end{tabular}\n\\caption{" + table_name + "}\n\\end{table}"
    
    # Replace nan with space
    latex_code = latex_code.replace('nan', ' ')
    return latex_code

# Convert DataFrame to LaTeX code
latex_output = df_to_latex(data)

# Print or save the LaTeX output
print(latex_output)
