import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('WHO COVID-19 cases.csv')
df.drop(columns=['Country_code', 'New_cases', 'New_deaths'], inplace=True)
df['Date_reported'] = pd.to_datetime(df['Date_reported'])
df = df[df['Continent'] != 'Uncategorized']

total_cases = df.groupby(['Continent'])['Cumulative_cases'].sum().reset_index()
cases_for_year = df.groupby(['Continent', df['Date_reported'].dt.year])['Cumulative_cases'].sum().reset_index()
deaths_total_case_per_year = df.groupby(df['Date_reported'].dt.year)['Cumulative_deaths'].sum().reset_index()

plt.figure(figsize=(8, 6))

diagr = sns.barplot(total_cases, x="Continent", y='Cumulative_cases', color='skyblue', edgecolor='black')
plt.yscale('log')
for p in diagr.patches:
    diagr.annotate(f'{p.get_height():.2e}',
                   (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom')
plt.xlabel('Continent')
plt.ylabel('Cases')
plt.title('number of detected cases of covid-19 by region')
diagr.spines['right'].set_visible(False)
diagr.spines['top'].set_visible(False)
plt.grid(axis='y', alpha=0.5)
plt.show()


pivot_df = cases_for_year.pivot(index='Date_reported', columns='Continent', values='Cumulative_cases')
line_chart = pivot_df.plot(kind='line', marker='o')
plt.title('Number of diseases by continent')
plt.xlabel('Year')
plt.ylabel('Number of diseases')
line_chart.spines['right'].set_visible(False)
line_chart.spines['top'].set_visible(False)
plt.grid(alpha=0.5)
plt.legend(title='Continent')
plt.show()

plt.plot(deaths_total_case_per_year['Date_reported'],
         deaths_total_case_per_year['Cumulative_deaths'],
         color='orange', linewidth=2)
plt.title('Amount of total deaths')
plt.xlabel('Year')
plt.ylabel('Amount')
diagr.spines['right'].set_visible(False)
diagr.spines['top'].set_visible(False)
plt.grid(alpha=0.5)
plt.show()
