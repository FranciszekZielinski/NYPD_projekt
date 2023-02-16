import pandas as pd
import argparse
import analiza

parser = argparse.ArgumentParser()


parser.add_argument('co2_file', type=str, help='CSV file containing CO2  data')
parser.add_argument('population_file', type=str, help='CSV file containing population data')
parser.add_argument('gdp_file', type=str, help='CSV file containing GDP data')

args = parser.parse_args()


gdp_file = args.gdp_file
population_file = args.population_file
CO2_file = args.co2_file


gdp = pd.read_csv(gdp_file,skiprows=4)
population = pd.read_csv(population_file,skiprows=4)
co2 = pd.read_csv(CO2_file)



analiza.drop_columns(gdp,population)


co2 = analiza.change_co2(co2)

gdp = analiza.digits_columns_to_int(gdp)
population = analiza.digits_columns_to_int(population)

years = analiza.select_same_years(co2,population,gdp)

co2 = analiza.drop_years(co2, years)

population = analiza.drop_years(population, years)

gdp = analiza.drop_years(gdp, years)

co2 = co2.reset_index()

co2 = co2.rename(columns={"Country": "Country Name"})


co2 = pd.melt(co2, id_vars=['Country Name'], var_name='Year', value_name='co2')


population = pd.melt(population, id_vars=['Country Name'], var_name='Year', value_name='population')



gdp = pd.melt(gdp, id_vars=['Country Name'], var_name='Year', value_name='gdp')



merged_df = pd.merge(population, gdp, on=['Country Name', 'Year'])


merged_df['Country Name'] = merged_df['Country Name'].str.upper()


new_merged_df = pd.merge(merged_df,co2 , on=['Country Name', 'Year'])


new_merged_df = new_merged_df.reset_index(drop = True)


analiza.top_richess(new_merged_df)



analiza.top_emitters(new_merged_df)


analiza.change_in_emission(new_merged_df)
