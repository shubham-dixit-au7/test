// importing packages
const express = require('express')
const hbs = require('hbs')
const morgan = require('morgan')
const path = require('path')

const routes =require('./route.js')

//setting up the PORT number
const PORT =  process.env.port || 8088;


//setting up express
const app = express();


//setting up middleware
app.use(morgan('tiny'));
app.use(express.urlencoded({ extended: false }));
app.use(express.json());


//setting the hbs template engine
app.set('view engine', 'hbs');
app.set('views', 'src/views');

//setting up the partial pages
hbs.registerPartials(path.join(__dirname, "view", "partials"));


//mounting the default route
app.use('/',routes)

// players DB
players = [];


app.listen(PORT, () => {
    console.log("Express server listing on ${PORT}");
});
