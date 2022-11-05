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
import {BrowserRouter, Route, Routes, Link, Navigate} from 'react-router-dom'
import NotFound404 from './components/NotFound404';
import ProjectUser from './components/Userprojects';
import ProjectDetail from './components/ProjectDetail';

class App extends React.Component {
  constructor (props){
    super(props);
    this.state = {
      'users': [],      
      'footer': [],
      'projects': [],
      'notes': [],
    }
  }

  componentDidMount() {
   
    const footer = [
      'This project was built with engines of Django 3.2.8 on backend, React JS 18.2.0 on frontend and PostgreSQL as a DB. OS Ubuntu server 22.04.',
      'Made by Eugene Lavrenko'
    ];

    this.setState({      
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
        <BrowserRouter>
        <div className="menu container">
          <nav className='navigation'>
            <li className="menu-item">
              <Link to="/">Users</Link>
            </li>
            <li className="menu-item">
              <Link to="/projects">Projects</Link>
            </li>
            <li className="menu-item">
              <Link to="/todos">Notes</Link>
            </li>          
          </nav>
        </div>
          <Routes>
            <Route exact path="/" element={<Navigate to="/users"/>}/>
            <Route exact path="/users">
              <Route index element={<UserList  users={this.state.users}/>}/>
              <Route path=":userId" element={<ProjectUser projects={this.state.projects}/>}/>
            </Route>        
            <Route exact path="/projects">
              <Route index element={<ProjectList projects={this.state.projects}/>}/>
              <Route path=":projectId" element={<ProjectDetail projects={this.state.projects}/>}/>
            </Route>         
            <Route exact path="/todos" element={<NoteList notes={this.state.notes}/>}/>
            <Route path="*" element={<NotFound404/>}/>            
          </Routes>
        </BrowserRouter>                
        <FooterBlock footer={this.state.footer}/>
      </div>       
      )
  };  
};

export default App;
