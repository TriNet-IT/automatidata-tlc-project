import pandas as pd
import numpy as np

# 1. Building dataframe
df = pd.read_csv(r"H:\Python_Cousera\Automatidata\2017_Yellow_Taxi_Trip_Data.csv")
print("****************************************************************************************************************************************************************************************************")

# 2b. Understand the data - Inspect the data

print(df.head(10))

#Các cột có sự khác nhau về kiểu dữ liệu là non-numeric. Trong đó, có hai kiểu là datetime. Không có giá trị null
print(df.info())

#Số tiền cước tối đa là một giá trị rất lớn (1000 đôla) so với phạm vi giá trị từ 25 - 75%. Ngoài ra, việc có các giá trị âm cho số tiền cước là điều đáng ngờ. Hầu hết các chuyến đi từ 1-3 dặm, nhưng giá trị tối đa lại trên 33 dặm 
print(df.describe())

print("****************************************************************************************************************************************************************************************************")

# 2c. Understand the data - Investiagte the variables

print("Sort the data by trip distance from maximum to minimum value")
df_sort = df.sort_values(by='trip_distance', ascending=False)
print(df_sort.head(10))
print()

print("Sort the data by total amount and print the top 20 values")
total_amount_sorted = df.sort_values(by='total_amount', ascending=False)['total_amount']
print(total_amount_sorted.head(20))
print()

print("Sort the data by total amount and print the bottom 20 values")
print(total_amount_sorted.tail(20))
print()

print("How many of each payment type are represented in the data?")
print(df["payment_type"].value_counts())
print()

print("What is the average tip for trips paid for with credit card?")
avg_cc_tip = df[df["payment_type"] == 1]["tip_amount"].mean()
print("Avg. cc tip: ", avg_cc_tip)
print()

print("What is the average tip for trips paid for with cash?")
avg_cash_tip = df[df["payment_type"] == 2]["tip_amount"].mean()
print("Avg. cash tip: ", avg_cash_tip)
print()

print("How many times is each vendor ID represented in the data?")
print(df["VendorID"].value_counts())
print()

print("What is the mean total amount for each vendor?") 
print(df.groupby("VendorID").mean(numeric_only=True)[["total_amount"]])
print()

print("Filter the data for credit card payments only")
credit_card = df[df["payment_type"] == 1]
print(credit_card)
print()

print("Filter the credit-card-only data for passenger count only")
print(credit_card["passenger_count"].value_counts())
print()

print("Calculate the average tip amount for each passenger count (credit card payments only)")
print(credit_card.groupby(["passenger_count"]).mean(numeric_only=True)[["tip_amount"]])

#Sau khi xem xét tập dữ liệu, hai biến có nhiều khả năng giúp xây dựng mô hình dự đoán giá cước taxi là total_amount và trip_distance vì các biến này hiển thị hình ảnh về một chuyến đi taxi
