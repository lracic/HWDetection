# HW Recognition #

**API URL:** http://51.195.100.125:5000/analyze<br />
**Method:** POST<br />
**Required Input:** file<br />
**Postman collection:** Last page<br />

**Output:** List of rectangle objects<br />
Rectangle object is defined as:<br />

```{
    'min_x': float,
    'max_x': float,   
    'min_y': float,  
    'max_y': float  
}```

Sample of output:<br />

`[
    {
        'min_x': 100, 
        'max_x': 200, 
        'min_y': 100, 
        'max_y': 200
    },
    {
        'min_x': 222.5, 
        'max_x': 250, 
        'min_y': 500, 
        'max_y': 700
    },
]`

**Test page:** http://51.195.100.125:5000/<br />
**CSS:** to be added<br />
**Description:**<br />

At the moment, the API is returning *test data* (a box around 10% of the border of the image) since the training of the network unfortunately failed last night. The training is in the progress at the moment and as soon as it is done, the API will be updated.<br />

After the model is done training and the API is updated, the bounding boxes will be drawn with the coordinates that the model outputs as predictions of where handwritten data is on the page.  <br />


 
Postman collection:<br />

`{
    "info": {
        "name": "HW Recognition",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
    },
    "item": [
        {
            "name": "http://51.195.100.125:5000/analyze",
            "request": {
                "method": "POST",
                "header": [],
                "body": {
                    "mode": "formdata",
                    "formdata": [
                        {
                            "key": "file",
                            "type": "file",
                            "src": "/C:/001.jpg"
                        }
                    ]
                },
                "url": {
                    "raw": "http://51.195.100.125:5000/analyze",
                    "protocol": "http",
                    "host": [
                        "51",
                        "195",
                        "100",
                        "125"
                    ],
                    "port": "5000",
                    "path": [
                        "analyze"
                    ]
                }
            },
            "response": []
        }
    ],
    "protocolProfileBehavior": {}
}`


