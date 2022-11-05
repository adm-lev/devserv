import React from "react";


const ProjectItem = ({project}) => {
    return (
        <ul class="project-item">
            <li>{project.name}</li>
            <li>{project.users}</li>
            <li>{project.projectUrl}</li>  
            {/* <li><button>Delete</button></li>   */}
        </ul>
    )
};

const ProjectList = ({projects}) => {
    const clear_projects = []
    for (const i in projects.results){
        clear_projects.push(projects.results[i])
    }
    return (
        <div class="project-div">
            <ul class="project-list">
                <li>Project name</li>
                <li>User name</li>
                <li>Project URL</li>                               
            </ul>
            {clear_projects.map((project_) => <ProjectItem project={project_}/>)}
        </div>    
    )
    
};

export default ProjectList;