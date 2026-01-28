import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('/Users/vijais/Documents/vs code/archive/data.csv')

# for col in df.columns:
#     print (col)


# print(df.nunique())


cols=["Cost Price","Retail Price","Total","Profit Margin","Order Total","Shipping Cost","Discount $","Sub Total"]

df[cols] = df[cols].apply(
    lambda col: col.astype(str).str.replace("$", "", regex=False).str.replace(",", "", regex=False).astype(float)
)

df["Order Date"] = pd.to_datetime(df["Order Date"], format="%d-%m-%Y")
# print(df[["Order Date"]])

df["Revenue"]=(df["Order Quantity"] * df["Retail Price"]) - df["Discount $"]
# print(df[["Revenue"]].sum())


grp=df.groupby("Customer Type")

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title("Profit Margin by Customer Type")
plt.ylabel("Amount in $")
(grp["Profit Margin"].sum()).plot(kind="bar")

plt.subplot(1,2,2)
plt.title("Order Quantity by Customer Type")
plt.ylabel("No. of Orders")
(grp["Order Quantity"].sum()).plot(kind="bar")
# grp.plot(kind="bar")
plt.show()


# print(df[["Order Quantity","Retail Price","Revenue","Sub Total","Profit Margin","Order Total","Shipping Cost","Total","Discount $"]].head())

df["Month"]=df["Order Date"].dt.month
grp1=df.groupby("Month")

plt.figure(figsize=(8,5))

plt.subplot(1,2,1)
grp1["Profit Margin"].sum().plot(kind="bar")
plt.title("Profit Margin by Month")
plt.ylabel("Amount in $")

plt.subplot(1,2,2)
grp1["Revenue"].sum().plot(kind="bar")
plt.title("Revenue by Month")
plt.ylabel("Amount in $")

plt.show()


