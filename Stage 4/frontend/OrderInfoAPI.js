// Getting orders
function get_orders_api(){
    results = Orders.query.all()
    result_list = []
    for (item in results){
        item_list = []
        for (i in item.items){
            item_list.append({
                'id': i.id,
                'pname': i.pname,
                'flavors': i.flavors,
                'price': i.price
            })
        }
        result_list.append({
            "id": item.id,
            "email": item.email,
            'total': item.total,
            'items': item_list
        })
    }
    return json.dumps({'data':result_list})}
    