import React from 'react'
import { useParams } from 'react-router-dom'


const BookItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.name}</td>
            <td>{item.author.last_name}</td>
        </tr>
    )
}


const BookList = ({items}) => {
    let { id } = useParams();
    console.log(id)
    let filtered_items = items.filter((item) => item.author.id == id)
    return (
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>NAME</th>
                    <th>AUTHOR</th>
                </tr>
            </thead>
            <tbody>
                {filtered_items.map((item, key) => <BookItem key={key} item={item} />)}
            </tbody>
        </table>
    )
}

export default BookList