const express = require('express')
const app = express()

app.get('/', function (req, res) {
  //make a request to the main file
    res.sendFile(__dirname + '/login.html')
})

app.get('/mainDB', function (req, res) {
    //make a request to the main file
      res.sendFile(__dirname + '/main.html')
  })

app.listen(3000, function () {
    console.log('app Stas:200(ok) --> app init on this link: http://127.0.0.1:3000')
})