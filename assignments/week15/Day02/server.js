const express = require('express');
const app = express();
const path = require('path')

let arr = []

let counter = 1

//For parsing json body
app.use(express.json())

app.set('views', 'src/view')
app.set('view engine', 'pug')

//GET Return all items in the array
app.get('/', (req, res) => {
    // res.send(arr)
    res.render('index', { message: 'All items', item: `Total items ${counter - 1}`, array: arr })
})

//GET Return item with id in the array
app.get('/:id', (req, res) => {
    const id = req.params.id

    let item = getItem(id)

    res.render('index', item === null ? { message: "No matched item found", item: "No item", array: arr } : { message: 'Item Found', item: item.element, array: arr })
})

//POST Push object in array
app.post('/', (req, res) => {
    let item = req.body

    //Assign id to object
    item.id = counter++

    //insert item in array
    arr.push(item)

    res.render('index', { message: "Item Added", item: item, array: arr })
})

//DELETE
app.delete('/:id', (req, res) => {
    const id = req.params.id

    let elem = getItem(id)

    res.render('index', elem === null ? { message: 'Not found', item: `No item with id : ${id}`, array: arr } : { message: "Deleted", item: arr.splice(elem.index, 1)[0], array: arr })
})

//PUT update element
app.put('/:id', (req, res) => {
    const id = req.params.id
    const body = req.body

    const item = getItem(id)

    //Check if item is available
    if (item === null) {
        res.status(404)
            .json({ message: `No item found with id : ${id}` })
    } else {
        //Add current id to body
        let id = item.element.id
        body.id = id

        //Update the item
        arr.splice(item.index, 1, body)

        res.status(200).render('index', { message: 'Updated', item: body, array: arr })
    }
})

//Get specified item 
function getItem(id) {
    let item1 = null
    arr.forEach((element, index) => {
        if (String(element.id) === id) {
            item1 = { element, index }
        }
    })
    return item1
}

//Start server on port 3000
app.listen(3000, () => {
    console.log("Server started")
})