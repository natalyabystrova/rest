import React from 'react'
import {Link} from 'react-router-dom'


const BookItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.name}</td>
            <td>{item.author.last_name}</td>
            <td><button onClick={()=>deleteBook(item.id)}type='button'>Delete</button></td>
        </tr>
    )
}


const BookList = ({items}) => {
    return (
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>NAME</th>
                    <th>AUHTOR</th>
                    <th></th>
                </tr>
                {items.map((item) => <BookItem item={item} deleteBook={deleteBook}
/>)}
            </thead>
            <tbody>
                {items.map((item, key) => <BookItem key={key} item={item} />)}
            </tbody>
        </table>
        <Link to='/books/create'>Create</Link>
    )
}


export default BookList