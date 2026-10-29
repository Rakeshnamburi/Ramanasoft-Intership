# # Task 6: Stock Portfolio Management System  


# # Problem Statement:  
# # You are building a stock portfolio management system. Stock transactions are stored as tuples: 
# # (stock_symbol, transaction_type, quantity, price_per_share, date) where transaction_type is either 
# # "BUY" or "SELL". You need to calculate portfolio performance and provide investment insights




# # Sample Input:  

transactions = [  
("AAPL", "BUY", 100, 150.00, "2023-01-15"),  
("GOOGL", "BUY", 50, 2800.00, "2023-01-20"),  
("AAPL", "BUY", 50, 160.00, "2023-02-10"),  
("MSFT", "BUY", 75, 300.00, "2023-02-15"),  
("AAPL", "SELL", 75, 170.00, "2023-03-05"),  
("GOOGL", "SELL", 20, 2900.00, "2023-03-10"),  
("TSLA", "BUY", 40, 800.00, "2023-03-15"),  
("MSFT", "SELL", 25, 320.00, "2023-04-01"),  
("TSLA", "SELL", 15, 750.00, "2023-04-10"),  
("AAPL", "BUY", 25, 155.00, "2023-04-15")  
]  
current_prices = {  
"AAPL": 175.00,  
"GOOGL": 2850.00,  
"MSFT": 310.00,  
"TSLA": 780.00  
}


# # 1. Calculate current holdings for each stock

stock_holdings = {}
for transaction in transactions:
    stock_symbol, transaction_type, quantity, price_per_share, date = transaction
    if transaction_type == "BUY":
        stock_holdings[stock_symbol] = stock_holdings.get(stock_symbol, 0) + quantity
    elif transaction_type == "SELL":
        stock_holdings[stock_symbol] = stock_holdings.get(stock_symbol, 0) - quantity

for stock, holdings in stock_holdings.items():
    print(f"Stock: {stock}, Current Holdings: {holdings}")

# # ekkada use chesina technique enti ante prathi transaction lo stock symbol, transaction type, quantity, price per share, and date ni unpack chesthundi.
# # If transaction type is "BUY", it adds the quantity to the current holdings for that stock. If transaction type is "SELL", it subtracts the quantity from the current holdings. 
# # Finally, it prints the current holdings for each stock.
# # buy and sell transactions ni iterate chesi, stock symbol ki corresponding quantity ni add or subtract chesthundi. Final ga, current holdings print chesthundi.
# # price and share and date ni unpack chesi, transaction type check chesi, stock symbol ki corresponding quantity ni add or subtract chesthundi. Final ga, current holdings print chesthundi.
# # f stock endhuku use chesam ante, stock symbol ki corresponding quantity ni track cheyadaniki use chesam.
# # buy chesinapudu + and sell chesinapudu - chesthundi. Final ga, current holdings print chesthundi.



# # 2. Determine profit/loss for each stock  
loss_profit = {}
for transaction in transactions:
    stock_symbol, transaction_type, quantity, price_per_share, date = transaction
    if transaction_type == "SELL":
        buy_transactions = [t for t in transactions if t[0] == stock_symbol and t[1] == "BUY"]
        total_buy_quantity = sum(t[2] for t in buy_transactions)
        total_buy_cost = sum(t[2] * t[3] for t in buy_transactions)
        average_buy_price = total_buy_cost / total_buy_quantity if total_buy_quantity > 0 else 0
        profit_loss = (price_per_share - average_buy_price) * quantity
        loss_profit[stock_symbol] = loss_profit.get(stock_symbol, 0) + profit_loss  

for stock, profit_loss in loss_profit.items():
    print(f"Stock: {stock}, Profit/Loss: ${profit_loss:.2f}")   

#     # ekkada sum function use chesi prathi stock ki buy transactions ni filter chesi, total buy quantity and total buy cost calculate chesthundi.
#     # average buy price calculate chesi, sell transaction price tho compare chesi profit or loss calculate
#     # t[2] * t[3] ante prathi buy transaction lo quantity and price per share ni multiply chesi total buy cost calculate chesthundi.
#     # Final ga, profit or loss print chesthundi.
#     # stock symbol ki corresponding profit or loss ni track cheyadaniki loss_profit dictionary use chesthundi.
#     # transaction type "SELL" unte, buy transactions ni filter chesi, total buy quantity and total buy cost calculate chesthundi.
#     # Average buy price calculate chesi, sell transaction price tho compare chesi profit or loss calculate chesthundi. Final ga, profit or loss print chesthundi.
#     # total buy quantity and total buy cost calculate chesi, average buy price calculate chesi, sell transaction price tho compare chesi profit or loss calculate chesthundi. Final ga, profit or loss print chesthundi.
#     # share - price * quantity ante prathi sell transaction lo price per share and quantity ni multiply chesi profit or loss calculate chesthundi.

#     # 3. Find the best and worst performing stocks  

best_stock = max(loss_profit.items(), key=lambda x: x[1])
worst_stock = min(loss_profit.items(), key=lambda x: x[1])

print(f"Best performing stock: {best_stock[0]}, Profit/Loss: ${best_stock[1]:.2f}")
print(f"Worst performing stock: {worst_stock[0]}, Profit/Loss: ${worst_stock[1]:.2f}")

#     # 4. Calculate total portfolio value and overall profit/loss

total_portfolio_value = sum(stock_holdings[stock] * current_prices[stock] for stock in stock_holdings)
overall_profit_loss = sum(loss_profit.values()) 

print(f"Total Portfolio Value: ${total_portfolio_value:.2f}")
print(f"Overall Profit/Loss: ${overall_profit_loss:.2f}")

# ekkada 2f endhuku use chesam ante, total portfolio value calculate chesi, overall profit or loss calculate chesthundi.


     # 5. Identify stocks with the highest trading volume  

stock_volumes = {}
for transaction in transactions:
    stock_symbol, transaction_type, quantity, price_per_share, date = transaction
    stock_volumes[stock_symbol] = stock_volumes.get(stock_symbol, 0) + quantity

highest_volume_stock = max(stock_volumes.items(), key=lambda x: x[1])
print(f"Stock with the highest trading volume: {highest_volume_stock[0]}, Volume: {highest_volume_stock[1]}")   


# ekkada highest trading volume identify cheyadaniki, prathi transaction lo stock symbol and quantity ni track chesi, stock_volumes dictionary lo store chesthundi.
# Final ga, max function use chesi highest trading volume unna stock ni find chesthundi.
# x:x[1] ante prathi stock volume tuple lo 2nd element (volume) ni key ga use chesi max function use chesi highest trading volume unna stock ni find chesthundi. 
# Final ga, highest trading volume stock and volume print chesthundi.



