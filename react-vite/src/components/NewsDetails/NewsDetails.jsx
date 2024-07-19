import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useParams } from "react-router-dom"
import { fetchDeleteComment, fetchNewsDetails, fetchAddLike, fetchDeleteLike } from "../../redux/news"
import OpenModalButton from "../OpenModalButton"
import CreateNewsComment from "../Comments/CreateNewsComment"
import './NewsDetails.css'
import { BiSolidLike } from "react-icons/bi";
import LoginFormModal from "../LoginFormModal"


const NewsDetails = () => {
    let { newsId } = useParams()
    newsId = +newsId
    const dispatch = useDispatch()
    const news = useSelector(state => state.news[newsId])
    const user = useSelector(state => state.session.user)

    useEffect(() => {
        dispatch(fetchNewsDetails(newsId))
    }, [dispatch, newsId])

    const checkComments = () => {
        const comments = news?.comments?.find(comment => comment.user_id === user.id)
        return comments
    }

    const handleDelete = async (id) => {
        await dispatch(fetchDeleteComment(id, newsId))
    }

    const handleLike = (news) => {
        if (user) {
            const userLike = news.user_likes.find(like => like.user_id === user.id)
            if (userLike) {
                dispatch(fetchDeleteLike(userLike.id, news.id))
            } else {
                dispatch(fetchAddLike(news.id))
            }
        } else {
            alert('Sign in to like this post.');
        }
    }

    if (!news) {
        return <h1>Loading...</h1>
    }

    return (
        <>
            <div className="post-container">
                <h1 className="news-title">{news.title}</h1>
                <div className="post-dets-container">
                <div className="news-user">{news.users.username}</div>
                <div className="news-det">{news.details}</div>
                </div>
                <div className="news-det-likes">
                    <button
                        className={`like-button ${news.user_likes?.some(like => like.user_id === user.id) ? 'liked' : ''}`}
                        onClick={() => handleLike(news)}><BiSolidLike /> {news.user_likes?.length}
                    </button>
                </div>
            </div>
            <div className="comments">
                {user ? (
                    <div className="add-comment-button">
                        <OpenModalButton
                            modalComponent={<CreateNewsComment newsId={newsId} />}
                            buttonText={!checkComments() ? 'Add Comment' : 'Add Another Comment'}
                        />
                    </div>
                ): (
                    <div className="add-comment-button">
                    <OpenModalButton
                    buttonText='Sign in to join the discussion'
                    modalComponent={<LoginFormModal />}
                />
                </div>
                )}
                <div className="news-dets-comments">
                    {news.comments?.length ? (
                        news.comments.map(comment => (
                            <div className="news-dets-each-comment" key={comment.id}>
                                <div className="news-comment-user">{comment.users.username}</div>
                                <div className="news-comment-content">{comment.content}</div>
                                {user && user.id === comment.user_id && (
                                    <div className="comment-buttons">
                                        <OpenModalButton
                                            modalComponent={<CreateNewsComment comment={comment} newsId={comment.news_id} />}
                                            buttonText='Edit'
                                        />
                                        <button className="delete-comment" onClick={() => handleDelete(comment.id)}>Delete</button>
                                    </div>
                                )}
                            </div>
                        ))
                    ) : <p className="news-dets-no-comments">No comments yet</p>
                    }
                </div>
            </div>
        </>
    )
}

export default NewsDetails
