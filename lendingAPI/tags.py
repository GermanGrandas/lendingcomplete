tags = [
    {
        "name" : "create_product",
        "description" :"Create new product",
        "parameters" : [{
            "in": "body",
            "name": "body",
            "description": "Product to be created",
            "required": "true",
            "schema": {
                "user_id" : "str",
                "product_id": "str",
                "date": "date",
                "amount": "float",
                "status": "str"
            }          
        }],
        "responses" : {
            "200" : {
                "description": "The product was correctly saved"
            },
            "500" : {
                "description":"Something Happened"
            }
        }
    }
]