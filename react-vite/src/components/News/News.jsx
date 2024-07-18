import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { fetchAddLike, fetchAllNews } from "../../redux/news"
import { NavLink } from "react-router-dom"
import { BiSolidLike } from "react-icons/bi";
import OpenModalButton from "../OpenModalButton/OpenModalButton";
import LoginFormModal from "../LoginFormModal";
import './News.css'

const News = () => {
    const dispatch = useDispatch()
    const news = useSelector(state => Object.values(state.news))
    const user = useSelector(state => state.session.user)

    useEffect(() => {
        dispatch(fetchAllNews())
    }, [dispatch])
console.log(user)
    const handleLike = (post) => {
        if (user) {
            dispatch(fetchAddLike(post.id))
        } else {
            alert('Sign in to like this post.')
        }
    }

    if (!news) {
        return <h1>Loading...</h1>
    }
    return (
        <>
        <div className="news-container">
        <h1 className="news-header">News</h1>
        <p className="news-description">
            Welcome to the Yotes4Ever news page!
            <OpenModalButton
                buttonText='Sign in'
                modalComponent={<LoginFormModal />}
            />
            to interact with other fans or post any news that you&aposve heard about the future of the Yotes in the desert.
        </p>
        {news.map(post => (
            <div key={post.id} className="news-card">
            <NavLink to={`/news/${post.id}`}>
                <div>{post.users.username}</div>
                <div>{post.title}</div>
                <div>{post.details}</div>
            </NavLink>
                <button className="like-button" onClick={() => handleLike(post)}><BiSolidLike /> {post.likes}</button>
            </div>
        ))}
        </div>
        </>
    )
}

export default News
