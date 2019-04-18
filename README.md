#Open Server
1. Open terminal and cd to folder path
2. Run this command "python api.py"
3. This message will appear so the sever is running
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

#Run on Postman

1. Type url "http://127.0.0.1:5000/"
2. On body tap will appear json data

 /
  
    "Title": "Dimension Assesment",
    
    "Name": "Perakit Sakulsaithongkum",
    
    "Function & Path": {
    
        "FirstFactorial": "api/firstfactorial/",
        
        "FirstReverse": "api/firstreverse/",
        
        "AlphabetSoup": "api/alphabetsoup/"
        
    }
/

![alt text](https://github.com/gapprapp/Dimension-Assessment/blob/master/readme%20pic/postman.png)
  
3. Copy path from json (ex. api/firstfactorial/) with function you want to run
4. Paste it at the end of url
5. Change "GET" to "POST"
6. click "form-data"
7. Type Key as "input"
8. Type Value as "parameter"



