import React from "react";


class UserForm extends React.Component {
    constructor (props) {
        super(props);
        this.state = {
            userName: '',
            firstName: '',
            lastName: '',
            email: '',
        };
    }
        handleChange (event){
            this.setState({
                [event.target.name]: [event.target.value]
            });
        }

        handleSubmit (event) {

            this.props.createUser(
                this.state.userName,
                this.state.firstName,
                this.state.lastName,
                this.state.email
            );

            // console.log(this.state.userName);
            // console.log(this.state.firstName);
            // console.log(this.state.lastName);
            // console.log(this.state.email);
            event.preventDefault();
        }

        render () {
            return(
                <form onSubmit={event => this.handleSubmit(event)}>
                    <div className="form-group">
                        <label htmlFor="userName">User name</label>
                        <input type="text" className="form-control" name="userName" 
                            value={this.state.userName} onChange={event => this.handleChange(event)}/>
                        <label htmlFor="firstName">First name</label>
                        <input type="text" className="form-control" name="firstName" 
                            value={this.state.firstName} onChange={event => this.handleChange(event)}/>
                        <label htmlFor="lastName">Last name</label>
                        <input type="text" className="form-control" name="lastName"
                            value={this.state.lastName} onChange={event => this.handleChange(event)}/>
                        <label htmlFor="email">E-mail</label>
                        <input type="email" className="form-control" name="email"
                            value={this.state.email} onChange={event => this.handleChange(event)}/>                        
                    </div>
                    <input type="submit" className="btn btn-primary" value="Save"/>
                </form>
            );
        }
    
    
}

export default UserForm;