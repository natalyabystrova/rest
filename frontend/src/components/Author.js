import React from 'react'

const AuthorItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.first_name}</td>
            <td>{item.last_name}</td>
            <td>{item.birthday_year}</td>
        </tr>
    )
}


const AuthorList = ({items}) => {
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>FIRST_NAME</th>
                <th>LAST_NAME</th>
                <th>BIRTHDAY_YEAR</th>
            </tr>
            {items.map((item) => <AuthorItem item={item} />)}
        </table>
    )
}
export default AuthorList