prices = {
    "Store_A": {"Apple": 0.50, "Banana": 0.30},
    "Store_B": {"Apple": 0.60, "Banana": 0.25},
    "Store_C": {"Apple": 0.55, "Banana": 0.35}
}
for id, info in prices.items():
    print("Store:",id)
    for x in info:
        print(x, ":",info[x])