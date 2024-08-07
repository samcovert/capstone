import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { fetchAllMerch } from "../../redux/merch"
import { NavLink, useNavigate } from "react-router-dom"
import OpenModalButton from "../OpenModalButton"
import DeleteMerch from "../DeleteMerch"
import { fetchAllNews } from "../../redux/news"
import DeleteNews from "../DeleteNews"
import { fetchAllMemories } from "../../redux/memories"
import DeleteMemory from "../DeleteMemory"
import './UserProfile.css'

const UserProfile = () => {
    const dispatch = useDispatch()
    const navigate = useNavigate()
    const user = useSelector(state => state.session.user)
    const merch = useSelector(state => Object.values(state.merchandise).filter(item => item.user_id === user?.id))
    const news = useSelector(state => Object.values(state.news).filter(post => post.users?.id === user?.id))
    const memories = useSelector(state => Object.values(state.memories).filter(memory => memory.user?.id === user?.id))


    useEffect(() => {
        dispatch(fetchAllMerch())
        dispatch(fetchAllNews())
        dispatch(fetchAllMemories())
    }, [dispatch])

    return (
        <>
            <h1 className="user-profile-header">{user.username}&apos;s Profile</h1>
            <div className="user-profile">
                <div className="user-profile-container">
                    <h1 className="user-profile-sub">Your Items for Sale</h1>
                    {merch?.map(item => (
                        <div key={item.id} className="merch-card">
                            <div className="user-merch-content">
                                <NavLink to={`/merch/${item.id}`}>
                                    <img className="merch-image" src={item.images[0]?.url} />
                                    <div className='merch-card-bottom'>
                                        <div className='merch-name'>
                                            {item.name}
                                        </div>
                                    </div>
                                </NavLink>
                                <div className="user-card-buttons">
                                    <OpenModalButton
                                        buttonText='Delete'
                                        modalComponent={<DeleteMerch merchId={item.id} />}
                                    />
                                    <button className="edit-button" onClick={(e) => { e.preventDefault(); navigate(`/merch/${item.id}/edit`) }}>Edit</button>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
                <div className="user-profile-container">
                    <h1 className="user-profile-sub">Your News Posts</h1>
                    {news?.map(post => (
                        <>
                                <div className="user-news-card" key={post.id}>
                            <NavLink to={`/news/${post.id}`}>
                                    <div className="news-card-title">{post.title}</div>
                                    <div className="news-card-details">{post.details}</div>
                            </NavLink>
                            <div className="user-card-buttons">
                            <OpenModalButton
                                    modalComponent={<DeleteNews newsId={post.id} />}
                                    buttonText='Delete'
                                />
                                <NavLink to={`/news/${post.id}/edit`}>
                                    <button className="edit-button">Edit</button>
                                </NavLink>
                            </div>
                        </div>
                        </>
                    ))}
            </div>
            <div className="user-profile-container">
                <h1 className="user-profile-sub">Your Memories</h1>
                {memories?.map(memory => (
                    <div className="mem-card" key={memory.id}>
                        <NavLink to={`/memories/${memory.id}`}>
                            <img className="mem-image" src={memory.images[0]?.url} />
                            <div className="mem-name">{memory.title}</div>
                        </NavLink>
                        <div className="user-card-buttons">
                        <OpenModalButton
                            modalComponent={<DeleteMemory memoryId={memory.id} />}
                            buttonText='Delete'
                        />
                        <NavLink to={`/memories/${memory.id}/edit`}>
                            <button className="edit-button">Edit</button>
                        </NavLink>
                        </div>
                    </div>
                ))}
            </div>
        </div >
        </>
    )
}

export default UserProfile
