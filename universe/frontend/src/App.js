import logo from './logo.svg';
import './App.css';
import React from 'react';
import UserList from './components/User';
import MenuBlock from './components/Menu';
import FooterBlock from './components/Footer';
import axios from 'axios';

class App extends React.Component {
  constructor (props){
    super(props);
    this.state = {
      'users': [],
      'menu': [],
      'footer': [],
    }
  }

  componentDidMount() {
    const menu = [
      'Main',
      'Projects',
      'Users',
      'Notes',
      'Contacts',
    ];

    const footer = [
      'This project was built with engines of Django 3.2.8 on backend, React JS 18.2.0 on frontend and PostgreSQL as a DB. OS Ubuntu server 22.04.',
      'Made by Eugene Lavrenko'
    ];

    axios.get('http://localhost/api/users/').then(response => {
      this.setState({
        'users': response.data,
        'menu': menu,
        'footer': footer,
      });
    }).catch(error => console.log(error))
  };

  render() {
    return (        
      <div>
        <MenuBlock menu={this.state.menu}/>
        <UserList users={this.state.users}/>
        <FooterBlock footer={this.state.footer}/>
      </div> 
      
      )
  };
}

export default App;
