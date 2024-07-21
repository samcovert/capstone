import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { fetchAddLike, fetchAllNews, fetchDeleteLike } from "../../redux/news"
import { NavLink, useNavigate } from "react-router-dom"
import { BiSolidLike } from "react-icons/bi";
import OpenModalButton from "../OpenModalButton/OpenModalButton";
import LoginFormModal from "../LoginFormModal";
import './News.css'

const News = () => {
    const dispatch = useDispatch()
    const news = useSelector(state => Object.values(state.news))
    const user = useSelector(state => state.session.user)
    const navigate = useNavigate()

    useEffect(() => {
        dispatch(fetchAllNews())
    }, [dispatch])

    const handleLike = (post, e) => {
        e.preventDefault()
        if (user) {
            const userLike = post.user_likes.find(like => like.user_id === user.id)
            if (userLike) {
                dispatch(fetchDeleteLike(userLike.id, post.id))
            } else {
                dispatch(fetchAddLike(post.id))
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
            <div className="news-container">
                <h1 className="news-header">News</h1>
                <div className="news-description">
                <p className="news-text"> Welcome to the Yotes4Ever news page!</p>
                <p className="news-text-smaller">Interact with other fans, or post any news that you have heard about the future of the Yotes in the desert.
                </p>
                    {!user ? (
                            <OpenModalButton
                                buttonText='Sign in to join the fun'
                                modalComponent={<LoginFormModal />}
                            />
                    ) : <div className="new-post-div"><button className="new-post-button" onClick={() => navigate('/news/new')}>Make a new post</button> </div>}
                </div>
                {news.map(post => (
                    <NavLink key={post.id} to={`/news/${post.id}`}>
                    <div className="news-card">
                            <div className="news-card-user">{post.users.username}</div>
                            <div className="news-card-title">{post.title}</div>
                            <div className="news-card-details">{post.details}</div>
                        <div className="news-card-bottom">
                        <button
                            className={`like-button ${post.user_likes?.some(like => like.user_id === user?.id) ? 'liked' : ''}`}
                            onClick={(e) => handleLike(post, e)}><BiSolidLike /> {post.likes}
                        </button>
                        <div className="news-card-bottom-comments">
                            {post.comments?.length} {post.comments?.length === 1 ? 'comment' : 'comments'}
                        </div>
                        </div>
                    </div>
                    </NavLink>
                ))}
            </div>
        </>
    )
}

export default News
