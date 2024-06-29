import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useParams } from "react-router-dom"
import { fetchNewsDetails } from "../../redux/News"


const NewsDetails = () => {
    let { newsId } = useParams()
    newsId = +newsId
    const dispatch = useDispatch()
    const news = useSelector(state => state.news[newsId])

    useEffect(() => {
        dispatch(fetchNewsDetails(newsId))
    }, [dispatch])

    console.log(news)
    if (!news) {
        return <h1>Loading...</h1>
    }
    return (
        <>
        <h1>{news.title}</h1>
        <div>{news.users.username}</div>
        <div>{news.details}</div>
        <div>{news.likes}</div>
        <div className="comments">
            {news.comments.map(comment => (
                <div key={comment.id}>
                    {comment.content}
                    {comment.users.username}
                </div>
            ))}
        </div>
        </>
    )
}

export default NewsDetails
