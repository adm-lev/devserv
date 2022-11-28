import React from "react";
import { Link } from "react-router-dom";



const UserItem = ({user, deleteUser}) => {
    return (
        <ul className="user-item">
            <li>
            <Link to={`/users/${user.id}`}>{user.firstName}</Link>
            </li>
            <li>{user.lastName}</li>
            <li>{user.userName}</li>
            <li>{user.email}</li>
            <li><button onClick={() => deleteUser(user.id)} type="button">Delete</button></li>
        </ul>
    )
};

const UserList = ({users, deleteUser}) => {
    const clear_users = []
    for (const i in users.results){
        clear_users.push(users.results[i])
    }
    
    return (
        <div className="all-cont">
            <div className="user-div">
                <ul className="user-list">
                    <li>First name</li>
                    <li>Last name</li>
                    <li>Username</li>
                    <li>Email</li>               
                </ul>                     
                {clear_users.map((user_) => <UserItem user={user_} deleteUser={deleteUser}/>)}       
            </div>            
                <Link className="create-btn" to={'/users/create'}>Create</Link>
        </div>
            
    )
    
};

export default UserList;