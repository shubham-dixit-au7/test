const express = require('express');
const app = express();

let arr = []

let counter = 1

app.use(express.json())

//GET Return all items in the array
app.get('/', (req, res) => {
    res.send(arr)
})

//GET Return item with id in the array
app.get('/:id', (req, res) => {
    const id = req.params.id

    let item = getItem(id)

    res.json(item === null ? { message: "No matched item found" } : { item: item.element })
})

//POST Push object in array
app.post('/', (req, res) => {
    let item = req.body

    //Assign id to object
    item.id = counter++

    //insert item in array
    arr.push(item)

    res.json({ message: "Item Added", item: item, array: arr })
})

//DELETE
app.delete('/:id', (req, res) => {
    const id = req.params.id

    let elem = getItem(id)

    res.json(elem === null ? { messge: `No Item with id : ${id}` } : { message: "Deleted", item: arr.splice(elem.index, 1)[0], array: arr })
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

        res.status(200)
            .json({ message: 'Updated', item: body, array: arr })
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