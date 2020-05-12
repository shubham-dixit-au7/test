const express = require('express');
const path = require('path');

const routes = express.Router();

// Home page
routes.get('/', (req, res) => {
    res.status(200).sendFile(path.join(__dirname, '/public/index.html'));
});

// view all players
routes.get('/view', (req, res) => {
    res.render('view', {players});
});

// add a player
routes.get('/add', (req, res) => {
    let data ={};
    if (req.query.addFailed){
        data.addFailed = true;
    } else if (req.query.added) {
        data.added = true;
    };
    res.render('add', data);
});

routes.post('/addTennisPlayer', (req, res) => {
    if (req.body.name && req.body.country){
        players.push({
            "name": req.body.name,
            "country": req.body.country
        });
        res.redirect('/add?added=true');
    } else {
        res.redirect('/add?addFailed=true');
    }
});

// update a player
routes.get('/update', (req, res) => {
    let data ={};
    if (req.query.updateFailed){
        data.updateFailed = true;
    } else if (req.query.updated) {
        data.updated = true;
    } else if (req.query.no_match) {
        data.no_match = true;
    };
    res.render('update', data);
});

routes.put('/updateTennisPlayer', (req, res) => {
    if (req.body.name && req.body.country){
        const found = players.some(player => player.name === req.body.name);
        if (found) {
            players.forEach(player => {
                if (player.name === req.body.name){
                    player.country = req.body.country;
                }
            })
            res
            res.redirect('/update?updated=true');
        } else {
            res.redirect('/update?no_match=true');
        }
    } else {
        res.redirect('/update?updateFailed=true');
    }
});


// delete a player
routes.get('/delete', (req, res) => {
    let data ={};
    if (req.query.deleteFailed){
        data.deleteFailed = true;
    } else if (req.query.deleted) {
        data.deleted = true;
    } else if (req.query.no_match) {
        data.no_match = true;
    };
    res.render('delete', data);
});

routes.post('/deleteTennisPlayer', (req, res) => {
    if (req.body.name && req.body.country){
        const found = players.some(player => player.name === req.body.name && player.country === req.body.country);
        if (found) {
            players = players.filter(player => !(player.name === req.body.name && player.country === req.body.country));
            for (let player of players){

            }
            res.redirect('/delete?deleted=true');
        } else {
            res.redirect('/delete?no_match=true');
        }
    } else {
        res.redirect('/delete?deleteFailed=true');
    }
});

module.exports = routes;