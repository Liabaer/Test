import json

x = {
    "planRouteParam": {
        "orderParamList": [
            {
                "orderId": "21435897",
                "pickUpJob":
                    {
                        "readyTime": "1617305129",
                        "dueTime": "1617305489",
                        "serviceTime": "2M",
                        "longitude": 145.121612,
                        "latitude": -37.816033
                    },
                "deliveryJob": {
                    "readyTime": "1617305365",
                    "dueTime": "1617305725",
                    "serviceTime": "1M",
                    "longitude": 145.121635,
                    "latitude": -37.81596
                },
                "status": "preparing",
            },
            {
                "orderId": "21436210",
                "pickUpJob":
                    {
                        "readyTime": "1617305710",
                        "dueTime": "1617306070",
                        "serviceTime": "2M",
                        "longitude": 145.094842,
                        "latitude": -37.857932
                    },
                "deliveryJob": {
                    "readyTime": "1617304990",
                    "dueTime": "1617305170",
                    "serviceTime": "1M",
                    "longitude": 145.094842,
                    "latitude": -37.857932
                },
                "status": "preparing",
            }
        ],
        "easiRider": {
            "longitude": 145.122944,
            "latitude": -37.911291,
            "startTime": "2",
        },
        "taskcode": "e03b3196913e11eb82ab06ebd4b32378",
    }
}
print(json.dumps(x))