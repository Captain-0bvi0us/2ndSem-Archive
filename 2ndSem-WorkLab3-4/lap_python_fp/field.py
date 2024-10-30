def field (items, *args):
    assert len(args)>0, "Список пуст"
    for item in items:
        for arg in args:
            if arg not in item:
                pass
            else:
                print(f"{arg.title()}:{item[arg]}")
                print("-"*20)
def main():
    goods = [
        {"name": "sofa", "color": "white"},
        {"name": "chair", "price": 1000, "color": "black"},
        {"name": "desk", "price": 2990, "color": "brown"},
        {"color": "blue"},
    ]
    field(goods, "name", "price")
main()