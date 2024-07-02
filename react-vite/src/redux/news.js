const GET_ALL_NEWS = '/news/GET_ALL_NEWS'
const GET_ONE_NEWS = '/news/GET_ONE_NEWS'
const CREATE_NEWS = '/news/CREATE_NEWS'
const EDIT_NEWS = '/news/EDIT_NEWS'
const DELETE_NEWS = '/news/DELETE_NEWS'

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
        default:
            return state
    }
}

export default newsReducer
