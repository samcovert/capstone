import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { fetchAllNews } from "../../redux/News"


const News = () => {
    const dispatch = useDispatch()
    const news = useSelector(state => Object.values(state.news))

    useEffect(() => {
        dispatch(fetchAllNews())
    }, [dispatch])
console.log(news)
    if (!news) {
        return <h1>Loading...</h1>
    }
    return (
        <>
        <h1>News</h1>
        {news.map(post => (
            <div key={post.id} className="news-card">
                <div>{post.users.username}</div>
                <div>{post.title}</div>
                <div>{post.details}</div>
                <div>{post.likes}</div>
            </div>
        ))}
        </>
    )
}

export default News
