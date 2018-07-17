# Dependencies and Setup
import pandas as pd
import numpy as np

# Raw data file
purchase_data_file = "Resources/purchase_data.csv"

# Read purchasing file and store into pandas data frame
purchase_data = pd.read_csv(purchase_data_file)
purchase_data.head()

# Display total number of players
player_count = purchase_data['Purchase ID'].nunique()
player_count

# Display number of unique items
unique_items = purchase_data['Item ID'].value_counts()
unique_items.count()

# Display average price
avg_price = purchase_data['Price'].mean()
avg_price

# Display number of purchases
purchase_count = purchase_data["Price"].value_counts()
purchase_count.count()

# Display total revenue
total_revenue = purchase_data["Price"].sum()
total_revenue

# Create a summary data frame to hold the results
df_purchase = pd.DataFrame({"Total Revenue":[total_revenue], 
                            "Average Price":[avg_price], 
                            "Number of Purchases":[purchase_count.count()], 
                            "Items":[unique_items.count()]})
df_purchase

# Display number of records per gender
gender_count = purchase_data["Gender"].value_counts()
gender_count

# Create a data frame that holds gender count summary
gender_demo_df = pd.DataFrame(gender_count)
gender_demo_df.head()

# Change column name from 'Gender' to 'Count'
gender_demo_df = gender_demo_df.rename(
    columns={"Gender":"Count"})
gender_demo_df.head()

# Find avg purchase price by gender
avg_gender_purchase_price = grouped_purchase_df['Price'].mean()
avg_gender_purchase_price

# Create data frame
avg_gender_purchase_df = pd.DataFrame(avg_gender_purchase_price)
avg_gender_purchase_df

# Find total spent
total_spent = purchase_data["Price"].sum()
total_spent

# Normalized purchasing price
norm_purch = total_spent/gender_count
norm_purch

gender_demo_table = pd.DataFrame({"Average Price": avg_gender_purchase_price.round(2), "Count" : gender_count, "Normalized Purchasing Price" : norm_purch})
gender_demo_table

# Establish bins for ages
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

# Categorize existing players using age bins
pd.cut(purchase_data["Age"], age_bins, labels = group_names).head()

purchase_data["Age Group"] = pd.cut(purchase_data["Age"], age_bins, labels = group_names)
purchase_data.head()

# Calculate the numbers and percentages by age group
purchase_group = purchase_data.groupby("Age Group")
purchase_group.head()

# Separate data into fields according to 'Age Group' values
grouped_age_df = purchase_data.groupby(['Age Group'])
print(grouped_age_df)

grouped_age_df.count()

# Calculate number of unique players
unique_players = purchase_data["SN"].nunique()
unique_players

# Calculate number of players per age group
player_count = grouped_age_df["SN"].nunique()
player_count

player_df = pd.DataFrame(player_count)
player_df = player_df.rename(columns={"SN":"Players"})
player_df


# Calculate player makeup of each age group
players_by_age = player_df["Players"]/unique_players
players_by_age

player_percentage_df = pd.DataFrame(players_by_age)
player_percentage_df = player_percentage_df.rename(columns={"Players":"Player Percentage"})
player_percentage_df

# Convert decimal to percentage
player_percentage_df['Player Percentage'] = pd.Series(["{0:.2f}%".format(val*100) for val in player_percentage_df['Player Percentage']], index = player_percentage_df.index)
player_percentage_df

# Calculate average price by age group
avg_price_age = grouped_age_df["Price"].mean()
avg_price_age

# Create data frame
avg_price_age_df = pd.DataFrame(avg_price_age)
avg_price_age_df

# Change column name from 'Age Group' to 'Avg Price'
avg_price_age_df = avg_price_age_df.rename(columns={"Age Group":"Avg Price"})
avg_price_age_df

# Calculate total revenue by age group
total_revenue_age = grouped_age_df["Price"].sum()
total_revenue_age

# Create data frame
total_revenue_age_df = pd.DataFrame(total_revenue_age)
total_revenue_age_df

# Change column name from 'Price' to 'Total Price'
total_revenue_age_df = total_revenue_age_df.rename(columns={"Price":"Total Spent"})
total_revenue_age_df

# Calculate total revenue
total_revenue = total_revenue_age_df["Total Spent"].sum()
total_revenue.round(2)
2379.77

# Percentage of total revenue by age group
age_revenue = total_revenue_age_df["Total Spent"]/total_revenue
age_revenue

# Create data frame
age_revenue_df = pd.DataFrame(age_revenue)
age_revenue_df

# Change column name from 'Total Price' to 'Percent of Total'
age_revenue_df = age_revenue_df.rename(columns={"Total Spent":"Percent of Total"})
age_revenue_df

# Convert 'Percent of Total' values from decimal to percentage
age_revenue_df['Percent of Total'] = pd.Series(["{0:.2f}%".format(val*100) for val in age_revenue_df['Percent of Total']], index = age_revenue_df.index)
age_revenue_df
Percent of Total
Age Group	
<10	3.24%
10-14	3.48%
15-19	17.35%
20-24	46.81%
25-29	12.31%
30-34	8.99%
35-39	6.21%
40+	1.61%

# Create a summary data frame to hold the results
age_demo_table = pd.DataFrame({"Average Purchase Price": avg_price_age.round(2).map('${:,.2f}'.format), 
                               "Player Count": player_count, 
                               "Player Percentage": age_revenue_df['Percent of Total'], 
                               "Total Purchase Value" : total_revenue_age.map('${:,.2f}'.format)})
age_demo_table


# Set SN as new index
sn_df = purchase_data.set_index("SN")
sn_df.head()

# Grab data contained within columns 'Item ID', 'Item Name', and 'Price'
items_df = purchase_data.loc[: , ["Item ID" , "Item Name" , "Price"]]

# Item demographics
item_total_purch = items_df.groupby(["Item ID" , "Item Name"]).sum()["Price"]
item_total_purch = item_total_purch.rename("Item Total Purchase Value")

item_avg_purch = items_df.groupby(["Item ID" , "Item Name"]).mean()["Price"]
item_avg_purch = item_avg_purch.rename("Item Avg Purchase Value")

item_count = items_df.groupby(["Item ID" , "Item Name"]).count()["Price"]
item_count = item_count.rename("Item Purchase Count")

# Create summary data frame
pop_items_table = pd.DataFrame({"Total Purchase Value": item_total_purch.round(2).map('${:,.2f}'.format), 
                               "Avg Item Price": item_avg_purch, 
                               "Purchase Count": item_count })
pop_items_table.head()

prof_items_table = pop_items_table.sort_values("Total Purchase Value" , ascending = False)                                
prof_items_table.head()
