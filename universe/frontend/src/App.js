// import logo from './logo.svg';
import './App.css';
import React from 'react';
import UserList from './components/User';
import MenuBlock from './components/Menu';
import FooterBlock from './components/Footer';
import axios from 'axios';
import ProjectList from './components/Projects';
import NoteList from './components/Notes';
import tabSwitch from './tunning';

class App extends React.Component {
  constructor (props){
    super(props);
    this.state = {
      'users': [],
      'menu': [],
      'footer': [],
      'projects': [],
      'notes': [],
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

    this.setState({
      'menu': menu,
      'footer': footer,
    })

    axios.get('http://localhost/api/users/').then(response => {
      this.setState({
        'users': response.data,        
      });      
    }).catch(error => console.log(error))

    

    axios.get('http://localhost/api/projects/').then(response => {
      this.setState({
        'projects': response.data,        
      });
    }).catch(error => console.log(error))

    axios.get('http://localhost/api/todos/').then(response => {
      this.setState({
        'notes': response.data,        
      });
    }).catch(error => console.log(error))

  };

  render() {
    return (        
      <div>
        <MenuBlock menu={this.state.menu}/>
        <UserList  users={this.state.users}/>
        
        <hr/>
        <ProjectList projects={this.state.projects}/>
        <hr/>
        <NoteList notes={this.state.notes}/>
        <FooterBlock footer={this.state.footer}/>
      </div> 
      
      )
  };
  
}

export default App;
