import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useParams } from "react-router-dom"
import { fetchDeleteComment, fetchNewsDetails } from "../../redux/news"
import OpenModalButton from "../OpenModalButton"
import CreateNewsComment from "../Comments/CreateNewsComment"


const NewsDetails = () => {
    let { newsId } = useParams()
    newsId = +newsId
    const dispatch = useDispatch()
    const news = useSelector(state => state.news[newsId])
    const user = useSelector(state => state.session.user)

    useEffect(() => {
        dispatch(fetchNewsDetails(newsId))
    }, [dispatch, newsId])

    const handleDelete = async (id) => {
        await dispatch(fetchDeleteComment(id, newsId))
    }

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
            <div>
                <OpenModalButton
                    modalComponent={<CreateNewsComment newsId={newsId} />}
                    buttonText='Add Comment'
                />
            </div>
            {news.comments?.length ? (
                news.comments.map(comment => (
                <div key={comment.id}>
                    {comment.content}
                    {comment.users.username}
                    {user && user.id === comment.user_id && (
                        <div className="review-buttons">
                        <OpenModalButton
                            modalComponent={<CreateNewsComment comment={comment} newsId={comment.news_id} />}
                            buttonText='Update'
                        />
                        <button onClick={() => handleDelete(comment.id)}>Delete</button>
                        </div>
                    )}
                </div>
            ))
        ): <p>No comments yet</p>
        }
        </div>
        </>
    )
}

export default NewsDetails
