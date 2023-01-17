import React from 'react';
import AuthorList from './components/Author.js'
import BookList from './components/Book.js'
import {HashRouter, Route} from 'react-router-dom'



class App extends React.Component {
    constructor(props) {
    super(props)
    const author1 = {id: 1, first_name: 'Александр', last_name: 'Грин', birthday_year: 1880}
    const author2 = {id: 2, first_name: 'Александр', last_name: 'Пушкин', birthday_year: 1799}
    const authors = [author1, author2]
    const book1 = {id: 1, name: 'Алые паруса', author: author1}
    const book2 = {id: 2, name: 'Золотая цепь', author: author1}
    const book3 = {id: 3, name: 'Пиковая дама', author: author2}
    const book4 = {id: 4, name: 'Руслан и Людмила', author: author2}
    const books = [book1, book2, book3, book4]
    this.state = {
        'authors': authors,
        'books': books
    }
  }

    render() {
        return (
            <div className="App">
                <HashRouter>
<                                <Route exact path='/' component={() => <AuthorList
items={this.state.authors} />} />
                                 <Route exact path='/books' component={() => <BookList
items={this.state.books} />} />
                </HashRouter>
            </div>
        )
    }
}
export default App;







