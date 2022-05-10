import React from 'react';
import APIService from './APIService';
import {useCookies} from 'react-cookie';

function ArticleList(props){

    const [token] = useCookies(['mytoken'])

    const editBtn = (article) => {
        /*Pass back to App.js */
        props.editBtn(article)
    }

    const deleteBtn = (article) => {
        APIService.DeleteArticle(article.id, token['mytoken'])
        .then(() => props.deleteBtn(article))
    }

    return (
        /*if props.articles is present then map it*/
        <div>
             
            {props.articles && props.articles.map(article => {
                return (
                    <div key = {article.id}>
                        <h3>{article.title}</h3>
                        <p>{article.description}</p>
                        { /* Code for buttons */ }
                        
                        <div className="row">
                            <div className="col-md-1">
                                <button className="btn btn-primary" onClick={() => editBtn(article)}>Update</button>
                            </div>
                            <div className="col">
                                <button onClick = {() => deleteBtn(article)} className="btn btn-danger">Delete</button>
                            </div>        
                        </div>  
                        { /* horizontal Line between articles */ }  
                        <hr className="hrclass"/>
                    </div>
                )
            })}
        </div>
    )
}

export default ArticleList

