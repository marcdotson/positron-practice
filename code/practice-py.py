import polars as pl
import polars.selectors as cs

customer_data = pl.read_csv('customer_data.csv')
customer_data.shape
customer_data.columns

customer_data.filter(pl.col('college_degree') == 'Yes')
customer_data.filter(pl.col('region') != 'West')
customer_data.filter(pl.col('gender') != 'Female', pl.col('income') > 70000)

customer_data.slice(0, 5)

customer_data.sort(pl.col('birth_year'))
customer_data.sort(pl.col('birth_year'), descending=True)

customer_data.select(pl.col('region'), pl.col('review_text'))
customer_data.select(pl.col(['region', 'review_text']))

customer_data.with_columns(income = pl.col('income') / 1000)

store_transactions = pl.read_csv('store_transactions.csv')
store_transactions.shape
store_transactions.columns

customer_data.join(store_transactions, on='customer_id', how='left')
customer_data.join(store_transactions, on='customer_id', how='inner')

(customer_data
 .join(store_transactions, on='customer_id', how='left')
 .filter(pl.col('region') == 'West', pl.col('feb_2005') == pl.col('feb_2005').max())
 .with_columns(age = 2024 - pl.col('birth_year'))
 .select(pl.col(['age', 'feb_2005']))
 .sort(pl.col('age'), descending=True)
 .slice(0, 1)
)

(customer_data
 .group_by(pl.col('region'))
 .agg(n = pl.len())
)

(customer_data
 .group_by(pl.col(['region', 'college_degree']))
 .agg(n = pl.len())
)

(customer_data
  .select(pl.col('income'))
  .mean()
)

(customer_data
  .select(pl.col(['income', 'credit']))
  .mean()
)

(customer_data
 .group_by(pl.col(['gender', 'region']))
 .agg(
   n = pl.len(), 
   avg_income = pl.col('income').mean(), 
   avg_credit = pl.col('credit').mean()
  )
 .sort(pl.col('avg_income'), descending=True)
)

