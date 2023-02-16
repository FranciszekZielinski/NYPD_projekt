import numpy as np
import pandas as pd


def select_same_years(df1,df2,df3):
    years_columns1 = [col for col in df1.columns if str(col).isdigit()]
    years_columns2 = [col for col in df2.columns if str(col).isdigit()]
    years_columns3 = [col for col in df3.columns if str(col).isdigit()]
    years_columns1_str = list(map(str, years_columns1))
    years_columns2_str = list(map(str, years_columns2))
    years_columns3_str = list(map(str, years_columns3))
    common_years = [x for x in years_columns1_str if x in years_columns2_str and x in years_columns3_str]
    common_years = list(map(int, common_years))
    return common_years



def drop_columns(df1,df2):
    df1 = df1.drop(['Country Code','Indicator Name', 'Indicator Code', 'Unnamed: 66'], axis=1)
    df2 = df2.drop(['Country Code','Indicator Name', 'Indicator Code', 'Unnamed: 66'], axis=1)
    return df1, df2

def digits_columns_to_int(df):
    new_names = {}
    for col in df.columns:
        if col.isdigit():
            new_names[col] = int(col)
        else:
            new_names[col] = col
    df = df.rename(columns=new_names)
    return df




def change_co2(co2):
    co2 = co2.groupby(["Country", "Year"]).sum().reset_index()
    co2 = co2.pivot(index="Country", columns="Year", values="Total")
    return co2



def drop_years(df,common_years):
    droped = [col for col in df.columns if str(col).isdigit() and col not in common_years]
    return df.drop(droped, axis=1)



def top_emitters(df):
    df['co2_per_capita'] = df['co2'] / df['population']

    grouped = df.groupby('Year').apply(lambda x: x.sort_values('co2_per_capita', ascending=False))
    grouped = grouped.drop('Year', axis=1)
    top5 = grouped.groupby('Year').head(5)

    result = top5[['Country Name', 'co2_per_capita', 'co2']]

    return result




def top_richess(df):
    df['gdp_per_capita'] = df['gdp'] / df['population']

    grouped = df.groupby('Year').apply(lambda x: x.sort_values('gdp_per_capita', ascending=False))
    grouped = grouped.drop('Year', axis=1)
    top5 = grouped.groupby('Year').head(5)

    result = top5[['Country Name', 'gdp_per_capita', 'gdp']]

    return result


def change_in_emission(df):
    if 'co2_per_capita' not in df.columns:
        df['co2_per_capita'] = df['co2'] / df['population']
    year = df['Year'].max()
    threshold = year - 10
    last_10_years = df[df['Year'] >= threshold]
    last_10_years = last_10_years.sort_values(['Country Name','Year'])
    result = last_10_years.groupby('Country Name')['co2_per_capita'].agg(['first', 'last'])
    result['change'] = result['last'] - result['first']
    result = result.sort_values('change', ascending=False)
    return result
