'use strict';
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
import LoginForm from './components/Auth';
import Cookies from 'universal-cookie';

class App extends React.Component {
  constructor (props){
    super(props);
    this.state = {
      'users': [],      
      'footer': [],
      'projects': [],
      'notes': [],
      'accessToken': '',
      'refreshToken': '',
      'token': '',
      'loggedAs': '',
    };
  }

  logout () {
    this.setToken('');
    this.setState({
      'users': [],
      'projects': [],
      'notes': [],
      'loggedAs': '',
    })
  }

  isAuth () {
    return !!this.state.accessToken;    
    // return !!this.state.token;
    
  }

  setToken (token) {      
    const cookies = new Cookies();
    cookies.set('accessToken', token['access']);
    cookies.set('refreshToken', token['refresh']);
    cookies.set('loggedAs', this.state.loggedAs);
    // cookies.set('token', token);    
    this.setState({
      'accessToken': token['access'],
      'refreshToken': token['refresh'],
      // 'token': token
    }, () => this.loadData());
  }

  getTokenStorage () {
    const cookies = new Cookies();
    const token = cookies.get('accessToken');
    const user = cookies.get('loggedAs');
    // const token = cookies.get('token');    
    this.setState({
      'accessToken': token['access'],
      'refreshToken': token['refresh'],
      'loggedAs': user,
      // 'token': token
    }, () => this.loadData());
  }

  getToken (username,password) {
    const baseUrl = 'http://localhost:8000/api';
    const data = {username: username, password: password};    
    axios.post(baseUrl+'/token/', data).then(response => {
    // axios.post(baseUrl+'-token-auth/', data).then(response => { 
      // this.setToken(response.data['token']);   
      this.setToken(response.data);   
      this.setState({
        'loggedAs': username
      });        
    }).catch(error => alert('Wrong username or password'));
  }

  getHeaders () {
    let headers = {      
      'Content-Type': 'application/json',      
    };
    if (this.isAuth()) {
      headers['Authorization'] = 'Bearer ' + this.state.accessToken;
      // headers['Authorization'] = 'Token '+this.state.token;
    };    
    return headers;
  }

  loadData () {
    const baseUrl = 'http://localhost:8000/api';
    const headers = this.getHeaders();
    const footer = [
      'This project was built with engines of Django 3.2.8 on backend, React JS 18.2.0 on frontend and PostgreSQL as a DB. OS Ubuntu server 22.04.',
      'Made by Eugene Lavrenko'
    ];

    this.setState({      
      'footer': footer,
    });

    axios.get(baseUrl+'/users/',{headers}).then(response => {
      this.setState({
        'users': response.data,        
      });      
    }).catch(error => console.log(error));    
    console.log(headers)
    axios.get(baseUrl+'/projects/', {headers}).then(response => {
      this.setState({
        'projects': response.data,        
      });
    }).catch(error => console.log(error));

    axios.get(baseUrl+'/todos/', {headers}).then(response => {
      this.setState({
        'notes': response.data,        
      });
    }).catch(error => console.log(error));
  };
  

  componentDidMount() {   
    this.getTokenStorage();
  }

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
            <li className="menu-item">
              {this.isAuth() ? <button onClick={() => this.logout()}>
                              {`Logout as ${this.state.loggedAs}`}
                              </button> : <Link to="/login">Login</Link>}
            </li>        
          </nav>
        </div>
          <Routes>
            <Route exact path="/" element={<Navigate to="/users"/>}/>
            <Route exact path="/login" element={<LoginForm getToken={(username, password) => 
              this.getToken(username, password)}/>}/>
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
