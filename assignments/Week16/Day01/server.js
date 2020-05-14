const express = require('express')
const app = express()
const uuid = require('uuid').v4

const cookieParser = require('cookie-parser')

const config = {
    maxAge: 1000 * 60 * 10,
    httpOnly: true,
    signed: true
}

//Pass secret key to encrypt the cookie
app.use(cookieParser('secret_key'))

//Index
app.get('/', (req, res) => {
    const id = uuid()
    res.cookie('token', id, config)
    res.cookie('max_age', Number(config.maxAge)/60000  , config)
    res.send('Cookie Created , follow link : localhost:3000/cookie')
})

//Get Cookie
app.get('/cookie', (req, res) => {
    res.send(req.signedCookies)
})

app.listen(3000, console.log('Server started'))