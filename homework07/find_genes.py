'''A Python program that displays all the genes in a genome
Created Spring 2018
Homework07
@author: Nana Osei Asiedu Yirenkyi (na29)'''


#Function definition for finding a gene 
def find_gene(genome):
    '''receives a genome and returns all possible genes or false if otherwise'''
    
    if "ATG" in genome:
        a_t_g = genome.find("ATG")
        if ("TAA" in genome) and (genome.find("TAA") > a_t_g):
            t_a_a = genome.find("TAA")
            new_gene = genome[a_t_g + 3:t_a_a]
            gene_list.append(new_gene)
            genome = genome[t_a_a:]
            return genome
        elif ("TAG" in genome) and (genome.find("TAG") > a_t_g):
            t_a_g = genome.find("TAG")
            new_gene = genome[a_t_g + 3:t_a_g]
            genome = genome[t_a_g:]
            gene_list.append(new_gene)
            return genome
        elif "TGA" in genome and (genome.find("TGA") > a_t_g):
            tga = genome.find("TGA")
            new_gene = genome[a_t_g + 3 : tga]
            genome = genome[tga:]
            gene_list.append(new_gene)
            return genome
    else:
        return False
    
#Prompts the user to enter a genome    
user_genome = input("Enter a genome string:").upper()

#Creates an empty list to keep track of genes found
gene_list = []


#Infinite loop for finding possible genes in genome
while True:
    user_genome = find_gene(user_genome)
    if len(gene_list) <= 0:
        print("No gene is found")
        break
    if user_genome == False:
        break

#Printing genes 
order = 1
if len(gene_list) > 0:
    for g in gene_list:
        if ("ATG" or "TAG" or "TAA" or "TGA" not in g) and (len(g) % 3 == 0) :
            print("Gene", order ,':', gene_list[order-1])
            order += 1