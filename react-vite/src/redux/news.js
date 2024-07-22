const GET_ALL_NEWS = '/news/GET_ALL_NEWS'
const GET_ONE_NEWS = '/news/GET_ONE_NEWS'
const CREATE_NEWS = '/news/CREATE_NEWS'
const EDIT_NEWS = '/news/EDIT_NEWS'
const DELETE_NEWS = '/news/DELETE_NEWS'
const ADD_COMMENT = '/news/ADD_COMMENT'
const EDIT_COMMENT = '/news/EDIT_COMMENT'
const DELETE_COMMENT = '/news/DELETE_COMMENT'
const ADD_LIKE = '/news/ADD_LIKE'
const REMOVE_LIKE = '/news/REMOVE_LIKE'

const getAllNews = news => {
    return {
        type: GET_ALL_NEWS,
        news
    }
}

const getOneNews = news => {
    return {
        type: GET_ONE_NEWS,
        news
    }
}

const createNews = news => {
    return {
        type: CREATE_NEWS,
        news
    }
}

const editNews = news => {
    return {
        type: EDIT_NEWS,
        news
    }
}

const deleteNews = newsId => {
    return {
        type: DELETE_NEWS,
        newsId
    }
}

const addComment = comment => {
    return {
        type: ADD_COMMENT,
        comment
    }
}

const editComment = comment => {
    return {
        type: EDIT_COMMENT,
        comment
    }
}

const deleteComment = (commentId, newsId) => {
    return {
        type: DELETE_COMMENT,
        commentId,
        newsId
    }
}

const addLike = news => {
    return {
        type: ADD_LIKE,
        news
    }
}

const removeLike = (id, newsId) => {
    return {
        type: REMOVE_LIKE,
        id,
        newsId
    }
}

export const fetchAllNews = () => async (dispatch) => {
    const res = await fetch('/api/news/')

    if (res.ok) {
        const news = await res.json()
        dispatch(getAllNews(news))
        return news
    }
}

export const fetchNewsDetails = (newsId) => async (dispatch) => {
    const res = await fetch(`/api/news/${newsId}/`)

    if (res.ok) {
        const news = await res.json()
        dispatch(getOneNews(news))
        return news
    }
}

export const fetchCreateNews = (news) => async (dispatch) => {
    const res = await fetch('/api/news/new/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(news)
    })

    if (res.ok) {
        const news = await res.json()
        dispatch(createNews(news))
        return news
    }
}

export const fetchEditNews = (news, newsId) => async (dispatch) => {
    const res = await fetch(`/api/news/${newsId}/edit/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(news)
    })

    if (res.ok) {
        const updatedNews = await res.json();
        dispatch(editNews(updatedNews))
        dispatch(fetchNewsDetails(newsId))
        return updatedNews
    }
}

export const fetchDeleteNews = (newsId) => async (dispatch) => {
    const res = await fetch(`/api/news/${newsId}/delete/`, {
        method: 'DELETE'
    })
    if (res.ok) {
        dispatch(deleteNews(newsId))
        return
    }
}

export const fetchAddComment = (comment) => async (dispatch) => {
    const res = await fetch('/api/news/comment/new/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(comment)
    })
    if (res.ok) {
        const newComment = await res.json()
        dispatch(addComment(newComment))
        return newComment
    }
}

export const fetchEditComment = (comment, commentId, newsId) => async (dispatch) => {
    const res = await fetch(`/api/news/${commentId}/comment/edit/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(comment)
    })
    if (res.ok) {
        const updatedComment = await res.json()
        dispatch(editComment(updatedComment))
        dispatch(fetchNewsDetails(newsId))
        return updatedComment
    }
}

export const fetchDeleteComment = (commentId, newsId) => async (dispatch) => {
    const res = await fetch(`/api/news/${commentId}/comment/delete/`, {
        method: 'DELETE'
    })
    if (res.ok) {
        dispatch(deleteComment(commentId))
        dispatch(fetchNewsDetails(newsId))
        return
    }
}

export const fetchAddLike = (newsId) => async (dispatch) => {
    const res = await fetch(`/api/news/${newsId}/like/`, {
        method: 'POST'
    })
    if (res.ok) {
        const updatedNews = await res.json()
        dispatch(addLike(updatedNews))
        return updatedNews
    }
};

export const fetchDeleteLike = (id, newsId) => async (dispatch) => {
    const res = await fetch(`/api/news/${id}/like/delete/`, {
        method: 'DELETE'
    })
    if (res.ok) {
        dispatch(removeLike(id, newsId))
        return
    }
}

const initialState = {}
const newsReducer = (state=initialState, action) => {
    switch (action.type) {
        case GET_ALL_NEWS: {
            const newsState = { ...state }
            action.news.forEach(post => (newsState[post.id] = post))
            return newsState
        }
        case GET_ONE_NEWS: {
            return {
                ...state,
                [action.news.id]: action.news
            }
        }
        case CREATE_NEWS: {
            const newState = {
                ...state,
                [action.news.id]: action.news
            }
            return newState
        }
        case EDIT_NEWS: {
            return {
                ...state,
                [action.news.id]: action.news
            }
        }
        case DELETE_NEWS: {
            const newState = { ...state }
            delete newState[action.newsId]
            return newState
        }
        case ADD_COMMENT: {
            const newState = { ...state }
            const newsPost = newState[action.comment.news_id]
            if (newsPost) {
                newsPost.comments = [...newsPost.comments, action.comment]
            }
            return newState
        }
        case EDIT_COMMENT: {
            const newState = { ...state };
            const newsPost = newState[action.comment.news_id]
            if (newsPost) {
                newsPost.comments = newsPost.comments.map(comment =>
                    comment.id === action.comment.id ? action.comment : comment
                )
            }
            return newState
        }
        case DELETE_COMMENT: {
            const newState = { ...state }
            const newsPost = newState[action.newsId]
            if (newsPost) {
                newsPost.comments = newsPost.comments.filter(comment => comment.id !== action.commentId)
            }
            return newState;
        }
        case ADD_LIKE: {
            return {
                ...state,
                [action.news.id]: action.news
            }
        }
        case REMOVE_LIKE: {
            const newState = { ...state }
            const post = { ...newState[action.newsId] }
            if (post) {
                post.user_likes = post.user_likes.filter(like => like.id !== action.id)
                post.likes -= 1
                newState[action.newsId] = post
            }
            return newState;
        }
        default:
            return state
    }
}

export default newsReducer
