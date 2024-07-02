library(tidyverse)

customer_data <- read_csv(here::here("data", "customer_data.csv"))

glimpse(customer_data)

filter(customer_data, college_degree == "Yes")

filter(customer_data, region != "West")

filter(customer_data, gender == "Female", income > 70000)

slice(customer_data, 1:5)

arrange(customer_data, birth_year)

arrange(customer_data, desc(birth_year))

select(customer_data, region, review_text)

mutate(customer_data, income = income / 1000)

store_transactions <- read_csv("store_transactions.csv")

glimpse(store_transactions)

left_join(customer_data, store_transactions, join_by(customer_id))

inner_join(customer_data, store_transactions, join_by(customer_id))

customer_data |> 
  left_join(store_transactions, join_by(customer_id)) |> 
  filter(region == "West", feb_2005 == max(feb_2005)) |> 
  mutate(age = 2024 - birth_year) |> 
  select(age, feb_2005) |> 
  arrange(desc(age)) |> 
  slice(1)

customer_data |> 
  count(region)

customer_data |> 
  count(region, college_degree)

customer_data |>
  summarize(avg_income = mean(income))

customer_data |>
  summarize(
    avg_income = mean(income),
    avg_credit = mean(credit)
  )

customer_data |>
  group_by(gender, region) |>
  summarize(
    n = n(),
    avg_income = mean(income),
    avg_credit = mean(credit)
  ) |> 
  arrange(desc(avg_income))

customer_data |>
  group_by(gender, region) |> 
  ggplot(aes(x = region, y = income)) +
  geom_col()

customer_data |>
  group_by(gender, region) |> 
  ggplot(aes(x = region, y = income, color = married)) +
  geom_col() +
  facet_wrap(~ married)
