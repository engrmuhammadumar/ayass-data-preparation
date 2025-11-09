#!/usr/bin/env python
# coding: utf-8

# # Gene Symbols and IDs Conversion

# In[2]:


#Two files

# 1. Read the contents of the first file into a list
with open('IDs_Only.txt', 'r') as f1:
    first_file_lines = f1.readlines()

# 2. Read the contents of the second file into a dictionary with ID as key and Gene.symbol as value
id_gene_dict = {}
with open('ID_and_Symbol.txt', 'r') as f2:
    for line in f2:
        parts = line.strip().split()
        if len(parts) == 2:
            id_gene_dict[parts[0]] = parts[1]

# Update the first file content with matching Gene.symbol values
updated_content = []
for line in first_file_lines:
    id_value = line.strip()
    gene_symbol = id_gene_dict.get(id_value, '')  # If the ID exists in the dictionary, get its Gene.symbol; otherwise, use an empty string
    updated_content.append(f"{id_value}\t{gene_symbol}\n")

# Write the updated content back to the first file
with open('Output_files', 'w') as f1:
    f1.writelines(updated_content)

