import React from 'react'
import {Link} from 'react-router-dom'

const AuthorItem = ({item}) => {
    return (
        <tr>
            <td><Link to={`author/${item.id}`}>{item.id}</Link></td>
            <td>{item.first_name}</td>
            <td>{item.last_name}</td>
            <td>{item.birthday_year}</td>
        </tr>
    )
}


const AuthorList = ({items}) => {
    return (
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>FIRST_NAME</th>
                    <th>LAST_NAME</th>
                    <th>BIRTHDAY_YEAR</th>
                </tr>
            </thead>
            <tbody>
                {items.map((item, key) => <AuthorItem key={key} item={item} />)}
            </tbody>
        </table>
    )
}
export default AuthorList