const GET_ALL_NEWS = '/news/GET_ALL_NEWS'

const getAllNews = news => {
    return {
        type: GET_ALL_NEWS,
        news
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

const initialState = {}
const newsReducer = (state=initialState, action) => {
    switch (action.type){
        case GET_ALL_NEWS: {
            const newsState = { ...state }
            action.news.forEach(post => (newsState[post.id] = post))
            return newsState
        }
        default:
            return state
    }
}

export default newsReducer
