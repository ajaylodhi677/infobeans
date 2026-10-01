products=[
         {"name":"laptop","price":8000},
         {"name":"mpobiole","price":6000},
         {"name":"paper","price":15000}
]
result=sorted(products,key=lambda x:x["price"])
print(result)