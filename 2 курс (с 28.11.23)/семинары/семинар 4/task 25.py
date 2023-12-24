# text = "a a a b c a a d c d d"
# list_symbol = text.split()
# print(list_symbol)
# uniq_symbols = dict()
# print(uniq_symbols)
# for symbol in uniq_symbols:
#     if symbol not in uniq_symbols:
#         uniq_symbols[symbol] = 0
#         print(symbol, end = " ")
    
#     else:
#         uniq_symbols[symbol] +=1
#         print(f"{symbol}_{uniq_symbols[symbol]}", end = " ")
        
        
        
        
text = "a a a b c a a d c d d"
list_symbols = text.split()
print(list_symbols)
uniq_symbols = dict()
print()
result=""
for symbol in list_symbols:
    if symbol not in uniq_symbols:
        result += f'{symbol} '
    else:
        result += f'{symbol}_{uniq_symbols[symbol]} '
    uniq_symbols[symbol] = uniq_symbols.get(symbol,0)+1        
print(result.strip())